"""Audit the execution target and freeze a separate, unapproved research model."""
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
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import brier_score_loss, roc_auc_score
from threadpoolctl import threadpool_limits

from src.crawler.market_clock import KST, completed_price_cutoff
from src.evaluator.forward_price_forecast import valid_record_time
from src.evaluator.next_open_provenance import seal_provenance
from src.features.completed_price_dataset import HISTORY_FEATURE_VERSION
from src.features.next_open_dataset import TARGET_VERSION, build_next_open_dataset, valid_candle
from src.features.price_learning_dataset import load_snapshots, temporal_partitions
from src.models.monthly_price_walkforward import monthly_split, paired_interval
from src.models.improvement_families import BASELINE, family_spec
from src.models.price_forecaster import date_weights, fit_estimator, json_text, resolve_stock
from src.models.relative_price_selection import block_interval, rank_candidates
from src.models.selected_price_model import (
    COLUMNS, ROOT, factories, fit_data_digest, partition_info, prepare_selected_features,
    to_logits, write_json,
)


def load_inputs(data_root, as_of):
    audit = raw_audit(data_root)
    structural = ['duplicate_dates', 'invalid_dates', 'weekend_dates', 'nonfinite_ohlcv',
                  'nonpositive_close', 'negative_volume', 'invalid_active_candles']
    if any(audit[key] for key in structural):
        raise ValueError('Raw history has structural defects; do not silently clean and train.')
    raw, source = load_snapshots(data_root)
    provenance = raw.attrs.get('history_provenance', {})
    if (raw.attrs.get('feature_version') != HISTORY_FEATURE_VERSION or source.get('skipped_files')
            or provenance.get('failed_stocks', 0) or provenance.get('unreadable_stocks', 0)):
        raise ValueError('Complete checksum-verified historical inputs are required.')
    cutoff = pd.Timestamp(as_of)
    raw = raw[raw.signal_date.le(cutoff) & raw.snapshot_date.le(cutoff)].copy()
    return prepare_selected_features(raw, COLUMNS), provenance


def fit_classifier(train, calibration, reference=False, family=BASELINE):
    def labels(part):
        return part.same_close_return_reference.gt(.003).astype(int) if reference else part.target.astype(int)
    if train.label_available_date.max() >= calibration.signal_date.min():
        raise ValueError('Training labels overlap calibration.')
    if labels(train).nunique() != 2 or labels(calibration).nunique() != 2:
        raise ValueError('Both target classes required.')
    with threadpool_limits(limits=2):
        model = fit_estimator(factories()[family_spec(family)['factory']], train[COLUMNS], labels(train), date_weights(train))
        calibrator = LogisticRegression(C=1., solver='liblinear', max_iter=1000, random_state=42)
        calibrator.fit(to_logits(model.predict_proba(calibration[COLUMNS])[:, 1]), labels(calibration),
                       sample_weight=date_weights(calibration))
    return {'classifier': model, 'calibrator': calibrator}


def predict_probability(bundle, frame):
    if not np.isfinite(frame[COLUMNS]).all(axis=None):
        raise ValueError('Finite matching feature inputs required.')
    with threadpool_limits(limits=2):
        p = bundle['calibrator'].predict_proba(to_logits(bundle['classifier'].predict_proba(frame[COLUMNS])[:, 1]))[:, 1]
    if not np.isfinite(p).all() or np.any((p < 0) | (p > 1)):
        raise ValueError('Invalid probability output.')
    return p


