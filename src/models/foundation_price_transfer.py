"""Controlled transfer of frozen 2024 time-series patterns; no reliability promotion."""
from datetime import datetime, timezone
import argparse
import hashlib
import json
from pathlib import Path
import uuid

import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from threadpoolctl import threadpool_limits

from src.crawler.market_clock import KST, completed_price_cutoff
from src.features.foundation_price_features import FOUNDATION_COLUMNS, FoundationWindows, load_frozen_pipeline, shuffled_foundation
from src.features.next_open_dataset import TARGET_VERSION, build_next_open_dataset
from src.features.price_sequences import sample_input_candidates
from src.models.monthly_price_walkforward import monthly_split
from src.models.next_open_price_model import load_inputs, selection_summary
from src.models.pairwise_price_model import CONTEXT, calibrated_probability, cross_section_inputs, fit_monotone_calibration
from src.models.price_forecaster import date_weights, fit_estimator, json_text, resolve_stock
from src.models.relative_price_selection import rank_candidates
from src.models.selected_price_model import COLUMNS, ROOT, partition_info, write_json
from src.models.selective_price_model import paired_success

ARMS = ['price_only', 'foundation_shuffled', 'foundation_augmented']
PRIMARY = ARMS[-1]
BASIC_COLUMNS = COLUMNS + CONTEXT + ['foundation_available']


def validate_protocol(p):
    fixed = dict(experiment='next_open_foundation_transfer_v1', model_id='amazon/chronos-bolt-tiny',
                 model_revision='6904c2c38d12fb281d38cbf589c9171bfc050066',
                 horizon_sessions=5, cost_assumption=.003, daily_cap=5, probability_threshold=.6,
                 primary_arm=PRIMARY, primary_comparisons=2, production_promotion=False, candidate_pool_change=False)
    if any(p.get(k) != v for k, v in fixed.items()):
        raise ValueError('Unsupported frozen transfer protocol.')
    if (p['training_sessions'] < 15 or p['calibration_sessions'] < 3 or p['sequence_sessions'] < 2
            or p['training_samples_per_date'] < 1 or p['batch_size'] < 1 or p['logistic_C'] <= 0):
        raise ValueError('Invalid fixed compute budget.')


def model_frame(frame, name, p):
    return shuffled_foundation(frame, p['shuffle_seed']) if name == 'foundation_shuffled' else frame


def fit_heads(train, calibration, p):
    if (train.label_available_date.max() >= calibration.signal_date.min()
            or train.signal_date.min() < pd.Timestamp(p['pretrained_available_from'])):
        raise ValueError('Fitting crosses calibration or predates public pretrained availability.')
    heads, calibrators = {}, {}
    with threadpool_limits(limits=p['threads']):
        for name in ARMS:
            print('Fitting fixed foundation comparison: ' + name, flush=True)
            columns = BASIC_COLUMNS if name == 'price_only' else BASIC_COLUMNS + FOUNDATION_COLUMNS
            fitting, cal = model_frame(train, name, p), model_frame(calibration, name, p)
            model = make_pipeline(StandardScaler(), LogisticRegression(C=p['logistic_C'], max_iter=1500,
                                                                         solver='lbfgs', random_state=p['seed']))
            fit_estimator(model, fitting[columns], fitting.target.astype(int), date_weights(fitting))
            score = model.decision_function(cal[columns])
            heads[name] = model
            calibrators[name] = fit_monotone_calibration(score, cal, p['calibration_l2'])
    return dict(heads=heads, calibrators=calibrators, protocol=p)


def predict_heads(bundle, frame):
    result = frame.copy().reset_index(drop=True)
    p = bundle['protocol']
    with threadpool_limits(limits=p['threads']):
        for name in ARMS:
            columns = BASIC_COLUMNS if name == 'price_only' else BASIC_COLUMNS + FOUNDATION_COLUMNS
            current = model_frame(result, name, p)
            score = bundle['heads'][name].decision_function(current[columns])
            result['score_' + name] = score
            result['probability_' + name] = calibrated_probability(bundle['calibrators'][name], score, current)
    result['recommendation'] = 'ABSTAIN'
    return result


