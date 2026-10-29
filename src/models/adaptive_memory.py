"""Causal case memory plus delayed-feedback expert weighting; research only."""
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
from scipy.special import softmax
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import RobustScaler
from threadpoolctl import threadpool_limits

from src.crawler.market_clock import KST
from src.evaluator.forward_price_forecast import valid_record_time
from src.features.completed_price_dataset import HISTORY_FEATURE_VERSION
from src.features.price_learning_dataset import build_dataset, load_snapshots
from src.models.distributional_selector import four_partitions, selection_metrics
from src.models.monthly_price_walkforward import paired_interval
from src.models.price_forecaster import date_weights, fit_estimator, json_text, resolve_stock
from src.models.relative_price_selection import block_interval, daily_portfolio, probability_metrics, random_portfolios, rank_candidates
from src.models.selected_price_model import COLUMNS, ROOT, factories, fit_data_digest, partition_info, prepare_selected_features, to_logits, write_json

EXPERTS = ['fixed_base', 'case_memory', 'recent_prior']
METHODS = EXPERTS + ['fixed_average', 'adaptive']


def input_sample(inputs, per_date, seed):
    rows = []
    for day, part in inputs.groupby('signal_date', sort=True):
        part = part.sort_values('stock_code')
        rng = np.random.default_rng(np.random.SeedSequence([seed, int(pd.Timestamp(day).strftime('%Y%m%d'))]))
        rows.append(part.iloc[rng.permutation(len(part))[:per_date]])
    return pd.concat(rows).sort_values(['signal_date', 'stock_code']).reset_index(drop=True)


def fit_base(train, calibration):
    if train.label_available_date.max() >= calibration.signal_date.min():
        raise ValueError('Base training labels overlap probability calibration.')
    with threadpool_limits(limits=2):
        model = fit_estimator(factories()['extra_trees'], train[COLUMNS], train.target, date_weights(train))
        calibrator = LogisticRegression(C=1., solver='liblinear', max_iter=1000, random_state=42)
        calibrator.fit(to_logits(model.predict_proba(calibration[COLUMNS])[:, 1]), calibration.target,
                       sample_weight=date_weights(calibration))
    return {'model': model, 'calibrator': calibrator, 'scaler': RobustScaler().fit(train[COLUMNS]),
            'base_prior': float(np.average(calibration.target, weights=date_weights(calibration))),
            'known_label_date': calibration.label_available_date.max()}


def router_weights(log_weights, floor):
    if not 0 <= floor < 1 / len(EXPERTS):
        raise ValueError('Invalid expert weight floor.')
    values = np.asarray(log_weights, dtype=float)
    if values.shape != (len(EXPERTS),) or not np.isfinite(values).all():
        raise ValueError('Invalid expert log weights.')
    return floor + (1 - floor * len(EXPERTS)) * softmax(values)


def delayed_updates(pending, label_lookup, as_of, log_weights, protocol):
    audits, remaining = [], []
    for batch in pending:
        keys = pd.MultiIndex.from_frame(batch[['stock_code', 'signal_date']])
        answers = label_lookup.reindex(keys)
        if answers[['target', 'label_available_date']].isna().any(axis=None) or not answers.label_available_date.lt(as_of).all():
            remaining.append(batch)
            continue
        target = answers.target.to_numpy(dtype=float)
        losses = np.mean((batch[EXPERTS].to_numpy() - target[:, None]) ** 2, axis=0)
        log_weights = protocol['router_loss_discount'] * log_weights - protocol['router_learning_rate'] * losses
        log_weights -= log_weights.max()
        audits.append({'issued_date': str(pd.Timestamp(batch.signal_date.iloc[0]).date()),
                       'update_as_of': str(pd.Timestamp(as_of).date()),
                       'latest_label': str(pd.Timestamp(answers.label_available_date.max()).date()),
                       'cases': len(batch), 'date_mean_brier': losses.tolist(),
                       'weights_after': router_weights(log_weights, protocol['router_weight_floor']).tolist()})
    return remaining, log_weights, audits


