"""Retrospective monthly refitting with matched frozen controls and mature labels only."""
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
from sklearn.metrics import brier_score_loss, mean_absolute_error, roc_auc_score
from threadpoolctl import threadpool_limits

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from src.features.completed_price_dataset import HISTORY_FEATURE_VERSION
from src.features.price_learning_dataset import FEATURES, build_dataset, load_snapshots
from src.models.market_context_experiment import date_metrics
from src.models.price_forecaster import (
    PROBABILITY_THRESHOLD, classifiers, date_weights, json_text, logits,
    new_regressor, predict_values, save_artifacts,
)


def monthly_split(dataset, as_of, training_sessions, calibration_sessions):
    as_of = pd.Timestamp(as_of).normalize()
    known = dataset[(dataset['signal_date'] <= as_of) & (dataset['target_date'] <= as_of)
                    & (dataset['label_available_date'] <= as_of)]
    days = sorted(known['signal_date'].unique())
    if training_sessions < 15 or calibration_sessions < 3 or len(days) < calibration_sessions:
        raise ValueError('Insufficient mature signal dates for the requested fitting protocol.')
    calibration_days = days[-calibration_sessions:]
    calibration_start = pd.Timestamp(calibration_days[0])
    calibration = known[known['signal_date'].isin(calibration_days)].copy()
    eligible = known[(known['signal_date'] < calibration_start)
                     & (known['label_available_date'] < calibration_start)]
    training_days = sorted(eligible['signal_date'].unique())
    if len(training_days) < training_sessions:
        raise ValueError('Insufficient purged training history for window ' + str(training_sessions))
    train = eligible[eligible['signal_date'].isin(training_days[-training_sessions:])].copy()
    if train['target'].nunique() < 2 or calibration['target'].nunique() < 2:
        raise ValueError('Both training and calibration require two classes.')
    if not train['label_available_date'].max() < calibration_start or calibration['label_available_date'].max() > as_of:
        raise ValueError('As-of label availability violation.')
    return train, calibration


def month_plan(dataset, calendar, start, end):
    evaluation = dataset[dataset['signal_date'].between(pd.Timestamp(start), pd.Timestamp(end))]
    if evaluation.empty:
        raise ValueError('No fully resolved evaluation rows in the requested interval.')
    plan = []
    for month in sorted(evaluation['signal_date'].dt.to_period('M').unique()):
        earlier = calendar[calendar < month.start_time]
        if len(earlier) == 0:
            raise ValueError('No quote session before evaluation month.')
        as_of = pd.Timestamp(earlier[-1])
        test = evaluation[evaluation['signal_date'].dt.to_period('M') == month].copy()
        if as_of >= test['signal_date'].min():
            raise ValueError('Fitting must precede every evaluated signal date.')
        plan.append((str(month), as_of, test))
    return plan


def partition_record(part):
    return {'rows': len(part), 'signal_dates': int(part['signal_date'].nunique()),
            'start': str(part['signal_date'].min().date()), 'end': str(part['signal_date'].max().date()),
            'latest_label_available': str(part['label_available_date'].max().date()),
            'positive_rate': float(part['target'].mean())}