def evaluate(frame, p):
    masks = {name: frame.index.isin(rank_candidates(frame, 'score_' + name, p['daily_cap']).index) for name in ARMS}
    observed = frame[frame.target.notna()]
    return dict(input_candidates=len(frame), evaluated_cases=len(observed), unresolved_cases=int(frame.target.isna().sum()),
                foundation_supported=int(frame.foundation_available.sum()),
                date_brier={name: float(np.average((observed['probability_' + name] - observed.target) ** 2,
                                                         weights=date_weights(observed))) if len(observed) else None for name in ARMS},
                top5={name: selection_summary(frame, mask) for name, mask in masks.items()},
                fixed_policy={name: selection_summary(frame, frame.index.isin(rank_candidates(
                    frame[frame['probability_' + name].ge(p['probability_threshold'])], 'score_' + name, p['daily_cap']).index)) for name in ARMS},
                primary_top5_comparisons={name: paired_success(frame, masks[name], masks[PRIMARY], p) for name in ARMS[:-1]})


def cache_key(data_root, p):
    digest = hashlib.sha256((Path(data_root) / 'history_manifest.json').read_bytes())
    digest.update(json_text(p).encode())
    for name in ['src/features/foundation_price_features.py', 'src/models/foundation_price_transfer.py',
                 'src/features/price_sequences.py', 'src/models/pairwise_price_model.py',
                 'src/features/next_open_dataset.py', 'src/features/ohlcv_information.py']:
        digest.update((ROOT / name).read_bytes())
    return digest.hexdigest()


def prepare_features(inputs, frame, needed, data_root, p, root):
    key = cache_key(data_root, p)
    path = Path(root) / 'feature_cache' / (key + '.joblib')
    if path.exists():
        if hashlib.sha256(path.read_bytes()).hexdigest() != path.with_suffix('.sha256').read_text().strip():
            raise ValueError('Frozen foundation feature cache changed.')
        features = joblib.load(path)
    else:
        print(f'Extracting local frozen features for {len(needed)} candidates', flush=True)
        pipeline = load_frozen_pipeline(ROOT / p['asset_dir'], p)
        windows = FoundationWindows(inputs, p['sequence_sessions'])
        features = windows.features(needed, pipeline, p['batch_size'])
        path.parent.mkdir(parents=True, exist_ok=True)
        temporary = path.with_suffix('.tmp')
        joblib.dump(features, temporary, compress=3)
        temporary.replace(path)
        path.with_suffix('.sha256').write_text(hashlib.sha256(path.read_bytes()).hexdigest())
    result = frame.merge(features, on=['stock_code', 'signal_date'], how='inner', validate='1:1')
    if len(result) != len(needed) or not np.isfinite(result[BASIC_COLUMNS + FOUNDATION_COLUMNS]).all(axis=None):
        raise ValueError('Foundation features cannot silently drop eligible candidates.')
    return result


def render_report(summary):
    def percentage(value):
        return 'N/A' if value is None else f'{value:.2%}'
    lines = ['# Frozen Foundation Price Transfer', '',
             'RESEARCH ONLY. Frozen Chronos-Bolt-Tiny weights from the exact 2024 commit; no external inference service or remote custom code.',
             'This adds learned price-pattern features, not guaranteed new market information. It is not a newly invented foundation architecture.',
             'Same BUY next-open/fifth-close target and 0.3% assumed cost for all arms. No outcome-based inference-universe filtering.',
             'Supervised heads share input-only sampled training rows, fixed logistic capacity, full calibration rows and monotone-score calibration.',
             'The price-only control includes the same input-availability indicator. The shuffled control preserves each date and availability pattern.',
             'Open/close quantile ratios are INPUT PROXIES, not a joint return probability distribution, predicted profit or confidence interval.',
             'Unsupported/invalid price sequences keep the candidate and explicit zero-feature fallback plus availability flag.', '',
             '| Period | Method | All candidates | Foundation supported | Top5 evaluated | Unknown | Conditional daily success | Conditional net proxy | Brier |',
             '|---|---|---:|---:|---:|---:|---:|---:|---:|']
    for period, metrics in summary['results'].items():
        for name in ARMS:
            m = metrics['top5'][name]
            lines.append(f"| {period} | {name} | {metrics['input_candidates']} | {metrics['foundation_supported']} | {m['evaluated_cases']} | {m['unresolved_cases']} | {percentage(m['conditional_date_success_rate'])} | {percentage(m['conditional_mean_net_return_proxy'])} | {metrics['date_brier'][name]} |")
    lines += ['', '## Prespecified Fit', '', '```json', json_text(summary['fit']), '```', '',
              '## Full Development Results', '', '```json', json_text(summary['results']), '```', '',
              'Repeatedly inspected development history cannot certify the 60% prospective goal. All recommendations remain ABSTAIN.',
              'Current-universe survivorship, retrospective adjustment, observed-universe calendar and unmodeled fills remain limitations.',
              'Official model: https://huggingface.co/amazon/chronos-bolt-tiny', '']
    return '\n'.join(lines)


