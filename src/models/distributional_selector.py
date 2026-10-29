"""Selective payoff-distribution research; neither trading nor a reliability guarantee."""
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
from scipy.optimize import minimize_scalar
from scipy.special import softmax
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import log_loss
from threadpoolctl import threadpool_limits

from src.crawler.market_clock import KST, completed_price_cutoff
from src.evaluator.forward_price_forecast import valid_record_time
from src.features.completed_price_dataset import HISTORY_FEATURE_VERSION
from src.features.price_learning_dataset import build_dataset, load_snapshots
from src.models.price_forecaster import date_weights, fit_estimator, json_text, resolve_stock
from src.models.relative_price_selection import (
    block_interval, daily_portfolio, probability_metrics, random_portfolios, rank_candidates,
)
from src.models.selected_price_model import (
    COLUMNS, ROOT, factories, fit_data_digest, partition_info, prepare_selected_features, to_logits, write_json,
)

EDGES = np.array([-.03, .003, .03])
SEEDS = [17, 42, 73]


def outcome_bins(returns):
    values = np.asarray(returns, dtype=float)
    if not np.isfinite(values).all():
        raise ValueError('Outcome bins require finite returns.')
    return np.searchsorted(EDGES, values, side='left')


def complete_cohort(raw, as_of, minimum_stocks=100):
    cutoff = pd.Timestamp(as_of)
    raw = raw[raw.signal_date.le(cutoff) & raw.snapshot_date.le(cutoff)].copy()
    inputs = prepare_selected_features(raw, COLUMNS)
    eligible = inputs[np.isfinite(inputs[COLUMNS]).all(axis=1) & inputs.close.gt(0)
                      & inputs.volume_ratio_20d.gt(0)].copy()
    resolved, metadata = build_dataset(inputs, as_of=as_of)
    resolved = resolved[np.isfinite(resolved[COLUMNS]).all(axis=1)].copy()
    counts = eligible.groupby('signal_date').size().rename('eligible').to_frame()
    counts['resolved'] = resolved.groupby('signal_date').size().reindex(counts.index, fill_value=0)
    counts['included'] = counts.eligible.eq(counts.resolved) & counts.eligible.ge(minimum_stocks)
    # Exclude a whole incomplete-outcome date, never select surviving resolved stocks.
    frame = resolved[resolved.signal_date.isin(counts.index[counts.included])].copy()
    frame = frame.sort_values(['signal_date', 'stock_code']).reset_index(drop=True)
    if frame.empty or frame.duplicated(['stock_code', 'signal_date']).any():
        raise ValueError('No unique complete candidate-date cohort.')
    frame['universe_return'] = frame.groupby('signal_date').target_return.transform('mean')
    frame['relative_target'] = frame.target_return.gt(frame.universe_return).astype(int)
    return frame, counts, metadata


def four_partitions(dataset, protocol):
    cal, policy, test = [pd.Timestamp(protocol[key]) for key in
                         ['probability_calibration_start', 'policy_calibration_start', 'evaluation_start']]
    if not dataset.signal_date.min() < cal < policy < test <= dataset.signal_date.max():
        raise ValueError('Four temporal boundaries must be ordered inside history.')
    parts = [dataset[dataset.signal_date.lt(cal) & dataset.label_available_date.lt(cal)],
             dataset[dataset.signal_date.ge(cal) & dataset.signal_date.lt(policy) & dataset.label_available_date.lt(policy)],
             dataset[dataset.signal_date.ge(policy) & dataset.signal_date.lt(test) & dataset.label_available_date.lt(test)],
             dataset[dataset.signal_date.ge(test)]]
    for name, part in zip(['train', 'probability_calibration', 'policy_calibration', 'evaluation'], parts):
        if part.signal_date.nunique() < (15 if name == 'train' else 3) or part.target.nunique() != 2:
            raise ValueError('Insufficient dates/classes in ' + name)
    return tuple(part.copy().reset_index(drop=True) for part in parts)