def selection_summary(frame, selected):
    picked = frame.loc[selected].copy()
    resolved = picked[picked.target.notna()]
    dates = pd.DatetimeIndex(sorted(frame.signal_date.unique()))
    missing = picked.target.isna().sum()
    daily = resolved.groupby('signal_date').net_return_proxy.mean().reindex(dates, fill_value=0)
    # A missing selected outcome is not zero exposure. Withhold full-return
    # claims instead of silently averaging surviving stocks or replacing picks.
    interval = block_interval(daily.to_numpy()) if not missing and len(dates) >= 20 else {}
    successes = resolved.groupby('signal_date').target.mean()
    return {
        'selected_cases': len(picked), 'selected_dates': int(picked.signal_date.nunique()),
        'evaluated_cases': len(resolved), 'unresolved_cases': int(missing),
        'outcome_coverage': len(resolved) / len(picked) if len(picked) else None,
        'conditional_success_rate': float(resolved.target.mean()) if len(resolved) else None,
        'conditional_date_success_rate': float(successes.mean()) if len(successes) else None,
        'conditional_mean_net_return_proxy': float(resolved.net_return_proxy.mean()) if len(resolved) else None,
        'all_date_net_return_proxy': float(daily.mean()) if not missing else None,
        'all_date_net_lower_95': interval.get('lower'),
        'unknown_states': {str(k): int(v) for k, v in picked[picked.target.isna()].label_status.value_counts().items()},
    }


def evaluate(frame, probability, prior, threshold=.6, cap=5):
    scored = frame.copy().reset_index(drop=True)
    scored['probability_above_cost'] = probability
    ranked = rank_candidates(scored, 'probability_above_cost', 20)
    top_mask = scored.index.isin(ranked.index)
    policy = rank_candidates(scored[scored.probability_above_cost.ge(threshold)], 'probability_above_cost', cap)
    policy_mask = scored.index.isin(policy.index)
    scored['fixed_policy_selected'] = policy_mask
    scored['top20_monitoring_only'] = top_mask
    scored['recommendation'] = 'ABSTAIN'
    observed = scored[scored.target.notna()]
    metrics = {'input_candidates': len(scored), 'signal_dates': int(scored.signal_date.nunique()),
               'evaluated_cases': len(observed), 'unresolved_cases': int(scored.target.isna().sum()),
               'date_brier': None, 'past_constant_date_brier': None, 'mean_daily_auc': None,
               'top20': selection_summary(scored, top_mask), 'fixed_policy': selection_summary(scored, policy_mask)}
    if len(observed):
        weights = date_weights(observed)
        metrics['date_brier'] = float(brier_score_loss(observed.target, observed.probability_above_cost, sample_weight=weights))
        metrics['past_constant_date_brier'] = float(brier_score_loss(observed.target, np.full(len(observed), prior), sample_weight=weights))
        auc = [roc_auc_score(day.target, day.probability_above_cost) for _, day in observed.groupby('signal_date') if day.target.nunique() == 2]
        metrics['mean_daily_auc'] = float(np.mean(auc)) if auc else None
    return scored, metrics


def raw_audit(data_root):
    root = Path(data_root)
    manifest = json.loads((root / 'history_manifest.json').read_text())
    counts = dict(rows=0, duplicate_dates=0, invalid_dates=0, weekend_dates=0,
                  nonfinite_ohlcv=0, nonpositive_close=0, negative_volume=0,
                  zero_volume=0, invalid_active_candles=0, exceptional_one_day_moves=0)
    for stock in manifest['stocks']:
        if stock['status'] != 'success':
            continue
        f = pd.read_csv(root / 'raw' / (stock['stock_code'] + '.csv'))
        days = pd.to_datetime(f.date, errors='coerce')
        v = f[['open', 'high', 'low', 'close', 'volume']].apply(pd.to_numeric, errors='coerce')
        counts['rows'] += len(f)
        counts['duplicate_dates'] += int(days.duplicated().sum())
        counts['invalid_dates'] += int(days.isna().sum())
        counts['weekend_dates'] += int(days.dt.dayofweek.ge(5).sum())
        counts['nonfinite_ohlcv'] += int((~np.isfinite(v).all(axis=1)).sum())
        counts['nonpositive_close'] += int(v.close.le(0).sum())
        counts['negative_volume'] += int(v.volume.lt(0).sum())
        counts['zero_volume'] += int(v.volume.eq(0).sum())
        counts['invalid_active_candles'] += int((v.volume.gt(0) & ~valid_candle(v)).sum())
        counts['exceptional_one_day_moves'] += int(v.assign(date=days).sort_values('date').close.pct_change(fill_method=None).abs().gt(.305).sum())
    return counts


