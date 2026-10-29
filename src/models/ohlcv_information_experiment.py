"""Fixed two-arm information ablation; no automatic production promotion."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys
import uuid

import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from threadpoolctl import threadpool_limits

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from src.features.completed_price_dataset import HISTORY_FEATURE_VERSION
from src.features.ohlcv_information import OHLCV_FEATURES, add_ohlcv_information
from src.features.price_learning_dataset import FEATURES, build_dataset, load_snapshots, temporal_partitions
from src.models.monthly_price_walkforward import paired_interval, summarize
from src.models.price_forecaster import classifiers, date_weights, json_text, logits, new_regressor


def fit_information_arm(train, calibration, columns):
    if not train.label_available_date.max() < calibration.signal_date.min():
        raise ValueError('Training labels cross into calibration.')
    with threadpool_limits(limits=2):
        classifier = classifiers()['hist_gradient_boosting']
        classifier.fit(train[columns], train.target, sample_weight=date_weights(train))
        calibrator = LogisticRegression(C=1, solver='liblinear', max_iter=1000, random_state=42)
        calibrator.fit(logits(classifier, calibration[columns]), calibration.target, sample_weight=date_weights(calibration))
        regressor = new_regressor().fit(train[columns], train.target_return, sample_weight=date_weights(train))
    return {'classifier': classifier, 'calibrator': calibrator, 'regressor': regressor, 'features': columns,
            'baseline_probability': float(np.average(calibration.target, weights=date_weights(calibration))),
            'baseline_return': float(train.target_return.median())}


def information_predictions(model, frame, cost=.003):
    frame = frame.reset_index(drop=True)
    with threadpool_limits(limits=2):
        probability = model['calibrator'].predict_proba(logits(model['classifier'], frame[model['features']]))[:, 1]
        returns = model['regressor'].predict(frame[model['features']])
    if not np.isfinite(probability).all() or not np.isfinite(returns).all():
        raise ValueError('Nonfinite predictions.')
    result = frame[['stock_code', 'signal_date', 'target_date', 'label_available_date', 'target', 'target_return', 'net_return_proxy']].copy()
    result['probability_above_cost'] = probability
    result['predicted_close_return'] = returns
    result['selected_by_fixed_policy'] = (probability >= .6) & (returns > cost)
    result['own_baseline_probability'] = model['baseline_probability']
    result['common_rolling_baseline_probability'] = model['baseline_probability']
    result['baseline_return'] = model['baseline_return']
    result['origin'] = 'retrospective_information_ablation_not_prospective'
    result['recommendation'] = 'ABSTAIN'
    return result


def development_screen(metrics, paired):
    reasons = []
    if paired['upper_95'] is None or paired['upper_95'] >= 0:
        reasons.append('paired_probability_improvement_not_established')
    if metrics['date_brier'] >= metrics['common_date_baseline_brier']:
        reasons.append('does_not_beat_known_constant_probability')
    if metrics['mean_daily_cross_section_auc'] is None or metrics['mean_daily_cross_section_auc'] < .55:
        reasons.append('weak_cross_sectional_discrimination')
    if metrics['selected_count'] < 100 or metrics['selected_dates'] < 20:
        reasons.append('insufficient_fixed_policy_cases_or_dates')
    if metrics['all_dates_return_lower_95'] is None or metrics['all_dates_return_lower_95'] <= 0:
        reasons.append('positive_policy_net_proxy_not_established')
    return reasons


def render(summary):
    lines = ['# OHLCV Information Learning Experiment', '',
             'RESEARCH_ONLY. New historical inputs, not a confidence-score adjustment or deployment.', '',
             'Both arms share the original absolute five-session >0.3% target, rows, purged fitting dates, date weights, fixed HGB settings and 60%/0.3% policy.',
             'Extra features use only same-close or trailing OHLCV. Volume times adjusted close is a liquidity proxy, not actual traded value. Inactive zero-volume bars contribute neutral gap/range, never an invented future quote.',
             'The later chronological audit was predeclared as primary. It is historical development evidence, not claimed an untouched final test. Current-universe, adjustment and survivorship limitations remain.', '',
             '| Period | Model | Rows | Dates | Pooled AUC | Mean daily AUC | Date Brier | Past constant Brier |',
             '|---|---|---:|---:|---:|---:|---:|---:|']
    for period, results in summary['results'].items():
        for name, row in results.items():
            lines.append(f"| {period} | {name} | {row['evaluated_rows']} | {row['signal_dates']} | {row['roc_auc']} | {row['mean_daily_cross_section_auc']} | {row['date_brier']:.6f} | {row['common_date_baseline_brier']:.6f} |")
    lines += ['', '## Fixed Policy (Date-Equal)', '',
              '| Period | Model | Selected rows | Selected dates | Date-equal success | All-date five-session net proxy | Block lower 95% |',
              '|---|---|---:|---:|---:|---:|---:|']
    def pct(value):
        return 'n/a' if value is None else f'{value:.3%}'
    for period, results in summary['results'].items():
        for name, row in results.items():
            lines.append(f"| {period} | {name} | {row['selected_count']} | {row['selected_dates']} | {pct(row['selected_date_success_rate'])} | {pct(row['all_dates_mean_net_return_proxy'])} | {pct(row['all_dates_return_lower_95'])} |")
    lines += ['', 'Zero-selection dates are zero exposure proxies, not failed predictions. Overlapping close-to-close return proxies are not executable or compounded strategy returns.', '',
              '## Paired Enriched Minus Baseline Date Brier', '',
              '| Period | Difference | Five-session-block 95% interval |', '|---|---:|---|']
    for name, row in summary['paired'].items():
        lines.append(f"| {name} | {row['date_brier_delta']:.6f} | [{row['lower_95']}, {row['upper_95']}] |")
    lines += ['', 'Negative differences favor enriched inputs. Paired circular blocks: 5,000 resamples, seed 42; approximate development diagnostics, not independent guarantees.', '',
              'Primary development screen: ' + str(summary['development_screen_passed']),
              'Reasons: ' + ', '.join(summary['screen_reasons']),
              'Production promotion: False. Separate actual future validation is still required even if development passes.', '',
              '## Fit-Time Audit', '',
              'Fit as-of: ' + summary['fit_as_of'],
              'Train: ' + str(summary['partitions']['train']),
              'Calibration: ' + str(summary['partitions']['calibration']),
              'Common-cohort excluded rows: ' + str(summary['cohort_excluded_rows']),
              'Model bundles contain only fitting-period metadata, no later outcomes or scores.', '',
              'Dataset SHA256: ' + summary['dataset_sha256'],
              'Protocol SHA256: ' + summary['protocol_sha256'],
              'Artifacts (ignored): ' + summary['run_dir'], '',
              'No scoring formula, candidate pool, deployed/default model, or original forward ledger was changed.', '']
    return '\n'.join(lines)


def run_experiment(data_root, output_root, protocol, report_path):
    if (protocol['features_added'] != OHLCV_FEATURES or protocol['probability_threshold'] != .6
            or protocol['cost_assumption'] != .003 or protocol['production_promotion'] is not False
            or protocol['candidate_pool_change'] is not False or protocol['primary_period'] not in protocol['periods']):
        raise ValueError('Unsupported information protocol.')
    snapshots, source = load_snapshots(data_root)
    if snapshots.attrs.get('feature_version') != HISTORY_FEATURE_VERSION or source.get('skipped_files'):
        raise ValueError('Verified coherent completed history is required.')
    enriched = add_ohlcv_information(snapshots)
    dataset, metadata = build_dataset(enriched, as_of=protocol['labels_as_of'])
    finite = np.isfinite(dataset[OHLCV_FEATURES]).all(axis=1)
    excluded = int((~finite).sum())
    dataset = dataset[finite].copy()
    train, calibration, test = temporal_partitions(dataset, protocol['calibration_start'], protocol['test_start'])
    as_of = pd.DatetimeIndex(sorted(snapshots.signal_date.unique()))
    as_of = as_of[as_of < pd.Timestamp(protocol['test_start'])][-1]
    if calibration.label_available_date.max() > as_of:
        raise ValueError('Calibration outcome is not known by fitting as-of.')
    created = datetime.now(timezone.utc)
    run_dir = Path(output_root) / (created.strftime('%Y%m%dT%H%M%SZ') + '_' + uuid.uuid4().hex[:8])
    run_dir.mkdir(parents=True, exist_ok=False)
    protocol_hash = hashlib.sha256(json_text(protocol).encode()).hexdigest()
    implementation = {str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
                      for path in [Path(__file__), ROOT / 'src/features/ohlcv_information.py',
                                   ROOT / 'src/features/price_learning_dataset.py', ROOT / 'src/models/price_forecaster.py',
                                   ROOT / 'src/models/monthly_price_walkforward.py', ROOT / 'src/models/market_context_experiment.py']}
    partitions = {name: {'rows': len(part), 'dates': int(part.signal_date.nunique()),
                         'start': str(part.signal_date.min().date()), 'end': str(part.signal_date.max().date()),
                         'latest_label': str(part.label_available_date.max().date())}
                  for name, part in [('train', train), ('calibration', calibration)]}
    fits, predictions, results, paired = {}, {}, {name: {} for name in protocol['periods']}, {}
    for name, columns in [('baseline', FEATURES), ('enriched', FEATURES + OHLCV_FEATURES)]:
        print('Fitting fixed information arm: ' + name, flush=True)
        model = fit_information_arm(train, calibration, columns)
        fits[name] = model
        for period, (start, end) in protocol['periods'].items():
            part = test[test.signal_date.between(pd.Timestamp(start), pd.Timestamp(end))]
            if part.empty:
                raise ValueError('No labeled observations for ' + period)
            scored = information_predictions(model, part, protocol['cost_assumption'])
            predictions[(name, period)] = scored
            scored.to_csv(run_dir / (name + '_' + period + '.csv'), index=False)
            results[period][name] = summarize(scored)
    for period in protocol['periods']:
        paired[period] = paired_interval(predictions[('baseline', period)], predictions[('enriched', period)])
    reasons = development_screen(results[protocol['primary_period']]['enriched'], paired[protocol['primary_period']])
    fit_metadata = dict(schema='research_ohlcv_information_v1', as_of=str(as_of.date()), partitions=partitions,
                        protocol_sha256=protocol_hash, implementation_sha256=implementation,
                        history_provenance=metadata.get('history_provenance'), recommendation_gate_passed=False,
                        trained_at=created.isoformat(), target_definition=metadata['target_definition'])
    joblib.dump({'models': fits, 'metadata': fit_metadata}, run_dir / 'research_models.joblib', compress=3)
    (run_dir / 'model_metadata.json').write_text(json_text(fit_metadata) + '\n', encoding='utf-8')
    summary = dict(run_dir=str(run_dir), protocol=protocol, protocol_sha256=protocol_hash,
                   implementation_sha256=implementation, fit_as_of=str(as_of.date()), partitions=partitions,
                   cohort_excluded_rows=excluded, results=results, paired=paired,
                   development_screen_passed=not reasons, screen_reasons=reasons, recommendation_gate_passed=False,
                   dataset_sha256=hashlib.sha256(pd.util.hash_pandas_object(
                       dataset[['stock_code', 'signal_date', 'label_available_date', 'target_return'] + FEATURES + OHLCV_FEATURES], index=False
                   ).values.tobytes()).hexdigest())
    report_path = Path(report_path)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(render(summary), encoding='utf-8')
    report_path.with_suffix('.json').write_text(json_text(summary) + '\n', encoding='utf-8')
    print(json_text({'paired': paired, 'development_screen_passed': not reasons, 'screen_reasons': reasons}), flush=True)
    return summary


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--protocol', type=Path, default=ROOT / 'docs/model_experiments/ohlcv_information_protocol_20261021.json')
    parser.add_argument('--data-root', type=Path)
    parser.add_argument('--output-root', type=Path, default=ROOT / 'data/models/price_forecaster_ohlcv')
    parser.add_argument('--report-path', type=Path, default=ROOT / 'reports/daily_review/2026-10-21_ohlcv_information_experiment.md')
    args = parser.parse_args()
    protocol = json.loads(args.protocol.read_text())
    run_experiment(args.data_root or ROOT / protocol['data_root'], args.output_root, protocol, args.report_path)


if __name__ == '__main__':
    main()
