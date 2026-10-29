"""Matched OHLCV/context comparison with feature/family selection inside training."""
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

from src.features.completed_price_dataset import HISTORY_FEATURE_VERSION
from src.features.price_learning_dataset import build_dataset, load_snapshots, temporal_partitions
from src.models.monthly_price_walkforward import paired_interval
from src.models.ohlcv_information_experiment import development_screen
from src.models.price_forecaster import json_text
from src.models.selected_price_model import (
    COLUMNS, CONTEXT_COLUMNS, NAMES, ROOT, fit_data_digest, fit_selected, partition_info,
    prepare_selected_features, score_period, select_family, write_json,
)

FEATURE_SETS = {'ohlcv_19': COLUMNS, 'ohlcv_market_29': CONTEXT_COLUMNS}


def select_inputs(train, progress_root=None):
    choices, outcomes = {}, {}
    for arm, columns in FEATURE_SETS.items():
        print('Training-only feature arm: ' + arm, flush=True)
        path = Path(progress_root) / (arm + '_progress.json') if progress_root else None
        name, scores, constant, folds, oof = select_family(train, progress_path=path, columns=columns)
        choices[arm] = {'family': name, 'scores': scores, 'constant_brier': constant, 'folds': folds}
        outcomes[arm] = oof
    selected_arm = min(choices, key=lambda arm: (
        choices[arm]['scores'][choices[arm]['family']], arm, choices[arm]['family']))
    return selected_arm, choices, outcomes


def render_report(summary):
    lines = ['# OHLCV + Market Context Model Selection', '',
             'RESEARCH_ONLY. No production promotion. All external periods are previously inspected historical development data.', '',
             '## Training-Only Selection', '',
             'Chosen input: ' + summary['selected_arm'],
             'Chosen family: ' + summary['selected_family'],
             'Three purged expanding folds select the input/family. Calibration and external scores do not choose them.',
             'Market inputs describe the observed current universe, not KOSPI/KOSDAQ or an investable index.', '',
             '| Input | Family | Training-only date Brier |', '|---|---|---:|']
    for arm, choice in summary['choices'].items():
        for family, score in choice['scores'].items():
            lines.append(f'| {arm} | {family} | {score:.6f} |')
    lines += ['', '## Identical-Row Historical Evaluation', '',
              '| Period | Input | Rows | Dates | AUC | Daily AUC | Date Brier | Constant Brier | Policy cases | Policy dates |',
              '|---|---|---:|---:|---:|---:|---:|---:|---:|---:|']
    for period, arms in summary['results'].items():
        for arm, metrics in arms.items():
            lines.append(f"| {period} | {arm} | {metrics['evaluated_rows']} | {metrics['signal_dates']} | {metrics['roc_auc']} | {metrics['mean_daily_cross_section_auc']} | {metrics['date_brier']:.6f} | {metrics['common_date_baseline_brier']:.6f} | {metrics['selected_count']} | {metrics['selected_dates']} |")
    lines += ['', '## Context Minus OHLCV', '', '| Period | Date Brier difference | 95% five-date-block interval |', '|---|---:|---|']
    for period, paired in summary['paired'].items():
        lines.append(f"| {period} | {paired['date_brier_delta']:.6f} | [{paired['lower_95']}, {paired['upper_95']}] |")
    lines += ['', '## Fixed Policy and Empirical Range', '',
              '| Period | Input | All-date net return proxy | Block lower 95% | Range coverage | Range width |',
              '|---|---|---:|---:|---:|---:|']
    for period, arms in summary['results'].items():
        for arm, metrics in arms.items():
            lines.append(f"| {period} | {arm} | {metrics['all_dates_mean_net_return_proxy']} | {metrics['all_dates_return_lower_95']} | {metrics['empirical_interval_coverage']:.2%} | {metrics['empirical_interval_width']:.2%} |")
    lines += ['', 'Fixed policy remains p >= 0.60 AND median return proxy > 0.003. No-selection days are zero exposure.',
              'Overlapping close-to-close outcomes are not executable strategy or compounded returns. Empirical ranges have no coverage guarantee.', '',
              'Development screen: ' + str(summary['development_screen_passed']),
              'Reasons: ' + ', '.join(summary['screen_reasons']),
              'Recommendation gate: False, including when the training-selected input is OHLCV only.', '',
              '## Audit', '', 'Fit as-of: ' + summary['fit_as_of'],
              'Partitions: ' + str(summary['partitions']),
              'Common finite-29-feature cohort exclusions: ' + str(summary['cohort_excluded_rows']),
              'Both arms use the same rows, label definition, dates, weights and calibration method.',
              'Each regressor uses its own feature set; it is a conditional-median proxy, not an expected mean.',
              'Current-universe, adjustment and repeated historical research limitations remain. No independent prospective result is claimed.',
              'Protocol SHA256: ' + summary['protocol_sha256'], 'Ignored artifacts: ' + summary['run_dir'], '']
    return '\n'.join(lines)