def case_predictions(base, query, sampled_memory, prior_groups, day, protocol):
    mature_groups = prior_groups[prior_groups.label_available_date.lt(day)].copy()
    by_day = mature_groups.groupby('signal_date')[['total', 'count']].sum().sort_index().tail(protocol['prior_dates'])
    prior = float((by_day.total / by_day['count']).mean()) if len(by_day) else base['base_prior']
    memory = sampled_memory[sampled_memory.label_available_date.lt(day)].copy()
    days = sorted(memory.signal_date.unique())[-protocol['memory_dates']:]
    memory = memory[memory.signal_date.isin(days)].sort_values(['signal_date', 'stock_code']).reset_index(drop=True)
    output = pd.DataFrame({'case_memory': prior, 'recent_prior': prior, 'neighbor_dates': 0,
                            'neighbor_rms_distance': np.nan, 'case_supported': False}, index=np.arange(len(query)))
    if memory.empty:
        return output, None
    with threadpool_limits(limits=2):
        memory_x = np.clip(base['scaler'].transform(memory[COLUMNS]), -10, 10)
        query_x = np.clip(base['scaler'].transform(query[COLUMNS]), -10, 10)
        search = NearestNeighbors(n_neighbors=min(protocol['memory_neighbors'], len(memory)), algorithm='brute', n_jobs=2).fit(memory_x)
        distances, indices = search.kneighbors(query_x)
    calendar = np.array(sorted(sampled_memory.signal_date.unique()), dtype='datetime64[ns]')
    issue_position = np.searchsorted(calendar, np.datetime64(day))
    memory_days, targets = memory.signal_date.to_numpy(), memory.target.to_numpy()
    rows = []
    for number, (distance, neighbors) in enumerate(zip(distances, indices, strict=True)):
        source_days, inverse = np.unique(memory_days[neighbors], return_inverse=True)
        days_found = len(source_days)
        rms = float(np.median(distance) / np.sqrt(len(COLUMNS)))
        supported = days_found >= protocol['min_neighbor_dates'] and rms <= protocol['max_neighbor_rms_distance']
        scale = max(float(np.median(distance)), 1e-6)
        kernel = np.exp(-np.square(distance / scale))
        # One effective vote per source date, not one per correlated stock row.
        totals = np.bincount(inverse, weights=kernel)
        daily_target = np.bincount(inverse, weights=kernel * targets[neighbors]) / np.maximum(totals, 1e-12)
        similarity = np.zeros(days_found)
        np.maximum.at(similarity, inverse, kernel)
        age = np.maximum(issue_position - np.searchsorted(calendar, source_days), 0)
        weights = similarity * np.exp2(-age / protocol['memory_half_life_dates'])
        smooth = protocol['prior_strength_dates']
        probability = float((np.dot(weights, daily_target) + smooth * prior) / (weights.sum() + smooth))
        rows.append([probability if supported else prior, prior, days_found, rms, supported])
    output = pd.DataFrame(rows, columns=list(output.columns))
    output['case_supported'] = output.case_supported.astype(bool)
    return output, memory.label_available_date.max()