def implementation_digest():
    digest = hashlib.sha256()
    for path in [Path(__file__), ROOT / 'src/features/next_open_dataset.py',
                 ROOT / 'src/features/ohlcv_information.py', ROOT / 'src/models/selected_price_model.py',
                 ROOT / 'src/models/price_forecaster.py', ROOT / 'src/models/monthly_price_walkforward.py',
                 ROOT / 'src/models/improvement_families.py']:
        digest.update(str(path.relative_to(ROOT)).encode())
        digest.update(path.read_bytes())
    return digest.hexdigest()


def render_report(summary):
    lines = ['# Execution Target Audit / 진입 가격 기준 점검', '',
             'RESEARCH_ONLY. No recommendation, production promotion, candidate-pool reduction or legacy label rewrite.', '',
             '## What Changed', '',
             'The signal uses completed closing data. The new target starts at the NEXT observed session open, not the already observed signal close.',
             'Both fixed ExtraTrees models use the same 19 inputs, training/calibration dates and resolved fit rows. Only the supervised target differs.',
             'Both are evaluated on the new next-open target. This is NOT a before/after success-rate comparison against different answers.',
             'Rank and threshold selections use every input-eligible candidate before outcomes are inspected. Unknown picks are never replaced.',
             'Suspended/missing execution bars and exceptional single-session price discontinuities remain explicitly unresolved. Corporate-action causes are not inferred.',
             'The 30.5% review threshold is a conservative research heuristic, not a claim about all exchange rules. Multi-session gains are not clipped.', '',
             '## Raw Data Audit', '', '```json', json_text(summary['raw_audit']), '```', '',
             '## Outcome Audit', '', '```json', json_text(summary['dataset']), '```', '',
             '## Matched Historical Development Results', '',
             '| Period | Training target | Input candidates | Resolved | Unresolved | Date Brier | Past constant Brier | Daily AUC |',
             '|---|---|---:|---:|---:|---:|---:|---:|']
    for period, roles in summary['results'].items():
        for role, m in roles.items():
            lines.append(f"| {period} | {role} | {m['input_candidates']} | {m['evaluated_cases']} | {m['unresolved_cases']} | {m['date_brier']} | {m['past_constant_date_brier']} | {m['mean_daily_auc']} |")
    lines += ['', 'Success/return numbers below are conditional on resolved outcomes. They are not complete-policy performance when unresolved > 0.', '',
              '| Period | Training target | Group | Selected | Resolved | Unresolved | Conditional success | Conditional daily success | Conditional net proxy | Full-policy all-date net proxy |',
              '|---|---|---|---:|---:|---:|---:|---:|---:|---:|']
    for period, roles in summary['results'].items():
        for role, metrics in roles.items():
            for group in ['fixed_policy', 'top20']:
                m = metrics[group]
                lines.append(f"| {period} | {role} | {group} | {m['selected_cases']} | {m['evaluated_cases']} | {m['unresolved_cases']} | {m['conditional_success_rate']} | {m['conditional_date_success_rate']} | {m['conditional_mean_net_return_proxy']} | {m['all_date_net_return_proxy']} |")
    lines += ['', '## Paired Probability Error: New Minus Control', '',
              'Negative favors next-open training; five-session-block intervals are development diagnostics only.', '',
              '```json', json_text(summary['paired_brier']), '```', '',
              '## Timing and Limits', '', '```json', json_text(summary['partitions']), '```', '',
              'Repeatedly inspected historical dates are development evidence, not independent final validation. No hyperparameter or policy search was performed.',
              'Current-universe survivorship, retrospective adjustments, an observed-universe calendar, exceptional corporate actions and unmodeled fills remain limitations.',
              'Overlapping five-session returns minus 0.3% assumed cost are research proxies, not compounded trading returns or investment advice.',
              'All output recommendations remain ABSTAIN. Genuine new predictions require immutable recording after signal close and before next opening.', '']
    return '\n'.join(lines)