def temperature_probability(raw_probability, temperature):
    raw_probability = np.asarray(raw_probability, dtype=float)
    if (raw_probability.ndim != 2 or raw_probability.shape[1] != 4 or not np.isfinite(raw_probability).all()
            or np.any((raw_probability < 0) | (raw_probability > 1))
            or not np.allclose(raw_probability.sum(axis=1), 1) or not .25 <= temperature <= 4):
        raise ValueError('Invalid multiclass probabilities/temperature.')
    return softmax(np.log(np.clip(raw_probability, 1e-9, 1)) / temperature, axis=1)


def fit_distribution(train, calibration):
    if train.label_available_date.max() >= calibration.signal_date.min():
        raise ValueError('Training labels overlap probability calibration.')
    y, y_cal = outcome_bins(train.target_return), outcome_bins(calibration.target_return)
    if set(y) != {0, 1, 2, 3}:
        raise ValueError('Training requires all four payoff outcomes.')
    clipped = np.clip(train.target_return.to_numpy(), -.2, .2)
    weights = date_weights(train)
    bin_return = [float(np.average(clipped[y == k], weights=weights[y == k])) for k in range(4)]
    bin_log = [float(np.average(np.log1p(clipped[y == k] - .003), weights=weights[y == k])) for k in range(4)]
    models, temperatures = [], []
    with threadpool_limits(limits=2):
        for seed in SEEDS:
            print('Fitting payoff distribution seed ' + str(seed), flush=True)
            model = factories()['extra_trees'].set_params(random_state=seed)
            fit_estimator(model, train[COLUMNS], y, weights)
            raw = model.predict_proba(calibration[COLUMNS])
            fitted = minimize_scalar(lambda t: log_loss(y_cal, temperature_probability(raw, t), labels=[0, 1, 2, 3],
                                                        sample_weight=date_weights(calibration)),
                                     bounds=(.25, 4), method='bounded')
            if not fitted.success:
                raise ValueError('Temperature calibration did not converge.')
            models.append(model)
            temperatures.append(float(fitted.x))
        # Same feature/cohort/timing control, not an older differently fitted model.
        binary = fit_estimator(factories()['extra_trees'], train[COLUMNS], train.target, weights)
        calibrator = LogisticRegression(C=1., solver='liblinear', max_iter=1000, random_state=42)
        calibrator.fit(to_logits(binary.predict_proba(calibration[COLUMNS])[:, 1]), calibration.target,
                       sample_weight=date_weights(calibration))
    return {'models': models, 'temperatures': temperatures, 'features': COLUMNS,
            'bin_return': bin_return, 'bin_log_utility': bin_log,
            'binary_control': binary, 'binary_calibrator': calibrator,
            'baseline_probability': float(np.average(calibration.target, weights=date_weights(calibration)))}


def predict_distribution(bundle, features):
    if list(features.columns) != COLUMNS or not np.isfinite(features).all(axis=None):
        raise ValueError('Distributional input schema/values mismatch.')
    with threadpool_limits(limits=2):
        probabilities = np.stack([temperature_probability(model.predict_proba(features), temperature)
                                  for model, temperature in zip(bundle['models'], bundle['temperatures'], strict=True)])
        binary = bundle['binary_calibrator'].predict_proba(to_logits(bundle['binary_control'].predict_proba(features)[:, 1]))[:, 1]
    positive = probabilities[:, :, 2:].sum(axis=2)
    utility = probabilities @ np.array(bundle['bin_log_utility'])
    return pd.DataFrame({'probability_above_cost': positive.mean(axis=0), 'positive_floor': positive.min(axis=0),
                         'downside_ceiling': probabilities[:, :, 0].max(axis=0),
                         'probability_disagreement': positive.std(axis=0), 'utility_score': utility.min(axis=0),
                         'clipped_return_proxy': probabilities.mean(axis=0) @ np.array(bundle['bin_return']),
                         'binary_probability': binary})


def score_frame(bundle, frame):
    frame = frame.reset_index(drop=True).copy()
    outputs = predict_distribution(bundle, frame[COLUMNS])
    for column in outputs:
        frame[column] = outputs[column].to_numpy()
    frame['recommendation'] = 'ABSTAIN'
    frame['origin'] = 'retrospective_development_not_prospective'
    return frame