def replay(base, inputs, labels, protocol, start=None):
    start = pd.Timestamp(start or protocol['policy_calibration_start'])
    if pd.Timestamp(base['known_label_date']) >= start:
        raise ValueError('The fixed base must be calibrated before replay starts.')
    if inputs.duplicated(['stock_code', 'signal_date']).any() or labels.duplicated(['stock_code', 'signal_date']).any():
        raise ValueError('Replay requires unique original stock/date observations.')
    sampled = input_sample(inputs, protocol['memory_sample_per_date'], protocol['memory_seed'])
    sampled = sampled.merge(labels[['stock_code', 'signal_date', 'target', 'label_available_date']],
                            on=['stock_code', 'signal_date'], how='left', validate='one_to_one')
    prior_groups = labels.groupby(['signal_date', 'label_available_date']).target.agg(total='sum', count='size').reset_index()
    lookup = labels.set_index(['stock_code', 'signal_date'])[['target', 'label_available_date']]
    pending, output, update_audits, day_audits = [], [], [], []
    log_weights = np.zeros(len(EXPERTS))
    for number, (day, part) in enumerate(inputs[inputs.signal_date.ge(start)].groupby('signal_date', sort=True), 1):
        part = part.sort_values('stock_code').reset_index(drop=True)
        pending, log_weights, updates = delayed_updates(pending, lookup, day, log_weights, protocol)
        update_audits.extend(updates)
        memory, latest_label = case_predictions(base, part, sampled, prior_groups, day, protocol)
        with threadpool_limits(limits=2):
            fixed = base['calibrator'].predict_proba(to_logits(base['model'].predict_proba(part[COLUMNS])[:, 1]))[:, 1]
        scored = part[['stock_code', 'signal_date', 'close', 'return_20d']].copy()
        scored['fixed_base'] = fixed
        for column in memory:
            scored[column] = memory[column].to_numpy()
        weights = router_weights(log_weights, protocol['router_weight_floor'])
        scored['fixed_average'] = scored[EXPERTS].mean(axis=1)
        scored['adaptive'] = scored[EXPERTS].to_numpy() @ weights
        scored['probability_above_cost'] = scored.adaptive
        scored['recommendation'] = 'ABSTAIN'
        for name, value in zip(EXPERTS, weights, strict=True):
            scored['weight_' + name] = value
        pending.append(scored[['stock_code', 'signal_date'] + EXPERTS].copy())
        output.append(scored)
        day_audits.append({'signal_date': str(pd.Timestamp(day).date()), 'cases': len(scored),
                           'memory_latest_label': str(pd.Timestamp(latest_label).date()) if latest_label is not None else None,
                           'weights_before_prediction': weights.tolist(), 'updates_so_far': len(update_audits)})
        if number % 20 == 0:
            print(f'Prequential dates: {number}; resolved batch updates: {len(update_audits)}', flush=True)
    if not output:
        raise ValueError('No eligible replay observations.')
    return pd.concat(output, ignore_index=True), update_audits, day_audits, log_weights


def complete_predictions(predictions, labels):
    answers = predictions.merge(labels[['stock_code', 'signal_date', 'label_available_date', 'target', 'target_return', 'net_return_proxy']],
                                 on=['stock_code', 'signal_date'], how='inner', validate='one_to_one')
    coverage = predictions.groupby('signal_date').size().rename('issued').to_frame()
    coverage['resolved'] = answers.groupby('signal_date').size().reindex(coverage.index, fill_value=0)
    coverage['complete'] = coverage.issued.eq(coverage.resolved)
    answers = answers[answers.signal_date.isin(coverage.index[coverage.complete])].copy().reset_index(drop=True)
    if not answers.empty:
        answers['universe_return'] = answers.groupby('signal_date').target_return.transform('mean')
        answers['relative_target'] = answers.target_return.gt(answers.universe_return).astype(int)
    return answers, coverage


def policy_mask(frame, threshold, protocol):
    mask = pd.Series(False, index=frame.index)
    if threshold is not None:
        eligible = frame[frame.adaptive.ge(threshold) & frame.case_supported
                         & frame.fixed_base.sub(frame.case_memory).abs().le(protocol['policy_max_base_case_disagreement'])]
        top = rank_candidates(eligible, 'adaptive', protocol['policy_daily_cap'])
        mask.loc[top.index] = True
    return mask


def choose_policy(frame, protocol):
    trials = []
    for threshold in protocol['policy_thresholds']:
        m = selection_metrics(frame, policy_mask(frame, threshold, protocol), protocol,
                              .05 / (2 * len(protocol['policy_thresholds'])))
        passed = (m['cases'] >= protocol['policy_min_cases'] and m['dates'] >= protocol['policy_min_dates']
                  and m['date_success_rate'] is not None and m['date_success_rate'] >= protocol['policy_min_date_success']
                  and m['date_success_lower'] is not None and m['date_success_lower'] >= protocol['policy_min_success_lower']
                  and m['all_date_net_lower'] is not None and m['all_date_net_lower'] > 0)
        trials.append({'threshold': threshold, 'metrics': m, 'passed': bool(passed)})
    passing = [row for row in trials if row['passed']]
    return (max(passing, key=lambda row: (row['metrics']['all_date_net_lower'], row['threshold']))['threshold'] if passing else None), trials