def run_experiment(data_root, output_root, protocol, report_path):
    if (protocol['algorithm'] != 'extra_trees_fixed_existing_parameters' or protocol['features'] != 'existing_19_ohlcv_only'
            or protocol['horizon_sessions'] != 5
            or protocol['cost_assumption'] != .003 or protocol['probability_threshold'] != .6
            or protocol['daily_selection_cap'] != 5 or protocol.get('production_promotion') is not False):
        raise ValueError('Unsupported fixed execution audit protocol.')
    inputs, provenance = load_inputs(data_root, protocol['labels_as_of'])
    cohort, dataset_metadata = build_next_open_dataset(inputs, protocol['labels_as_of'])
    known = cohort[cohort.target.notna()].copy()
    train, calibration, _ = temporal_partitions(known, protocol['calibration_start'], protocol['evaluation_start'])
    digest = fit_data_digest(train, calibration, COLUMNS)
    trained_at = datetime.now(timezone.utc).isoformat()
    run_id = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '_' + uuid.uuid4().hex[:8]
    run = Path(output_root) / 'runs' / run_id
    run.mkdir(parents=True, exist_ok=False)
    prior = float(np.average(calibration.target, weights=date_weights(calibration)))
    metadata = dict(target_version=TARGET_VERSION, features=COLUMNS, dataset_sha256=digest,
                    trained_at=trained_at, as_of=str(calibration.label_available_date.max().date()),
                    data_root=str(Path(data_root).resolve()), horizon_sessions=5, cost_assumption=.003,
                    status='RESEARCH_ONLY', recommendation_enabled=False, history_provenance=provenance,
                    partitions={'train': partition_info(train), 'calibration': partition_info(calibration)},
                    protocol=protocol, baseline_probability=prior)
    metadata['implementation_sha256'] = implementation_digest()
    metadata['protocol_sha256'] = hashlib.sha256(json_text(protocol).encode()).hexdigest()
    results, predictions = {}, {}
    models = {}
    for role, reference in [('same_close_trained_control', True), ('next_open_trained', False)]:
        print('Fitting fixed target audit: ' + role, flush=True)
        bundle = fit_classifier(train, calibration, reference)
        bundle['metadata'] = metadata
        models[role] = bundle
        for period, (start, end) in protocol['periods'].items():
            frame = cohort[cohort.signal_date.between(start, end)].copy()
            if frame.empty:
                raise ValueError('No eligible candidates in required audit period: ' + period)
            scored, metrics = evaluate(frame, predict_probability(bundle, frame), prior)
            results.setdefault(period, {})[role] = metrics
            predictions.setdefault(period, {})[role] = scored
            scored[['stock_code', 'signal_date', 'entry_date', 'target_date', 'label_available_date', 'label_status',
                    'target', 'target_return', 'net_return_proxy', 'probability_above_cost',
                    'fixed_policy_selected', 'top20_monitoring_only', 'recommendation']].to_csv(
                        run / (period + '_' + role + '.csv'), index=False)
    paired = {}
    for period, roles in predictions.items():
        reference = roles['same_close_trained_control']
        mask = reference.target.notna()
        candidate = roles['next_open_trained']
        paired[period] = paired_interval(reference[mask].reset_index(drop=True), candidate[mask].reset_index(drop=True))
    joblib.dump(models['next_open_trained'], run / 'model.joblib')
    write_json(metadata, run / 'model_metadata.json')
    summary = dict(run_dir=str(run.resolve()), raw_audit=raw_audit(data_root), dataset=dataset_metadata,
                   partitions=metadata['partitions'], results=results, paired_brier=paired,
                   recommendation_gate_passed=False, gate_reasons=['no_independent_next_open_forward_evidence'])
    write_json(summary, run / 'summary.json')
    report = Path(report_path)
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text(render_report(summary), encoding='utf-8')
    write_json(summary, report.with_suffix('.json'))
    write_json({'run_dir': str(run.resolve()), 'model_sha256': hashlib.sha256((run / 'model.joblib').read_bytes()).hexdigest()},
               Path(output_root) / 'latest.json')
    return summary


