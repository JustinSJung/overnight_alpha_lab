"""Training-only family selection and empirical uncertainty; research use only."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import sys
import uuid

import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier, HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import brier_score_loss
from sklearn.model_selection import TimeSeriesSplit
from threadpoolctl import threadpool_limits

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from src.crawler.market_clock import KST, completed_price_cutoff
from src.features.completed_price_dataset import HISTORY_FEATURE_VERSION
from src.features.market_context import MARKET_FEATURES, add_market_context
from src.features.ohlcv_information import OHLCV_FEATURES, add_ohlcv_information
from src.features.price_learning_dataset import FEATURES, build_dataset, load_snapshots, make_features, temporal_partitions
from src.models.monthly_price_walkforward import paired_interval, summarize
from src.models.ohlcv_information_experiment import development_screen
from src.models.price_forecaster import classifiers, date_weights, fit_estimator, json_text, new_regressor, resolve_stock

COLUMNS = FEATURES + OHLCV_FEATURES
CONTEXT_COLUMNS = COLUMNS + MARKET_FEATURES
NAMES = ['linear', 'hgb_shallow', 'hgb_medium', 'extra_trees', 'fixed_mean']


def checked_columns(columns):
    columns = list(columns)
    if columns != COLUMNS and columns != CONTEXT_COLUMNS:
        raise ValueError('Unsupported selected-model feature schema.')
    return columns


def prepare_selected_features(raw, columns, min_stocks=100):
    columns = checked_columns(columns)
    frame = add_ohlcv_information(raw)
    if columns == CONTEXT_COLUMNS:
        frame = add_market_context(frame, min_stocks)
    frame[FEATURES] = make_features(frame)
    return frame


def fit_data_digest(train, calibration, columns):
    fit_rows = pd.concat([train.assign(partition='train'), calibration.assign(partition='calibration')])
    keys = ['partition', 'stock_code', 'signal_date', 'label_available_date', 'target', 'target_return'] + checked_columns(columns)
    return hashlib.sha256(pd.util.hash_pandas_object(
        fit_rows[keys].sort_values(['partition', 'signal_date', 'stock_code']),
        index=False).to_numpy().tobytes()).hexdigest()


def factories():
    existing = classifiers()
    return {
        'linear': existing['logistic_regression'],
        'hgb_shallow': existing['hist_gradient_boosting'],
        'hgb_medium': HistGradientBoostingClassifier(max_iter=150, learning_rate=.04, max_leaf_nodes=15,
                                                     max_depth=4, min_samples_leaf=160, l2_regularization=20,
                                                     early_stopping=False, random_state=42),
        'extra_trees': ExtraTreesClassifier(n_estimators=96, max_depth=12, min_samples_leaf=100,
                                            max_features=.75, n_jobs=2, random_state=42),
    }


def write_json(value, path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(json_text(value) + '\n', encoding='utf-8')
    os.replace(temporary, path)


def raw_probability(models, name, features):
    if name == 'fixed_mean':
        values = np.mean([models[key].predict_proba(features)[:, 1] for key in factories()], axis=0)
    else:
        values = models[name].predict_proba(features)[:, 1]
    if not np.isfinite(values).all() or np.any((values < 0) | (values > 1)):
        raise ValueError('Invalid model probabilities.')
    return values


def to_logits(probability):
    p = np.clip(np.asarray(probability, dtype=float), 1e-6, 1 - 1e-6)
    return np.log(p / (1 - p)).reshape(-1, 1)


def fold_plan(train, splits=3):
    days = np.array(sorted(train.signal_date.unique()))
    plans = []
    for fitting_days, validation_days in TimeSeriesSplit(n_splits=splits).split(days):
        start = pd.Timestamp(days[validation_days[0]])
        fitting = train[train.signal_date.isin(days[fitting_days]) & train.label_available_date.lt(start)].copy()
        validation = train[train.signal_date.isin(days[validation_days])].copy()
        if fitting.signal_date.nunique() < 15 or fitting.target.nunique() != 2 or validation.empty:
            raise ValueError('Insufficient mature data in a purged family-selection fold.')
        if fitting.label_available_date.max() >= validation.signal_date.min():
            raise ValueError('Fold labels cross into validation.')
        plans.append((fitting, validation))
    return plans


def partition_info(frame):
    return {'rows': len(frame), 'dates': int(frame.signal_date.nunique()),
            'start': str(frame.signal_date.min().date()), 'end': str(frame.signal_date.max().date()),
            'latest_label': str(frame.label_available_date.max().date())}


def select_family(train, splits=3, progress_path=None, columns=COLUMNS):
    columns = checked_columns(columns)
    audits, parts = [], []
    for number, (fitting, validation) in enumerate(fold_plan(train, splits), 1):
        scored = validation[['stock_code', 'signal_date', 'target']].copy()
        scored['past_constant'] = float(np.average(fitting.target, weights=date_weights(fitting)))
        with threadpool_limits(limits=2):
            for name, model in factories().items():
                print(f'Training-only CV fold {number}/{splits}: {name}', flush=True)
                fit_estimator(model, fitting[columns], fitting.target, date_weights(fitting))
                scored[name] = model.predict_proba(validation[columns])[:, 1]
        scored['fixed_mean'] = scored[list(factories())].mean(axis=1)
        parts.append(scored)
        audits.append({'fold': number, 'train': partition_info(fitting), 'validation': partition_info(validation)})
        if progress_path:
            write_json({'completed_folds': number, 'folds': audits}, progress_path)
    oof = pd.concat(parts, ignore_index=True).sort_values(['signal_date', 'stock_code']).reset_index(drop=True)
    if oof.duplicated(['stock_code', 'signal_date']).any():
        raise ValueError('Duplicated out-of-fold stock/date observations.')
    weights = date_weights(oof)
    scores = {name: float(brier_score_loss(oof.target, oof[name], sample_weight=weights)) for name in NAMES}
    reference = float(brier_score_loss(oof.target, oof.past_constant, sample_weight=weights))
    winner = min(scores, key=lambda name: (scores[name], name))
    return winner, scores, reference, audits, oof


def weighted_quantiles(values, weights, quantiles=(.05, .95)):
    values, weights = np.asarray(values, dtype=float), np.asarray(weights, dtype=float)
    if values.shape != weights.shape or values.ndim != 1 or not len(values):
        raise ValueError('Residual values and weights must be aligned nonempty vectors.')
    if not np.isfinite(values + weights).all() or np.any(weights <= 0):
        raise ValueError('Residual inputs require finite values and positive weights.')
    order = np.argsort(values, kind='stable')
    v, w = values[order], weights[order]
    cdf = (np.cumsum(w) - .5 * w) / w.sum()
    return np.interp(quantiles, cdf, v)


def fit_selected(train, calibration, winner, as_of, columns=COLUMNS):
    columns = checked_columns(columns)
    if (train.label_available_date.max() >= calibration.signal_date.min()
            or calibration.label_available_date.max() > pd.Timestamp(as_of)):
        raise ValueError('As-of training/calibration label-time violation.')
    names = list(factories()) if winner == 'fixed_mean' else sorted({winner, 'hgb_shallow'})
    models, calibrators = {}, {}
    with threadpool_limits(limits=2):
        for name in names:
            print('Final fitting: ' + name, flush=True)
            models[name] = fit_estimator(factories()[name], train[columns], train.target, date_weights(train))
        for role, name in [('anchor', 'hgb_shallow'), ('selected', winner)]:
            calibrator = LogisticRegression(C=1., solver='liblinear', max_iter=1000, random_state=42)
            calibrator.fit(to_logits(raw_probability(models, name, calibration[columns])), calibration.target,
                           sample_weight=date_weights(calibration))
            calibrators[role] = calibrator
        regressor = fit_estimator(new_regressor(), train[columns], train.target_return, date_weights(train))
        residual = calibration.target_return.to_numpy() - regressor.predict(calibration[columns])
    bounds = weighted_quantiles(residual, date_weights(calibration))
    return {'models': models, 'calibrators': calibrators, 'regressor': regressor, 'selected_name': winner,
            'residual_bounds': bounds.tolist(), 'features': columns,
            'baseline_probability': float(np.average(calibration.target, weights=date_weights(calibration))),
            'baseline_return': float(train.target_return.median())}


def predict_values(bundle, features, role='selected'):
    if list(features.columns) != checked_columns(bundle['features']) or role not in {'selected', 'anchor'}:
        raise ValueError('Selected model feature schema/role mismatch.')
    name = bundle['selected_name'] if role == 'selected' else 'hgb_shallow'
    with threadpool_limits(limits=2):
        p = bundle['calibrators'][role].predict_proba(to_logits(raw_probability(bundle['models'], name, features)))[:, 1]
        point = bundle['regressor'].predict(features)
    low, high = bundle['residual_bounds']
    if not np.isfinite(p).all() or not np.isfinite(point).all() or not np.isfinite(low + high) or low > high:
        raise ValueError('Nonfinite or reversed empirical forecast range.')
    return p, point, point + low, point + high


def score_period(bundle, test, role):
    test = test.reset_index(drop=True)
    p, point, low, high = predict_values(bundle, test[bundle['features']], role)
    frame = test[['stock_code', 'signal_date', 'target_date', 'label_available_date', 'target', 'target_return', 'net_return_proxy']].copy()
    frame['probability_above_cost'], frame['predicted_close_return'] = p, point
    frame['empirical_return_lower'], frame['empirical_return_upper'] = low, high
    frame['selected_by_fixed_policy'] = (p >= .6) & (point > .003)
    frame['own_baseline_probability'] = bundle['baseline_probability']
    frame['common_rolling_baseline_probability'] = bundle['baseline_probability']
    frame['baseline_return'] = bundle['baseline_return']
    frame['recommendation'] = 'ABSTAIN'
    frame['origin'] = 'retrospective_development_not_prospective'
    metrics = summarize(frame)
    metrics['empirical_interval_coverage'] = float(np.average((test.target_return >= low) & (test.target_return <= high), weights=date_weights(test)))
    metrics['empirical_interval_width'] = float(np.average(high - low, weights=date_weights(test)))
    return frame, metrics


def render_report(summary):
    lines = ['# Training-Only Model Selection Research', '',
             'RESEARCH_ONLY. Model family is selected inside training; all external scores remain historical development evidence.', '',
             '## Selection and Timing', '',
             'Selected family: ' + summary['selected_name'],
             'Fixed families and fixed unweighted ensemble are compared on three purged expanding folds using date-equal raw Brier. No calibration/test scores choose the family.',
             'The matched shallow-HGB anchor uses exactly the same newer train/calibration rows. Do not compare absolute AUC changes to an older differently timed model as a family effect.',
             'The shared return point is an absolute-error conditional-median proxy, not an expected mean. Empirical residual ranges have no coverage guarantee under regime change and dependent outcomes.', '',
             '| Family | Training-only OOF date Brier |', '|---|---:|']
    for name, value in summary['cv_scores'].items():
        lines.append(f'| {name} | {value:.6f} |')
    lines += [f"| Past fold-training constant | {summary['cv_constant_brier']:.6f} |", '',
              'The minimum training-CV score is selection-optimistic, not an independent final validation.', '',
              '## External Historical Comparison', '',
              '| Period | Role | Rows | Dates | Pooled AUC | Daily AUC | Date Brier | Known constant Brier | Empirical band coverage | Band width |',
              '|---|---|---:|---:|---:|---:|---:|---:|---:|---:|']
    for period, roles in summary['results'].items():
        for role, row in roles.items():
            lines.append(f"| {period} | {role} | {row['evaluated_rows']} | {row['signal_dates']} | {row['roc_auc']} | {row['mean_daily_cross_section_auc']} | {row['date_brier']:.6f} | {row['common_date_baseline_brier']:.6f} | {row['empirical_interval_coverage']:.2%} | {row['empirical_interval_width']:.2%} |")
    lines += ['', '## Fixed Policy', '', '| Period | Role | Cases | Dates | Date-equal success | All-date five-session net proxy | Block lower 95% |', '|---|---|---:|---:|---:|---:|---:|']
    for period, roles in summary['results'].items():
        for role, row in roles.items():
            lines.append(f"| {period} | {role} | {row['selected_count']} | {row['selected_dates']} | {row['selected_date_success_rate']} | {row['all_dates_mean_net_return_proxy']} | {row['all_dates_return_lower_95']} |")
    lines += ['', 'The 60% probability / 0.3% median-proxy policy is unchanged. No-selection dates are zero exposure proxies. These are overlapping close-to-close research outcomes, not executable/compounded strategy returns.', '',
              '## Paired Selected Minus Matched Anchor', '', '| Period | Date Brier difference | 95% five-session-block interval |', '|---|---:|---|']
    for period, row in summary['paired'].items():
        lines.append(f"| {period} | {row['date_brier_delta']:.6f} | [{row['lower_95']}, {row['upper_95']}] |")
    lines += ['', 'Primary development screen: ' + str(summary['development_screen_passed']),
              'Reasons: ' + ', '.join(summary['screen_reasons']),
              'Production recommendation gate: False. Original forward ledgers, public model and candidate pool unchanged.', '',
              '## Fit-Time Audit', '', 'Fit as-of: ' + summary['fit_as_of'],
              'Partitions: ' + str(summary['partitions']),
              'Common-cohort excluded rows: ' + str(summary['cohort_excluded_rows']),
              'Residual bounds use calibration outcomes only. No external test score/label is in the as-of bundle.',
              'The July-September interval has already been inspected in prior research; October is a short diagnostic tail, not adequate new evidence or a selection period.',
              'Current-universe and retrospectively adjusted-price limitations remain.', '',
              'Protocol SHA256: ' + summary['protocol_sha256'], 'Artifacts (ignored): ' + summary['run_dir'], '']
    return '\n'.join(lines)


def run_training(data_root, output_root, protocol, report_path):
    if (protocol['candidates'] != NAMES or protocol['cv_splits'] != 3 or protocol['probability_threshold'] != .6
            or protocol['cost_assumption'] != .003 or protocol['production_promotion'] is not False
            or protocol['candidate_pool_change'] is not False or protocol['hyperparameter_search_on_test'] is not False):
        raise ValueError('Unsupported training-selection protocol.')
    raw, source = load_snapshots(data_root)
    if (raw.attrs.get('feature_version') != HISTORY_FEATURE_VERSION or source.get('skipped_files')
            or raw.attrs.get('history_provenance', {}).get('failed_stocks', 0)):
        raise ValueError('Verified complete OHLCV history is required.')
    dataset, dataset_metadata = build_dataset(add_ohlcv_information(raw), as_of=protocol['labels_as_of'])
    valid = np.isfinite(dataset[COLUMNS]).all(axis=1)
    excluded = int((~valid).sum())
    dataset = dataset[valid].copy()
    train, calibration, test = temporal_partitions(dataset, protocol['calibration_start'], protocol['test_start'])
    dates = pd.DatetimeIndex(sorted(raw.signal_date.unique()))
    as_of = dates[dates < pd.Timestamp(protocol['test_start'])][-1]
    root = Path(output_root)
    run_dir = root / 'runs' / (datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '_' + uuid.uuid4().hex[:8])
    run_dir.mkdir(parents=True, exist_ok=False)
    winner, cv_scores, cv_reference, folds, oof = select_family(train, progress_path=run_dir / 'progress.json')
    write_json({'selected_name': winner, 'cv_scores': cv_scores, 'cv_constant_brier': cv_reference, 'folds': folds}, run_dir / 'training_selection.json')
    np.savez_compressed(run_dir / 'training_oof.npz', stock_code=oof.stock_code.to_numpy(dtype='U6'),
                        signal_date=oof.signal_date.to_numpy(dtype='datetime64[ns]'), target=oof.target.to_numpy(),
                        **{name: oof[name].to_numpy() for name in NAMES + ['past_constant']})
    bundle = fit_selected(train, calibration, winner, as_of)
    protocol_hash = hashlib.sha256(json_text(protocol).encode()).hexdigest()
    implementation = {str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
                      for path in [Path(__file__), ROOT / 'src/features/ohlcv_information.py',
                                   ROOT / 'src/features/price_learning_dataset.py', ROOT / 'src/features/completed_price_dataset.py',
                                   ROOT / 'src/models/price_forecaster.py', ROOT / 'src/models/monthly_price_walkforward.py',
                                   ROOT / 'src/models/market_context_experiment.py', ROOT / 'src/models/ohlcv_information_experiment.py']}
    partitions = {'train': partition_info(train), 'calibration': partition_info(calibration)}
    fit_digest = fit_data_digest(train, calibration, COLUMNS)
    bundle['metadata'] = {'schema': 'research_training_selected_price_v1', 'as_of': str(as_of.date()),
                          'trained_at': datetime.now(timezone.utc).isoformat(), 'features': COLUMNS,
                          'partitions': partitions, 'selected_name': winner, 'cv_scores': cv_scores,
                          'protocol_sha256': protocol_hash, 'implementation_sha256': implementation,
                          'dataset_sha256': fit_digest, 'horizon_sessions': 5, 'cost_assumption': .003,
                          'target_definition': dataset_metadata['target_definition'],
                          'history_provenance': dataset_metadata.get('history_provenance'),
                          'recommendation_gate_passed': False, 'data_root': str(Path(data_root).resolve())}
    joblib.dump(bundle, run_dir / 'model.joblib', compress=3)
    write_json(bundle['metadata'], run_dir / 'model_metadata.json')
    results, paired = {}, {}
    for period, (start, end) in protocol['periods'].items():
        part = test[test.signal_date.between(pd.Timestamp(start), pd.Timestamp(end))]
        if part.empty:
            raise ValueError('No historical evaluation observations for ' + period)
        results[period], predictions = {}, {}
        for role in ['anchor', 'selected']:
            frame, metrics = score_period(bundle, part, role)
            predictions[role], results[period][role] = frame, metrics
            frame.to_csv(run_dir / (role + '_' + period + '.csv'), index=False)
        paired[period] = paired_interval(predictions['anchor'], predictions['selected'])
    primary = protocol['primary_period']
    reasons = development_screen(results[primary]['selected'], paired[primary])
    if results[primary]['selected']['empirical_interval_coverage'] < .85:
        reasons.append('empirical_interval_undercoverage')
    summary = {'selected_name': winner, 'cv_scores': cv_scores, 'cv_constant_brier': cv_reference, 'folds': folds,
               'run_dir': str(run_dir), 'fit_as_of': str(as_of.date()), 'partitions': partitions,
               'results': results, 'paired': paired, 'protocol': protocol, 'protocol_sha256': protocol_hash,
               'implementation_sha256': implementation, 'cohort_excluded_rows': excluded,
               'development_screen_passed': not reasons, 'screen_reasons': reasons, 'recommendation_gate_passed': False}
    report_path = Path(report_path)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(render_report(summary), encoding='utf-8')
    write_json(summary, report_path.with_suffix('.json'))
    write_json({'run_id': run_dir.name}, root / 'latest.json')
    print(json_text({'selected_name': winner, 'cv_scores': cv_scores, 'paired': paired,
                     'development_screen_passed': not reasons, 'screen_reasons': reasons}), flush=True)
    return summary


def load_selected(model_dir, now=None):
    now = now or datetime.now(KST)
    if now.tzinfo is None:
        raise ValueError('Timezone-aware query required.')
    now = now.astimezone(KST)
    root = Path(model_dir)
    run_id = json.loads((root / 'latest.json').read_text())['run_id']
    if not run_id or run_id in {'.', '..'} or Path(run_id).name != run_id:
        raise ValueError('Invalid research run identifier.')
    bundle = joblib.load(root / 'runs' / run_id / 'model.joblib')
    metadata = bundle['metadata']
    if (metadata.get('schema') != 'research_training_selected_price_v1'
            or checked_columns(bundle['features']) != metadata.get('features')
            or metadata.get('recommendation_gate_passed') is not False or pd.Timestamp(metadata['trained_at']) > pd.Timestamp(now)
            or pd.Timestamp(metadata['as_of']).date() > now.date()):
        raise ValueError('Only already-trained research selection bundles are supported.')
    return bundle


def query_selected(model_dir, data_root, stock, now=None):
    now = now or datetime.now(KST)
    if now.tzinfo is None:
        raise ValueError('Timezone-aware query required.')
    now = now.astimezone(KST)
    bundle = load_selected(model_dir, now)
    data_root = Path(data_root or bundle['metadata']['data_root'])
    raw, source = load_snapshots(data_root)
    if (raw.attrs.get('feature_version') != HISTORY_FEATURE_VERSION or source.get('skipped_files')
            or raw.attrs.get('history_provenance', {}).get('failed_stocks', 0)):
        raise ValueError('Verified completed-history inputs are required.')
    code = resolve_stock(stock, [ROOT, data_root])
    cutoff = pd.Timestamp(completed_price_cutoff(now))
    raw = raw[raw.signal_date.le(cutoff) & raw.snapshot_date.le(cutoff)].copy()
    if bundle['features'] == COLUMNS:
        raw = raw[raw.stock_code.eq(code)].copy()
    if raw.empty:
        raise ValueError('No completed prices for this stock.')
    prepared = prepare_selected_features(raw, bundle['features'], bundle['metadata'].get('market_min_stocks', 100))
    row = prepared[prepared.stock_code.eq(code)].sort_values('signal_date').tail(1).copy()
    if row.empty or not np.isfinite(row[bundle['features']]).all(axis=None) or row.volume_ratio_20d.iloc[0] <= 0:
        raise ValueError('Insufficient active completed features.')
    p, point, low, high = predict_values(bundle, row[bundle['features']])
    return {'stock_code': code, 'signal_date': str(pd.Timestamp(row.signal_date.iloc[0]).date()),
            'model_family': bundle['selected_name'], 'probability_above_cost': round(float(p[0]), 6),
            'return_median_proxy': round(float(point[0]), 6), 'empirical_return_lower': round(float(low[0]), 6),
            'empirical_return_upper': round(float(high[0]), 6), 'nominal_calibration_coverage': .9,
            'interval_note': 'Empirical historical residual range, NOT guaranteed coverage or confidence.',
            'horizon_sessions': 5, 'cost_assumption': .003, 'as_of': now.date().isoformat(),
            'status': 'STALE_DATA' if (now.date() - pd.Timestamp(row.signal_date.iloc[0]).date()).days > 7 else 'RESEARCH_ONLY',
            'recommendation': 'ABSTAIN', 'recommendation_ko': '추천 보류'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['train', 'predict'])
    parser.add_argument('--protocol', type=Path, default=ROOT / 'docs/model_experiments/selected_model_protocol_20261021.json')
    parser.add_argument('--model-dir', type=Path, default=ROOT / 'data/models/price_forecaster_selected')
    parser.add_argument('--data-root', type=Path)
    parser.add_argument('--stock')
    parser.add_argument('--report-path', type=Path, default=ROOT / 'reports/daily_review/2026-10-21_selected_price_model.md')
    args = parser.parse_args()
    try:
        if args.command == 'train':
            protocol = json.loads(args.protocol.read_text())
            run_training(args.data_root or ROOT / protocol['data_root'], args.model_dir, protocol, args.report_path)
        else:
            if not args.stock:
                raise ValueError('predict requires --stock')
            print(json_text(query_selected(args.model_dir, args.data_root, args.stock)))
    except (ValueError, FileNotFoundError) as error:
        parser.exit(2, str(error) + '\n')
    except Exception as error:
        parser.exit(2, 'Selected research model failed: ' + type(error).__name__ + '\n')


if __name__ == '__main__':
    main()