def policy_selection(frame, policy, protocol):
    selected = pd.Series(False, index=frame.index)
    if policy is None:
        return selected
    eligible = frame[frame.positive_floor.ge(policy['probability_floor'])
                     & frame.downside_ceiling.le(policy['downside_ceiling'])
                     & frame.probability_disagreement.le(protocol['policy_max_disagreement']) & frame.utility_score.gt(0)]
    top = rank_candidates(eligible, 'utility_score', protocol['policy_daily_cap'])
    selected.loc[top.index] = True
    return selected


def selection_metrics(frame, selected, protocol, alpha=.05):
    dates = pd.DatetimeIndex(sorted(frame.signal_date.unique()))
    picked = frame[selected]
    grouped = picked.groupby('signal_date')
    success = grouped.target.mean().reindex(dates)
    net = grouped.net_return_proxy.mean().reindex(dates, fill_value=0)
    lower_success = None
    if success.notna().sum() >= 20:
        rng = np.random.default_rng(protocol['bootstrap_seed'])
        block = protocol['bootstrap_block_sessions']
        starts = rng.integers(0, len(dates), (protocol['bootstrap_samples'], int(np.ceil(len(dates) / block))))
        indices = ((starts[:, :, None] + np.arange(block)) % len(dates)).reshape(len(starts), -1)[:, :len(dates)]
        active = success.notna().to_numpy()[indices].sum(axis=1)
        sums = success.fillna(0).to_numpy()[indices].sum(axis=1)
        values = sums[active > 0] / active[active > 0]
        lower_success = float(np.quantile(values, alpha / 2)) if len(values) else None
    interval = block_interval(net.to_numpy(), protocol['bootstrap_samples'], protocol['bootstrap_block_sessions'],
                              alpha, protocol['bootstrap_seed'])
    return {'cases': len(picked), 'dates': int(picked.signal_date.nunique()),
            'success_count': int(picked.target.sum()), 'failure_count': int(len(picked) - picked.target.sum()),
            'pooled_success_rate': float(picked.target.mean()) if len(picked) else None,
            'date_success_rate': float(success.mean()) if success.notna().any() else None,
            'date_success_lower': lower_success, 'all_date_net_proxy': interval['mean'],
            'all_date_net_lower': interval['lower'], 'alpha': alpha}


def select_policy(frame, protocol):
    policies = [{'probability_floor': p, 'downside_ceiling': loss}
                for p in protocol['policy_probability_floors'] for loss in protocol['policy_downside_ceilings']]
    trials, passing = [], []
    for policy in policies:
        # Nine policies and two bounds per policy: conservative family correction.
        metrics = selection_metrics(frame, policy_selection(frame, policy, protocol), protocol, alpha=.05 / (2 * len(policies)))
        passed = (metrics['cases'] >= protocol['policy_min_cases'] and metrics['dates'] >= protocol['policy_min_dates']
                  and metrics['date_success_rate'] is not None and metrics['date_success_rate'] >= protocol['policy_min_date_success']
                  and metrics['date_success_lower'] is not None and metrics['date_success_lower'] >= protocol['policy_min_success_lower']
                  and metrics['all_date_net_lower'] is not None and metrics['all_date_net_lower'] > 0)
        row = {'policy': policy, 'metrics': metrics, 'passed': bool(passed)}
        trials.append(row)
        if passed:
            passing.append(row)
    if not passing:
        return None, trials
    best = max(passing, key=lambda row: (row['metrics']['all_date_net_lower'], row['policy']['probability_floor'],
                                       -row['policy']['downside_ceiling']))
    return best['policy'], trials