def evaluate(frame, policy, prior, protocol):
    scored = frame.reset_index(drop=True).copy()
    probabilities = {name: probability_metrics(scored, scored[name].to_numpy(), 'target', prior) for name in METHODS}
    paired = {}
    for name in METHODS[:-1]:
        reference = scored.copy()
        reference['probability_above_cost'] = reference[name]
        paired[name] = paired_interval(reference, scored)
    pool = scored.groupby('signal_date').target_return.mean()
    portfolios = {name: daily_portfolio(rank_candidates(scored, name, protocol['primary_top_k']), pool)
                  for name in ['fixed_base', 'case_memory', 'fixed_average', 'adaptive', 'return_20d']}
    random, _ = random_portfolios(scored, [protocol['primary_top_k']], protocol['random_replicates'])
    portfolios['random_mean'] = random[protocol['primary_top_k']]
    returns = {name: block_interval((portfolios['adaptive'].mean_return - daily.mean_return).to_numpy(),
                                   protocol['bootstrap_samples'], protocol['bootstrap_block_sessions'], .05 / 5, protocol['bootstrap_seed'])
               for name, daily in portfolios.items() if name != 'adaptive'}
    return {'probabilities': probabilities, 'paired_brier': paired,
            'policy': selection_metrics(scored, policy_mask(scored, policy, protocol), protocol),
            'top20': {name: {column: float(daily[column].mean()) for column in ['absolute_success_rate', 'net_return_proxy', 'excess_vs_pool']}
                      for name, daily in portfolios.items()}, 'paired_top20_returns': returns}


def render(summary):
    return '\n'.join(['# Delayed-Feedback Case Memory Router', '',
                      'RESEARCH_ONLY. Inspired by retrieval augmentation and discounted expert advice; NOT a TabR/AgACI replication, proof, world-first discovery or reliable trading system.',
                      'Historical prequential DEVELOPMENT replay: earlier evaluation labels may enter memory/weights only after strict availability. Not static holdout evidence.',
                      'Each issue batch is predicted before outcomes are joined. Router updates require every original case in that batch to resolve; once per date, not once per stock.',
                      'Case votes aggregate by source date. Neighbor support and agreement are heuristics, NOT calibrated confidence bounds.', '',
                      '## Fixed Fit and Policy', '', json_text(summary['partitions']), '',
                      'Selected policy: ' + str(summary['policy']), 'Policy trials: ' + json_text(summary['policy_trials']), '',
                      '## Historical Evaluation', '', json_text(summary['results']), '',
                      '## Availability Audit', '', json_text(summary['availability']),
                      'Coverage: ' + json_text(summary['coverage']),
                      'No incomplete-date reranking. Complete-date evaluation and partially observed past case memory retain missing-outcome bias limitations.',
                      'Fixed Top20 is diagnostic only. Overlapping close-to-close cost proxies are not executable/compounded returns or a tradable index.',
                      'Screen reasons: ' + ', '.join(summary['screen_reasons']), 'Production recommendation gate: False.', '',
                      'References (inspiration, not assumed guarantees):', '- https://arxiv.org/abs/2307.14338',
                      '- https://arxiv.org/abs/1005.1918', '- https://proceedings.mlr.press/v162/zaffran22a.html', '',
                      'Current-universe, retrospectively adjusted prices and repeatedly viewed historical data limitations remain.',
                      'Protocol SHA256: ' + summary['protocol_sha256'], 'Ignored run: ' + summary['run_dir'], ''])