def load_model(model_root):
    pointer = json.loads((Path(model_root) / 'latest.json').read_text())
    path = Path(pointer['run_dir']) / 'model.joblib'
    if hashlib.sha256(path.read_bytes()).hexdigest() != pointer['model_sha256']:
        raise ValueError('Next-open model checksum mismatch.')
    bundle = joblib.load(path)
    m = bundle['metadata']
    if m['target_version'] != TARGET_VERSION or m['features'] != COLUMNS or m['recommendation_enabled'] is not False:
        raise ValueError('Unsupported research bundle.')
    return bundle


def fit_current(data_root, output_root, as_of, family=BASELINE):
    """Fit a fixed recent-data protocol for FUTURE evaluation, never past scoring."""
    if pd.Timestamp(as_of).date() > completed_price_cutoff():
        raise ValueError('Completed labels only.')
    inputs, provenance = load_inputs(data_root, as_of)
    cohort, dataset_metadata = build_next_open_dataset(inputs, as_of)
    known = cohort[cohort.target.notna()].copy()
    spec = family_spec(family)
    train, calibration = monthly_split(known, as_of, training_sessions=spec['training_sessions'],
                                       calibration_sessions=spec['calibration_sessions'])
    bundle = fit_classifier(train, calibration, family=family)
    digest = fit_data_digest(train, calibration, COLUMNS)
    bundle['metadata'] = dict(
        target_version=TARGET_VERSION, features=COLUMNS, dataset_sha256=digest, model_family=family,
        trained_at=datetime.now(timezone.utc).isoformat(), as_of=str(calibration.label_available_date.max().date()),
        requested_as_of=str(pd.Timestamp(as_of).date()),
        data_root=str(Path(data_root).resolve()), horizon_sessions=5, cost_assumption=.003,
        status='RESEARCH_ONLY', recommendation_enabled=False, history_provenance=provenance,
        baseline_probability=float(np.average(calibration.target, weights=date_weights(calibration))),
        partitions={'train': partition_info(train), 'calibration': partition_info(calibration)},
        fitting_protocol={**spec, 'features': COLUMNS,
                          'selection': 'Prespecified family; no historical performance-based promotion'},
        evaluation_role='New forward-only challenger; recent calibration outcomes are NOT independent test results',
        dataset=dataset_metadata)
    bundle['metadata']['implementation_sha256'] = implementation_digest()
    run_id = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '_' + uuid.uuid4().hex[:8]
    run = Path(output_root) / 'runs' / run_id
    run.mkdir(parents=True, exist_ok=False)
    joblib.dump(bundle, run / 'model.joblib')
    write_json(bundle['metadata'], run / 'model_metadata.json')
    write_json({'run_dir': str(run.resolve()), 'model_sha256': hashlib.sha256((run / 'model.joblib').read_bytes()).hexdigest()},
               Path(output_root) / 'latest.json')
    return {'run_dir': str(run.resolve()), 'partitions': bundle['metadata']['partitions'],
            'status': 'awaiting_genuine_forward_evaluation', 'recommendation_enabled': False}


def current_predictions(bundle, data_root, now=None):
    now = now or datetime.now(KST)
    if now.tzinfo is None or pd.Timestamp(bundle['metadata']['trained_at']) > pd.Timestamp(now):
        raise ValueError('Timezone-aware current time after model creation required.')
    inputs, _ = load_inputs(data_root, completed_price_cutoff(now))
    origin = inputs.signal_date.max()
    latest = inputs[inputs.signal_date.eq(origin) & inputs.volume.gt(0)
                    & np.isfinite(inputs[COLUMNS]).all(axis=1)].copy().sort_values('stock_code')
    if latest.empty:
        raise ValueError('No eligible completed inputs.')
    frame = latest[['stock_code', 'signal_date']].reset_index(drop=True)
    frame['origin_close'] = latest.close.to_numpy()
    frame['source_manifest_sha256'] = hashlib.sha256((Path(data_root) / 'history_manifest.json').read_bytes()).hexdigest()
    frame['probability_above_cost'] = predict_probability(bundle, latest)
    frame['recommendation'], frame['status'] = 'ABSTAIN', 'RESEARCH_ONLY'
    return frame


