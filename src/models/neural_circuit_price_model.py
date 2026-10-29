"""Small biological-circuit-inspired sequence research with matched controls."""
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
from scipy.special import expit
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import brier_score_loss
from sklearn.preprocessing import StandardScaler
from threadpoolctl import threadpool_limits
import torch
from torch import nn
from ncps.torch import CfC
from ncps.wirings import AutoNCP

from src.crawler.market_clock import KST, completed_price_cutoff
from src.evaluator.forward_price_forecast import valid_record_time
from src.evaluator.research_shadow_ledger import existing_full_tree_shadow, grade_shadow, seal_ledger
from src.features.next_open_dataset import TARGET_VERSION, build_next_open_dataset
from src.features.price_sequences import PriceSequences, sample_input_candidates
from src.models.next_open_price_model import evaluate, load_inputs
from src.models.price_forecaster import date_weights, fit_estimator, json_text, resolve_stock
from src.models.relative_price_selection import block_interval
from src.models.selected_price_model import COLUMNS, ROOT, factories, fit_data_digest, partition_info, to_logits, write_json

ARMS = ['last_mlp', 'gru', 'cfc_dense', 'cfc_ncp']


class SequenceClassifier(nn.Module):
    def __init__(self, kind, protocol):
        super().__init__()
        self.kind = kind
        hidden = protocol['hidden_units']
        input_size = protocol.get('input_size', len(COLUMNS))
        if kind == 'last_mlp':
            self.network = nn.Sequential(nn.Linear(input_size, 64), nn.ReLU(),
                                         nn.Linear(64, hidden), nn.ReLU(), nn.Linear(hidden, 1))
        elif kind == 'gru':
            self.network = nn.GRU(input_size, hidden, batch_first=True)
            self.readout = nn.Linear(hidden, 1)
        elif kind in {'cfc_dense', 'cfc_ncp'}:
            if kind == 'cfc_ncp':
                units = AutoNCP(hidden, protocol['motor_units'],
                                sparsity_level=protocol['wiring_sparsity'], seed=protocol['wiring_seed'])
                self.network = CfC(input_size, units, return_sequences=False, batch_first=True)
                self.readout = nn.Linear(protocol['motor_units'], 1)
            else:
                self.network = CfC(input_size, hidden, return_sequences=False, batch_first=True,
                                   backbone_units=protocol['dense_backbone_units'], backbone_layers=1,
                                   backbone_dropout=0.)
                self.readout = nn.Linear(hidden, 1)
        else:
            raise ValueError('Unsupported neural arm.')

    def forward(self, values):
        if self.kind == 'last_mlp':
            return self.network(values[:, -1]).squeeze(-1)
        output, state = self.network(values)
        final = state[-1] if self.kind == 'gru' else output
        return self.readout(final).squeeze(-1)


def fit_normalizer(train, columns=COLUMNS):
    return StandardScaler().fit(train[list(columns)], sample_weight=date_weights(train))


def last_values(frame, scaler, clip):
    return np.clip(scaler.transform(frame[list(scaler.feature_names_in_)]), -clip, clip).astype(np.float32)