def evaluate_period(bundle, frame, protocol):
    scored = score_frame(bundle, frame)
    selected = policy_selection(scored, bundle['policy'], protocol)
    scored['selected_by_research_policy'] = selected
    policy = selection_metrics(scored, selected, protocol)
    portfolios = {}
    pool = scored.groupby('signal_date').target_return.mean()
    for name, column in [('distribution_utility', 'utility_score'), ('binary_control', 'binary_probability'), ('momentum', 'return_20d')]:
        daily = daily_portfolio(rank_candidates(scored, column, protocol['primary_top_k']), pool)
        portfolios[name] = daily
    random, _ = random_portfolios(scored, [protocol['primary_top_k']], protocol['random_replicates'])
    portfolios['random_mean'] = random[protocol['primary_top_k']]
    comparisons = {}
    for name in ['binary_control', 'momentum', 'random_mean']:
        delta = portfolios['distribution_utility'].mean_return - portfolios[name].mean_return
        comparisons[name] = block_interval(delta.to_numpy(), protocol['bootstrap_samples'], protocol['bootstrap_block_sessions'],
                                          .05 / 3, protocol['bootstrap_seed'])
    return scored, {'policy': policy, 'probability': probability_metrics(scored, scored.probability_above_cost.to_numpy(),
                                                                      'target', bundle['baseline_probability']),
                     'binary_probability': probability_metrics(scored, scored.binary_probability.to_numpy(),
                                                               'target', bundle['baseline_probability']),
                     'top20': {name: {column: float(daily[column].mean()) for column in
                                      ['absolute_success_rate', 'net_return_proxy', 'excess_vs_pool']}
                               for name, daily in portfolios.items()}, 'paired_top20': comparisons}


def render_report(summary):
    lines = ['# Selective Payoff-Distribution Research', '',
             'RESEARCH_ONLY. No new algorithm discovery, financial guarantee, conformal guarantee or independent final validation is claimed.',
             'Four payoff bins, three calibrated seed models, pessimistic ensemble utility and a separately fitted abstention policy.',
             'This is an engineering experiment inspired by selective prediction, not an implementation or proof of Deep Gamblers or conformal risk control.',
             'The ensemble floor/ceiling are model disagreement heuristics, NOT statistical confidence bounds.',
             'Clipped within-bin utility is a coarse train-derived proxy, NOT expected executable profit.', '',
             'Selected policy: ' + str(summary['policy']), '',
             '## Four Disjoint Partitions', '', str(summary['partitions']), '',
             '## Nine Policy-Calibration Trials', '',
             '| Probability floor | Loss ceiling | Cases | Dates | Date success | Simultaneous success lower | All-date net lower | Passed |',
             '|---:|---:|---:|---:|---:|---:|---:|---|']
    for row in summary['policy_trials']:
        p, m = row['policy'], row['metrics']
        lines.append(f"| {p['probability_floor']} | {p['downside_ceiling']} | {m['cases']} | {m['dates']} | {m['date_success_rate']} | {m['date_success_lower']} | {m['all_date_net_lower']} | {row['passed']} |")
    lines += ['', 'Five-session circular block bootstrap, 5,000 samples. Nine policies x two bounds use Bonferroni correction; approximate historical diagnostics, not an assumption-free guarantee.', '',
              '## Fixed Top20 Diagnostic, Not Activated Recommendations', '',
              '| Period | Method | Date success | Five-session net proxy | Excess vs pool |', '|---|---|---:|---:|---:|']
    for period, result in summary['results'].items():
        for name, m in result.get('top20', {}).items():
            lines.append(f"| {period} | {name} | {m['absolute_success_rate']:.4%} | {m['net_return_proxy']:.4%} | {m['excess_vs_pool']:.4%} |")
    lines += ['', '## External Policy/Probability Evidence', '', json_text(summary['results']), '',
              'Screen reasons: ' + ', '.join(summary['screen_reasons']),
              'Recommendation gate: False. No policy passing calibration means no forced recommendations.',
              'Complete-date coverage (all data, including immature tail): ' + str(summary['coverage']),
              'Whole incomplete dates are excluded; no resolving-stock-only hindsight ranking. This complete-date filter remains a limitation.',
              'Current-universe, adjusted-history, dependent and overlapping close-to-close outcome limitations remain.',
              'Existing broad candidate pool, scoring, public model and original forward records unchanged.', '',
              'Inspiration, not replication or claimed theoretical guarantee:',
              '- https://arxiv.org/abs/1907.00208', '- https://arxiv.org/abs/2310.01262', '',
              'Protocol SHA256: ' + summary['protocol_sha256'], 'Ignored run: ' + summary['run_dir'], '']
    return '\n'.join(lines)