def fit_asof(train, calibration, as_of, window, metadata, output_dir):
    as_of = pd.Timestamp(as_of)
    if not train['label_available_date'].max() < calibration['signal_date'].min():
        raise ValueError('Training labels cross into calibration.')
    if calibration['label_available_date'].max() > as_of:
        raise ValueError('Calibration uses labels unavailable at fit time.')
    with threadpool_limits(limits=2):
        classifier = classifiers()['hist_gradient_boosting']
        classifier.fit(train[FEATURES], train['target'])
        calibrator = LogisticRegression(C=1.0, solver='liblinear', max_iter=1000, random_state=42)
        calibrator.fit(logits(classifier, calibration[FEATURES]), calibration['target'])
        regressor = new_regressor().fit(train[FEATURES], train['target_return'])
        bundle = {'classifier': classifier, 'calibrator': calibrator, 'regressor': regressor}
        probability, returns = predict_values(bundle, calibration[FEATURES])
    fit_rows = pd.concat([train.assign(fit_partition='train'), calibration.assign(fit_partition='calibration')])
    fingerprint = hashlib.sha256(pd.util.hash_pandas_object(
        fit_rows[['stock_code', 'signal_date', 'label_available_date', 'target_return', 'fit_partition'] + FEATURES], index=False
    ).values.tobytes()).hexdigest()
    known_metadata = {key: metadata[key] for key in [
        'target_definition', 'execution_note', 'universe_note', 'history_provenance',
        'horizon_sessions', 'cost_assumption', 'data_root', 'experiment_protocol_sha256', 'implementation_sha256',
    ] if key in metadata}
    prior = float(calibration['target'].mean())
    known_metadata.update({
        'feature_version': HISTORY_FEATURE_VERSION, 'features': FEATURES,
        'source_ref': 'monthly_price_walkforward_v1/' + str(window), 'asof_only': True,
        'dataset_sha256': fingerprint, 'trained_at': datetime.now(timezone.utc).isoformat(),
        'as_of': str(as_of.date()), 'latest_signal_date': str(as_of.date()),
        'classifier': 'hist_gradient_boosting', 'training_window_sessions': window,
        'probability_threshold': PROBABILITY_THRESHOLD, 'baseline_probability': prior,
        'baseline_return': float(train['target_return'].median()),
        'calibration_parameters': {'slope': float(calibrator.coef_[0, 0]), 'intercept': float(calibrator.intercept_[0])},
        'partitions': {'train': partition_record(train), 'calibration': partition_record(calibration)},
        'test': {'base_rate': prior, 'roc_auc': None, 'recommendation_gate_passed': False,
                 'gate_reasons': ['retrospective_walkforward_requires_future_validation'],
                 'base_rate_source': 'known_calibration_prevalence_not_future_test',
                 'evaluation_role': 'No future-month labels or evaluation scores are attached to this as-of bundle.'},
    })
    bundle['metadata'] = known_metadata
    diagnostics = calibration[['stock_code', 'signal_date', 'target']].copy()
    diagnostics['probability_above_cost'] = probability
    diagnostics['predicted_close_return'] = returns
    diagnostics['role'] = 'calibrator_fit_diagnostic_not_independent_validation'
    _, run_dir = save_artifacts(bundle, diagnostics, output_dir, predictions_name='calibration_predictions.csv')
    return bundle, run_dir


def predict_month(bundle, run_dir, test, variant, common_prior):
    model_asof = pd.Timestamp(bundle['metadata']['as_of'])
    if not model_asof < test['signal_date'].min():
        raise ValueError('Evaluation inputs must follow the fitted as-of date.')
    with threadpool_limits(limits=2):
        probability, returns = predict_values(bundle, test[FEATURES])
    if not np.isfinite(probability).all() or not np.isfinite(returns).all():
        raise ValueError('Nonfinite walk-forward predictions.')
    result = test[['stock_code', 'signal_date', 'target_date', 'label_available_date', 'target', 'target_return', 'net_return_proxy']].copy()
    result['probability_above_cost'] = probability
    result['predicted_close_return'] = returns
    result['selected_by_fixed_policy'] = (probability >= PROBABILITY_THRESHOLD) & (returns > bundle['metadata']['cost_assumption'])
    result['own_baseline_probability'] = bundle['metadata']['baseline_probability']
    result['common_rolling_baseline_probability'] = common_prior
    result['baseline_return'] = bundle['metadata']['baseline_return']
    result['model_asof'] = str(model_asof.date())
    result['model_run'] = Path(run_dir).name
    result['variant'] = variant
    result['recorded_at'] = datetime.now(timezone.utc).isoformat()
    result['origin'] = 'retrospective_replay_not_prospective_forecast'
    result['recommendation'] = 'ABSTAIN'
    return result