def train_network(kind, seed, protocol, store, train, scaler, progress=None):
    torch.manual_seed(seed)
    torch.use_deterministic_algorithms(True)
    torch.set_num_threads(protocol['compute_threads'])
    model = SequenceClassifier(kind, protocol)
    optimizer = torch.optim.AdamW(model.parameters(), lr=protocol['learning_rate'], weight_decay=protocol['weight_decay'])
    weights = date_weights(train).astype(np.float32)
    targets = train.target.to_numpy(dtype=np.float32)
    losses = []
    for epoch in range(protocol['epochs']):
        model.train()
        order = np.random.default_rng(np.random.SeedSequence([seed, epoch])).permutation(len(train))
        total = 0.
        for start in range(0, len(order), protocol['batch_size']):
            positions = order[start:start + protocol['batch_size']]
            if kind == 'last_mlp':
                values = last_values(train.iloc[positions], scaler, protocol['normalization_clip'])[:, None]
            else:
                values = store.windows(train.sequence_end.iloc[positions], scaler.mean_, scaler.scale_, protocol['normalization_clip'])
            optimizer.zero_grad(set_to_none=True)
            logits = model(torch.from_numpy(values))
            loss = (nn.functional.binary_cross_entropy_with_logits(logits, torch.from_numpy(targets[positions]), reduction='none')
                    * torch.from_numpy(weights[positions])).mean()
            if not torch.isfinite(loss):
                raise ValueError('Nonfinite neural training loss.')
            loss.backward()
            norm = nn.utils.clip_grad_norm_(model.parameters(), protocol['gradient_clip'])
            if not torch.isfinite(norm):
                raise ValueError('Nonfinite neural gradients.')
            optimizer.step()
            total += float(loss.detach()) * len(positions)
        losses.append(total / len(train))
        print(f'{kind} seed={seed} epoch={epoch + 1}/{protocol["epochs"]} training_loss={losses[-1]:.6f}', flush=True)
        if progress:
            write_json(dict(arm=kind, seed=seed, completed_epochs=epoch + 1, losses=losses), progress)
    model.eval()
    return model, losses


def raw_network_probabilities(models, frame, store, scaler, protocol, fallback=None):
    kind = models[0].kind
    output = np.tile(np.asarray(fallback, dtype=float), (len(models), 1)) if fallback is not None else np.zeros((len(models), len(frame)))
    positions = np.arange(len(frame)) if kind == 'last_mlp' else np.flatnonzero(frame.sequence_available.to_numpy())
    if kind != 'last_mlp' and fallback is None and len(positions) != len(frame):
        raise ValueError('Missing sequence requires an explicit snapshot fallback.')
    for number, model in enumerate(models):
        model.eval()
        with torch.inference_mode():
            for start in range(0, len(positions), protocol['batch_size']):
                where = positions[start:start + protocol['batch_size']]
                part = frame.iloc[where]
                values = (last_values(part, scaler, protocol['normalization_clip'])[:, None] if kind == 'last_mlp'
                          else store.windows(part.sequence_end, scaler.mean_, scaler.scale_, protocol['normalization_clip']))
                output[number, where] = expit(model(torch.from_numpy(values)).numpy().astype(float))
    if not np.isfinite(output).all() or np.any((output < 0) | (output > 1)):
        raise ValueError('Invalid neural probability.')
    return output


def raw_probabilities(bundle, frame, store):
    p, scaler = bundle['protocol'], bundle['scaler']
    result = {}
    result['last_mlp'] = raw_network_probabilities(bundle['networks']['last_mlp'], frame, store, scaler, p)
    fallback = result['last_mlp'].mean(axis=0)
    for name in ARMS[1:]:
        result[name] = raw_network_probabilities(bundle['networks'][name], frame, store, scaler, p, fallback)
    with threadpool_limits(limits=2):
        result['extra_trees'] = bundle['tree'].predict_proba(last_values(frame, scaler, p['normalization_clip']))[:, 1][None]
    return result


def calibrated_probabilities(bundle, frame, store):
    raw = raw_probabilities(bundle, frame, store)
    result = {name: bundle['calibrators'][name].predict_proba(to_logits(values.mean(axis=0)))[:, 1]
              for name, values in raw.items()}
    return result, raw


def validate_protocol(p):
    if (p['neural_arms'] != ARMS or p['primary_model'] != 'cfc_ncp'
            or p['horizon_sessions'] != 5 or p['cost_assumption'] != .003
            or p['probability_threshold'] != .6 or p['daily_selection_cap'] != 5
            or p['production_promotion'] is not False or p['compute_device'] != 'cpu'
            or not 2 <= p['sequence_sessions'] <= 100 or not 1 <= p['epochs'] <= 50
            or not p['seeds'] or len(set(p['seeds'])) != len(p['seeds'])
            or not 1 <= p['training_candidates_per_date'] <= 901
            or not 1 <= p['motor_units'] < p['hidden_units'] - 2):
        raise ValueError('Unsupported fixed neural-circuit protocol.')


