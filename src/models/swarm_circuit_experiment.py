"""Nature-inspired peer communication hypothesis, with shuffled-message control."""
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
from threadpoolctl import threadpool_limits
import torch

from src.crawler.market_clock import KST, completed_price_cutoff
from src.evaluator.forward_price_forecast import valid_record_time
from src.evaluator.research_shadow_ledger import existing_full_tree_shadow, grade_shadow, seal_ledger
from src.features.peer_price_messages import PEER_COLUMNS, add_peer_messages, fit_peer_graph
from src.features.price_sequences import PriceSequences
from src.models.neural_circuit_price_model import (
    SequenceClassifier, fit_normalizer, load_research, paired_error, prepare_experiment,
    raw_network_probabilities, train_network,
)
from src.models.next_open_price_model import evaluate, load_inputs
from src.models.price_forecaster import date_weights, json_text, resolve_stock
from src.models.selected_price_model import COLUMNS, ROOT, to_logits, write_json

VARIANTS = {'peer_ncp_real': ('cfc_ncp', False), 'peer_ncp_shuffled': ('cfc_ncp', True),
            'peer_gru_real': ('gru', False)}
MESSAGE_COLUMNS = COLUMNS + PEER_COLUMNS


def local_raw(parent, frame, store):
    snapshot = raw_network_probabilities(parent['networks']['last_mlp'], frame, store, parent['scaler'], parent['protocol']).mean(axis=0)
    return raw_network_probabilities(parent['networks']['cfc_ncp'], frame, store, parent['scaler'], parent['protocol'], snapshot).mean(axis=0)


def message_frame(inputs, cohort, graph, protocol, shuffled=False):
    calendar = pd.DatetimeIndex(sorted(inputs.signal_date.unique()))
    first = calendar.get_indexer([cohort.signal_date.min()])[0]
    if first < 0:
        raise ValueError('Message endpoint missing from observed calendar.')
    start = calendar[max(0, first - protocol['sequence_sessions'] + 1)]
    context = inputs[inputs.signal_date.between(start, cohort.signal_date.max())]
    augmented = add_peer_messages(context, graph, shuffled)
    store = PriceSequences(augmented, protocol['sequence_sessions'], MESSAGE_COLUMNS)
    frame = cohort.merge(augmented[['stock_code', 'signal_date'] + PEER_COLUMNS],
                         on=['stock_code', 'signal_date'], how='left', validate='1:1')
    if frame[PEER_COLUMNS].isna().any(axis=None):
        raise ValueError('Every input candidate needs an explicit peer availability value.')
    return store, store.attach(frame)


def predict_variants(bundle, inputs, cohort, base_store):
    parent = bundle['parent']
    raw_local = local_raw(parent, cohort, base_store)
    outputs = {'local_ncp': parent['calibrators']['cfc_ncp'].predict_proba(to_logits(raw_local))[:, 1]}
    transformed = {}
    for name, (_, shuffled) in VARIANTS.items():
        if shuffled not in transformed:
            transformed[shuffled] = message_frame(inputs, cohort, bundle['graph'], bundle['protocol'], shuffled)
        store, frame = transformed[shuffled]
        part = bundle['variants'][name]
        raw = raw_network_probabilities(part['models'], frame, store, part['scaler'], bundle['protocol'], raw_local).mean(axis=0)
        outputs[name] = part['calibrator'].predict_proba(to_logits(raw))[:, 1]
    return outputs


def render_report(summary):
    lines = ['# Signed Peer Communication / 종목 간 정보 교환 실험', '',
             'RESEARCH_ONLY. A design hypothesis inspired by decentralized communication, not a biological simulation, causal discovery or a high-confidence finance claim.', '',
             'The parent local NCP is fixed. Peer models use the same fitting endpoints, labels, seeds, epochs and calibration period.',
             'Edges use only pre-calibration training inputs. Positive and negative lag associations must replicate in two training halves. No evaluation outcome chooses an edge.',
             'The shuffled control preserves each target degree and signed weights but changes source identities. The real-message GRU controls whether any benefit needs the biological circuit.',
             'All candidates remain present; missing peer information is explicitly encoded as zero coverage, not a fabricated stock price.', '',
             '## Graph Audit', '', '```json', json_text(summary['graph_audit']), '```', '',
             '## Historical Development', '',
             '| Period | Arm | Candidates | Resolved | Unknown | Date Brier | Daily AUC | Top20 conditional daily success | Top20 conditional net proxy |',
             '|---|---|---:|---:|---:|---:|---:|---:|---:|']
    for period, arms in summary['results'].items():
        for name, m in arms.items():
            lines.append(f"| {period} | {name} | {m['input_candidates']} | {m['evaluated_cases']} | {m['unresolved_cases']} | {m['date_brier']} | {m['mean_daily_auc']} | {m['top20']['conditional_date_success_rate']} | {m['top20']['conditional_mean_net_return_proxy']} |")
    lines += ['', 'Unknown selected outcomes are not replaced; conditional returns do not establish full policy performance.', '',
              '## Primary Real Peer NCP Minus Controls', '',
              'Three prespecified family-adjusted five-session-block intervals. Previously inspected periods remain development evidence, not independent validation.',
              '```json', json_text(summary['primary_paired_error']), '```', '',
              'No production model, scoring formula, old original ledger or public confidence metric was replaced. All recommendations remain ABSTAIN.',
              'Lag correlations are associations, not causal evidence. Current-universe and retrospectively adjusted-price biases remain. The graph is frozen, not an online ant-colony optimizer.', '']
    return '\n'.join(lines)


