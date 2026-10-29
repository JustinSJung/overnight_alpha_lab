"""Fixed 2x2 research comparison: market context versus per-date training weights."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import brier_score_loss, log_loss, mean_absolute_error, roc_auc_score
from threadpoolctl import threadpool_limits

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from src.features.completed_price_dataset import HISTORY_FEATURE_VERSION
from src.features.market_context import MARKET_FEATURES, MARKET_FEATURE_VERSION, add_market_context
from src.features.price_learning_dataset import FEATURES, build_dataset, load_snapshots, temporal_partitions
from src.models.price_forecaster import (
    PROBABILITY_THRESHOLD, block_bootstrap_lower, choose_classifier, date_weights, fit_estimator, json_text,
    logits, new_regressor, predict_values, save_artifacts, validation_summary,
)

ARMS = [('price_row', False, False), ('price_date', False, True),
        ('market_row', True, False), ('market_date', True, True)]


def return_baseline(train, balanced):
    if not balanced:
        return float(train['target_return'].median())
    order = np.argsort(train['target_return'].to_numpy())
    weights = date_weights(train)[order]
    index = np.searchsorted(np.cumsum(weights), weights.sum() / 2)
    return float(train['target_return'].to_numpy()[order[index]])


def date_metrics(predictions, common_baseline, with_uncertainty=False):
    predictions = predictions.assign(signal_date=pd.to_datetime(predictions['signal_date']).dt.normalize())
    weights = date_weights(predictions)
    y = predictions['target']
    probability = predictions['probability_above_cost']
    aucs = [float(roc_auc_score(day['target'], day['probability_above_cost']))
            for _, day in predictions.groupby('signal_date') if day['target'].nunique() == 2]
    selected = predictions[predictions['selected_by_fixed_policy']]
    daily_selected = selected.groupby('signal_date').agg(count=('target', 'size'), success=('target', 'mean'))
    calendar = pd.DatetimeIndex(sorted(predictions['signal_date'].unique()))
    selected_returns = selected.groupby('signal_date')['net_return_proxy'].mean() if len(selected) else pd.Series(dtype=float)
    all_date_returns = selected_returns.reindex(calendar, fill_value=0.0)
    baseline = np.asarray(common_baseline, dtype=float)
    if baseline.ndim == 0:
        baseline = np.full(len(y), baseline.item())
    if baseline.shape != (len(y),):
        raise ValueError('Baseline probabilities must align with evaluated rows.')
    result = {
        'date_brier': float(brier_score_loss(y, probability, sample_weight=weights)),
        'common_date_baseline_brier': float(brier_score_loss(y, baseline, sample_weight=weights)),
        'date_log_loss': float(log_loss(y, probability, sample_weight=weights, labels=[0, 1])),
        'date_return_mae': float(np.average(abs(predictions['target_return'] - predictions['predicted_close_return']), weights=weights)),
        'mean_daily_cross_section_auc': float(np.mean(aucs)) if aucs else None,
        'daily_auc_dates': len(aucs),
        'selected_date_success_rate': float(daily_selected['success'].mean()) if len(selected) else None,
        'selected_top_two_date_share': float(daily_selected['count'].nlargest(2).sum() / len(selected)) if len(selected) else None,
        'all_dates_mean_net_return_proxy': float(all_date_returns.mean()),
        'all_dates_return_lower_95': block_bootstrap_lower(all_date_returns.to_numpy()) if with_uncertainty else None,
    }
    return result


def fit_variant(dataset, metadata, source, output_dir, as_of, calibration_start, test_start,
                name, market, balanced, context_metadata):
    columns = FEATURES + MARKET_FEATURES if market else FEATURES
    train, calibration, test = temporal_partitions(dataset, calibration_start, test_start)
    train_weights = date_weights(train) if balanced else None
    calibration_weights = date_weights(calibration) if balanced else None
    with threadpool_limits(limits=2):
        classifier_name, classifier, cv = choose_classifier(train, columns, balanced)
        calibrator = LogisticRegression(C=1.0, solver='liblinear', max_iter=1000, random_state=42)
        fit_estimator(calibrator, logits(classifier, calibration[columns]), calibration['target'], calibration_weights)
        regressor = fit_estimator(new_regressor(), train[columns], train['target_return'], train_weights)
        bundle = {'classifier': classifier, 'calibrator': calibrator, 'regressor': regressor}
        probability, expected_return = predict_values(bundle, test[columns])
    prior = float(np.average(calibration['target'], weights=calibration_weights))
    summary, predictions = validation_summary(test, probability, expected_return, prior, metadata['cost_assumption'])
    baseline_return = return_baseline(train, balanced)
    summary['baseline_return_mae'] = float(mean_absolute_error(test['target_return'], np.full(len(test), baseline_return)))
    if summary['return_mae'] >= summary['baseline_return_mae']:
        summary['gate_reasons'].append('return_forecast_does_not_beat_training_median')
    summary['gate_reasons'].append('development_experiment_requires_future_validation')
    summary['recommendation_gate_passed'] = False
    common_prior = float(np.average(calibration['target'], weights=date_weights(calibration)))
    summary.update(date_metrics(predictions, common_prior, with_uncertainty=True))
    summary['common_date_baseline_return_mae'] = float(np.average(
        abs(test['target_return'] - return_baseline(train, True)), weights=date_weights(test)))
    for lower, upper in [(0, .2), (.2, .4), (.4, .6), (.6, .8), (.8, 1)]:
        mask = (probability >= lower) & ((probability < upper) if upper < 1 else (probability <= upper))
        if mask.any():
            summary.setdefault('calibration_bins', []).append({
                'range': [lower, upper], 'count': int(mask.sum()),
                'mean_probability': float(probability[mask].mean()),
                'observed_rate': float(test.loc[mask, 'target'].mean()),
            })
    predictions['market_return_20d'] = test['market_return_20d'].to_numpy()
    predictions['market_regime'] = np.where(predictions['market_return_20d'] > 0, 'up_proxy', 'down_or_flat_proxy')
    fingerprint = hashlib.sha256(pd.util.hash_pandas_object(
        dataset[['stock_code', 'signal_date', 'label_available_date', 'target_return'] + columns], index=False
    ).values.tobytes()).hexdigest()
    run_metadata = dict(metadata, **source)
    run_metadata.update({
        'feature_version': MARKET_FEATURE_VERSION if market else HISTORY_FEATURE_VERSION,
        'source_ref': 'market_context_date_balance_v1/' + name,
        'trained_at': datetime.now(timezone.utc).isoformat(), 'as_of': str(as_of),
        'dataset_sha256': fingerprint, 'classifier': classifier_name, 'features': columns,
        'training_cv': cv, 'baseline_probability': prior, 'baseline_return': baseline_return,
        'calibration_parameters': {'slope': float(calibrator.coef_[0, 0]), 'intercept': float(calibrator.intercept_[0])},
        'date_balanced_training': balanced, 'variant': name, 'market_context': context_metadata,
        'probability_threshold': PROBABILITY_THRESHOLD, 'test': summary,
        'fixed_temporal_boundaries': {'calibration_start': calibration_start, 'test_start': test_start},
        'latest_signal_date': str(dataset['signal_date'].max().date()),
        'partitions': {label: {'rows': len(part), 'start': str(part['signal_date'].min().date()),
                              'end': str(part['signal_date'].max().date()), 'positive_rate': float(part['target'].mean()),
                              'latest_label_available': str(part['label_available_date'].max().date())}
                       for label, part in [('train', train), ('calibration', calibration), ('test', test)]},
    })
    bundle['metadata'] = run_metadata
    _, run_dir = save_artifacts(bundle, predictions, output_dir)
    return run_metadata, predictions, run_dir


def prepare_dataset(data_root, as_of, min_stocks=100):
    snapshots, source = load_snapshots(data_root)
    if snapshots.attrs.get('feature_version') != HISTORY_FEATURE_VERSION:
        raise ValueError('The comparison requires coherent completed OHLCV history.')
    snapshots = snapshots[(snapshots['signal_date'] <= pd.Timestamp(as_of))
                          & (snapshots['snapshot_date'] <= pd.Timestamp(as_of))].copy()
    contextual = add_market_context(snapshots, min_stocks)
    dataset, metadata = build_dataset(contextual, as_of=as_of)
    before = len(dataset)
    dataset = dataset[np.isfinite(dataset[MARKET_FEATURES]).all(axis=1)].reset_index(drop=True)
    if dataset.empty:
        raise ValueError('No common rows with sufficiently populated completed market context.')
    metadata.update({
        'data_root': str(Path(data_root).resolve()), 'common_rows': len(dataset),
        'training_rows': len(dataset), 'signal_dates': int(dataset['signal_date'].nunique()),
        'rows_excluded_for_market_context': before - len(dataset),
        'common_dataset_sha256': hashlib.sha256(pd.util.hash_pandas_object(
            dataset[['stock_code', 'signal_date', 'target_return'] + FEATURES + MARKET_FEATURES], index=False
        ).values.tobytes()).hexdigest(),
        'evaluation_role': 'Previously inspected historical dates: development comparison, not an untouched final test.',
    })
    return dataset, metadata, source, contextual.attrs['market_context']


def comparison_report(results, metadata):
    def number(value, percent=False):
        return 'n/a' if value is None else (f'{value:.2%}' if percent else f'{value:.6f}')
    lines = ['# Market Context and Date-Balanced Learning', '',
             'RESEARCH_ONLY. No production model replacement, scoring change, or trading.', '',
             '## Fixed Comparison', '',
             metadata['evaluation_role'],
             'All four arms use identical observations, temporal boundaries, five-session labels, and the unchanged 60%/0.3% selection policy.',
             'Classifier selection uses three purged expanding folds inside training only. Final historical scores do not select a winner or tune thresholds.',
             'Date-balanced arms weight each signal date equally in scaling, fitting, calibration and training-fold loss.',
             'Market context is an active observed-universe proxy, not KOSPI/KOSDAQ. It uses only completed same-day/past quotes.',
             'No forward predictions are backdated. Every arm remains recommendation-disabled pending future validation.', '',
             f"Common rows: {metadata['common_rows']}; excluded for context: {metadata['rows_excluded_for_market_context']}.",
             f"Common dataset SHA256: {metadata['common_dataset_sha256']}", '',
             '## Comparable Metrics', '',
             '| Arm | Classifier | Pooled AUC | Mean daily AUC | Date Brier | Constant date Brier | Date return MAE |',
             '|---|---|---:|---:|---:|---:|---:|']
    for entry in results:
        test = entry['test']
        lines.append(f"| {entry['variant']} | {entry['classifier']} | {number(test['roc_auc'])} | {number(test['mean_daily_cross_section_auc'])} | {number(test['date_brier'])} | {number(test['common_date_baseline_brier'])} | {number(test['date_return_mae'])} |")
    lines += ['', 'Smaller Brier/MAE is better. The constant date baseline is the same past calibration-period date-weighted prevalence for every arm.',
              'Mean daily AUC averages cross-sectional AUC only on dates containing both classes; dates are correlated and five-session labels overlap.', '',
              '## Fixed Policy Selection', '',
              '| Arm | Selected rows | Signal dates | Pooled success | Date-equal success | Top-two-date share | Selected-date five-session net proxy | Selected-date block lower 95% |',
              '|---|---:|---:|---:|---:|---:|---:|---:|']
    for entry in results:
        test = entry['test']
        lines.append(f"| {entry['variant']} | {test['selected_count']} | {test['selected_dates']} | {number(test['selected_success_rate'], True)} | {number(test['selected_date_success_rate'], True)} | {number(test['selected_top_two_date_share'], True)} | {number(test['selected_daily_mean_net_return_proxy'], True)} | {number(test['selected_daily_return_lower_95'], True)} |")
    lines += ['', 'Per-date selection metrics include dates with selections only. These are overlapping close-to-close research returns after assumed cost, not executable daily portfolio returns.',
              'A pooled success rate is not model reliability. No recommendation gate is relaxed.', '',
              'Selected-date block resampling uses the sequence of selected dates, which may have gaps.', '',
              '## All Signal Dates', '',
              '| Arm | All-date mean five-session net proxy | Calendar-sequence block lower 95% |', '|---|---:|---:|']
    for entry in results:
        test = entry['test']
        lines.append(f"| {entry['variant']} | {number(test['all_dates_mean_net_return_proxy'], True)} | {number(test['all_dates_return_lower_95'], True)} |")
    lines += ['', 'Includes every test signal date; dates with no policy selection have zero exposure proxy, not failed prediction labels. Blocks contain five consecutive observed signal dates.',
              'Zero from an abstaining model is not evidence of useful predictive performance. These proxies are not compounded portfolio returns.', '',
              '## Monthly Diagnostics', '', '| Arm | Month | Rows | AUC | Date Brier | Constant date Brier |', '|---|---|---:|---:|---:|---:|']
    for entry in results:
        for month in entry['monthly']:
            lines.append(f"| {entry['variant']} | {month['month']} | {month['rows']} | {number(month['auc'])} | {number(month['date_brier'])} | {number(month['baseline_date_brier'])} |")
    lines += ['', '## Regime Diagnostics', '', '| Arm | Known-at-close regime | Rows | AUC | Date Brier |', '|---|---|---:|---:|---:|']
    for entry in results:
        for regime in entry['regimes']:
            lines.append(f"| {entry['variant']} | {regime['regime']} | {regime['rows']} | {number(regime['auc'])} | {number(regime['date_brier'])} |")
    lines += ['', 'Regimes split on the observed-universe trailing 20-session return, not future outcomes.', '', '## Artifacts', '']
    for entry in results:
        lines += [f"- {entry['variant']}: {entry['run_dir']}", f"  Gate: {', '.join(entry['test']['gate_reasons'])}"]
    lines += ['', 'Current-universe/survivorship and retrospective adjusted-price limitations remain. Future timestamped predictions on multiple dates are required.', '']
    return '\n'.join(lines)


def run_experiment(data_root, output_root, protocol, report_path):
    if protocol['arms'] != [arm[0] for arm in ARMS] or protocol['horizon_sessions'] != 5 or protocol['cost_assumption'] != .003 or protocol['probability_threshold'] != PROBABILITY_THRESHOLD:
        raise ValueError('Unsupported experiment protocol; do not silently change the target or policy.')
    dataset, metadata, source, context = prepare_dataset(data_root, protocol['training_as_of'], protocol['market_min_stocks'])
    metadata['experiment_protocol_sha256'] = hashlib.sha256(json_text(protocol).encode()).hexdigest()
    metadata['implementation_sha256'] = {str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
                                         for path in [Path(__file__), ROOT / 'src/features/market_context.py', ROOT / 'src/models/price_forecaster.py']}
    results = []
    print(json_text({'common_rows': len(dataset), 'context_excluded': metadata['rows_excluded_for_market_context']}), flush=True)
    for name, market, balanced in ARMS:
        print('Training ' + name, flush=True)
        fitted, predictions, run_dir = fit_variant(
            dataset, metadata, source, Path(output_root) / name, protocol['training_as_of'],
            protocol['calibration_start'], protocol['development_test_start'], name, market, balanced, context)
        monthly = []
        _, calibration, _ = temporal_partitions(dataset, protocol['calibration_start'], protocol['development_test_start'])
        prior = float(np.average(calibration['target'], weights=date_weights(calibration)))
        for month, part in predictions.groupby(predictions['signal_date'].dt.strftime('%Y-%m')):
            diagnostics = date_metrics(part, prior)
            monthly.append({'month': month, 'rows': len(part),
                            'auc': float(roc_auc_score(part['target'], part['probability_above_cost'])) if part['target'].nunique() == 2 else None,
                            'date_brier': diagnostics['date_brier'], 'baseline_date_brier': diagnostics['common_date_baseline_brier']})
        regimes = []
        for regime, part in predictions.groupby('market_regime'):
            regimes.append({'regime': regime, 'rows': len(part),
                            'auc': float(roc_auc_score(part['target'], part['probability_above_cost'])) if part['target'].nunique() == 2 else None,
                            'date_brier': date_metrics(part, prior)['date_brier']})
        results.append({'variant': name, 'classifier': fitted['classifier'], 'features': fitted['features'],
                        'run_dir': str(run_dir), 'test': fitted['test'], 'partitions': fitted['partitions'],
                        'monthly': monthly, 'regimes': regimes})
        report_path = Path(report_path)
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(comparison_report(results, metadata), encoding='utf-8')
        report_path.with_suffix('.json').write_text(json_text({'protocol': protocol, 'data': metadata, 'results': results}) + '\n', encoding='utf-8')
        print(json_text({'variant': name, 'classifier': fitted['classifier'], 'test': fitted['test']}), flush=True)
    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--protocol', type=Path, default=ROOT / 'docs/model_experiments/market_context_protocol_20261021.json')
    parser.add_argument('--data-root', type=Path)
    parser.add_argument('--output-root', type=Path, default=ROOT / 'data/models/price_forecaster_context')
    parser.add_argument('--report-path', type=Path, default=ROOT / 'reports/daily_review/2026-10-21_market_context_experiment.md')
    args = parser.parse_args()
    protocol = json.loads(args.protocol.read_text(encoding='utf-8'))
    run_experiment(args.data_root or ROOT / protocol['data_root'], args.output_root, protocol, args.report_path)


if __name__ == '__main__':
    main()
