"""Out-of-time recommendation triage; never an automatically approved model."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import uuid

import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from threadpoolctl import threadpool_limits

from src.crawler.market_clock import KST, completed_price_cutoff
from src.evaluator.forward_price_forecast import valid_record_time
from src.evaluator.research_shadow_ledger import grade_shadow, seal_ledger
from src.features.next_open_dataset import TARGET_VERSION, build_next_open_dataset
from src.models.monthly_price_walkforward import monthly_split
from src.models.next_open_price_model import fit_classifier, load_inputs, predict_probability, selection_summary
from src.models.price_forecaster import date_weights, json_text, resolve_stock
from src.models.relative_price_selection import rank_candidates
from src.models.selected_price_model import COLUMNS, ROOT, partition_info, to_logits, write_json

GATE_COLUMNS = [
    'base_logit', 'tree_dispersion', 'novelty_rms', 'base_prior_gap',
    'return_5d', 'return_20d', 'volatility_20d', 'distance_ma20', 'volume_ratio_20d',
    'market_mean_return', 'market_up_fraction', 'market_dispersion',
    'recent_bias', 'recent_brier', 'feedback_coverage', 'feedback_dates',
]
OUTCOME_COLUMNS = ['entry_date', 'target_date', 'expected_target_date', 'label_available_date', 'target',
                   'target_return', 'net_return_proxy', 'label_status']
ARMS = ['monthly_base', 'probability_only', 'learned_gate']


def validate_protocol(p):
    fixed = dict(experiment='next_open_selective_gate_v1', gate_algorithm='fixed_shallow_hgb',
                 horizon_sessions=5, cost_assumption=.003, daily_cap=5, probability_threshold=.6,
                 production_promotion=False, candidate_pool_change=False, primary_comparisons=2)
    if any(p.get(k) != v for k, v in fixed.items()):
        raise ValueError('Unsupported prespecified selective protocol.')
    if (p['base_training_sessions'] < 15 or p['base_calibration_sessions'] < 3
            or p['gate_training_sessions'] < 15 or p['gate_calibration_sessions'] < 3
            or p['feedback_sessions'] < 1 or p['bootstrap_samples'] < 100
            or p['bootstrap_block_sessions'] < 5):
        raise ValueError('Insufficient fitting/feedback/block budget.')


def validate_replay(frame):
    if frame.empty or frame.duplicated(['stock_code', 'signal_date']).any():
        raise ValueError('Unique out-of-time stock/date predictions required.')
    if (not frame.prediction_asof.lt(frame.signal_date).all()
            or not frame.base_latest_label.le(frame.prediction_asof).all()):
        raise ValueError('Base predictions contain future fitted labels.')


def fit_month_base(cohort, as_of, p):
    train, calibration = monthly_split(cohort[cohort.target.notna()], as_of,
                                       p['base_training_sessions'], p['base_calibration_sessions'])
    bundle = fit_classifier(train, calibration)
    center = train[COLUMNS].median().to_numpy()
    scale = (train[COLUMNS].quantile(.75) - train[COLUMNS].quantile(.25)).to_numpy()
    scale = np.where(scale > 1e-8, scale, 1.)
    bundle.update(center=center, scale=scale,
                  prior=float(np.average(calibration.target, weights=date_weights(calibration))),
                  as_of=pd.Timestamp(as_of), latest_label=calibration.label_available_date.max())
    return bundle, {'train': partition_info(train), 'calibration': partition_info(calibration)}


def base_features(bundle, candidates):
    frame = candidates[['stock_code', 'signal_date', 'close'] + OUTCOME_COLUMNS].copy().reset_index(drop=True)
    p = predict_probability(bundle, candidates)
    # Four groups of the SAME forest quantify internal dispersion, not independent experts.
    groups = np.array_split(np.arange(len(bundle['classifier'].estimators_)), 4)
    x = candidates[COLUMNS].to_numpy()
    with threadpool_limits(limits=2):
        group_probability = [np.mean([bundle['classifier'].estimators_[i].predict_proba(x)[:, 1]
                                     for i in group], axis=0) for group in groups]
    frame['tree_dispersion'] = np.std(group_probability, axis=0)
    standardized = (x - bundle['center']) / bundle['scale']
    frame['novelty_rms'] = np.sqrt(np.mean(np.clip(standardized, -20, 20) ** 2, axis=1))
    frame['monthly_base'] = p
    frame['base_logit'] = to_logits(p).ravel()
    frame['base_prior'], frame['base_prior_gap'] = bundle['prior'], p - bundle['prior']
    frame['prediction_asof'], frame['base_latest_label'] = bundle['as_of'], bundle['latest_label']
    for col in ['return_5d', 'return_20d', 'volatility_20d', 'distance_ma20', 'volume_ratio_20d']:
        frame[col] = candidates[col].to_numpy()
    returns = pd.Series(candidates.return_1d.to_numpy(), index=frame.index)
    frame['market_mean_return'] = returns.groupby(frame.signal_date).transform('mean')
    frame['market_up_fraction'] = returns.gt(0).groupby(frame.signal_date).transform('mean')
    frame['market_dispersion'] = returns.groupby(frame.signal_date).transform('std').fillna(0)
    return frame


def add_feedback(frame, history, sessions):
    """Only scheduled-mature cohorts and actually resolved labels BEFORE each issue day."""
    validate_replay(history)
    result = frame.copy()
    for day, indexes in result.groupby('signal_date', sort=True).groups.items():
        old = history[history.signal_date.lt(day) & history.expected_target_date.lt(day)]
        days = sorted(old.signal_date.unique())[-sessions:]
        old = old[old.signal_date.isin(days)]
        known = old[old.target.notna() & old.label_available_date.lt(day)]
        bias, brier = 0., .25
        if len(known):
            daily = known.assign(error=known.target - known.monthly_base,
                                loss=(known.target - known.monthly_base) ** 2).groupby('signal_date')[['error', 'loss']].mean()
            bias, brier = float(daily.error.mean()), float(daily.loss.mean())
        result.loc[indexes, 'recent_bias'] = bias
        result.loc[indexes, 'recent_brier'] = brier
        result.loc[indexes, 'feedback_coverage'] = len(known) / len(old) if len(old) else 0.
        result.loc[indexes, 'feedback_dates'] = known.signal_date.nunique()
    if not np.isfinite(result[GATE_COLUMNS]).all(axis=None):
        raise ValueError('Gate features must be finite; do not silently drop candidates.')
    return result


def fit_gate(replay, as_of, p):
    validate_replay(replay)
    train, calibration = monthly_split(replay[replay.target.notna()], as_of,
                                       p['gate_training_sessions'], p['gate_calibration_sessions'])
    # The target is the unchanged BUY outcome, not a new easier success definition.
    with threadpool_limits(limits=2):
        gate = HistGradientBoostingClassifier(max_iter=80, learning_rate=.04, max_leaf_nodes=7,
                                              max_depth=3, min_samples_leaf=400, l2_regularization=10,
                                              early_stopping=False, random_state=42)
        gate.fit(train[GATE_COLUMNS], train.target.astype(int), sample_weight=date_weights(train))
        probability_only = LogisticRegression(C=1., solver='liblinear', max_iter=1000, random_state=42)
        probability_only.fit(train[['base_logit']], train.target.astype(int), sample_weight=date_weights(train))
        calibrators = {}
        for name, model, columns in [('learned_gate', gate, GATE_COLUMNS),
                                     ('probability_only', probability_only, ['base_logit'])]:
            cal = LogisticRegression(C=1., solver='liblinear', max_iter=1000, random_state=42)
            cal.fit(to_logits(model.predict_proba(calibration[columns])[:, 1]), calibration.target.astype(int),
                    sample_weight=date_weights(calibration))
            calibrators[name] = cal
    return dict(gate=gate, probability_only=probability_only, calibrators=calibrators,
                latest_label=calibration.label_available_date.max(), as_of=pd.Timestamp(as_of),
                partitions={'train': partition_info(train), 'calibration': partition_info(calibration)})


def gate_predictions(bundle, frame):
    if (bundle['latest_label'] > frame.signal_date.min()
            or not np.isfinite(frame[GATE_COLUMNS]).all(axis=None)):
        raise ValueError('Future gate labels or invalid gate features.')
    result = frame.copy()
    with threadpool_limits(limits=2):
        for name, model, columns in [('learned_gate', bundle['gate'], GATE_COLUMNS),
                                     ('probability_only', bundle['probability_only'], ['base_logit'])]:
            raw = model.predict_proba(frame[columns])[:, 1]
            result[name] = bundle['calibrators'][name].predict_proba(to_logits(raw))[:, 1]
    if not np.isfinite(result[ARMS]).all(axis=None) or not result[ARMS].ge(0).all(axis=None) or not result[ARMS].le(1).all(axis=None):
        raise ValueError('Invalid gate probabilities.')
    result['recommendation'] = 'ABSTAIN'
    return result


def selection_masks(frame, p):
    """Equal daily budgets depend ONLY on inputs; outcomes cannot alter selection."""
    masks = {}
    for name in ARMS:
        masks['top5_' + name] = frame.index.isin(rank_candidates(frame, name, p['daily_cap']).index)
    chosen = rank_candidates(frame[frame.learned_gate.ge(p['probability_threshold'])], 'learned_gate', p['daily_cap'])
    counts = chosen.groupby('signal_date').size()
    for name in ARMS:
        ordered = frame.sort_values(['signal_date', name, 'stock_code'], ascending=[True, False, True], kind='stable')
        rank = ordered.groupby('signal_date').cumcount() + 1
        selected = ordered.index[rank.le(ordered.signal_date.map(counts).fillna(0))]
        masks['matched_policy_' + name] = frame.index.isin(selected)
    return masks


def paired_success(frame, left, right, p):
    dates = pd.DatetimeIndex(sorted(frame.signal_date.unique()))
    daily, unknown = [], 0
    for mask in [left, right]:
        selected = frame.loc[mask]
        grouped = selected.groupby('signal_date').target.agg(['mean', 'count', 'size']).reindex(dates)
        unknown += int(selected.target.isna().sum())
        daily.append(grouped['mean'].where(grouped['count'].eq(grouped['size'])))
    valid = daily[0].notna() & daily[1].notna()
    differences = (daily[1] - daily[0]).to_numpy()
    observed = differences[valid.to_numpy()]
    # Bootstrap the FULL date axis. Unknown dates stay unknown, not compressed out.
    result = {'conditional_date_success_difference': float(observed.mean()) if len(observed) else None,
              'paired_complete_dates': int(valid.sum()), 'total_dates': len(dates),
              'unresolved_selected_across_arms': unknown, 'family_adjusted_lower': None,
              'family_adjusted_upper': None, 'complete_period_lower': None,
              'interpretation': 'Conditional on complete paired selected outcomes; not full policy evidence if any are unknown'}
    if len(observed) >= 20:
        rng = np.random.default_rng(42)
        block = p['bootstrap_block_sessions']
        starts = rng.integers(0, len(dates), size=(p['bootstrap_samples'], int(np.ceil(len(dates) / block))))
        indices = ((starts[:, :, None] + np.arange(block)) % len(dates)).reshape(p['bootstrap_samples'], -1)[:, :len(dates)]
        values = differences[indices]
        n = np.isfinite(values).sum(axis=1)
        estimates = np.nansum(values, axis=1)[n > 0] / n[n > 0]
        alpha = .05 / p['primary_comparisons']
        lo, hi = np.quantile(estimates, [alpha / 2, 1 - alpha / 2])
        result.update(family_adjusted_lower=float(lo), family_adjusted_upper=float(hi),
                      complete_period_lower=float(lo) if valid.all() else None)
    return result


def evaluate_gate(frame, p):
    frame = frame.copy().reset_index(drop=True)
    masks = selection_masks(frame, p)
    groups = {name: selection_summary(frame, mask) for name, mask in masks.items()}
    observed = frame[frame.target.notna()]
    probabilities = {}
    for name in ARMS:
        probabilities[name] = dict(date_brier=float(np.average((observed[name] - observed.target) ** 2,
                                                               weights=date_weights(observed))) if len(observed) else None,
                                   mean_forecast=float(observed[name].mean()) if len(observed) else None,
                                   observed_success_rate=float(observed.target.mean()) if len(observed) else None)
    comparisons = {name: paired_success(frame, masks['top5_' + name], masks['top5_learned_gate'], p)
                   for name in ARMS[:-1]}
    return dict(input_candidates=len(frame), evaluated_cases=len(observed), unresolved_cases=int(frame.target.isna().sum()),
                signal_dates=int(frame.signal_date.nunique()), probabilities=probabilities,
                selections=groups, primary_top5_comparisons=comparisons)


def experiment_key(data_root, p):
    digest = hashlib.sha256((Path(data_root) / 'history_manifest.json').read_bytes())
    digest.update(json_text(p).encode())
    for name in ['src/models/selective_price_model.py', 'src/models/next_open_price_model.py',
                 'src/features/next_open_dataset.py', 'src/models/selected_price_model.py',
                 'src/models/monthly_price_walkforward.py']:
        digest.update((ROOT / name).read_bytes())
    return digest.hexdigest()


def render_report(summary):
    def num(value, percent=False):
        return 'N/A' if value is None else (f'{value:.2%}' if percent else f'{value:.6f}')
    lines = ['# Selective Recommendation Research / 추천 판단 모델', '',
             'RESEARCH ONLY. Historical development replay, not live validation or investment advice.',
             'Same next-open to fifth-close BUY target, cost 0.3%, complete input candidate universe.',
             'Monthly base fits and gate fits use only labels available BEFORE each evaluated month.',
             'Gate training uses genuinely out-of-time base predictions, never in-sample fitted predictions.',
             'Recent errors use only scheduled-mature cohorts and resolved labels strictly before the signal day.',
             'Tree-group dispersion is internal variation of one forest, NOT independent-model agreement.',
             'Gate parameters, periods, Top5 budget and 60% rule were fixed before running. No tuning on these results.', '',
             '## Equal Daily Top5 Monitoring Budget', '',
             '| Period | Method | Candidates | Selected | Evaluated | Unknown | Conditional date success | Conditional net proxy |',
             '|---|---|---:|---:|---:|---:|---:|---:|']
    for period, metrics in summary['results'].items():
        for name in ARMS:
            m = metrics['selections']['top5_' + name]
            lines.append(f"| {period} | {name} | {metrics['input_candidates']} | {m['selected_cases']} | {m['evaluated_cases']} | {m['unresolved_cases']} | {num(m['conditional_date_success_rate'], True)} | {num(m['conditional_mean_net_return_proxy'], True)} |")
    lines += ['', 'Unknown selected outcomes are never replaced. Conditional results are not complete-policy returns.',
              'The Top5 comparison is a monitoring diagnostic, NOT a recommendation to buy five stocks daily.', '',
              '## Primary Paired Gate Minus Control', '', '```json',
              json_text(summary['results']['primary_development']['primary_top5_comparisons']), '```', '',
              'Two prespecified comparisons use Bonferroni family-adjusted five-session-block intervals.',
              'Unknown dates remain on the bootstrap calendar; full-period lower bounds are withheld when any paired date is incomplete.', '',
              '## Full Metrics and Probability Calibration', '', '```json', json_text(summary['results']), '```', '',
              'Threshold-policy controls have the exact same per-date selected count as the gate, chosen without inspecting outcomes.',
              'No selections, missing outcomes, probability error and conditional success are reported separately.', '',
              '## Label-Time Audit', '', '```json', json_text(summary['fits']), '```', '',
              '## Limits', '',
              'Repeatedly inspected historical prices, current-universe survivorship, retrospective adjustments and an observed-universe calendar remain limitations.',
              'Five-session overlapping returns after assumed cost are research proxies, not compounded executable portfolio returns.',
              'A second model can fail or simply recalibrate the first. Compare against the probability-only control, not only the base.',
              'No high reliability is certified from historical development. All recommendations remain ABSTAIN.',
              'Run: ' + summary['run_dir'], '']
    return '\n'.join(lines)


def run_experiment(data_root, output_root, p, report):
    validate_protocol(p)
    inputs, _ = load_inputs(data_root, p['labels_as_of'])
    cohort, _ = build_next_open_dataset(inputs, p['labels_as_of'])
    calendar = pd.DatetimeIndex(sorted(inputs.signal_date.unique()))
    key = experiment_key(data_root, p)
    output_root = Path(output_root)
    cache = output_root / 'cache' / key
    cache.mkdir(parents=True, exist_ok=True)
    plan = cohort[cohort.signal_date.ge(p['replay_start'])]
    parts, base_fits, last_base = [], [], None
    for month, part in plan.groupby(plan.signal_date.dt.to_period('M'), sort=True):
        as_of = calendar[calendar < month.start_time][-1]
        path = cache / f'{month}.joblib'
        if path.exists():
            if hashlib.sha256(path.read_bytes()).hexdigest() != path.with_suffix('.sha256').read_text().strip():
                raise ValueError('Replay checkpoint checksum changed.')
            item = joblib.load(path)
            print(f'Verified cached base replay: {month}', flush=True)
        else:
            print(f'Fitting out-of-time base: {month}; as-of {as_of.date()}', flush=True)
            base, audit = fit_month_base(cohort, as_of, p)
            scored = base_features(base, part.sort_values(['signal_date', 'stock_code']).reset_index(drop=True))
            validate_replay(scored)
            item = dict(base=base, scored=scored, audit=dict(month=str(month), as_of=str(as_of.date()), **audit))
            temporary = path.with_suffix('.tmp')
            joblib.dump(item, temporary, compress=3)
            temporary.replace(path)
            path.with_suffix('.sha256').write_text(hashlib.sha256(path.read_bytes()).hexdigest())
        parts.append(item['scored'])
        base_fits.append(item['audit'])
        last_base = item['base']
    replay = pd.concat(parts, ignore_index=True).sort_values(['signal_date', 'stock_code']).reset_index(drop=True)
    validate_replay(replay)
    replay = add_feedback(replay, replay, p['feedback_sessions'])
    run = output_root / 'runs' / (datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '_' + uuid.uuid4().hex[:8])
    run.mkdir(parents=True, exist_ok=False)
    predicted, gate_fits = [], []
    test = replay[replay.signal_date.ge(p['evaluation_start'])]
    for month, part in test.groupby(test.signal_date.dt.to_period('M'), sort=True):
        as_of = calendar[calendar < month.start_time][-1]
        print(f'Fitting out-of-time recommendation gate: {month}', flush=True)
        gate = fit_gate(replay, as_of, p)
        predicted.append(gate_predictions(gate, part))
        gate_fits.append(dict(month=str(month), as_of=str(as_of.date()), **gate['partitions']))
    predictions = pd.concat(predicted, ignore_index=True).sort_values(['signal_date', 'stock_code']).reset_index(drop=True)
    results = {}
    for name, (start, end) in p['periods'].items():
        part = predictions[predictions.signal_date.between(start, end)].reset_index(drop=True)
        if part.empty:
            raise ValueError('No input candidates in evaluation period: ' + name)
        results[name] = evaluate_gate(part, p)
    current = fit_gate(replay, pd.Timestamp(p['labels_as_of']), p)
    metadata = dict(schema='selective_price_v1', target_version=TARGET_VERSION, dataset_sha256=key,
                    trained_at=datetime.now(timezone.utc).isoformat(), as_of=p['labels_as_of'],
                    data_root=str(Path(data_root).resolve()), features=GATE_COLUMNS, protocol=p,
                    baseline_probability=last_base['prior'], recommendation_enabled=False,
                    evaluation_role='Retrospective development, not independent validation')
    joblib.dump(dict(base=last_base, gate=current, feedback_history=replay,
                     metadata=metadata), run / 'model.joblib', compress=3)
    predictions.to_csv(run / 'development_predictions.csv', index=False)
    write_json(metadata, run / 'model_metadata.json')
    checksums = {name: hashlib.sha256((run / name).read_bytes()).hexdigest()
                 for name in ['model.joblib', 'model_metadata.json', 'development_predictions.csv']}
    write_json(checksums, run / 'checksums.json')
    summary = dict(run_dir=str(run.resolve()), results=results, fits={'base': base_fits, 'gate': gate_fits,
                   'current_gate': current['partitions']}, recommendation_gate_passed=False,
                   gate_reasons=['requires_genuine_new_future_validation'], protocol_sha256=hashlib.sha256(json_text(p).encode()).hexdigest())
    write_json(summary, run / 'summary.json')
    Path(report).parent.mkdir(parents=True, exist_ok=True)
    Path(report).write_text(render_report(summary), encoding='utf-8')
    write_json(summary, Path(report).with_suffix('.json'))
    write_json(dict(run_dir=str(run.resolve()), checksums_sha256=hashlib.sha256((run / 'checksums.json').read_bytes()).hexdigest()), output_root / 'latest.json')
    return summary


def load_gate(root):
    pointer = json.loads((Path(root) / 'latest.json').read_text())
    run = Path(pointer['run_dir'])
    if hashlib.sha256((run / 'checksums.json').read_bytes()).hexdigest() != pointer['checksums_sha256']:
        raise ValueError('Selective manifest changed.')
    for name, digest in json.loads((run / 'checksums.json').read_text()).items():
        if Path(name).name != name or hashlib.sha256((run / name).read_bytes()).hexdigest() != digest:
            raise ValueError('Selective artifact checksum mismatch.')
    bundle = joblib.load(run / 'model.joblib')
    m = bundle['metadata']
    if (m != json.loads((run / 'model_metadata.json').read_text()) or m['schema'] != 'selective_price_v1'
            or m['target_version'] != TARGET_VERSION or m['features'] != GATE_COLUMNS or m['recommendation_enabled'] is not False):
        raise ValueError('Unsupported selective model metadata.')
    validate_protocol(m['protocol'])
    return bundle


def current_predictions(bundle, data_root, now=None):
    now = now or datetime.now(KST)
    m = bundle['metadata']
    if now.tzinfo is None or pd.Timestamp(m['trained_at']) > pd.Timestamp(now):
        raise ValueError('Current timezone-aware clock after fitting required.')
    cutoff = completed_price_cutoff(now)
    inputs, _ = load_inputs(data_root, cutoff)
    cohort, _ = build_next_open_dataset(inputs, cutoff)
    origin = cohort.signal_date.max()
    if pd.Timestamp(m['as_of']) > origin or origin.to_period('M') != bundle['base']['as_of'].to_period('M') + 1:
        raise ValueError('Use matching current-month base and nonfuture gate; refit for a new month.')
    latest = cohort[cohort.signal_date.eq(origin)].sort_values('stock_code').reset_index(drop=True)
    frame = base_features(bundle['base'], latest)
    # Refresh ONLY answers on the original historical prediction keys, never their probabilities.
    history = bundle['feedback_history'].drop(columns=OUTCOME_COLUMNS)
    answers, _ = build_next_open_dataset(inputs, cutoff, candidate_keys=history[['stock_code', 'signal_date']])
    history = history.merge(answers[['stock_code', 'signal_date'] + OUTCOME_COLUMNS],
                            on=['stock_code', 'signal_date'], how='left', validate='1:1')
    frame = add_feedback(frame, history, m['protocol']['feedback_sessions'])
    frame = gate_predictions(bundle['gate'], frame)
    output = frame[['stock_code', 'signal_date', 'close']].rename(columns={'close': 'origin_close'})
    for name in ARMS:
        output['probability_' + name] = frame[name]
    for name, mask in selection_masks(frame, m['protocol']).items():
        output[name] = mask
    output['probability_above_cost'] = frame.learned_gate
    output['recommendation'], output['status'] = 'ABSTAIN', 'RESEARCH_ONLY'
    return output


def freeze_selective(bundle, data_root, output_dir, now=None):
    live = now is None
    now = now or datetime.now(KST)
    frame = current_predictions(bundle, data_root, now)
    if live:
        now = datetime.now(KST)
    origin = frame.signal_date.max()
    if not (valid_record_time(origin, pd.Timestamp(now))
            and valid_record_time(origin, pd.Timestamp(now) + pd.Timedelta(seconds=60))):
        raise ValueError('Outside original recording window; never backdate selective predictions.')
    m = bundle['metadata']
    frame['recorded_at'], frame['model_trained_at'] = now.isoformat(), m['trained_at']
    frame['model_dataset_sha256'], frame['target_version'] = m['dataset_sha256'], TARGET_VERSION
    frame['horizon_sessions'], frame['cost_assumption'], frame['validation_base_rate'] = 5, .003, m['baseline_probability']
    frame['source_manifest_sha256'] = hashlib.sha256((Path(data_root) / 'history_manifest.json').read_bytes()).hexdigest()
    frame['prediction_id'] = [hashlib.sha256('|'.join([code, str(origin.date()), m['dataset_sha256'], m['trained_at'], 'selective']).encode()).hexdigest()[:24] for code in frame.stock_code]
    key = hashlib.sha256((m['dataset_sha256'] + m['trained_at']).encode()).hexdigest()[:16]
    path = Path(output_dir) / f'ml_selective_forward_{origin:%Y%m%d}_{key}.csv'
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('x', encoding='utf-8-sig') as handle:
        frame.to_csv(handle, index=False)
    seal_ledger(path, 'selective_gate', m, 'learned_gate', ARMS)
    return dict(ledger=str(path), frozen_predictions=len(frame), recommendation_enabled=False)


def grade_selective(path, inputs, as_of, p, now=None):
    validate_protocol(p)
    frame, summary = grade_shadow(path, inputs, as_of, 'selective_gate', now)
    scored = frame.rename(columns={f'probability_{name}': name for name in ARMS})
    for name, mask in selection_masks(scored, p).items():
        if name not in frame:
            raise ValueError('Original selective policy is missing.')
        original = frame[name].map({True: True, False: False, 'True': True, 'False': False})
        if original.isna().any() or not np.array_equal(original.to_numpy(dtype=bool), mask):
            raise ValueError('Original selective policy differs from the fixed input-only rule.')
    summary['selection_diagnostics'] = evaluate_gate(scored, p)
    return frame, summary


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['train', 'predict', 'freeze', 'grade'])
    parser.add_argument('--protocol', type=Path, default=ROOT / 'docs/model_experiments/selective_price_protocol_20261023.json')
    parser.add_argument('--data-root', type=Path)
    parser.add_argument('--model-dir', type=Path, default=ROOT / 'data/models/price_selective_gate')
    parser.add_argument('--report', type=Path, default=ROOT / 'reports/daily_review/2026-10-23_selective_recommendation.md')
    parser.add_argument('--stock')
    parser.add_argument('--ledger', type=Path)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--output-dir', type=Path, default=ROOT / 'data/predictions')
    args = parser.parse_args()
    if args.command == 'train':
        p = json.loads(args.protocol.read_text())
        summary = run_experiment(args.data_root or ROOT / p['data_root'], args.model_dir, p, args.report)
        print(json_text(dict(run_dir=summary['run_dir'], recommendation_gate_passed=False)))
    elif args.command == 'grade':
        if not args.ledger or not args.data_root or not args.output or args.output.resolve() == args.ledger.resolve():
            parser.error('grade requires --ledger, --data-root and separate --output')
        inputs, _ = load_inputs(args.data_root, completed_price_cutoff())
        p = json.loads(args.protocol.read_text())
        frame, summary = grade_selective(args.ledger, inputs, completed_price_cutoff(), p)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        frame.to_csv(args.output, index=False)
        print(json_text(summary))
    else:
        bundle = load_gate(args.model_dir)
        data_root = args.data_root or bundle['metadata']['data_root']
        if args.command == 'freeze':
            print(json_text(freeze_selective(bundle, data_root, args.output_dir)))
        else:
            if not args.stock:
                parser.error('predict requires --stock')
            code = resolve_stock(args.stock, [ROOT, data_root])
            frame = current_predictions(bundle, data_root)
            matched = frame[frame.stock_code.eq(code)]
            if matched.empty:
                parser.exit(2, 'No eligible completed inputs for this stock.\n')
            print(json_text(matched.iloc[0].to_dict() | {'note': 'Research snapshot, not measured reliability or a recommendation.'}))


if __name__ == '__main__':
    main()