def prepare_experiment(inputs, p):
    store = PriceSequences(inputs, p['sequence_sessions'])
    cohort, target_meta = build_next_open_dataset(inputs, p['labels_as_of'])
    cohort = store.attach(cohort)
    cal, test = pd.Timestamp(p['calibration_start']), pd.Timestamp(p['evaluation_start'])
    if not cohort.signal_date.min() < cal < test <= cohort.signal_date.max():
        raise ValueError('Invalid neural experiment temporal boundaries.')
    sampled = sample_input_candidates(cohort[cohort.signal_date.lt(cal)], p['training_candidates_per_date'], p['training_sampler_seed'])
    train = sampled[sampled.target.notna() & sampled.label_available_date.lt(cal) & sampled.sequence_available].copy()
    calibration = cohort[cohort.signal_date.ge(cal) & cohort.signal_date.lt(test)
                         & cohort.target.notna() & cohort.label_available_date.lt(test)].copy()
    for name, frame in [('train', train), ('calibration', calibration)]:
        if frame.signal_date.nunique() < 3 or frame.target.nunique() != 2:
            raise ValueError('Insufficient dates/classes in ' + name)
    if train.label_available_date.max() >= calibration.signal_date.min():
        raise ValueError('Training labels cross probability calibration.')
    return store, cohort, train.reset_index(drop=True), calibration.reset_index(drop=True), target_meta


def paired_error(reference, candidate, protocol):
    keys = ['stock_code', 'signal_date', 'target']
    if not reference[keys].equals(candidate[keys]):
        raise ValueError('Architecture comparisons require identical rows/outcomes.')
    mask = reference.target.notna()
    delta = ((candidate.loc[mask, 'probability_above_cost'] - candidate.loc[mask, 'target']) ** 2
             - (reference.loc[mask, 'probability_above_cost'] - reference.loc[mask, 'target']) ** 2)
    daily = delta.groupby(reference.loc[mask, 'signal_date']).mean()
    return block_interval(daily.to_numpy(), protocol['bootstrap_samples'], protocol['bootstrap_block_sessions'],
                          protocol['family_alpha'] / protocol['primary_comparisons'], protocol['bootstrap_seed'])