def run_training(data_root, output_root, protocol, report_path):
    if (protocol['horizon_sessions'] != 5 or protocol['cost_assumption'] != .003
            or protocol['production_promotion'] is not False or protocol['candidate_pool_change'] is not False
            or protocol['test_search'] is not False or protocol['world_first_or_guarantee_claim'] is not False):
        raise ValueError('Unsupported adaptive-memory protocol.')
    raw, source = load_snapshots(data_root)
    if (raw.attrs.get('feature_version') != HISTORY_FEATURE_VERSION or source.get('skipped_files')
            or raw.attrs.get('history_provenance', {}).get('failed_stocks', 0)):
        raise ValueError('Complete verified OHLCV history required.')
    cutoff = pd.Timestamp(protocol['labels_as_of'])
    raw = raw[raw.signal_date.le(cutoff) & raw.snapshot_date.le(cutoff)].copy()
    prepared = prepare_selected_features(raw, COLUMNS)
    inputs = prepared[np.isfinite(prepared[COLUMNS]).all(axis=1) & prepared.close.gt(0) & prepared.volume_ratio_20d.gt(0)].copy()
    labels, _ = build_dataset(prepared, as_of=protocol['labels_as_of'])
    labels = labels[np.isfinite(labels[COLUMNS]).all(axis=1)].copy()
    train, cal, _, _ = four_partitions(labels, protocol)
    print('Fitting fixed base before prequential replay.', flush=True)
    base = fit_base(train, cal)
    predictions, updates, days, log_weights = replay(base, inputs, labels, protocol)
    policy_start, test_start = pd.Timestamp(protocol['policy_calibration_start']), pd.Timestamp(protocol['evaluation_start'])
    policy_predictions = predictions[predictions.signal_date.ge(policy_start) & predictions.signal_date.lt(test_start)]
    policy_data, _ = complete_predictions(policy_predictions, labels[labels.label_available_date.lt(test_start)])
    if policy_data.empty:
        raise ValueError('No complete known policy-calibration outcomes.')
    policy, trials = choose_policy(policy_data, protocol)
    evaluated, coverage = complete_predictions(predictions, labels)
    results, period_coverage = {}, {}
    for name, (start, end) in protocol['periods'].items():
        part = evaluated[evaluated.signal_date.between(pd.Timestamp(start), pd.Timestamp(end))]
        count = coverage[coverage.index.to_series().between(pd.Timestamp(start), pd.Timestamp(end)).to_numpy()]
        period_coverage[name] = {'issued_dates': len(count), 'complete_dates': int(count.complete.sum()), 'evaluated_rows': len(part)}
        if part.empty:
            if name == protocol['primary_period']:
                raise ValueError('Required evaluation period has no complete outcomes.')
            results[name] = {'status': 'unavailable_no_complete_outcome_dates'}
        else:
            results[name] = {'status': 'prequential_historical_development_only', **evaluate(part, policy, base['base_prior'], protocol)}
    main = results[protocol['primary_period']]
    reasons = []
    if policy is None:
        reasons.append('no_policy_passed_separate_policy_calibration')
    if main['policy']['cases'] < 100 or main['policy']['dates'] < 20:
        reasons.append('insufficient_external_policy_evidence')
    if main['policy']['date_success_lower'] is None or main['policy']['date_success_lower'] < .6:
        reasons.append('external_60_percent_success_lower_not_established')
    if main['policy']['all_date_net_lower'] is None or main['policy']['all_date_net_lower'] <= 0:
        reasons.append('external_positive_net_proxy_not_established')
    if main['probabilities']['adaptive']['mean_daily_auc'] is None or main['probabilities']['adaptive']['mean_daily_auc'] < .55:
        reasons.append('weak_daily_discrimination')
    if any(row['upper_95'] is None or row['upper_95'] >= 0 for row in main['paired_brier'].values()):
        reasons.append('probability_advantage_over_all_controls_not_established')
    if any(row['lower'] is None or row['lower'] <= 0 for row in main['paired_top20_returns'].values()):
        reasons.append('top20_advantage_over_all_references_not_established')
    root = Path(output_root)
    run_dir = root/'runs'/(datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'_'+uuid.uuid4().hex[:8])
    run_dir.mkdir(parents=True, exist_ok=False)
    partitions = {'train': partition_info(train), 'probability_calibration': partition_info(cal), 'policy_calibration': partition_info(policy_data)}
    protocol_hash = hashlib.sha256(json_text(protocol).encode()).hexdigest()
    paths = [Path(__file__), ROOT/'src/models/distributional_selector.py', ROOT/'src/models/selected_price_model.py',
             ROOT/'src/models/relative_price_selection.py', ROOT/'src/models/monthly_price_walkforward.py',
             ROOT/'src/models/price_forecaster.py', ROOT/'src/features/ohlcv_information.py',
             ROOT/'src/features/price_learning_dataset.py', ROOT/'src/features/completed_price_dataset.py']
    implementation = {str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest() for path in paths}
    latest = predictions[predictions.signal_date.eq(predictions.signal_date.max())].copy()
    base_digest = fit_data_digest(train, cal, COLUMNS)
    mature = labels[labels.label_available_date.lt(latest.signal_date.iloc[0])].sort_values(['signal_date', 'stock_code'])
    state_digest = hashlib.sha256(base_digest.encode() + protocol_hash.encode()
                                  + pd.util.hash_pandas_object(mature[['stock_code', 'signal_date', 'label_available_date', 'target', 'target_return']], index=False).to_numpy().tobytes()
                                  + pd.util.hash_pandas_object(latest[['stock_code', 'signal_date'] + METHODS], index=False).to_numpy().tobytes()).hexdigest()
    metadata = {'schema': 'research_adaptive_memory_v1', 'trained_at': datetime.now(timezone.utc).isoformat(),
                'base_known_label_date': str(pd.Timestamp(base['known_label_date']).date()),
                'signal_date': str(pd.Timestamp(latest.signal_date.iloc[0]).date()), 'data_root': str(Path(data_root).resolve()),
                'base_dataset_sha256': base_digest, 'dataset_sha256': state_digest, 'partitions': partitions,
                'latest_known_label_date': str(pd.Timestamp(mature.label_available_date.max()).date()),
                'protocol_sha256': protocol_hash, 'implementation_sha256': implementation, 'recommendation_gate_passed': False}
    latest.to_csv(run_dir/'latest_predictions.csv', index=False)
    metadata['latest_predictions_sha256'] = hashlib.sha256((run_dir/'latest_predictions.csv').read_bytes()).hexdigest()
    joblib.dump({'base': base, 'protocol': protocol, 'policy': policy, 'log_weights': log_weights, 'metadata': metadata}, run_dir/'model.joblib', compress=3)
    write_json(metadata, run_dir/'model_metadata.json')
    predictions.to_csv(run_dir/'prequential_predictions.csv', index=False)
    write_json(updates, run_dir/'resolved_batch_updates.json')
    write_json(days, run_dir/'daily_availability_audit.json')
    summary = {'partitions': partitions, 'policy': policy, 'policy_trials': trials, 'results': results,
               'availability': {'issued_dates': len(days), 'issued_predictions': len(predictions), 'resolved_batch_updates': len(updates),
                                'last_weights': router_weights(log_weights, protocol['router_weight_floor']).tolist()},
               'coverage': period_coverage, 'screen_reasons': reasons, 'development_screen_passed': not reasons,
               'recommendation_gate_passed': False, 'protocol': protocol, 'protocol_sha256': protocol_hash,
               'implementation_sha256': implementation, 'run_dir': str(run_dir)}
    report_path = Path(report_path)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(render(summary), encoding='utf-8')
    write_json(summary, report_path.with_suffix('.json'))
    write_json({'run_id': run_dir.name}, root/'latest.json')
    print(json_text({key: summary[key] for key in ['policy', 'screen_reasons', 'availability', 'run_dir']}), flush=True)
    return summary