def run_experiment(data_root, parent_root, output_root, experiment, report_path):
    if experiment['primary_model'] != 'peer_ncp_real' or experiment['production_promotion'] is not False:
        raise ValueError('Unsupported peer experiment.')
    parent = load_research(parent_root)
    p = dict(parent['protocol'], input_size=len(MESSAGE_COLUMNS), primary_comparisons=experiment['primary_comparisons'],
             family_alpha=experiment['family_alpha'])
    inputs, _ = load_inputs(data_root, p['labels_as_of'])
    store, cohort, train, calibration, _ = prepare_experiment(inputs, parent['protocol'])
    with threadpool_limits(limits=2):
        graph = fit_peer_graph(inputs, train.signal_date.max(), experiment['graph_top_k'], experiment['minimum_half_pairs'],
                               experiment['minimum_abs_correlation'], experiment['shuffle_seed'])
    run = Path(output_root) / 'runs' / (datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '_' + uuid.uuid4().hex[:8])
    run.mkdir(parents=True, exist_ok=False)
    parent_pointer = json.loads((Path(parent_root) / 'latest.json').read_text())
    write_json(parent_pointer, run / 'parent/latest.json')
    bundle = dict(parent=parent, protocol=p, graph=graph, variants={})
    raw_cal_local = local_raw(parent, calibration, store)
    transformed = {}
    fit_cohort = pd.concat([train, calibration], ignore_index=True)
    for name, (kind, shuffled) in VARIANTS.items():
        if shuffled not in transformed:
            transformed[shuffled] = message_frame(inputs, fit_cohort, graph, p, shuffled)
        peer_store, full_frame = transformed[shuffled]
        keys = ['stock_code', 'signal_date']
        peer_train = train[keys].merge(full_frame, on=keys, how='left', validate='1:1')
        peer_cal = calibration[keys].merge(full_frame, on=keys, how='left', validate='1:1')
        scaler = fit_normalizer(peer_train, MESSAGE_COLUMNS)
        models = []
        for seed in p['seeds']:
            model, _ = train_network(kind, seed, p, peer_store, peer_train, scaler, run / 'progress.json')
            torch.save(model.state_dict(), run / f'{name}_{seed}.pt')
            models.append(model)
        raw = raw_network_probabilities(models, peer_cal, peer_store, scaler, p, raw_cal_local).mean(axis=0)
        calibrator = LogisticRegression(C=1., solver='liblinear', max_iter=1000, random_state=42)
        calibrator.fit(to_logits(raw), peer_cal.target, sample_weight=date_weights(peer_cal))
        bundle['variants'][name] = dict(models=models, scaler=scaler, calibrator=calibrator)
    del transformed, peer_store, full_frame, peer_train, peer_cal, fit_cohort
    results, primary_frames = {}, {}
    for period, (start, end) in p['periods'].items():
        frame = cohort[cohort.signal_date.between(start, end)].reset_index(drop=True)
        outputs = predict_variants(bundle, inputs, frame, store)
        results[period] = {}
        for name, probability in outputs.items():
            scored, metrics = evaluate(frame, probability, parent['metadata']['baseline_probability'])
            results[period][name] = metrics
            keep = ['stock_code', 'signal_date', 'label_status', 'target', 'target_return', 'net_return_proxy',
                    'probability_above_cost', 'fixed_policy_selected', 'top20_monitoring_only', 'recommendation']
            scored[keep].to_csv(run / f'{period}_{name}.csv', index=False)
            if period == p['primary_period']:
                primary_frames[name] = scored[keep].copy()
    paired = {name: paired_error(frame, primary_frames['peer_ncp_real'], p)
              for name, frame in primary_frames.items() if name != 'peer_ncp_real'}
    audit = {key: value for key, value in graph.items() if key not in {'weights', 'shuffled_weights', 'codes'}}
    audit['stocks'] = len(graph['codes'])
    metadata = dict(schema='swarm_circuit_v1', target_version=parent['metadata']['target_version'], protocol=p,
                    experiment=experiment, trained_at=datetime.now(timezone.utc).isoformat(),
                    as_of=parent['metadata']['as_of'], baseline_probability=parent['metadata']['baseline_probability'],
                    parent_dataset_sha256=parent['metadata']['dataset_sha256'], data_root=str(Path(data_root).resolve()),
                    recommendation_enabled=False)
    metadata['dataset_sha256'] = hashlib.sha256(parent['metadata']['dataset_sha256'].encode() + graph['weights'].tobytes()
                                              + graph['shuffled_weights'].tobytes() + json_text(experiment).encode()).hexdigest()
    metadata['implementation_sha256'] = hashlib.sha256(Path(__file__).read_bytes() + (ROOT / 'src/features/peer_price_messages.py').read_bytes()).hexdigest()
    auxiliary = {name: {key: value for key, value in part.items() if key != 'models'} for name, part in bundle['variants'].items()}
    joblib.dump(dict(graph=graph, variants=auxiliary), run / 'estimators.joblib')
    write_json(metadata, run / 'model_metadata.json')
    checksums = {str(path.relative_to(run)): hashlib.sha256(path.read_bytes()).hexdigest() for path in run.rglob('*')
                 if path.is_file() and (path.suffix in {'.pt', '.joblib'} or path.name in {'model_metadata.json', 'latest.json'})}
    write_json(checksums, run / 'checksums.json')
    summary = dict(run_dir=str(run.resolve()), graph_audit=audit, results=results,
                   primary_paired_error=paired, recommendation_gate_passed=False,
                   gate_reasons=['development_only_requires_independent_future_validation'])
    write_json(summary, run / 'summary.json')
    report = Path(report_path)
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text(render_report(summary), encoding='utf-8')
    write_json(summary, report.with_suffix('.json'))
    write_json({'run_dir': str(run.resolve()), 'checksums_sha256': hashlib.sha256((run / 'checksums.json').read_bytes()).hexdigest()},
               Path(output_root) / 'latest.json')
    return summary