def run_training(data_root, output_root, protocol, report_path):
    if (protocol['horizon_sessions'] != 5 or protocol['cost_assumption'] != .003
            or protocol['return_bin_edges'] != EDGES.tolist() or protocol['ensemble_seeds'] != SEEDS
            or protocol['policy_probability_floors'] != [.55, .6, .65] or protocol['policy_downside_ceilings'] != [.1, .2, .3]
            or protocol['policy_daily_cap'] != 5 or protocol['primary_top_k'] != 20
            or protocol['production_promotion'] is not False or protocol['candidate_pool_change'] is not False
            or protocol['test_hyperparameter_search'] is not False or protocol['conformal_guarantee_claim'] is not False
            or protocol['novelty_claim'] is not False):
        raise ValueError('Unsupported distributional protocol.')
    raw, source = load_snapshots(data_root)
    if (raw.attrs.get('feature_version') != HISTORY_FEATURE_VERSION or source.get('skipped_files')
            or raw.attrs.get('history_provenance', {}).get('failed_stocks', 0)):
        raise ValueError('Complete verified OHLCV history required.')
    dataset, coverage, data_metadata = complete_cohort(raw, protocol['labels_as_of'], protocol['minimum_stocks_per_date'])
    train, calibration, policy_calibration, test = four_partitions(dataset, protocol)
    evaluation_parts = {name: test[test.signal_date.between(pd.Timestamp(start), pd.Timestamp(end))]
                        for name, (start, end) in protocol['periods'].items()}
    if evaluation_parts[protocol['primary_period']].empty:
        raise ValueError('No complete outcomes in the required primary evaluation period.')
    root = Path(output_root)
    run_dir = root / 'runs' / (datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '_' + uuid.uuid4().hex[:8])
    run_dir.mkdir(parents=True, exist_ok=False)
    bundle = fit_distribution(train, calibration)
    bundle['policy'], trials = select_policy(score_frame(bundle, policy_calibration), protocol)
    bundle['protocol'] = protocol
    partitions = {name: partition_info(part) for name, part in
                  [('train', train), ('probability_calibration', calibration), ('policy_calibration', policy_calibration)]}
    protocol_hash = hashlib.sha256(json_text(protocol).encode()).hexdigest()
    implementation = {str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
                      for path in [Path(__file__), ROOT/'src/models/selected_price_model.py',
                                   ROOT/'src/models/relative_price_selection.py', ROOT/'src/models/price_forecaster.py',
                                   ROOT/'src/features/ohlcv_information.py', ROOT/'src/features/price_learning_dataset.py',
                                   ROOT/'src/features/completed_price_dataset.py']}
    as_of = pd.Timestamp(raw.loc[raw.signal_date.lt(pd.Timestamp(protocol['evaluation_start'])), 'signal_date'].max())
    bundle['metadata'] = {'schema': 'research_distributional_selector_v1', 'features': COLUMNS,
                          'trained_at': datetime.now(timezone.utc).isoformat(), 'as_of': str(as_of.date()),
                          'data_root': str(Path(data_root).resolve()), 'partitions': partitions,
                          'dataset_sha256': fit_data_digest(train, pd.concat([calibration, policy_calibration]), COLUMNS),
                          'protocol_sha256': protocol_hash, 'implementation_sha256': implementation,
                          'target_definition': data_metadata['target_definition'], 'recommendation_gate_passed': False}
    joblib.dump(bundle, run_dir/'model.joblib', compress=3)
    write_json(bundle['metadata'], run_dir/'model_metadata.json')
    results = {}
    period_coverage = {}
    for period, (start, end) in protocol['periods'].items():
        part = evaluation_parts[period]
        count = coverage[coverage.index.to_series().between(pd.Timestamp(start), pd.Timestamp(end)).to_numpy()]
        period_coverage[period] = {'eligible_dates': int(len(count)), 'complete_dates': int(count.included.sum()),
                                   'evaluated_rows': len(part)}
        if part.empty:
            results[period] = {'status': 'unavailable_no_complete_outcome_dates'}
            continue
        predictions, metrics = evaluate_period(bundle, part, protocol)
        predictions.to_csv(run_dir/(period + '.csv'), index=False)
        results[period] = {'status': 'historical_development_only', **metrics}
    main = results[protocol['primary_period']]
    reasons = []
    if bundle['policy'] is None:
        reasons.append('no_policy_passed_separate_policy_calibration')
    if main['policy']['cases'] < 100 or main['policy']['dates'] < 20:
        reasons.append('insufficient_external_policy_cases_or_dates')
    if main['policy']['date_success_lower'] is None or main['policy']['date_success_lower'] < .6:
        reasons.append('external_60_percent_success_lower_not_established')
    if main['policy']['all_date_net_lower'] is None or main['policy']['all_date_net_lower'] <= 0:
        reasons.append('external_positive_net_proxy_not_established')
    if any(row['lower'] is None or row['lower'] <= 0 for row in main['paired_top20'].values()):
        reasons.append('top20_advantage_over_all_references_not_established')
    summary = {'policy': bundle['policy'], 'policy_trials': trials, 'partitions': partitions,
               'results': results, 'coverage': {'eligible_dates': int(len(coverage)), 'complete_dates': int(coverage.included.sum()),
                                               'included_rows': len(dataset), 'by_period': period_coverage},
               'screen_reasons': reasons, 'development_screen_passed': not reasons, 'recommendation_gate_passed': False,
               'protocol': protocol, 'protocol_sha256': protocol_hash, 'implementation_sha256': implementation, 'run_dir': str(run_dir)}
    report_path = Path(report_path)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(render_report(summary), encoding='utf-8')
    write_json(summary, report_path.with_suffix('.json'))
    write_json({'run_id': run_dir.name}, root/'latest.json')
    print(json_text({'policy': bundle['policy'], 'screen_reasons': reasons, 'run_dir': str(run_dir)}), flush=True)
    return summary


