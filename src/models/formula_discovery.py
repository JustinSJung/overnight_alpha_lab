"""Bounded genetic signal synthesis with training-only survival; research only."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
from importlib.metadata import version
import json
from pathlib import Path
import uuid

import joblib
import numpy as np
import pandas as pd
from scipy.stats import spearmanr
from sklearn.linear_model import LogisticRegression, Ridge
from sklearn.model_selection import TimeSeriesSplit
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from threadpoolctl import threadpool_limits

from src.crawler.market_clock import KST, completed_price_cutoff
from src.evaluator.forward_price_forecast import valid_record_time
from src.features.completed_price_dataset import HISTORY_FEATURE_VERSION
from src.features.price_learning_dataset import load_snapshots
from src.models.distributional_selector import complete_cohort, four_partitions, selection_metrics
from src.models.monthly_price_walkforward import paired_interval
from src.models.price_forecaster import date_weights, fit_estimator, json_text, resolve_stock
from src.models.relative_price_selection import block_interval, daily_portfolio, probability_metrics, random_portfolios, rank_candidates
from src.models.selected_price_model import COLUMNS, ROOT, factories, partition_info, prepare_selected_features, to_logits, write_json

RANKS = ['rank__' + column for column in COLUMNS]
BASE = COLUMNS + RANKS


def require_runtime():
    if version('gplearn') != '0.4.3' or version('scikit-learn') != '1.8.0':
        raise ValueError('Use the pinned isolated .venv-discovery runtime, not the original model runtime.')


def rank_inputs(raw, as_of):
    cutoff = pd.Timestamp(as_of)
    inputs = prepare_selected_features(raw[raw.signal_date.le(cutoff) & raw.snapshot_date.le(cutoff)].copy(), COLUMNS)
    eligible = inputs[np.isfinite(inputs[COLUMNS]).all(axis=1) & inputs.volume_ratio_20d.gt(0) & inputs.close.gt(0)].copy()
    if eligible.duplicated(['stock_code', 'signal_date']).any():
        raise ValueError('Duplicate stock/date input ranks.')
    # Same-close eligible inputs define ranks BEFORE outcome availability is consulted.
    eligible[RANKS] = (eligible.groupby('signal_date')[COLUMNS].rank(method='average', pct=True) * 2 - 1).to_numpy()
    return eligible


def discovery_dataset(raw, protocol):
    inputs = rank_inputs(raw, protocol['labels_as_of'])
    dataset, coverage, _ = complete_cohort(raw, protocol['labels_as_of'], protocol['minimum_stocks_per_date'])
    dataset = dataset.merge(inputs[['stock_code', 'signal_date'] + RANKS], on=['stock_code', 'signal_date'], validate='one_to_one')
    if len(dataset) != int(coverage.loc[coverage.included, 'resolved'].sum()):
        raise ValueError('Input ranks and resolved cohort do not match.')
    dataset['label_available_date'] = dataset.groupby('signal_date').label_available_date.transform('max')
    return dataset, coverage


def discovery_sample(frame, limit, seed):
    if limit < 1:
        raise ValueError('Positive per-date discovery sample required.')
    rows = []
    for day, part in frame.groupby('signal_date', sort=True):
        part = part.sort_values('stock_code')
        rng = np.random.default_rng(np.random.SeedSequence([seed, int(pd.Timestamp(day).strftime('%Y%m%d'))]))
        rows.append(part.iloc[rng.permutation(len(part))[:limit]])
    return pd.concat(rows).sort_values(['signal_date', 'stock_code']).reset_index(drop=True)


def prefix_and_survival(train, boundary):
    boundary = pd.Timestamp(boundary)
    prefix = train[train.signal_date.lt(boundary) & train.label_available_date.lt(boundary)].copy()
    survival = train[train.signal_date.ge(boundary)].copy()
    if prefix.signal_date.nunique() < 15 or survival.signal_date.nunique() < 6:
        raise ValueError('Insufficient mature prefix or later training-only survival dates.')
    return prefix, survival


def fit_fingerprint(train, calibration, policy_calibration):
    frames = [part.assign(partition=name) for name, part in
              [('train', train), ('probability_calibration', calibration), ('policy_calibration', policy_calibration)]]
    values = pd.concat(frames).sort_values(['partition', 'signal_date', 'stock_code'])
    columns = ['partition', 'stock_code', 'signal_date', 'label_available_date', 'target', 'target_return'] + BASE
    return hashlib.sha256(pd.util.hash_pandas_object(values[columns], index=False).to_numpy().tobytes()).hexdigest()


def target_rank(frame):
    clipped = frame.target_return.clip(-.2, .2)
    return clipped.groupby(frame.signal_date).rank(method='average', pct=True).to_numpy() - .5


def crossfit_residuals(prefix, protocol):
    prefix = prefix.copy()
    prefix['relative_answer'] = target_rank(prefix)
    days = np.array(sorted(prefix.signal_date.unique()))
    rows, audits = [], []
    for fit_days, validation_days in TimeSeriesSplit(n_splits=protocol['residual_folds']).split(days):
        start = pd.Timestamp(days[validation_days[0]])
        fitting = prefix[prefix.signal_date.isin(days[fit_days]) & prefix.label_available_date.lt(start)]
        validation = prefix[prefix.signal_date.isin(days[validation_days])].copy()
        if fitting.signal_date.nunique() < protocol['residual_min_train_dates'] or validation.empty:
            raise ValueError('Insufficient purged residual-discovery fold history.')
        reference = make_pipeline(StandardScaler(), Ridge(alpha=protocol['residual_ridge_alpha']))
        fit_estimator(reference, fitting[BASE], fitting.relative_answer, date_weights(fitting))
        validation['gp_target'] = validation.relative_answer.to_numpy() - reference.predict(validation[BASE])
        rows.append(validation)
        audits.append({'train': partition_info(fitting), 'out_of_fold': partition_info(validation)})
    reference = make_pipeline(StandardScaler(), Ridge(alpha=protocol['residual_ridge_alpha']))
    fit_estimator(reference, prefix[BASE], prefix.relative_answer, date_weights(prefix))
    return pd.concat(rows).sort_values(['signal_date', 'stock_code']).reset_index(drop=True), reference, audits


def nonlinear_fractions(inputs, generated):
    inputs, generated = np.asarray(inputs), np.asarray(generated)
    design = np.column_stack([np.ones(len(inputs)), inputs])
    coefficients = np.linalg.lstsq(design, generated, rcond=None)[0]
    residual = generated - design @ coefficients
    denominator = np.std(generated, axis=0)
    return np.divide(np.std(residual, axis=0), denominator, out=np.zeros_like(denominator), where=denominator > 1e-10)


def correlation(left, right):
    left, right = np.asarray(left), np.asarray(right)
    if not np.isfinite(left).all() or not np.isfinite(right).all() or np.std(left) < 1e-10 or np.std(right) < 1e-10:
        return None
    return float(np.corrcoef(left, right)[0, 1])


def formula_values(generator, frame, clip):
    values = np.asarray(generator.transform(frame[RANKS].to_numpy()), dtype=float)
    if values.ndim != 2 or not np.isfinite(values).all():
        raise ValueError('Generated formula produced invalid values.')
    return np.clip(values, -clip, clip)


def evolve_formulas(train, protocol):
    from gplearn.genetic import SymbolicTransformer
    prefix, survival = prefix_and_survival(train, protocol['formula_validation_start'])
    residual_mode = protocol.get('discovery_mode') == 'crossfit_residual'
    if residual_mode:
        search_prefix, residual_reference, residual_audits = crossfit_residuals(prefix, protocol)
        survival = survival.copy()
        survival['gp_target'] = target_rank(survival) - residual_reference.predict(survival[BASE])
    else:
        search_prefix = prefix.assign(gp_target=target_rank(prefix))
        residual_reference, residual_audits = None, []
        survival = survival.assign(gp_target=survival.target_return)
    sample = discovery_sample(search_prefix, protocol['formula_sample_per_date'], protocol['formula_seed'])
    generator = SymbolicTransformer(population_size=protocol['formula_population'], generations=protocol['formula_generations'],
                                    hall_of_fame=protocol['formula_hall_of_fame'], n_components=protocol['formula_candidates'],
                                    tournament_size=10, init_depth=(2, 4), function_set=tuple(protocol['formula_functions']),
                                    parsimony_coefficient=protocol['formula_parsimony'], p_crossover=.75,
                                    p_subtree_mutation=.1, p_hoist_mutation=.05, p_point_mutation=.05,
                                    metric='pearson', max_samples=1., feature_names=RANKS, n_jobs=2,
                                    verbose=1, low_memory=True, random_state=protocol['formula_seed'])
    print('Evolving formulas on prefix-only sample: ' + str(len(sample)), flush=True)
    generator.fit(sample[RANKS].to_numpy(), sample.gp_target.to_numpy(), sample_weight=date_weights(sample))
    sampled = formula_values(generator, sample, protocol['formula_output_clip'])
    later = formula_values(generator, survival, protocol['formula_output_clip'])
    fractions = nonlinear_fractions(sample[BASE], sampled)
    blocks = np.array_split(np.array(sorted(survival.signal_date.unique())), 3)
    selected, signs, audits = [], [], []
    for number, program in enumerate(generator._best_programs):
        prefix_corr = correlation(sampled[:, number], sample.gp_target.to_numpy())
        sign = 1 if prefix_corr is None or prefix_corr >= 0 else -1
        redundant = max(abs(correlation(sampled[:, number], sample[column]) or 0) for column in RANKS)
        block_ics, block_counts = [], []
        for days in blocks:
            values = []
            for day in days:
                mask = survival.signal_date.eq(pd.Timestamp(day)).to_numpy()
                gene = later[mask, number] * sign
                answer = survival.loc[mask, 'gp_target'].to_numpy()
                if np.std(gene) > 1e-10 and np.std(answer) > 1e-10:
                    ic = float(spearmanr(gene, answer).statistic)
                    if np.isfinite(ic):
                        values.append(ic)
            block_ics.append(float(np.mean(values)) if values else None)
            block_counts.append(len(values))
        finite = [value for value in block_ics if value is not None]
        keep = (protocol['formula_min_nodes'] <= program.length_ <= protocol['formula_max_nodes']
                and prefix_corr is not None and redundant < protocol['formula_identity_correlation_ceiling']
                and (not residual_mode or fractions[number] >= protocol['formula_min_nonlinear_fraction'])
                and min(block_counts) >= protocol['formula_min_ic_dates_per_block']
                and len(finite) == 3 and np.mean(finite) >= protocol['formula_min_mean_daily_ic']
                and sum(value > 0 for value in finite) >= protocol['formula_min_positive_blocks'])
        audits.append({'formula_index': number, 'expression': str(program), 'nodes': program.length_,
                       'orientation_from_prefix': sign, 'prefix_correlation': prefix_corr,
                       'max_identity_correlation': redundant, 'survival_block_daily_ic': block_ics,
                       'nonlinear_residual_fraction': float(fractions[number]),
                       'survival_block_ic_dates': block_counts, 'retained': bool(keep)})
        if keep:
            selected.append(number)
            signs.append(sign)
    return {'generator': generator, 'selected': selected, 'signs': signs, 'formula_audit': audits,
            'sample': partition_info(sample), 'prefix': partition_info(prefix), 'survival': partition_info(survival),
            'residual_reference': residual_reference, 'residual_folds': residual_audits,
            'mode': protocol.get('discovery_mode', 'raw_rank')}


def feature_matrix(discovery, frame, with_formulas):
    output = frame[BASE].reset_index(drop=True).copy()
    if with_formulas and discovery['selected']:
        values = formula_values(discovery['generator'], frame, discovery['clip'])
        for number, sign in zip(discovery['selected'], discovery['signs'], strict=True):
            output['gene_' + str(number)] = values[:, number] * sign
    return output


def fit_heads(train, calibration, discovery):
    models, calibrators = {}, {}
    with threadpool_limits(limits=2):
        for role in ['rank_control', 'formula_augmented', 'tree_control']:
            print('Fitting discovered-signal head: ' + role, flush=True)
            model = factories()['extra_trees' if role == 'tree_control' else 'linear']
            train_x = train[COLUMNS] if role == 'tree_control' else feature_matrix(discovery, train, role == 'formula_augmented')
            cal_x = calibration[COLUMNS] if role == 'tree_control' else feature_matrix(discovery, calibration, role == 'formula_augmented')
            models[role] = fit_estimator(model, train_x, train.target, date_weights(train))
            calibrator = LogisticRegression(C=1., solver='liblinear', max_iter=1000, random_state=42)
            calibrator.fit(to_logits(model.predict_proba(cal_x)[:, 1]), calibration.target, sample_weight=date_weights(calibration))
            calibrators[role] = calibrator
    return {'models': models, 'calibrators': calibrators, 'discovery': discovery,
            'baseline_probability': float(np.average(calibration.target, weights=date_weights(calibration)))}


def predict_frame(bundle, frame):
    frame = frame.reset_index(drop=True).copy()
    with threadpool_limits(limits=2):
        for role, model in bundle['models'].items():
            features = frame[COLUMNS] if role == 'tree_control' else feature_matrix(bundle['discovery'], frame, role == 'formula_augmented')
            p = bundle['calibrators'][role].predict_proba(to_logits(model.predict_proba(features)[:, 1]))[:, 1]
            if not np.isfinite(p).all() or np.any((p < 0) | (p > 1)):
                raise ValueError('Invalid discovered-model probabilities.')
            frame[role] = p
    frame['probability_above_cost'] = frame.formula_augmented
    frame['recommendation'] = 'ABSTAIN'
    return frame


def policy_mask(frame, threshold, protocol):
    result = pd.Series(False, index=frame.index)
    if threshold is not None:
        top = rank_candidates(frame[frame.formula_augmented.ge(threshold)], 'formula_augmented', protocol['policy_daily_cap'])
        result.loc[top.index] = True
    return result


def choose_policy(frame, protocol):
    trials = []
    for threshold in protocol['policy_thresholds']:
        metrics = selection_metrics(frame, policy_mask(frame, threshold, protocol), protocol,
                                    .05 / (2 * len(protocol['policy_thresholds'])))
        passed = (metrics['cases'] >= protocol['policy_min_cases'] and metrics['dates'] >= protocol['policy_min_dates']
                  and metrics['date_success_rate'] is not None and metrics['date_success_rate'] >= protocol['policy_min_date_success']
                  and metrics['date_success_lower'] is not None and metrics['date_success_lower'] >= protocol['policy_min_success_lower']
                  and metrics['all_date_net_lower'] is not None and metrics['all_date_net_lower'] > 0)
        trials.append({'threshold': threshold, 'metrics': metrics, 'passed': bool(passed)})
    passing = [row for row in trials if row['passed']]
    return (max(passing, key=lambda row: (row['metrics']['all_date_net_lower'], row['threshold']))['threshold'] if passing else None), trials


def evaluate(bundle, frame, protocol):
    scored = predict_frame(bundle, frame)
    scored['selected_by_research_policy'] = policy_mask(scored, bundle['policy'], protocol)
    probabilities = {role: probability_metrics(scored, scored[role].to_numpy(), 'target', bundle['baseline_probability'])
                     for role in bundle['models']}
    paired = {}
    for role in ['rank_control', 'tree_control']:
        reference = scored.copy()
        reference['probability_above_cost'] = reference[role]
        paired[role] = paired_interval(reference, scored)
    pool = scored.groupby('signal_date').target_return.mean()
    portfolios = {role: daily_portfolio(rank_candidates(scored, role, protocol['primary_top_k']), pool)
                  for role in ['formula_augmented', 'rank_control', 'tree_control', 'return_20d']}
    random, _ = random_portfolios(scored, [protocol['primary_top_k']], protocol['random_replicates'])
    portfolios['random_mean'] = random[protocol['primary_top_k']]
    return_deltas = {role: block_interval((portfolios['formula_augmented'].mean_return - daily.mean_return).to_numpy(),
                                         protocol['bootstrap_samples'], protocol['bootstrap_block_sessions'], .05 / 4, protocol['bootstrap_seed'])
                     for role, daily in portfolios.items() if role != 'formula_augmented'}
    return scored, {'probabilities': probabilities, 'paired_brier': paired,
                     'policy': selection_metrics(scored, scored.selected_by_research_policy, protocol),
                     'top20': {role: {column: float(daily[column].mean()) for column in ['absolute_success_rate', 'net_return_proxy', 'excess_vs_pool']}
                               for role, daily in portfolios.items()}, 'paired_top20_returns': return_deltas}


def render(summary):
    lines = ['# AI Formula Discovery Research', '',
             'RESEARCH_ONLY. Genetic programming synthesizes formula candidates; novelty or high-reliability completion is NOT claimed.',
             'Library: gplearn 0.4.3. Separate scikit-learn 1.8.0 runtime; original model runtime unchanged.',
             'Within-date ranks are computed from eligible INPUTS before outcomes. Formula orientation is prefix-only. Survival uses three later TRAIN-only blocks.',
             'Discovery mode: ' + summary['discovery_mode'],
             'Residual mode evolves against purged out-of-fold residuals and rejects linear-span copies; survival IC then concerns residuals, not raw returns.',
             'No eval/exec or externally supplied Python programs; only fixed library arithmetic primitives.', '',
             '## Discovery Audit', '',
             'Retained formula count: ' + str(summary['retained_formulas']),
             'Discovery/survival: ' + str(summary['discovery_partitions']), '',
             '| Candidate | Nodes | Prefix correlation | Nonlinear fraction | Later training block ICs | Retained | Formula |', '|---:|---:|---:|---:|---|---|---|']
    for row in summary['formula_audit']:
        lines.append(f"| {row['formula_index']} | {row['nodes']} | {row['prefix_correlation']} | {row['nonlinear_residual_fraction']} | {row['survival_block_daily_ic']} | {row['retained']} | `{row['expression']}` |")
    lines += ['', '## Same-Cohort External Historical Diagnostics', '', json_text(summary['results']), '',
              'Fixed Top20 tables are diagnostics, NOT recommended stocks. Cost is a 0.3% proxy; overlapping close-to-close returns are not executable/compounded strategy returns.',
              'Sampled prefix rows are only an evolution compute budget, not a reduced live candidate pool. No final candidate generation is changed.',
              'Calibration policy trials: ' + json_text(summary['policy_trials']),
              'Selected policy threshold: ' + str(summary['policy']),
              'Screen reasons: ' + ', '.join(summary['screen_reasons']),
              'Recommendation gate: False. Historical dates were repeatedly inspected; future validation remains required.',
              'Coverage: ' + str(summary['coverage']),
              'Partitions: ' + str(summary['partitions']),
              'Current-universe, retrospectively adjusted prices and complete-date selection limitations remain.',
              'Protocol SHA256: ' + summary['protocol_sha256'], 'Ignored run: ' + summary['run_dir'], '']
    return '\n'.join(lines)


def run_training(data_root, output_root, protocol, report_path):
    require_runtime()
    if (protocol['horizon_sessions'] != 5 or protocol['cost_assumption'] != .003
            or protocol['production_promotion'] is not False or protocol['candidate_pool_change'] is not False
            or protocol['test_search'] is not False or protocol['world_first_or_guarantee_claim'] is not False
            or not 1 <= protocol['formula_population'] <= 256 or not 1 <= protocol['formula_generations'] <= 10
            or not 1 <= protocol['formula_candidates'] <= protocol['formula_hall_of_fame'] <= protocol['formula_population']
            or not 1 <= protocol['formula_sample_per_date'] <= 128):
        raise ValueError('Unsupported discovery protocol.')
    raw, source = load_snapshots(data_root)
    if (raw.attrs.get('feature_version') != HISTORY_FEATURE_VERSION or source.get('skipped_files')
            or raw.attrs.get('history_provenance', {}).get('failed_stocks', 0)):
        raise ValueError('Complete verified OHLCV input required.')
    dataset, coverage = discovery_dataset(raw, protocol)
    train, cal, policy_cal, test = four_partitions(dataset, protocol)
    parts = {name: test[test.signal_date.between(pd.Timestamp(start), pd.Timestamp(end))]
             for name, (start, end) in protocol['periods'].items()}
    if parts[protocol['primary_period']].empty:
        raise ValueError('No complete outcomes in required primary period.')
    root = Path(output_root)
    run_dir = root/'runs'/(datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'_'+uuid.uuid4().hex[:8])
    run_dir.mkdir(parents=True, exist_ok=False)
    discovery = evolve_formulas(train, protocol)
    discovery['clip'] = protocol['formula_output_clip']
    bundle = fit_heads(train, cal, discovery)
    bundle['policy'], trials = choose_policy(predict_frame(bundle, policy_cal), protocol)
    bundle['protocol'] = protocol
    partitions = {name: partition_info(part) for name, part in [('train', train), ('probability_calibration', cal), ('policy_calibration', policy_cal)]}
    paths = [Path(__file__), ROOT/'src/models/distributional_selector.py', ROOT/'src/models/selected_price_model.py',
             ROOT/'src/models/relative_price_selection.py', ROOT/'src/models/monthly_price_walkforward.py',
             ROOT/'src/models/price_forecaster.py', ROOT/'src/features/ohlcv_information.py',
             ROOT/'src/features/price_learning_dataset.py', ROOT/'src/features/completed_price_dataset.py']
    implementation = {str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest() for path in paths}
    protocol_hash = hashlib.sha256(json_text(protocol).encode()).hexdigest()
    fit_as_of = pd.Timestamp(raw.loc[raw.signal_date.lt(pd.Timestamp(protocol['evaluation_start'])), 'signal_date'].max())
    bundle['metadata'] = {'schema': 'research_formula_discovery_v1', 'features': BASE,
                          'trained_at': datetime.now(timezone.utc).isoformat(), 'as_of': str(fit_as_of.date()),
                          'data_root': str(Path(data_root).resolve()), 'partitions': partitions,
                          'dataset_sha256': fit_fingerprint(train, cal, policy_cal),
                          'implementation_sha256': implementation, 'protocol_sha256': protocol_hash,
                          'runtime': {'gplearn': version('gplearn'), 'scikit-learn': version('scikit-learn')},
                          'recommendation_gate_passed': False}
    joblib.dump(bundle, run_dir/'model.joblib', compress=3)
    write_json(bundle['metadata'], run_dir/'model_metadata.json')
    results, period_coverage = {}, {}
    for period, (start, end) in protocol['periods'].items():
        part = parts[period]
        selected = coverage[coverage.index.to_series().between(pd.Timestamp(start), pd.Timestamp(end)).to_numpy()]
        period_coverage[period] = {'eligible_dates': len(selected), 'complete_dates': int(selected.included.sum()), 'evaluated_rows': len(part)}
        if part.empty:
            results[period] = {'status': 'unavailable_no_complete_outcome_dates'}
            continue
        predictions, metrics = evaluate(bundle, part, protocol)
        predictions.to_csv(run_dir/(period+'.csv'), index=False)
        results[period] = {'status': 'historical_development_only', **metrics}
    main = results[protocol['primary_period']]
    reasons = []
    if not discovery['selected']:
        reasons.append('no_nontrivial_stable_formula_survived')
    if bundle['policy'] is None:
        reasons.append('no_high_reliability_policy_passed_policy_calibration')
    if main['policy']['cases'] < 100 or main['policy']['dates'] < 20:
        reasons.append('insufficient_external_policy_evidence')
    if main['policy']['date_success_lower'] is None or main['policy']['date_success_lower'] < .6:
        reasons.append('external_60_percent_success_lower_not_established')
    if main['policy']['all_date_net_lower'] is None or main['policy']['all_date_net_lower'] <= 0:
        reasons.append('external_positive_net_proxy_not_established')
    if any(row['upper_95'] is None or row['upper_95'] >= 0 for row in main['paired_brier'].values()):
        reasons.append('probability_advantage_over_both_controls_not_established')
    if any(row['lower'] is None or row['lower'] <= 0 for row in main['paired_top20_returns'].values()):
        reasons.append('top20_advantage_over_all_references_not_established')
    summary = {'retained_formulas': len(discovery['selected']), 'formula_audit': discovery['formula_audit'],
               'discovery_partitions': {key: discovery[key] for key in ['sample', 'prefix', 'survival']},
               'discovery_mode': discovery['mode'], 'residual_folds': discovery['residual_folds'],
               'partitions': partitions, 'policy': bundle['policy'], 'policy_trials': trials,
               'results': results, 'coverage': period_coverage, 'screen_reasons': reasons,
               'development_screen_passed': not reasons, 'recommendation_gate_passed': False,
               'implementation_sha256': implementation, 'protocol_sha256': protocol_hash, 'protocol': protocol, 'run_dir': str(run_dir)}
    report_path = Path(report_path)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(render(summary), encoding='utf-8')
    write_json(summary, report_path.with_suffix('.json'))
    write_json({'run_id': run_dir.name}, root/'latest.json')
    print(json_text({key: summary[key] for key in ['retained_formulas', 'policy', 'screen_reasons', 'run_dir']}), flush=True)
    return summary


def load_research(model_dir, now):
    require_runtime()
    root = Path(model_dir)
    run = json.loads((root/'latest.json').read_text())['run_id']
    if not run or run in {'.', '..'} or Path(run).name != run:
        raise ValueError('Invalid discovery run identifier.')
    bundle = joblib.load(root/'runs'/run/'model.joblib')
    meta = bundle['metadata']
    if (meta.get('schema') != 'research_formula_discovery_v1' or meta.get('features') != BASE
            or meta.get('recommendation_gate_passed') is not False or pd.Timestamp(meta['trained_at']) > pd.Timestamp(now)
            or pd.Timestamp(meta['as_of']).date() > now.date()):
        raise ValueError('Only already-trained research discovery bundles are supported.')
    return bundle


def current_inputs(bundle, data_root, now):
    raw, source = load_snapshots(data_root or bundle['metadata']['data_root'])
    if (raw.attrs.get('feature_version') != HISTORY_FEATURE_VERSION or source.get('skipped_files')
            or raw.attrs.get('history_provenance', {}).get('failed_stocks', 0)):
        raise ValueError('Verified complete OHLCV history required.')
    return rank_inputs(raw, completed_price_cutoff(now))


def query(model_dir, data_root, stock, now=None):
    now = now or datetime.now(KST)
    if now.tzinfo is None:
        raise ValueError('Timezone-aware query required.')
    now = now.astimezone(KST)
    bundle = load_research(model_dir, now)
    inputs = current_inputs(bundle, data_root, now)
    code = resolve_stock(stock, [ROOT, Path(data_root or bundle['metadata']['data_root'])])
    row = inputs[inputs.stock_code.eq(code)].sort_values('signal_date').tail(1)
    if row.empty:
        raise ValueError('No eligible completed prices for stock.')
    prediction = predict_frame(bundle, row).iloc[0]
    return {'stock_code': code, 'signal_date': str(pd.Timestamp(prediction.signal_date).date()),
            'probability_above_cost': float(prediction.probability_above_cost),
            'rank_control_probability': float(prediction.rank_control), 'tree_control_probability': float(prediction.tree_control),
            'synthesized_signal_count': len(bundle['discovery']['selected']), 'policy_available': bundle['policy'] is not None,
            'recommendation': 'ABSTAIN', 'status': 'STALE_DATA' if (now.date()-pd.Timestamp(prediction.signal_date).date()).days > 7 else 'RESEARCH_ONLY',
            'note': 'Synthesized formulas and probabilities are research candidates, NOT validated confidence or novel scientific discoveries.'}


def freeze(model_dir, data_root, output_dir, now=None):
    now = now or datetime.now(KST)
    if now.tzinfo is None:
        raise ValueError('Timezone-aware recording required.')
    now = now.astimezone(KST)
    bundle = load_research(model_dir, now)
    inputs = current_inputs(bundle, data_root, now)
    origin = inputs.signal_date.max()
    if pd.Timestamp(bundle['metadata']['as_of']) >= origin:
        raise ValueError('Signal must follow the model fit as-of date.')
    if not valid_record_time(origin, pd.Timestamp(now)):
        return {'status': 'outside_recording_window_no_backdated_forecast', 'frozen_predictions': 0}
    latest = inputs[inputs.signal_date.eq(origin)].copy().reset_index(drop=True)
    if latest.empty:
        raise ValueError('No eligible timely observations.')
    predictions = predict_frame(bundle, latest)
    ledger = predictions[['stock_code', 'signal_date', 'probability_above_cost', 'rank_control', 'tree_control', 'recommendation']].copy()
    meta = bundle['metadata']
    ledger['origin_close'] = latest.close.to_numpy()
    ledger['recorded_at'], ledger['model_trained_at'] = now.isoformat(), meta['trained_at']
    ledger['model_dataset_sha256'] = meta['dataset_sha256']
    ledger['horizon_sessions'], ledger['cost_assumption'] = 5, .003
    ledger['validation_base_rate'] = bundle['baseline_probability']
    ledger['selected_by_research_policy'] = policy_mask(predictions, bundle['policy'], bundle['protocol'])
    ledger['prediction_id'] = [hashlib.sha256('|'.join([code, str(origin.date()), meta['dataset_sha256'], meta['trained_at']]).encode()).hexdigest()[:20] for code in ledger.stock_code]
    key = hashlib.sha256((meta['dataset_sha256']+meta['trained_at']).encode()).hexdigest()[:16]
    output = Path(output_dir)/f'ml_discovery_forward_{origin:%Y%m%d}_{key}.csv'
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open('x', encoding='utf-8-sig') as handle:
        ledger.to_csv(handle, index=False)
    return {'status': 'awaiting_future_outcomes', 'frozen_predictions': len(ledger), 'ledger': str(output)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['train', 'predict', 'freeze'])
    parser.add_argument('--protocol', type=Path, default=ROOT/'docs/model_experiments/formula_residual_discovery_protocol_20261021.json')
    parser.add_argument('--data-root', type=Path)
    parser.add_argument('--model-dir', type=Path, default=ROOT/'data/models/price_formula_residual_discovery')
    parser.add_argument('--stock')
    parser.add_argument('--output-dir', type=Path, default=ROOT/'data/predictions')
    parser.add_argument('--report-path', type=Path, default=ROOT/'reports/daily_review/2026-10-21_formula_residual_discovery.md')
    args = parser.parse_args()
    try:
        if args.command == 'train':
            protocol = json.loads(args.protocol.read_text())
            run_training(args.data_root or ROOT/protocol['data_root'], args.model_dir, protocol, args.report_path)
        elif args.command == 'predict':
            if not args.stock:
                raise ValueError('predict requires --stock')
            print(json_text(query(args.model_dir, args.data_root, args.stock)))
        else:
            print(json_text(freeze(args.model_dir, args.data_root, args.output_dir)))
    except FileExistsError:
        parser.exit(2, 'Original discovery ledger already exists; preserved without overwrite.\n')
    except (ValueError, FileNotFoundError) as error:
        parser.exit(2, str(error)+'\n')
    except Exception as error:
        parser.exit(2, 'Formula discovery failed: '+type(error).__name__+'\n')


if __name__ == '__main__':
    main()