def render_report(summary):
    lines = ['# Neural Circuit Memory Research / 생체모방 신경회로 연구', '',
             'RESEARCH_ONLY. Known NCP/CfC architecture applied to a new project experiment; not a newly discovered universal algorithm or a finance performance guarantee.', '',
             '## Fixed Comparison', '',
             'Same 19 causal OHLCV inputs, next-open to fifth-close target after 0.3% assumed cost, date-equal fitting, partitions, fixed two-seed mean and sigmoid calibration.',
             'last_mlp uses only the final snapshot; GRU is the ordinary temporal control; dense CfC and sparse AutoNCP CfC test alternative dynamics/architectures.',
             'All recurrent models reset state per stock/window. Missing history uses a counted last_mlp fallback, never another stock or invented bars.',
             'Input-only per-date sampling limits training cost, not the prediction candidate pool. All arms use identical mature complete-sequence fitting endpoints.',
             'Architectures have different parameter counts; a difference cannot be attributed to wiring alone. No best seed, epoch, architecture or threshold is chosen using external outcomes.', '',
             '## Fit Audit', '', '```json', json_text(summary['partitions']), '```', '',
             '## Historical Development', '',
             '| Period | Arm | Candidates | Evaluated | Unknown | Date Brier | Past constant Brier | Daily AUC | Sequence fallback |',
             '|---|---|---:|---:|---:|---:|---:|---:|---:|']
    for period, arms in summary['results'].items():
        for arm, m in arms.items():
            lines.append(f"| {period} | {arm} | {m['input_candidates']} | {m['evaluated_cases']} | {m['unresolved_cases']} | {m['date_brier']} | {m['past_constant_date_brier']} | {m['mean_daily_auc']} | {m['sequence_fallback']} |")
    lines += ['', '## Equal-Coverage Monitoring and Fixed Policy', '',
              'Selections are ranked BEFORE outcomes; unknown selections are not replaced. Conditional results are not complete-policy performance.', '',
              '| Period | Arm | Group | Selected | Resolved | Unknown | Conditional daily success | Conditional mean net proxy |',
              '|---|---|---|---:|---:|---:|---:|---:|']
    for period, arms in summary['results'].items():
        for arm, metrics in arms.items():
            for group in ['top20', 'fixed_policy']:
                m = metrics[group]
                lines.append(f"| {period} | {arm} | {group} | {m['selected_cases']} | {m['evaluated_cases']} | {m['unresolved_cases']} | {m['conditional_date_success_rate']} | {m['conditional_mean_net_return_proxy']} |")
    lines += ['', '## Primary NCP Minus Each Control: Date Brier', '',
              'Four prespecified comparisons, Bonferroni family alpha 0.05; five-session circular-block bootstrap, 5,000 samples. Approximate development intervals, not untouched validation.', '',
              '```json', json_text(summary['primary_paired_error']), '```', '',
              '## Parameters and Calibration', '', '```json', json_text(summary['model_diagnostics']), '```', '',
              '## Limits', '',
              'These historical periods have already been inspected in earlier experiments. They remain development evidence, not a new independent test.',
              'Current-universe survivorship, retrospective adjustments, observed-universe calendars, outcome unavailability and unmodeled execution remain limitations.',
              'The primary research output is NCP CfC even if another model looks better; all outputs remain ABSTAIN. No production model, public dashboard metric or prior forecast is replaced.',
              'The comparison does not test bee/ant communication or homeostatic risk control. Those mechanisms must be separate ablations, not names attached to this model.', '',
              'References: https://github.com/mlech26l/ncps and https://arxiv.org/abs/2106.13898', '']
    return '\n'.join(lines)