def load_research(model_dir, now):
    root = Path(model_dir)
    run_id = json.loads((root/'latest.json').read_text())['run_id']
    if not run_id or run_id in {'.', '..'} or Path(run_id).name != run_id:
        raise ValueError('Invalid research run ID.')
    bundle = joblib.load(root/'runs'/run_id/'model.joblib')
    meta = bundle['metadata']
    if (meta.get('schema') != 'research_distributional_selector_v1' or bundle['features'] != COLUMNS
            or meta.get('recommendation_gate_passed') is not False or pd.Timestamp(meta['trained_at']) > pd.Timestamp(now)
            or pd.Timestamp(meta['as_of']).date() > now.date()):
        raise ValueError('Only already-trained research distribution bundles are supported.')
    return bundle


def research_inputs(bundle, data_root, now):
    raw, source = load_snapshots(data_root or bundle['metadata']['data_root'])
    if (raw.attrs.get('feature_version') != HISTORY_FEATURE_VERSION or source.get('skipped_files')
            or raw.attrs.get('history_provenance', {}).get('failed_stocks', 0)):
        raise ValueError('Verified complete price history required.')
    cutoff = pd.Timestamp(completed_price_cutoff(now))
    return prepare_selected_features(raw[raw.signal_date.le(cutoff) & raw.snapshot_date.le(cutoff)].copy(), COLUMNS)


def query(model_dir, data_root, stock, now=None):
    now = now or datetime.now(KST)
    if now.tzinfo is None:
        raise ValueError('Timezone-aware query required.')
    now = now.astimezone(KST)
    bundle = load_research(model_dir, now)
    frame = research_inputs(bundle, data_root, now)
    code = resolve_stock(stock, [ROOT, Path(data_root or bundle['metadata']['data_root'])])
    row = frame[frame.stock_code.eq(code)].sort_values('signal_date').tail(1)
    if row.empty or row.volume_ratio_20d.iloc[0] <= 0:
        raise ValueError('No active completed data for stock.')
    output = predict_distribution(bundle, row[COLUMNS]).iloc[0].to_dict()
    return {'stock_code': code, 'signal_date': str(pd.Timestamp(row.signal_date.iloc[0]).date()), **output,
            'policy_available': bundle['policy'] is not None, 'recommendation': 'ABSTAIN',
            'status': 'STALE_DATA' if (now.date()-pd.Timestamp(row.signal_date.iloc[0]).date()).days > 7 else 'RESEARCH_ONLY',
            'note': 'Ensemble bounds/disagreement are heuristics, NOT validated confidence; clipped return and utility are coarse proxies.'}