def summarize(predictions):
    if predictions.duplicated(['stock_code', 'signal_date']).any():
        raise ValueError('Duplicate stock/date predictions would inflate evaluation.')
    y, probability = predictions['target'], predictions['probability_above_cost']
    selected = predictions[predictions['selected_by_fixed_policy']]
    result = date_metrics(predictions, predictions['common_rolling_baseline_probability'].to_numpy(), with_uncertainty=True)
    result.update({
        'evaluated_rows': len(predictions), 'signal_dates': int(predictions['signal_date'].nunique()),
        'roc_auc': float(roc_auc_score(y, probability)) if y.nunique() == 2 else None,
        'brier_score': float(brier_score_loss(y, probability)),
        'own_baseline_brier_score': float(brier_score_loss(y, predictions['own_baseline_probability'])),
        'own_date_baseline_brier': float(brier_score_loss(y, predictions['own_baseline_probability'], sample_weight=date_weights(predictions))),
        'return_mae': float(mean_absolute_error(predictions['target_return'], predictions['predicted_close_return'])),
        'baseline_return_mae': float(mean_absolute_error(predictions['target_return'], predictions['baseline_return'])),
        'selected_count': len(selected), 'selected_dates': int(selected['signal_date'].nunique()),
        'selected_success_rate': float(selected['target'].mean()) if len(selected) else None,
        'recommendation_gate_passed': False,
    })
    result['calibration_bins'] = []
    for lower, upper in [(0, .2), (.2, .4), (.4, .6), (.6, .8), (.8, 1)]:
        part = predictions[(probability >= lower) & ((probability < upper) if upper < 1 else (probability <= upper))]
        if len(part):
            result['calibration_bins'].append({'range': [lower, upper], 'count': len(part),
                                               'mean_probability': float(part['probability_above_cost'].mean()),
                                               'observed_rate': float(part['target'].mean())})
    return result


def paired_interval(reference, candidate, samples=5000):
    columns = ['stock_code', 'signal_date', 'target']
    if not reference[columns].reset_index(drop=True).equals(candidate[columns].reset_index(drop=True)):
        raise ValueError('Paired comparison requires identical rows and outcomes.')
    left = (reference['probability_above_cost'] - reference['target']) ** 2
    right = (candidate['probability_above_cost'] - candidate['target']) ** 2
    delta = (right.to_numpy() - left.to_numpy())
    daily = pd.Series(delta).groupby(candidate['signal_date'].reset_index(drop=True)).mean().to_numpy()
    if len(daily) < 20:
        return {'date_brier_delta': float(daily.mean()), 'lower_95': None, 'upper_95': None}
    rng = np.random.default_rng(42)
    starts = rng.integers(0, len(daily), size=(samples, int(np.ceil(len(daily) / 5))))
    indices = ((starts[:, :, None] + np.arange(5)) % len(daily)).reshape(samples, -1)[:, :len(daily)]
    interval = np.quantile(daily[indices].mean(axis=1), [.025, .975])
    return {'date_brier_delta': float(daily.mean()), 'lower_95': float(interval[0]), 'upper_95': float(interval[1])}