def load_snapshot(model_dir, now):
    root = Path(model_dir)
    run = json.loads((root/'latest.json').read_text())['run_id']
    if not run or run in {'.', '..'} or Path(run).name != run:
        raise ValueError('Invalid memory-router run identifier.')
    path = root/'runs'/run
    metadata = json.loads((path/'model_metadata.json').read_text())
    if (metadata.get('schema') != 'research_adaptive_memory_v1' or metadata.get('recommendation_gate_passed') is not False
            or pd.Timestamp(metadata['trained_at']) > pd.Timestamp(now) or pd.Timestamp(metadata['signal_date']).date() > now.date()
            or pd.Timestamp(metadata['latest_known_label_date']) >= pd.Timestamp(metadata['signal_date'])):
        raise ValueError('Only already-produced research snapshots are supported.')
    if hashlib.sha256((path/'latest_predictions.csv').read_bytes()).hexdigest() != metadata['latest_predictions_sha256']:
        raise ValueError('Latest memory-router snapshot checksum mismatch.')
    predictions = pd.read_csv(path/'latest_predictions.csv', dtype={'stock_code': str}, parse_dates=['signal_date'])
    if (predictions.empty or predictions.stock_code.duplicated().any() or predictions.signal_date.nunique() != 1
            or predictions.signal_date.iloc[0].date().isoformat() != metadata['signal_date']
            or not np.isfinite(predictions[METHODS]).all(axis=None)
            or not predictions[METHODS].ge(0).all(axis=None) or not predictions[METHODS].le(1).all(axis=None)
            or not predictions.recommendation.eq('ABSTAIN').all()):
        raise ValueError('Invalid or non-research latest snapshot.')
    return metadata, predictions