def load_swarm(model_root):
    pointer = json.loads((Path(model_root) / 'latest.json').read_text())
    run = Path(pointer['run_dir'])
    if hashlib.sha256((run / 'checksums.json').read_bytes()).hexdigest() != pointer['checksums_sha256']:
        raise ValueError('Peer model checksum manifest changed.')
    for name, digest in json.loads((run / 'checksums.json').read_text()).items():
        if (Path(name).is_absolute() or '..' in Path(name).parts
                or hashlib.sha256((run / name).read_bytes()).hexdigest() != digest):
            raise ValueError('Peer artifact checksum mismatch.')
    metadata = json.loads((run / 'model_metadata.json').read_text())
    if metadata['schema'] != 'swarm_circuit_v1' or metadata['recommendation_enabled'] is not False:
        raise ValueError('Unsupported unapproved peer model.')
    bundle = joblib.load(run / 'estimators.joblib')
    bundle.update(parent=load_research(run / 'parent'), metadata=metadata, protocol=metadata['protocol'])
    for name, (kind, _) in VARIANTS.items():
        models = []
        for seed in bundle['protocol']['seeds']:
            model = SequenceClassifier(kind, bundle['protocol'])
            model.load_state_dict(torch.load(run / f'{name}_{seed}.pt', map_location='cpu', weights_only=True))
            model.eval()
            models.append(model)
        bundle['variants'][name]['models'] = models
    return bundle


def current_predictions(bundle, data_root, now=None):
    now = now or datetime.now(KST)
    if now.tzinfo is None or pd.Timestamp(bundle['metadata']['trained_at']) > pd.Timestamp(now):
        raise ValueError('Use a current timezone-aware clock after model creation.')
    inputs, _ = load_inputs(data_root, completed_price_cutoff(now))
    from src.features.next_open_dataset import build_next_open_dataset
    cohort, _ = build_next_open_dataset(inputs, completed_price_cutoff(now))
    store = PriceSequences(inputs, bundle['protocol']['sequence_sessions'])
    latest = store.attach(cohort[cohort.signal_date.eq(cohort.signal_date.max())]).sort_values('stock_code').reset_index(drop=True)
    outputs = predict_variants(bundle, inputs, latest, store)
    frame = latest[['stock_code', 'signal_date', 'close']].rename(columns={'close': 'origin_close'})
    for name, probability in outputs.items():
        frame['probability_' + name] = probability
    frame['probability_above_cost'] = outputs['peer_ncp_real']
    anchor = existing_full_tree_shadow(latest, now)
    if anchor is not None:
        frame['probability_existing_full_tree'], frame['anchor_dataset_sha256'], frame['anchor_trained_at'] = anchor
    frame['recommendation'], frame['status'] = 'ABSTAIN', 'RESEARCH_ONLY'
    return frame