def freeze(model_dir, data_root, output_dir, now=None):
    now = now or datetime.now(KST)
    if now.tzinfo is None:
        raise ValueError('Timezone-aware recording time required.')
    now = now.astimezone(KST)
    bundle = load_research(model_dir, now)
    frame = research_inputs(bundle, data_root, now)
    origin = frame.signal_date.max()
    if pd.Timestamp(bundle['metadata']['as_of']) >= origin:
        raise ValueError('Signal must follow fit as-of date.')
    if not valid_record_time(origin, pd.Timestamp(now)):
        return {'status': 'outside_recording_window_no_backdated_forecast', 'frozen_predictions': 0}
    latest = frame[frame.signal_date.eq(origin) & np.isfinite(frame[COLUMNS]).all(axis=1)
                   & frame.volume_ratio_20d.gt(0)].copy().reset_index(drop=True)
    if latest.empty:
        raise ValueError('No eligible forward observations.')
    ledger = pd.concat([latest[['stock_code', 'signal_date']].reset_index(drop=True), predict_distribution(bundle, latest[COLUMNS])], axis=1)
    meta = bundle['metadata']
    ledger['origin_close'] = latest.close.to_numpy()
    ledger['recorded_at'], ledger['model_trained_at'] = now.isoformat(), meta['trained_at']
    ledger['model_dataset_sha256'] = meta['dataset_sha256']
    ledger['horizon_sessions'], ledger['cost_assumption'] = 5, .003
    ledger['validation_base_rate'] = bundle['baseline_probability']
    ledger['selected_by_research_policy'] = policy_selection(ledger, bundle['policy'], bundle['protocol'])
    ledger['recommendation'] = 'ABSTAIN'
    ledger['prediction_id'] = [hashlib.sha256('|'.join([code, str(origin.date()), meta['dataset_sha256'], meta['trained_at']]).encode()).hexdigest()[:20] for code in ledger.stock_code]
    key = hashlib.sha256((meta['dataset_sha256']+meta['trained_at']).encode()).hexdigest()[:16]
    output = Path(output_dir)/f'ml_distribution_forward_{origin:%Y%m%d}_{key}.csv'
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open('x', encoding='utf-8-sig') as handle:
        ledger.to_csv(handle, index=False)
    return {'status': 'awaiting_future_outcomes', 'frozen_predictions': len(ledger), 'ledger': str(output)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['train', 'predict', 'freeze'])
    parser.add_argument('--protocol', type=Path, default=ROOT/'docs/model_experiments/distributional_selector_protocol_20261021.json')
    parser.add_argument('--data-root', type=Path)
    parser.add_argument('--model-dir', type=Path, default=ROOT/'data/models/price_distribution_selector')
    parser.add_argument('--stock')
    parser.add_argument('--output-dir', type=Path, default=ROOT/'data/predictions')
    parser.add_argument('--report-path', type=Path, default=ROOT/'reports/daily_review/2026-10-21_distributional_selector.md')
    args = parser.parse_args()
    try:
        if args.command == 'train':
            protocol = json.loads(args.protocol.read_text())
            run_training(args.data_root or ROOT/protocol['data_root'], args.model_dir, protocol, args.report_path)
        elif args.command == 'predict':
            if not args.stock:
                raise ValueError('predict requires --stock')
            print(json_text(query(args.model_dir, args.data_root, args.stock)))
        else:
            print(json_text(freeze(args.model_dir, args.data_root, args.output_dir)))
    except FileExistsError:
        parser.exit(2, 'Original research ledger exists; preserved without overwrite.\n')
    except (ValueError, FileNotFoundError) as error:
        parser.exit(2, str(error)+'\n')
    except Exception as error:
        parser.exit(2, 'Distribution research failed: '+type(error).__name__+'\n')


if __name__ == '__main__':
    main()