def run_experiment(data_root, output_root, protocol, report_path):
    validate_protocol(protocol)
    if pd.Timestamp(protocol['labels_as_of']).date() > completed_price_cutoff():
        raise ValueError('Completed price labels only.')
    torch.set_num_threads(protocol['compute_threads'])
    inputs, provenance = load_inputs(data_root, protocol['labels_as_of'])
    store, cohort, train, calibration, target_meta = prepare_experiment(inputs, protocol)
    scaler = fit_normalizer(train)
    fingerprint = hashlib.sha256(fit_data_digest(train, calibration, COLUMNS).encode())
    context = store.frame[store.frame.signal_date.le(calibration.signal_date.max())]
    fingerprint.update(pd.util.hash_pandas_object(context[['stock_code', 'signal_date'] + COLUMNS], index=False).to_numpy().tobytes())
    digest = fingerprint.hexdigest()
    run_id = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '_' + uuid.uuid4().hex[:8]
    run = Path(output_root) / 'runs' / run_id
    run.mkdir(parents=True, exist_ok=False)
    bundle = dict(protocol=protocol, scaler=scaler, networks={}, calibrators={})
    diagnostics = {}
    for kind in ARMS:
        models, traces = [], []
        for seed in protocol['seeds']:
            model, losses = train_network(kind, seed, protocol, store, train, scaler, run / 'progress.json')
            models.append(model)
            traces.append({'seed': seed, 'training_loss_by_epoch': losses})
            torch.save(model.state_dict(), run / f'{kind}_{seed}.pt')
        bundle['networks'][kind] = models
        diagnostics[kind] = dict(parameters=sum(v.numel() for v in models[0].parameters()), training=traces)
    with threadpool_limits(limits=2):
        bundle['tree'] = fit_estimator(factories()['extra_trees'], last_values(train, scaler, protocol['normalization_clip']),
                                        train.target, date_weights(train))
    raw_cal = raw_probabilities(bundle, calibration, store)
    for arm, values in raw_cal.items():
        calibrator = LogisticRegression(C=1., solver='liblinear', max_iter=1000, random_state=42)
        calibrator.fit(to_logits(values.mean(axis=0)), calibration.target, sample_weight=date_weights(calibration))
        bundle['calibrators'][arm] = calibrator
        diagnostics.setdefault(arm, {})['calibration_slope'] = float(calibrator.coef_[0, 0])
        diagnostics[arm]['calibration_intercept'] = float(calibrator.intercept_[0])
    prior = float(np.average(calibration.target, weights=date_weights(calibration)))
    results, primary_frames = {}, {}
    for period, (start, end) in protocol['periods'].items():
        frame = cohort[cohort.signal_date.between(start, end)].reset_index(drop=True)
        if frame.empty:
            raise ValueError('No input candidates in required period: ' + period)
        probabilities, raw = calibrated_probabilities(bundle, frame, store)
        results[period] = {}
        for arm, probability in probabilities.items():
            scored, metrics = evaluate(frame, probability, prior)
            metrics['sequence_fallback'] = int((~frame.sequence_available).sum()) if arm in ARMS[1:] else 0
            known = frame.target.notna()
            metrics['raw_seed_date_brier'] = [float(brier_score_loss(frame.loc[known, 'target'], seed_probability[known],
                                                                     sample_weight=date_weights(frame[known]))) for seed_probability in raw[arm]]
            results[period][arm] = metrics
            cols = ['stock_code', 'signal_date', 'label_status', 'target', 'target_return', 'net_return_proxy',
                    'probability_above_cost', 'fixed_policy_selected', 'top20_monitoring_only', 'recommendation']
            scored[cols].to_csv(run / f'{period}_{arm}.csv', index=False)
            if period == protocol['primary_period']:
                primary_frames[arm] = scored[cols].copy()
    paired = {arm: paired_error(frame, primary_frames['cfc_ncp'], protocol)
              for arm, frame in primary_frames.items() if arm != 'cfc_ncp'}
    metadata = dict(schema='neural_circuit_price_v1', target_version=TARGET_VERSION, features=COLUMNS,
                    dataset_sha256=digest, trained_at=datetime.now(timezone.utc).isoformat(),
                    as_of=str(calibration.label_available_date.max().date()), protocol=protocol,
                    baseline_probability=prior, data_root=str(Path(data_root).resolve()),
                    partitions={'train': partition_info(train), 'calibration': partition_info(calibration)},
                    history_provenance=provenance, recommendation_enabled=False)
    metadata['implementation_sha256'] = hashlib.sha256(Path(__file__).read_bytes() + (ROOT / 'src/features/price_sequences.py').read_bytes()).hexdigest()
    metadata['protocol_sha256'] = hashlib.sha256(json_text(protocol).encode()).hexdigest()
    metadata['runtime'] = {'torch': torch.__version__, 'ncps': '1.0.1'}
    joblib.dump({'scaler': scaler, 'calibrators': bundle['calibrators'], 'tree': bundle['tree']}, run / 'estimators.joblib')
    write_json(metadata, run / 'model_metadata.json')
    checksums = {path.name: hashlib.sha256(path.read_bytes()).hexdigest() for path in run.iterdir()
                 if path.suffix in {'.pt', '.joblib'} or path.name == 'model_metadata.json'}
    write_json(checksums, run / 'checksums.json')
    summary = dict(run_dir=str(run.resolve()), dataset_sha256=digest, partitions=metadata['partitions'],
                   target=target_meta, model_diagnostics=diagnostics, results=results,
                   primary_paired_error=paired, recommendation_gate_passed=False,
                   gate_reasons=['historical_development_only_requires_independent_future_validation'])
    write_json(summary, run / 'summary.json')
    report = Path(report_path)
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text(render_report(summary), encoding='utf-8')
    write_json(summary, report.with_suffix('.json'))
    write_json({'run_dir': str(run.resolve()), 'checksums_sha256': hashlib.sha256((run / 'checksums.json').read_bytes()).hexdigest()},
               Path(output_root) / 'latest.json')
    return summary