def run_experiment(data_root, output_root, protocol, report_path):
    if (protocol['feature_sets'] != list(FEATURE_SETS) or protocol['candidates'] != NAMES
            or protocol['cv_splits'] != 3 or protocol['probability_threshold'] != .6
            or protocol['cost_assumption'] != .003 or protocol['production_promotion'] is not False
            or protocol['candidate_pool_change'] is not False or protocol['hyperparameter_search_on_test'] is not False):
        raise ValueError('Unsupported joint feature-selection protocol.')
    raw, source = load_snapshots(data_root)
    if (raw.attrs.get('feature_version') != HISTORY_FEATURE_VERSION or source.get('skipped_files')
            or raw.attrs.get('history_provenance', {}).get('failed_stocks', 0)):
        raise ValueError('Complete verified OHLCV history is required.')
    cutoff = pd.Timestamp(protocol['labels_as_of'])
    raw = raw[raw.signal_date.le(cutoff) & raw.snapshot_date.le(cutoff)].copy()
    enriched = prepare_selected_features(raw, CONTEXT_COLUMNS, protocol['market_min_stocks'])
    dataset, dataset_metadata = build_dataset(enriched, as_of=protocol['labels_as_of'])
    valid = np.isfinite(dataset[CONTEXT_COLUMNS]).all(axis=1)
    excluded = int((~valid).sum())
    dataset = dataset[valid].copy()
    train, calibration, test = temporal_partitions(dataset, protocol['calibration_start'], protocol['test_start'])
    if train.empty or calibration.empty or test.empty:
        raise ValueError('Empty temporal partition.')
    dates = pd.DatetimeIndex(sorted(raw.signal_date.unique()))
    as_of = dates[dates < pd.Timestamp(protocol['test_start'])][-1]
    root = Path(output_root)
    run_dir = root / 'runs' / (datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '_' + uuid.uuid4().hex[:8])
    run_dir.mkdir(parents=True, exist_ok=False)
    selected_arm, choices, oofs = select_inputs(train, run_dir)
    write_json({'selected_arm': selected_arm, 'choices': choices}, run_dir / 'training_selection.json')
    for arm, oof in oofs.items():
        np.savez_compressed(run_dir / (arm + '_oof.npz'), stock_code=oof.stock_code.to_numpy(dtype='U6'),
                            signal_date=oof.signal_date.to_numpy(dtype='datetime64[ns]'), target=oof.target.to_numpy(),
                            **{name: oof[name].to_numpy() for name in NAMES + ['past_constant']})
    protocol_hash = hashlib.sha256(json_text(protocol).encode()).hexdigest()
    paths = ['src/models/context_model_selection.py', 'src/models/selected_price_model.py',
             'src/features/market_context.py', 'src/features/ohlcv_information.py',
             'src/features/price_learning_dataset.py', 'src/features/completed_price_dataset.py',
             'src/models/price_forecaster.py', 'src/models/monthly_price_walkforward.py',
             'src/models/ohlcv_information_experiment.py', 'src/models/market_context_experiment.py']
    implementation = {path: hashlib.sha256((ROOT / path).read_bytes()).hexdigest() for path in paths}
    partitions = {'train': partition_info(train), 'calibration': partition_info(calibration)}
    bundles = {}
    for arm, columns in FEATURE_SETS.items():
        bundle = fit_selected(train, calibration, choices[arm]['family'], as_of, columns=columns)
        bundle['metadata'] = {'schema': 'research_training_selected_price_v1', 'features': columns,
                              'as_of': str(as_of.date()), 'trained_at': datetime.now(timezone.utc).isoformat(),
                              'dataset_sha256': fit_data_digest(train, calibration, columns),
                              'partitions': partitions, 'selected_name': choices[arm]['family'],
                              'selected_input': arm, 'cv_scores': choices[arm]['scores'],
                              'market_min_stocks': protocol['market_min_stocks'],
                              'horizon_sessions': 5, 'cost_assumption': .003,
                              'protocol_sha256': protocol_hash, 'implementation_sha256': implementation,
                              'target_definition': dataset_metadata['target_definition'],
                              'history_provenance': dataset_metadata.get('history_provenance'),
                              'recommendation_gate_passed': False, 'data_root': str(Path(data_root).resolve())}
        joblib.dump(bundle, run_dir / (arm + '_model.joblib'), compress=3)
        bundles[arm] = bundle
    # The research pointer follows training-only selection, never external performance.
    joblib.dump(bundles[selected_arm], run_dir / 'model.joblib', compress=3)
    write_json(bundles[selected_arm]['metadata'], run_dir / 'model_metadata.json')
    results, paired = {}, {}
    for period, (start, end) in protocol['periods'].items():
        part = test[test.signal_date.between(pd.Timestamp(start), pd.Timestamp(end))]
        if part.empty:
            raise ValueError('No historical observations for ' + period)
        results[period], predictions = {}, {}
        for arm, bundle in bundles.items():
            frame, metrics = score_period(bundle, part, 'selected')
            frame.to_csv(run_dir / (arm + '_' + period + '.csv'), index=False)
            results[period][arm], predictions[arm] = metrics, frame
        paired[period] = paired_interval(predictions['ohlcv_19'], predictions['ohlcv_market_29'])
    primary = protocol['primary_period']
    reasons = development_screen(results[primary]['ohlcv_market_29'], paired[primary])
    if results[primary]['ohlcv_market_29']['empirical_interval_coverage'] < .85:
        reasons.append('empirical_interval_undercoverage')
    if selected_arm != 'ohlcv_market_29':
        reasons.append('context_not_selected_inside_training')
    summary = {'selected_arm': selected_arm, 'selected_family': choices[selected_arm]['family'],
               'choices': choices, 'partitions': partitions, 'fit_as_of': str(as_of.date()),
               'cohort_excluded_rows': excluded, 'results': results, 'paired': paired,
               'protocol': protocol, 'protocol_sha256': protocol_hash, 'implementation_sha256': implementation,
               'run_dir': str(run_dir), 'development_screen_passed': not reasons,
               'screen_reasons': reasons, 'recommendation_gate_passed': False}
    report_path = Path(report_path)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(render_report(summary), encoding='utf-8')
    write_json(summary, report_path.with_suffix('.json'))
    write_json({'run_id': run_dir.name}, root / 'latest.json')
    print(json_text({key: summary[key] for key in ['selected_arm', 'selected_family', 'paired', 'screen_reasons']}), flush=True)
    return summary


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--protocol', type=Path, default=ROOT / 'docs/model_experiments/context_selection_protocol_20261021.json')
    parser.add_argument('--data-root', type=Path)
    parser.add_argument('--model-dir', type=Path, default=ROOT / 'data/models/price_forecaster_context_selected')
    parser.add_argument('--report-path', type=Path, default=ROOT / 'reports/daily_review/2026-10-21_context_model_selection.md')
    args = parser.parse_args()
    try:
        protocol = json.loads(args.protocol.read_text())
        run_experiment(args.data_root or ROOT / protocol['data_root'], args.model_dir, protocol, args.report_path)
    except (ValueError, FileNotFoundError) as error:
        parser.exit(2, str(error) + '\n')
    except Exception as error:
        parser.exit(2, 'Context research failed: ' + type(error).__name__ + '\n')


if __name__ == '__main__':
    main()