def render_comparison(summary):
    def num(value, percentage=False):
        return 'n/a' if value is None else (f'{value:.2%}' if percentage else f'{value:.6f}')
    lines = ['# Monthly Price Walk-Forward Research', '',
             'RESEARCH_ONLY. Retrospective development replay, not prospective validation or trading.', '',
             '## Controls and Timing', '',
             'Nine price features, the existing histogram-gradient-boosting classifier/regressor, sigmoid calibration, five-session target and 60%/0.3% policy are fixed.',
             'For each training-window size, the frozen control is exactly the first monthly model. It is not the differently timed legacy fixed artifact.',
             'Refits occur before the calendar month using only mature labels. The first partial evaluation month still fits before its calendar month starts.',
             'Earlier evaluation outcomes can enter later refits only after becoming available. Already issued predictions are never regenerated with later models.',
             'All four variants use identical stock/date evaluation rows. Complete-outcome filtering and retrospective current-universe/adjusted-price limitations remain.',
             'No future-month evaluation labels or scores are attached to the as-of model bundles.', '',
             '## Aggregate Results', '',
             '| Variant | Rows | Dates | AUC | Date Brier | Own past-constant date Brier | Common monthly-constant date Brier |',
             '|---|---:|---:|---:|---:|---:|---:|']
    for name, metrics in summary['results'].items():
        lines.append(f"| {name} | {metrics['evaluated_rows']} | {metrics['signal_dates']} | {num(metrics['roc_auc'])} | {num(metrics['date_brier'])} | {num(metrics['own_date_baseline_brier'])} | {num(metrics['common_date_baseline_brier'])} |")
    lines += ['', 'Brier is lower-is-better. Own constants use each model\'s known calibration prevalence; common constants update monthly and are identical across windows.', '',
              '## Paired Monthly Minus Frozen', '', '| Window | Date Brier difference | Five-session-block 95% interval |', '|---|---:|---|']
    for window, comparison in summary['paired'].items():
        lines.append(f"| {window} | {num(comparison['date_brier_delta'])} | [{num(comparison['lower_95'])}, {num(comparison['upper_95'])}] |")
    lines += ['', 'Negative differences favor refitting. Intervals use 5,000 paired resamples of five consecutive observed signal dates, seed 42; they are development diagnostics, not guarantees.', '',
              '## Fixed Policy and All Dates', '',
              '| Variant | Selected rows | Selected dates | Pooled success | Date-equal selected success | All-date five-session net proxy | Calendar-block lower 95% |',
              '|---|---:|---:|---:|---:|---:|---:|']
    for name, metrics in summary['results'].items():
        lines.append(f"| {name} | {metrics['selected_count']} | {metrics['selected_dates']} | {num(metrics['selected_success_rate'], True)} | {num(metrics['selected_date_success_rate'], True)} | {num(metrics['all_dates_mean_net_return_proxy'], True)} | {num(metrics['all_dates_return_lower_95'], True)} |")
    lines += ['', 'No-selection dates are zero exposure proxies, not failed labels. Overlapping close-to-close outcomes after assumed cost are not executable portfolio returns. No gate is relaxed.', '',
              '## Monthly Results', '', '| Month | Variant | Rows | AUC | Date Brier | Common monthly-constant date Brier |', '|---|---|---:|---:|---:|---:|']
    for row in summary['monthly']:
        lines.append(f"| {row['month']} | {row['variant']} | {row['rows']} | {num(row['auc'])} | {num(row['date_brier'])} | {num(row['baseline_date_brier'])} |")
    lines += ['', '## Label-Time Audit', '',
              '| Month | Window | Fit as-of | Train signal range | Latest train label | Calibration signal range | Latest calibration label | Evaluated signal range |',
              '|---|---:|---|---|---|---|---|---|']
    for row in summary['fits']:
        train, calibration = row['partitions']['train'], row['partitions']['calibration']
        lines.append(f"| {row['month']} | {row['window']} | {row['as_of']} | {train['start']} to {train['end']} | {train['latest_label_available']} | {calibration['start']} to {calibration['end']} | {calibration['latest_label_available']} | {row['test_start']} to {row['test_end']} |")
    lines += ['', '## Probability Calibration', '', '| Variant | Forecast band | Rows | Mean forecast | Observed rate |', '|---|---|---:|---:|---:|']
    for name, metrics in summary['results'].items():
        for band in metrics['calibration_bins']:
            lines.append(f"| {name} | {band['range']} | {band['count']} | {num(band['mean_probability'], True)} | {num(band['observed_rate'], True)} |")
    lines += ['', '## Provenance', '', 'Common dataset SHA256: ' + summary['dataset_sha256'],
              'Protocol SHA256: ' + summary['protocol_sha256'], '',
              'No default model, candidate generator, dashboard, existing forward ledger or deployment was changed.',
              'Model files, calibration-fit diagnostics and historical prediction ledgers stay in the ignored experiment output directory.', '']
    return '\n'.join(lines)