def load_research(model_root):
    pointer = json.loads((Path(model_root) / 'latest.json').read_text())
    run = Path(pointer['run_dir'])
    if hashlib.sha256((run / 'checksums.json').read_bytes()).hexdigest() != pointer['checksums_sha256']:
        raise ValueError('Research checksum manifest changed.')
    checksums = json.loads((run / 'checksums.json').read_text())
    for name, digest in checksums.items():
        if Path(name).name != name or hashlib.sha256((run / name).read_bytes()).hexdigest() != digest:
            raise ValueError('Research artifact checksum mismatch.')
    metadata = json.loads((run / 'model_metadata.json').read_text())
    if (metadata['schema'] != 'neural_circuit_price_v1' or metadata['target_version'] != TARGET_VERSION
            or metadata['features'] != COLUMNS or metadata['recommendation_enabled'] is not False):
        raise ValueError('Unsupported neural research model.')
    p = metadata['protocol']
    validate_protocol(p)
    torch.set_num_threads(p['compute_threads'])
    bundle = joblib.load(run / 'estimators.joblib')
    bundle.update(metadata=metadata, protocol=p, networks={})
    for kind in ARMS:
        models = []
        for seed in p['seeds']:
            model = SequenceClassifier(kind, p)
            model.load_state_dict(torch.load(run / f'{kind}_{seed}.pt', map_location='cpu', weights_only=True))
            model.eval()
            models.append(model)
        bundle['networks'][kind] = models
    return bundle


def current_predictions(bundle, data_root, now=None):
    now = now or datetime.now(KST)
    if now.tzinfo is None or pd.Timestamp(bundle['metadata']['trained_at']) > pd.Timestamp(now):
        raise ValueError('Use a current timezone-aware clock after model creation.')
    inputs, _ = load_inputs(data_root, completed_price_cutoff(now))
    store = PriceSequences(inputs, bundle['protocol']['sequence_sessions'])
    cohort, _ = build_next_open_dataset(inputs, completed_price_cutoff(now))
    latest = store.attach(cohort[cohort.signal_date.eq(cohort.signal_date.max())]).sort_values('stock_code').reset_index(drop=True)
    if latest.empty or pd.Timestamp(bundle['metadata']['as_of']) > latest.signal_date.max():
        raise ValueError('No eligible post-fit completed inputs.')
    probabilities, _ = calibrated_probabilities(bundle, latest, store)
    frame = latest[['stock_code', 'signal_date', 'close', 'sequence_available']].rename(columns={'close': 'origin_close'})
    for name, values in probabilities.items():
        frame['probability_' + name] = values
    frame['probability_above_cost'] = probabilities['cfc_ncp']
    anchor = existing_full_tree_shadow(latest, now)
    if anchor is not None:
        frame['probability_existing_full_tree'], frame['anchor_dataset_sha256'], frame['anchor_trained_at'] = anchor
    frame['status'], frame['recommendation'] = 'RESEARCH_ONLY', 'ABSTAIN'
    return frame