def train(data_root, output_root, p, report):
    validate_protocol(p)
    inputs, _ = load_inputs(data_root, p['labels_as_of'])
    cohort, _ = build_next_open_dataset(inputs, p['labels_as_of'])
    frame = cross_section_inputs(cohort)
    train_all, calibration = monthly_split(frame[frame.target.notna()], p['fit_as_of'], p['training_sessions'], p['calibration_sessions'])
    eligible_fit = frame[frame.signal_date.between(train_all.signal_date.min(), train_all.signal_date.max())]
    sample = sample_input_candidates(eligible_fit, p['training_samples_per_date'], p['seed'])
    keys = ['stock_code', 'signal_date']
    train_keys = sample[keys].merge(train_all[keys], on=keys, validate='1:1')
    wanted = [train_keys, calibration[keys]]
    for start, end in p['periods'].values():
        wanted.append(frame[frame.signal_date.between(start, end)][keys])
    wanted = pd.concat(wanted, ignore_index=True).drop_duplicates()
    needed = frame.merge(wanted, on=keys, validate='1:1').sort_values(['signal_date', 'stock_code']).reset_index(drop=True)
    featured = prepare_features(inputs, frame, needed, data_root, p, output_root)
    fitting = featured.merge(train_keys, on=keys, validate='1:1')
    calibration = featured.merge(calibration[keys], on=keys, validate='1:1')
    bundle = fit_heads(fitting, calibration, p)
    results = {}
    for name, (start, end) in p['periods'].items():
        part = featured[featured.signal_date.between(start, end)].reset_index(drop=True)
        if part.empty or pd.Timestamp(p['fit_as_of']) >= part.signal_date.min():
            raise ValueError('Required evaluation dates must follow fitting.')
        results[name] = evaluate(predict_heads(bundle, part), p)
    metadata = dict(schema='foundation_price_transfer_v1', target_version=TARGET_VERSION, features=BASIC_COLUMNS,
                    trained_at=datetime.now(timezone.utc).isoformat(), as_of=str(calibration.label_available_date.max().date()),
                    dataset_sha256=cache_key(data_root, p), data_root=str(Path(data_root).resolve()),
                    protocol=p, recommendation_enabled=False, baseline_probability=bundle['calibrators'][PRIMARY]['prior'])
    bundle['metadata'] = metadata
    run = Path(output_root) / 'runs' / (datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '_' + uuid.uuid4().hex[:8])
    run.mkdir(parents=True, exist_ok=False)
    joblib.dump(bundle, run / 'model.joblib', compress=3)
    write_json(metadata, run / 'model_metadata.json')
    checksums = {name: hashlib.sha256((run / name).read_bytes()).hexdigest() for name in ['model.joblib', 'model_metadata.json']}
    write_json(checksums, run / 'checksums.json')
    summary = dict(run_dir=str(run.resolve()), metadata=metadata, results=results,
                   fit=dict(train=partition_info(fitting), calibration=partition_info(calibration),
                            training_input_samples=len(sample), unknown_sampled_training_labels=len(sample) - len(fitting)),
                   calibration_slopes={name: bundle['calibrators'][name]['own_score_slope'] for name in ARMS},
                   recommendation_gate_passed=False, gate_reasons=['independent_prospective_goal_not_met'])
    write_json(summary, run / 'summary.json')
    Path(report).parent.mkdir(parents=True, exist_ok=True)
    Path(report).write_text(render_report(summary), encoding='utf-8')
    write_json(summary, Path(report).with_suffix('.json'))
    write_json(dict(run_dir=str(run.resolve()), checksums_sha256=hashlib.sha256((run / 'checksums.json').read_bytes()).hexdigest()), Path(output_root) / 'latest.json')
    return summary