def freeze(bundle, data_root, output_dir, now=None):
    live_clock = now is None
    now = now or datetime.now(KST)
    frame = current_predictions(bundle, data_root, now)
    if live_clock:
        now = datetime.now(KST)
    origin = frame.signal_date.max()
    if not (valid_record_time(origin, pd.Timestamp(now))
            and valid_record_time(origin, pd.Timestamp(now) + pd.Timedelta(seconds=60))):
        raise ValueError('Outside recording window; never backdate predictions.')
    m = bundle['metadata']
    if pd.Timestamp(m['as_of']) > origin:
        raise ValueError('The last fitted label date cannot follow the signal close.')
    frame['recorded_at'] = now.isoformat()
    frame['model_dataset_sha256'], frame['model_trained_at'] = m['dataset_sha256'], m['trained_at']
    frame['target_version'], frame['horizon_sessions'], frame['cost_assumption'] = TARGET_VERSION, 5, .003
    frame['validation_base_rate'] = m['baseline_probability']
    frame['prediction_id'] = [hashlib.sha256('|'.join([code, str(origin.date()), m['dataset_sha256'], m['trained_at'], TARGET_VERSION]).encode()).hexdigest()[:24] for code in frame.stock_code]
    frame['fixed_policy_selected'] = frame.index.isin(rank_candidates(frame[frame.probability_above_cost.ge(.6)], 'probability_above_cost', 5).index)
    key = hashlib.sha256((m['dataset_sha256'] + m['trained_at']).encode()).hexdigest()[:16]
    path = Path(output_dir) / f'ml_next_open_forward_{origin:%Y%m%d}_{key}.csv'
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('x', encoding='utf-8-sig') as handle:
        frame.to_csv(handle, index=False)
    seal_provenance(path, m)
    return {'status': 'awaiting_future_outcomes', 'predictions': len(frame), 'ledger': str(path), 'recommendation_enabled': False}


def query_stock(bundle, data_root, query, now=None):
    code = resolve_stock(query, [ROOT, Path(data_root)])
    frame = current_predictions(bundle, data_root, now)
    result = frame[frame.stock_code.eq(code)]
    if result.empty:
        raise ValueError('No current eligible completed inputs for this stock.')
    return result.iloc[0].to_dict() | {
        'requested_stock': query, 'target_version': TARGET_VERSION,
        'note': 'Unapproved research probability, not measured reliability or a buy recommendation.'}