def freeze_research(bundle, data_root, output_dir, now=None):
    live_clock = now is None
    now = now or datetime.now(KST)
    frame = current_predictions(bundle, data_root, now)
    if live_clock:
        now = datetime.now(KST)
    origin = frame.signal_date.max()
    if not (valid_record_time(origin, pd.Timestamp(now))
            and valid_record_time(origin, pd.Timestamp(now) + pd.Timedelta(seconds=60))):
        raise ValueError('Outside recording window; never backdate research forecasts.')
    m = bundle['metadata']
    frame['recorded_at'] = now.isoformat()
    frame['model_dataset_sha256'], frame['model_trained_at'] = m['dataset_sha256'], m['trained_at']
    frame['target_version'], frame['horizon_sessions'], frame['cost_assumption'] = TARGET_VERSION, 5, .003
    frame['validation_base_rate'] = m['baseline_probability']
    frame['source_manifest_sha256'] = hashlib.sha256((Path(data_root) / 'history_manifest.json').read_bytes()).hexdigest()
    frame['prediction_id'] = [hashlib.sha256('|'.join([code, str(origin.date()), m['dataset_sha256'], m['trained_at'], 'neural_circuit']).encode()).hexdigest()[:24] for code in frame.stock_code]
    key = hashlib.sha256((m['dataset_sha256'] + m['trained_at']).encode()).hexdigest()[:16]
    output = Path(output_dir) / f'ml_neural_circuit_forward_{origin:%Y%m%d}_{key}.csv'
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open('x', encoding='utf-8-sig') as handle:
        frame.to_csv(handle, index=False)
    arms = [name.removeprefix('probability_') for name in frame if name.startswith('probability_') and name != 'probability_above_cost']
    seal_ledger(output, 'neural_circuit', m, 'cfc_ncp', arms)
    return dict(status='awaiting_future_outcomes', frozen_predictions=len(frame), ledger=str(output), recommendation_enabled=False)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['train', 'predict', 'freeze', 'grade'])
    parser.add_argument('--protocol', type=Path, default=ROOT / 'docs/model_experiments/neural_circuit_protocol_20261022.json')
    parser.add_argument('--data-root', type=Path)
    parser.add_argument('--model-dir', type=Path, default=ROOT / 'data/models/price_neural_circuit')
    parser.add_argument('--report', type=Path, default=ROOT / 'reports/daily_review/2026-10-22_neural_circuit_research.md')
    parser.add_argument('--stock')
    parser.add_argument('--output-dir', type=Path, default=ROOT / 'data/predictions')
    parser.add_argument('--ledger', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.command == 'train':
        p = json.loads(args.protocol.read_text())
        summary = run_experiment(args.data_root or ROOT / p['data_root'], args.model_dir, p, args.report)
        print(json_text({'run_dir': summary['run_dir'], 'recommendation_gate_passed': False}))
        return
    if args.command == 'grade':
        if not args.data_root or not args.ledger or not args.output or args.ledger.resolve() == args.output.resolve():
            parser.error('grade requires --data-root, --ledger and a separate --output')
        inputs, _ = load_inputs(args.data_root, completed_price_cutoff())
        graded, summary = grade_shadow(args.ledger, inputs, completed_price_cutoff(), 'neural_circuit')
        args.output.parent.mkdir(parents=True, exist_ok=True)
        graded.to_csv(args.output, index=False)
        print(json_text(summary))
        return
    bundle = load_research(args.model_dir)
    data_root = args.data_root or bundle['metadata']['data_root']
    if args.command == 'freeze':
        print(json_text(freeze_research(bundle, data_root, args.output_dir)))
    else:
        if not args.stock:
            parser.error('predict requires --stock')
        code = resolve_stock(args.stock, [ROOT, data_root])
        current = current_predictions(bundle, data_root)
        matched = current[current.stock_code.eq(code)]
        if matched.empty:
            parser.exit(2, 'No current eligible price inputs for this stock.\n')
        print(json_text(matched.iloc[0].to_dict() | {'note': 'Unapproved research probabilities, not measured reliability.'}))


if __name__ == '__main__':
    main()