def query(model_dir, stock, now=None):
    now = now or datetime.now(KST)
    if now.tzinfo is None:
        raise ValueError('Timezone-aware query required.')
    now = now.astimezone(KST)
    metadata, predictions = load_snapshot(model_dir, now)
    code = resolve_stock(stock, [ROOT, Path(metadata['data_root'])])
    row = predictions[predictions.stock_code.eq(code)]
    if len(row) != 1:
        raise ValueError('No unique eligible latest prediction for this stock.')
    row = row.iloc[0]
    return {'stock_code': code, 'signal_date': str(row.signal_date.date()),
            'probability_above_cost': float(row.adaptive), 'fixed_base_probability': float(row.fixed_base),
            'case_probability': float(row.case_memory), 'recent_prior': float(row.recent_prior),
            'neighbor_dates': int(row.neighbor_dates), 'case_supported': bool(row.case_supported),
            'recommendation': 'ABSTAIN', 'status': 'STALE_DATA' if (now.date()-row.signal_date.date()).days > 7 else 'RESEARCH_ONLY',
            'note': 'Causal historical research snapshot; neighbor support/model weights are NOT validated confidence.'}


def freeze(model_dir, output_dir, now=None):
    now = now or datetime.now(KST)
    if now.tzinfo is None:
        raise ValueError('Timezone-aware recording required.')
    now = now.astimezone(KST)
    metadata, predictions = load_snapshot(model_dir, now)
    origin = predictions.signal_date.max()
    if not valid_record_time(origin, pd.Timestamp(now)):
        return {'status': 'outside_recording_window_no_backdated_forecast', 'frozen_predictions': 0}
    ledger = predictions.copy()
    ledger['origin_close'] = ledger.close
    ledger['horizon_sessions'], ledger['cost_assumption'] = 5, .003
    ledger['validation_base_rate'] = ledger.recent_prior
    ledger['recorded_at'], ledger['model_trained_at'] = now.isoformat(), metadata['trained_at']
    ledger['model_dataset_sha256'] = metadata['dataset_sha256']
    ledger['prediction_id'] = [hashlib.sha256('|'.join([code, str(origin.date()), metadata['dataset_sha256'], metadata['trained_at']]).encode()).hexdigest()[:20] for code in ledger.stock_code]
    key = hashlib.sha256((metadata['dataset_sha256']+metadata['trained_at']).encode()).hexdigest()[:16]
    output = Path(output_dir)/f'ml_memory_forward_{origin:%Y%m%d}_{key}.csv'
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open('x', encoding='utf-8-sig') as handle:
        ledger.to_csv(handle, index=False)
    return {'status': 'awaiting_future_outcomes', 'frozen_predictions': len(ledger), 'ledger': str(output)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['train', 'predict', 'freeze'])
    parser.add_argument('--protocol', type=Path, default=ROOT/'docs/model_experiments/adaptive_memory_protocol_20261021.json')
    parser.add_argument('--data-root', type=Path)
    parser.add_argument('--model-dir', type=Path, default=ROOT/'data/models/price_memory_router')
    parser.add_argument('--stock')
    parser.add_argument('--output-dir', type=Path, default=ROOT/'data/predictions')
    parser.add_argument('--report-path', type=Path, default=ROOT/'reports/daily_review/2026-10-21_adaptive_memory.md')
    args = parser.parse_args()
    try:
        if args.command == 'train':
            protocol = json.loads(args.protocol.read_text())
            run_training(args.data_root or ROOT/protocol['data_root'], args.model_dir, protocol, args.report_path)
        elif args.command == 'predict':
            if not args.stock:
                raise ValueError('predict requires --stock')
            print(json_text(query(args.model_dir, args.stock)))
        else:
            print(json_text(freeze(args.model_dir, args.output_dir)))
    except FileExistsError:
        parser.exit(2, 'Original memory-router ledger exists; preserved without overwrite.\n')
    except (ValueError, FileNotFoundError) as error:
        parser.exit(2, str(error)+'\n')
    except Exception as error:
        parser.exit(2, 'Adaptive-memory research failed: '+type(error).__name__+'\n')


if __name__ == '__main__':
    main()