def run_experiment(data_root, output_root, protocol, report_path):
    windows = protocol['training_windows']
    if (len(windows) != 2 or len(set(windows)) != 2 or min(windows) < 15
            or protocol['classifier'] != 'hist_gradient_boosting' or protocol['features'] != FEATURES
            or protocol['horizon_sessions'] != 5 or protocol['cost_assumption'] != .003
            or protocol['probability_threshold'] != PROBABILITY_THRESHOLD):
        raise ValueError('Unsupported fitting/target protocol.')
    snapshots, _ = load_snapshots(data_root)
    if snapshots.attrs.get('feature_version') != HISTORY_FEATURE_VERSION:
        raise ValueError('Monthly replay requires coherent completed OHLCV history.')
    dataset, metadata = build_dataset(snapshots, as_of=protocol['labels_as_of'])
    calendar = pd.DatetimeIndex(sorted(snapshots.loc[snapshots['signal_date'] <= pd.Timestamp(protocol['labels_as_of']), 'signal_date'].unique()))
    plan = month_plan(dataset, calendar, protocol['evaluation_start'], protocol['evaluation_end'])
    for _, as_of, _ in plan:
        for window in windows:
            monthly_split(dataset, as_of, window, protocol['calibration_sessions'])
    metadata['data_root'] = str(Path(data_root).resolve())
    metadata['experiment_protocol_sha256'] = hashlib.sha256(json_text(protocol).encode()).hexdigest()
    metadata['implementation_sha256'] = {str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
                                         for path in [Path(__file__), ROOT / 'src/models/price_forecaster.py', ROOT / 'src/features/price_learning_dataset.py', ROOT / 'src/models/market_context_experiment.py']}
    anchors, predictions, fits = {}, {}, []
    monthly_results = []
    print(json_text({'months': len(plan), 'fit_count': len(plan) * len(windows), 'evaluation_rows': sum(len(test) for _, _, test in plan)}), flush=True)
    for month, as_of, test in plan:
        common_prior = None
        for window in windows:
            print(f'Fitting {month}, window={window}, as_of={as_of.date()}', flush=True)
            train, calibration = monthly_split(dataset, as_of, window, protocol['calibration_sessions'])
            bundle, run_dir = fit_asof(train, calibration, as_of, window, metadata, Path(output_root) / f'window_{window}' / month)
            prior = bundle['metadata']['baseline_probability']
            if common_prior is None:
                common_prior = prior
            elif not np.isclose(prior, common_prior, rtol=0, atol=1e-12):
                raise ValueError('Window variants unexpectedly have different calibration observations.')
            anchors.setdefault(window, (bundle, run_dir))
            for schedule, model_and_run in [('frozen', anchors[window]), ('monthly', (bundle, run_dir))]:
                name = f'{schedule}_{window}'
                scored = predict_month(*model_and_run, test, name, common_prior)
                predictions.setdefault(name, []).append(scored)
                diagnostics = date_metrics(scored, scored['common_rolling_baseline_probability'].to_numpy())
                monthly_results.append({'month': month, 'variant': name, 'rows': len(scored),
                                        'auc': float(roc_auc_score(scored['target'], scored['probability_above_cost'])) if scored['target'].nunique() == 2 else None,
                                        'date_brier': diagnostics['date_brier'], 'baseline_date_brier': diagnostics['common_date_baseline_brier']})
            fits.append({'month': month, 'window': window, 'as_of': str(as_of.date()), 'run_dir': str(run_dir),
                         'partitions': bundle['metadata']['partitions'],
                         'test_start': str(test['signal_date'].min().date()), 'test_end': str(test['signal_date'].max().date())})
    combined = {name: pd.concat(parts, ignore_index=True) for name, parts in predictions.items()}
    reference_keys = next(iter(combined.values()))[['stock_code', 'signal_date', 'target']]
    for name, frame in combined.items():
        if not reference_keys.equals(frame[['stock_code', 'signal_date', 'target']]):
            raise ValueError('Variants do not share the same evaluated observations.')
        directory = Path(output_root) / name
        directory.mkdir(parents=True, exist_ok=True)
        frame.to_csv(directory / 'historical_predictions.csv', index=False)
    summary = {'protocol': protocol, 'protocol_sha256': metadata['experiment_protocol_sha256'],
               'dataset_sha256': hashlib.sha256(pd.util.hash_pandas_object(
                   dataset[['stock_code', 'signal_date', 'label_available_date', 'target_return'] + FEATURES], index=False
               ).values.tobytes()).hexdigest(),
               'results': {name: summarize(frame) for name, frame in combined.items()},
               'paired': {str(window): paired_interval(combined[f'frozen_{window}'], combined[f'monthly_{window}']) for window in windows},
               'monthly': monthly_results, 'fits': fits}
    report_path = Path(report_path)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(render_comparison(summary), encoding='utf-8')
    report_path.with_suffix('.json').write_text(json_text(summary) + '\n', encoding='utf-8')
    print(json_text({'results': summary['results'], 'paired': summary['paired']}), flush=True)
    return summary


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--protocol', type=Path, default=ROOT / 'docs/model_experiments/monthly_walkforward_protocol_20261021.json')
    parser.add_argument('--data-root', type=Path)
    parser.add_argument('--output-root', type=Path, default=ROOT / 'data/models/price_forecaster_walkforward')
    parser.add_argument('--report-path', type=Path, default=ROOT / 'reports/daily_review/2026-10-21_monthly_price_walkforward.md')
    args = parser.parse_args()
    protocol = json.loads(args.protocol.read_text(encoding='utf-8'))
    run_experiment(args.data_root or ROOT / protocol['data_root'], args.output_root, protocol, args.report_path)


if __name__ == '__main__':
    main()