def freeze_swarm(bundle, data_root, output_dir, now=None):
    live_clock = now is None
    now = now or datetime.now(KST)
    frame = current_predictions(bundle, data_root, now)
    if live_clock:
        now = datetime.now(KST)
    origin = frame.signal_date.max()
    if (not valid_record_time(origin, pd.Timestamp(now))
            or not valid_record_time(origin, pd.Timestamp(now) + pd.Timedelta(seconds=60))
            or pd.Timestamp(bundle['metadata']['as_of']) > origin):
        raise ValueError('Never backdate peer forecasts or use future fitted labels.')
    m = bundle['metadata']
    frame['recorded_at'], frame['model_trained_at'] = now.isoformat(), m['trained_at']
    frame['model_dataset_sha256'] = m['dataset_sha256']
    frame['target_version'], frame['horizon_sessions'], frame['cost_assumption'] = m['target_version'], 5, .003
    frame['validation_base_rate'] = m['baseline_probability']
    frame['source_manifest_sha256'] = hashlib.sha256((Path(data_root) / 'history_manifest.json').read_bytes()).hexdigest()
    frame['prediction_id'] = [hashlib.sha256('|'.join([code, str(origin.date()), m['dataset_sha256'], m['trained_at'], 'peer']).encode()).hexdigest()[:24] for code in frame.stock_code]
    key = hashlib.sha256((m['dataset_sha256'] + m['trained_at']).encode()).hexdigest()[:16]
    path = Path(output_dir) / f'ml_swarm_circuit_forward_{origin:%Y%m%d}_{key}.csv'
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('x', encoding='utf-8-sig') as handle:
        frame.to_csv(handle, index=False)
    arms = [name.removeprefix('probability_') for name in frame if name.startswith('probability_') and name != 'probability_above_cost']
    seal_ledger(path, 'swarm_circuit', m, 'peer_ncp_real', arms)
    return dict(status='awaiting_future_outcomes', frozen_predictions=len(frame), ledger=str(path), recommendation_enabled=False)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['train', 'predict', 'freeze', 'grade'])
    parser.add_argument('--protocol', type=Path, default=ROOT / 'docs/model_experiments/swarm_circuit_protocol_20261022.json')
    parser.add_argument('--parent-model-dir', type=Path)
    parser.add_argument('--data-root', type=Path)
    parser.add_argument('--model-dir', type=Path, default=ROOT / 'data/models/price_swarm_circuit')
    parser.add_argument('--report', type=Path, default=ROOT / 'reports/daily_review/2026-10-22_swarm_circuit_research.md')
    parser.add_argument('--stock')
    parser.add_argument('--output-dir', type=Path, default=ROOT / 'data/predictions')
    parser.add_argument('--ledger', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.command == 'train':
        experiment = json.loads(args.protocol.read_text())
        summary = run_experiment(args.data_root or ROOT / experiment['data_root'],
                                 args.parent_model_dir or ROOT / experiment['parent_model_root'], args.model_dir, experiment, args.report)
        print(json_text({'run_dir': summary['run_dir'], 'recommendation_gate_passed': False}))
    elif args.command == 'grade':
        if not args.data_root or not args.ledger or not args.output or args.ledger.resolve() == args.output.resolve():
            parser.error('grade needs --data-root, --ledger and separate --output')
        inputs, _ = load_inputs(args.data_root, completed_price_cutoff())
        frame, summary = grade_shadow(args.ledger, inputs, completed_price_cutoff(), 'swarm_circuit')
        args.output.parent.mkdir(parents=True, exist_ok=True)
        frame.to_csv(args.output, index=False)
        print(json_text(summary))
    else:
        bundle = load_swarm(args.model_dir)
        data_root = args.data_root or bundle['metadata']['data_root']
        if args.command == 'freeze':
            print(json_text(freeze_swarm(bundle, data_root, args.output_dir)))
        else:
            if not args.stock:
                parser.error('predict requires --stock')
            code = resolve_stock(args.stock, [ROOT, data_root])
            frame = current_predictions(bundle, data_root)
            matched = frame[frame.stock_code.eq(code)]
            if matched.empty:
                parser.exit(2, 'No current eligible stock price inputs.\n')
            print(json_text(matched.iloc[0].to_dict()))


if __name__ == '__main__':
    main()