def grade(ledger, inputs, as_of, now=None):
    now = pd.Timestamp(now or datetime.now(KST))
    required = {'prediction_id', 'stock_code', 'signal_date', 'recorded_at', 'model_trained_at',
                'target_version', 'horizon_sessions', 'cost_assumption', 'probability_above_cost', 'validation_base_rate'}
    if (not required.issubset(ledger) or ledger.empty or ledger.prediction_id.duplicated().any()
            or ledger.duplicated(['stock_code', 'signal_date']).any()
            or not ledger.target_version.eq(TARGET_VERSION).all() or not ledger.horizon_sessions.eq(5).all()
            or not ledger.cost_assumption.eq(.003).all() or now.tzinfo is None
            or pd.Timestamp(as_of).date() > completed_price_cutoff(now.to_pydatetime())):
        raise ValueError('Invalid original next-open ledger or grading cutoff.')
    original = ledger.copy()
    original['signal_date'] = pd.to_datetime(original.signal_date)
    p = original[['probability_above_cost', 'validation_base_rate']].to_numpy(dtype=float)
    if not np.isfinite(p).all() or np.any((p < 0) | (p > 1)):
        raise ValueError('Invalid frozen probabilities.')
    for row in original.itertuples():
        recorded, trained = pd.Timestamp(row.recorded_at), pd.Timestamp(row.model_trained_at)
        if (recorded.tzinfo is None or trained.tzinfo is None or trained > recorded or recorded > now
                or not valid_record_time(row.signal_date, recorded)):
            raise ValueError('Invalid original prediction/model recording time.')
    outcomes, _ = build_next_open_dataset(inputs, as_of, candidate_keys=original)
    keys = ['stock_code', 'signal_date']
    cols = keys + ['entry_date', 'entry_open', 'target_date', 'label_available_date',
                   'label_status', 'target_return', 'net_return_proxy', 'target']
    result = original.merge(outcomes[cols], on=keys, how='left', validate='1:1')
    result['label_status'] = result.label_status.fillna('missing_original_signal_prices')
    observed = result[result.target.notna()]
    summary = dict(recorded_candidates=len(result), evaluated_cases=len(observed),
                   unresolved_cases=int(result.target.isna().sum()),
                   states={str(k): int(v) for k, v in result.label_status.value_counts().items()},
                   pooled_success_rate=float(observed.target.mean()) if len(observed) else None,
                   date_brier=None, frozen_baseline_date_brier=None,
                   recommendation_enabled=False)
    summary['status'] = ('awaiting_future_outcomes' if result.label_status.eq('awaiting_future_sessions').all()
                         else 'incomplete_forward_outcomes' if result.target.isna().any()
                         else 'forward_results_available')
    if 'fixed_policy_selected' in result:
        selected = result.fixed_policy_selected.map({True: True, False: False, 'True': True, 'False': False})
        if selected.isna().any():
            raise ValueError('Invalid frozen policy selection.')
        summary['fixed_policy'] = selection_summary(result, selected.astype(bool))
    if len(observed):
        weights = date_weights(observed)
        summary['date_brier'] = float(brier_score_loss(observed.target, observed.probability_above_cost, sample_weight=weights))
        summary['frozen_baseline_date_brier'] = float(brier_score_loss(observed.target, observed.validation_base_rate, sample_weight=weights))
    return result, summary


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['train', 'fit-current', 'predict', 'freeze', 'grade'])
    parser.add_argument('--data-root', type=Path)
    parser.add_argument('--model-dir', type=Path)
    parser.add_argument('--protocol', type=Path, default=ROOT / 'docs/model_experiments/next_open_protocol_20261021.json')
    parser.add_argument('--report', type=Path, default=ROOT / 'reports/daily_review/2026-10-21_execution_target_audit.md')
    parser.add_argument('--output-dir', type=Path, default=ROOT / 'data/predictions')
    parser.add_argument('--stock')
    parser.add_argument('--as-of', default=completed_price_cutoff().isoformat())
    parser.add_argument('--ledger', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.model_dir is None:
        name = 'price_next_open' if args.command == 'train' else 'price_next_open_current'
        args.model_dir = ROOT / 'data/models' / name
    if args.command == 'train':
        protocol = json.loads(args.protocol.read_text())
        summary = run_experiment(args.data_root or ROOT / protocol['data_root'], args.model_dir, protocol, args.report)
        print(json_text({'run_dir': summary['run_dir'], 'recommendation_gate_passed': False}))
    elif args.command == 'fit-current':
        if not args.data_root:
            parser.error('fit-current requires --data-root')
        if args.model_dir.resolve() == (ROOT / 'data/models/price_next_open').resolve():
            parser.error('Use a separate model-dir; preserve the historical matched audit model.')
        print(json_text(fit_current(args.data_root, args.model_dir, args.as_of)))
    elif args.command == 'grade':
        if not args.data_root or not args.ledger or not args.output:
            parser.error('grade requires --data-root, --ledger and a separate --output')
        if args.output.resolve() == args.ledger.resolve():
            parser.error('Never overwrite an original prediction ledger.')
        inputs, _ = load_inputs(args.data_root, args.as_of)
        ledger = pd.read_csv(args.ledger, dtype={'stock_code': str})
        result, summary = grade(ledger, inputs, args.as_of)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        result.to_csv(args.output, index=False)
        print(json_text(summary))
    else:
        bundle = load_model(args.model_dir)
        data_root = args.data_root or bundle['metadata']['data_root']
        if args.command == 'freeze':
            print(json_text(freeze(bundle, data_root, args.output_dir)))
        else:
            if not args.stock:
                parser.error('predict requires --stock')
            print(json_text(query_stock(bundle, data_root, args.stock)))


if __name__ == '__main__':
    main()