def load_model(root):
    pointer = json.loads((Path(root) / 'latest.json').read_text())
    run = Path(pointer['run_dir'])
    if hashlib.sha256((run / 'checksums.json').read_bytes()).hexdigest() != pointer['checksums_sha256']:
        raise ValueError('Foundation model manifest changed.')
    for name, digest in json.loads((run / 'checksums.json').read_text()).items():
        if Path(name).name != name or hashlib.sha256((run / name).read_bytes()).hexdigest() != digest:
            raise ValueError('Foundation supervised artifact checksum mismatch.')
    bundle = joblib.load(run / 'model.joblib')
    m = bundle['metadata']
    if m != json.loads((run / 'model_metadata.json').read_text()) or m['schema'] != 'foundation_price_transfer_v1' or m['recommendation_enabled'] is not False:
        raise ValueError('Unsupported foundation model.')
    validate_protocol(m['protocol'])
    return bundle


def predict_current(bundle, data_root, now=None):
    now = now or datetime.now(KST)
    if now.tzinfo is None or pd.Timestamp(bundle['metadata']['trained_at']) > pd.Timestamp(now):
        raise ValueError('Use a timezone-aware clock after model creation.')
    p = bundle['protocol']
    inputs, _ = load_inputs(data_root, completed_price_cutoff(now))
    cohort, _ = build_next_open_dataset(inputs, completed_price_cutoff(now))
    frame = cross_section_inputs(cohort[cohort.signal_date.eq(cohort.signal_date.max())])
    if pd.Timestamp(bundle['metadata']['as_of']) > frame.signal_date.max():
        raise ValueError('No current post-fit inputs.')
    pipeline = load_frozen_pipeline(ROOT / p['asset_dir'], p)
    features = FoundationWindows(inputs, p['sequence_sessions']).features(frame, pipeline, p['batch_size'])
    frame = frame.merge(features, on=['stock_code', 'signal_date'], validate='1:1')
    return predict_heads(bundle, frame)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['train', 'predict'])
    parser.add_argument('--protocol', type=Path, default=ROOT / 'docs/model_experiments/foundation_transfer_protocol_20261026.json')
    parser.add_argument('--data-root', type=Path)
    parser.add_argument('--model-dir', type=Path, default=ROOT / 'data/models/price_foundation_transfer')
    parser.add_argument('--report', type=Path, default=ROOT / 'reports/daily_review/2026-10-26_foundation_price_transfer.md')
    parser.add_argument('--stock')
    args = parser.parse_args()
    p = json.loads(args.protocol.read_text())
    data_root = args.data_root or ROOT / p['data_root']
    if args.command == 'train':
        summary = train(data_root, args.model_dir, p, args.report)
        print(json_text(dict(run_dir=summary['run_dir'], recommendation_gate_passed=False)))
    else:
        if not args.stock:
            parser.error('predict requires --stock')
        bundle = load_model(args.model_dir)
        code = resolve_stock(args.stock, [ROOT, data_root])
        frame = predict_current(bundle, data_root)
        matched = frame[frame.stock_code.eq(code)]
        if matched.empty:
            parser.exit(2, 'No eligible current inputs for this stock.\n')
        columns = ['stock_code', 'signal_date', 'foundation_available', 'recommendation'] + ['probability_' + name for name in ARMS]
        print(json_text(matched[columns].iloc[0].to_dict() | {'note': 'Unapproved research snapshot, not independently measured reliability.'}))


if __name__ == '__main__':
    main()
