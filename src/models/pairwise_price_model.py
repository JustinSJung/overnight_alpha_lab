"""Controlled within-day ranking on the unchanged next-open BUY outcome."""
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
from scipy.optimize import minimize
from scipy.special import expit

from src.crawler.market_clock import KST, completed_price_cutoff
from src.evaluator.forward_price_forecast import valid_record_time
from src.evaluator.research_shadow_ledger import grade_shadow, seal_ledger
from src.features.next_open_dataset import TARGET_VERSION, build_next_open_dataset
from src.models.monthly_price_walkforward import monthly_split
from src.models.next_open_price_model import load_inputs, selection_summary
from src.models.price_forecaster import date_weights, json_text, resolve_stock
from src.models.relative_price_selection import rank_candidates
from src.models.selected_price_model import COLUMNS, ROOT, partition_info, write_json
from src.models.selective_price_model import paired_success

ARMS = ['pointwise_raw', 'pointwise_cross_section', 'pairwise_cross_section']
PRIMARY = ARMS[-1]
RANK_COLUMNS = ['cross_' + name for name in COLUMNS]
CONTEXT = ['context_return_1d', 'context_return_5d', 'context_return_20d', 'context_up_fraction']


def validate_protocol(p):
    fixed = dict(experiment='next_open_pairwise_rank_v1', algorithm='catboost_fixed_pairlogit_and_logloss',
                 catboost_version='1.2.8', horizon_sessions=5, cost_assumption=.003,
                 daily_cap=5, probability_threshold=.6, primary_comparisons=2,
                 primary_arm=PRIMARY, production_promotion=False, candidate_pool_change=False)
    if any(p.get(k) != v for k, v in fixed.items()):
        raise ValueError('Unsupported fixed pairwise protocol.')
    if (p['training_sessions'] < 15 or p['calibration_sessions'] < 3 or p['iterations'] < 2
            or p['depth'] < 1 or p['pairs_per_date'] < 1 or p['calibration_l2'] <= 0
            or p['bootstrap_samples'] < 100 or p['bootstrap_block_sessions'] < 5):
        raise ValueError('Invalid fixed compute or calibration budget.')


def cross_section_inputs(cohort):
    if cohort.empty or cohort.duplicated(['stock_code', 'signal_date']).any():
        raise ValueError('Unique input candidates required.')
    if not np.isfinite(cohort[COLUMNS]).all(axis=None):
        raise ValueError('Finite inputs required; outcomes cannot select the cohort.')
    frame = cohort.sort_values(['signal_date', 'stock_code']).reset_index(drop=True).copy()
    # Compute BEFORE removing unknown future answers: ranks cannot depend on labels.
    frame[RANK_COLUMNS] = (frame.groupby('signal_date')[COLUMNS].rank(method='average', pct=True).to_numpy() * 2 - 1)
    for days in [1, 5, 20]:
        frame[f'context_return_{days}d'] = frame.groupby('signal_date')[f'return_{days}d'].transform('mean')
    frame['context_up_fraction'] = frame.return_1d.gt(0).groupby(frame.signal_date).transform('mean')
    return frame


def training_pairs(train, budget, seed):
    train = train.sort_values(['signal_date', 'stock_code']).reset_index(drop=True)
    if train.target.isna().any() or not train.target.isin([0, 1]).all():
        raise ValueError('Only resolved binary BUY labels may form training pairs.')
    pairs, weights, dates = [], [], 0
    for day, indexes in train.groupby('signal_date', sort=True).groups.items():
        index = np.asarray(indexes)
        positive = index[train.loc[index, 'target'].to_numpy() == 1]
        negative = index[train.loc[index, 'target'].to_numpy() == 0]
        total = len(positive) * len(negative)
        if not total:
            continue
        rng = np.random.default_rng(np.random.SeedSequence([seed, int(day.strftime('%Y%m%d'))]))
        chosen = rng.choice(total, size=min(budget, total), replace=False)
        pairs.extend(np.column_stack([positive[chosen // len(negative)], negative[chosen % len(negative)]]).tolist())
        # Equal total objective weight per informative date, not per available pair.
        weights.extend([len(train) / train.signal_date.nunique() / len(chosen)] * len(chosen))
        dates += 1
    if not pairs:
        raise ValueError('No dates contain both outcome classes.')
    return train, np.asarray(pairs, dtype=int), np.asarray(weights), dates


def calibration_matrix(score, frame):
    return np.column_stack([np.asarray(score, dtype=float), frame[CONTEXT].to_numpy(dtype=float)])


def fit_monotone_calibration(score, frame, penalty):
    x = calibration_matrix(score, frame)
    if frame.target.isna().any() or frame.target.nunique() != 2 or not np.isfinite(x).all():
        raise ValueError('Calibration requires finite past inputs and both known outcomes.')
    weights = date_weights(frame)
    weights = weights / weights.sum()
    center = np.average(x, axis=0, weights=weights)
    scale = np.sqrt(np.average((x - center) ** 2, axis=0, weights=weights))
    scale = np.where(scale > 1e-8, scale, 1.)
    z = np.column_stack([(x - center) / scale, np.ones(len(x))])
    y = frame.target.to_numpy(dtype=float)
    prior = float(np.dot(weights, y))
    initial = np.r_[np.zeros(x.shape[1]), np.log(prior / (1 - prior))]

    def objective(beta):
        logits = z @ beta
        loss = np.dot(weights, np.logaddexp(0, logits) - y * logits) + penalty * np.dot(beta[:-1], beta[:-1]) / 2
        gradient = z.T @ (weights * (expit(logits) - y))
        gradient[:-1] += penalty * beta[:-1]
        return float(loss), gradient

    fit = minimize(objective, initial, jac=True, method='L-BFGS-B',
                   bounds=[(0, None)] + [(None, None)] * (len(initial) - 1), options={'maxiter': 500, 'ftol': 1e-11})
    if not fit.success or not np.isfinite(fit.x).all():
        raise ValueError('Monotone calibration failed; do not publish an arbitrary fallback.')
    return dict(center=center, scale=scale, coefficients=fit.x, prior=prior,
                own_score_slope=float(fit.x[0]), latest_label=frame.label_available_date.max())


def calibrated_probability(calibration, score, frame):
    if calibration['latest_label'] > frame.signal_date.min():
        raise ValueError('Calibration uses future answers.')
    x = calibration_matrix(score, frame)
    if not np.isfinite(x).all():
        raise ValueError('Invalid calibration inputs.')
    z = np.column_stack([(x - calibration['center']) / calibration['scale'], np.ones(len(x))])
    return expit(z @ calibration['coefficients'])


def fit_models(frame, as_of, p):
    from catboost import CatBoostClassifier, CatBoostRanker, Pool, __version__
    if __version__ != p['catboost_version']:
        raise ValueError('Use the pinned ranking environment.')
    train, calibration = monthly_split(frame[frame.target.notna()], as_of,
                                       p['training_sessions'], p['calibration_sessions'])
    train = train.sort_values(['signal_date', 'stock_code']).reset_index(drop=True)
    calibration = calibration.sort_values(['signal_date', 'stock_code']).reset_index(drop=True)
    parameters = dict(iterations=p['iterations'], depth=p['depth'], learning_rate=p['learning_rate'],
                      l2_leaf_reg=p['l2_leaf_reg'], random_seed=p['seed'], thread_count=p['threads'],
                      bootstrap_type='No', boosting_type='Plain', random_strength=0,
                      leaf_estimation_iterations=1, border_count=64, verbose=False, allow_writing_files=False)
    ordered, pairs, pair_weights, informative = training_pairs(train, p['pairs_per_date'], p['seed'])
    models, calibrators = {}, {}
    for name in ARMS:
        columns = COLUMNS if name == 'pointwise_raw' else RANK_COLUMNS
        print('Fitting fixed rank comparison: ' + name, flush=True)
        if name == PRIMARY:
            model = CatBoostRanker(loss_function='PairLogit', **parameters)
            pool = Pool(ordered[columns], label=ordered.target.astype(int),
                        group_id=pd.factorize(ordered.signal_date)[0], pairs=pairs, pairs_weight=pair_weights)
        else:
            model = CatBoostClassifier(loss_function='Logloss', **parameters)
            pool = Pool(train[columns], label=train.target.astype(int), weight=date_weights(train))
        model.fit(pool)
        score = (model.predict(calibration[columns]) if name == PRIMARY
                 else model.predict(calibration[columns], prediction_type='RawFormulaVal'))
        calibrators[name] = fit_monotone_calibration(score, calibration, p['calibration_l2'])
        models[name] = model
    return dict(models=models, calibrators=calibrators), dict(train=partition_info(train), calibration=partition_info(calibration),
                informative_pair_dates=informative, training_pairs=len(pairs), pair_weight_sum=float(pair_weights.sum()))


def predict_models(bundle, frame):
    result = frame.copy().reset_index(drop=True)
    for name in ARMS:
        columns = COLUMNS if name == 'pointwise_raw' else RANK_COLUMNS
        model = bundle['models'][name]
        score = (model.predict(result[columns]) if name == PRIMARY
                 else model.predict(result[columns], prediction_type='RawFormulaVal'))
        result['score_' + name] = score
        result['probability_' + name] = calibrated_probability(bundle['calibrators'][name], score, result)
    if not np.isfinite(result[['score_' + x for x in ARMS] + ['probability_' + x for x in ARMS]]).all(axis=None):
        raise ValueError('Invalid ranking outputs.')
    result['recommendation'] = 'ABSTAIN'
    return result


def selection_masks(frame, p):
    masks = {}
    for name in ARMS:
        masks['top5_' + name] = frame.index.isin(rank_candidates(frame, 'score_' + name, p['daily_cap']).index)
    chosen = rank_candidates(frame[frame['probability_' + PRIMARY].ge(p['probability_threshold'])],
                             'score_' + PRIMARY, p['daily_cap'])
    counts = chosen.groupby('signal_date').size()
    for name in ARMS:
        ordered = frame.sort_values(['signal_date', 'score_' + name, 'stock_code'], ascending=[True, False, True], kind='stable')
        rank = ordered.groupby('signal_date').cumcount() + 1
        selected = ordered.index[rank.le(ordered.signal_date.map(counts).fillna(0))]
        masks['matched_policy_' + name] = frame.index.isin(selected)
    return masks


def evaluate_rank(frame, p):
    frame = frame.reset_index(drop=True)
    masks = selection_masks(frame, p)
    observed = frame[frame.target.notna()]
    return dict(input_candidates=len(frame), evaluated_cases=len(observed), unresolved_cases=int(frame.target.isna().sum()),
                signal_dates=int(frame.signal_date.nunique()),
                date_brier={name: float(np.average((observed['probability_' + name] - observed.target) ** 2,
                                                       weights=date_weights(observed))) if len(observed) else None for name in ARMS},
                selections={name: selection_summary(frame, mask) for name, mask in masks.items()},
                primary_top5_comparisons={name: paired_success(frame, masks['top5_' + name], masks['top5_' + PRIMARY], p) for name in ARMS[:-1]})


def implementation_digest():
    digest = hashlib.sha256()
    for name in ['src/models/pairwise_price_model.py', 'src/models/next_open_price_model.py',
                 'src/models/selected_price_model.py', 'src/features/next_open_dataset.py',
                 'src/features/price_learning_dataset.py', 'src/features/completed_price_dataset.py',
                 'src/features/ohlcv_information.py', 'src/models/monthly_price_walkforward.py']:
        digest.update(name.encode())
        digest.update((ROOT / name).read_bytes())
    return digest.hexdigest()


def save_run(bundle, data_root, frame, as_of, p, output_root, audit, results=None):
    metadata = dict(schema='pairwise_price_v1', target_version=TARGET_VERSION, features=COLUMNS, protocol=p,
                    as_of=str(pd.Timestamp(as_of).date()), trained_at=datetime.now(timezone.utc).isoformat(),
                    data_root=str(Path(data_root).resolve()), recommendation_enabled=False,
                    baseline_probability=bundle['calibrators'][PRIMARY]['prior'], implementation_sha256=implementation_digest(),
                    source_manifest_sha256=hashlib.sha256((Path(data_root) / 'history_manifest.json').read_bytes()).hexdigest())
    metadata['dataset_sha256'] = hashlib.sha256(json_text(metadata | {'trained_at': None}).encode()).hexdigest()
    run = Path(output_root) / 'runs' / (datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '_' + uuid.uuid4().hex[:8])
    run.mkdir(parents=True, exist_ok=False)
    bundle['metadata'] = metadata
    joblib.dump(bundle, run / 'model.joblib', compress=3)
    write_json(metadata, run / 'model_metadata.json')
    checksums = {name: hashlib.sha256((run / name).read_bytes()).hexdigest() for name in ['model.joblib', 'model_metadata.json']}
    write_json(checksums, run / 'checksums.json')
    summary = dict(run_dir=str(run.resolve()), metadata=metadata, fit=audit, results=results,
                   calibration_slopes={name: bundle['calibrators'][name]['own_score_slope'] for name in ARMS},
                   recommendation_gate_passed=False, gate_reasons=['independent_prospective_goal_not_met'])
    write_json(summary, run / 'summary.json')
    write_json(dict(run_dir=str(run.resolve()), checksums_sha256=hashlib.sha256((run / 'checksums.json').read_bytes()).hexdigest()), Path(output_root) / 'latest.json')
    return summary


def render_report(summary):
    def percentage(value):
        return 'N/A' if value is None else f'{value:.2%}'
    lines = ['# Within-Day Pairwise Price Learning', '',
             'RESEARCH ONLY. Same next-open BUY labels and assumed 0.3% cost. No broad candidate-pool reduction or trading.',
             'Two matched pointwise controls distinguish feature normalization from the pairwise objective.',
             'Features are ranked inside each day BEFORE outcomes are filtered. Cross-sectional ranks are never probabilities.',
             'Date-specific training pairs have equal total weight across informative days; pairs are compute samples, not an inference-universe cap.',
             'All engines use the same fixed tree/iteration/seed budget. No early stopping, threshold search or result-selected winner.',
             'Shared calibration context is fitted only on separate past calibration rows, with a nonnegative own-score coefficient.', '',
             '| Period | Method | Input candidates | Top5 selected | Evaluated | Unknown | Conditional daily success | Conditional net proxy | Brier |',
             '|---|---|---:|---:|---:|---:|---:|---:|---:|']
    for period, metrics in (summary['results'] or {}).items():
        for name in ARMS:
            m = metrics['selections']['top5_' + name]
            lines.append(f"| {period} | {name} | {metrics['input_candidates']} | {m['selected_cases']} | {m['evaluated_cases']} | {m['unresolved_cases']} | {percentage(m['conditional_date_success_rate'])} | {percentage(m['conditional_mean_net_return_proxy'])} | {metrics['date_brier'][name]} |")
    lines += ['', 'Unknown selections are never replaced. Conditional results do not establish complete-policy returns.',
              'This repeatedly inspected historical development history cannot certify the agreed 60% reliability goal.', '',
              '## Fit and Calibration', '', '```json', json_text(summary['fit']), '```', '',
              'Own-score calibration slopes: ' + json_text(summary['calibration_slopes']), '',
              '## Complete Diagnostics', '', '```json', json_text(summary['results']), '```', '',
              'Two primary comparisons use family-adjusted five-session blocks. Any missing paired date prevents a full-period lower-bound claim.',
              'Current-universe survivorship, retrospective corporate-action adjustment and an observed-universe calendar remain limitations.',
              'Overlapping return proxies are not compounded portfolio results or guaranteed executable profits.',
              'Official implementation: https://catboost.ai/docs/en/concepts/loss-functions-ranking', '']
    return '\n'.join(lines)


def train(data_root, output_root, p, report, current=False):
    validate_protocol(p)
    inputs, _ = load_inputs(data_root, p['labels_as_of'] if not current else completed_price_cutoff())
    cutoff = inputs.signal_date.max() if current else pd.Timestamp(p['labels_as_of'])
    cohort, _ = build_next_open_dataset(inputs, cutoff)
    frame = cross_section_inputs(cohort)
    as_of = cutoff if current else pd.Timestamp(p['fit_as_of'])
    bundle, audit = fit_models(frame, as_of, p)
    results = None
    if not current:
        results = {}
        for name, (start, end) in p['periods'].items():
            part = frame[frame.signal_date.between(start, end)].copy()
            if part.empty or as_of >= part.signal_date.min():
                raise ValueError('Evaluation must be nonempty and after fitting.')
            results[name] = evaluate_rank(predict_models(bundle, part), p)
    summary = save_run(bundle, data_root, frame, as_of, p, output_root, audit, results)
    if report is not None:
        Path(report).parent.mkdir(parents=True, exist_ok=True)
        Path(report).write_text(render_report(summary), encoding='utf-8')
        write_json(summary, Path(report).with_suffix('.json'))
    return summary


def load_model(root):
    pointer = json.loads((Path(root) / 'latest.json').read_text())
    run = Path(pointer['run_dir'])
    if hashlib.sha256((run / 'checksums.json').read_bytes()).hexdigest() != pointer['checksums_sha256']:
        raise ValueError('Pairwise manifest changed.')
    for name, digest in json.loads((run / 'checksums.json').read_text()).items():
        if Path(name).name != name or hashlib.sha256((run / name).read_bytes()).hexdigest() != digest:
            raise ValueError('Pairwise artifact checksum mismatch.')
    bundle = joblib.load(run / 'model.joblib')
    m = bundle['metadata']
    if (m != json.loads((run / 'model_metadata.json').read_text()) or m['schema'] != 'pairwise_price_v1'
            or m['target_version'] != TARGET_VERSION or m['features'] != COLUMNS or m['recommendation_enabled'] is not False):
        raise ValueError('Unsupported pairwise artifact.')
    validate_protocol(m['protocol'])
    return bundle


def current_predictions(bundle, data_root, now=None):
    now = now or datetime.now(KST)
    m = bundle['metadata']
    if now.tzinfo is None or pd.Timestamp(m['trained_at']) > pd.Timestamp(now):
        raise ValueError('Use a current aware clock after fitting.')
    inputs, _ = load_inputs(data_root, completed_price_cutoff(now))
    cohort, _ = build_next_open_dataset(inputs, completed_price_cutoff(now))
    frame = cross_section_inputs(cohort[cohort.signal_date.eq(cohort.signal_date.max())])
    if frame.empty or pd.Timestamp(m['as_of']) > frame.signal_date.max():
        raise ValueError('Use nonfuture fitted labels and current completed inputs.')
    scored = predict_models(bundle, frame)
    columns = ['stock_code', 'signal_date', 'close'] + ['score_' + x for x in ARMS] + ['probability_' + x for x in ARMS]
    output = scored[columns].rename(columns={'close': 'origin_close'})
    for name, mask in selection_masks(scored, m['protocol']).items():
        output[name] = mask
    output['probability_above_cost'], output['recommendation'], output['status'] = output['probability_' + PRIMARY], 'ABSTAIN', 'RESEARCH_ONLY'
    return output


def freeze(bundle, data_root, output_dir, now=None):
    live = now is None
    now = now or datetime.now(KST)
    frame = current_predictions(bundle, data_root, now)
    if live:
        now = datetime.now(KST)
    origin = frame.signal_date.max()
    if not (valid_record_time(origin, pd.Timestamp(now))
            and valid_record_time(origin, pd.Timestamp(now) + pd.Timedelta(seconds=60))):
        raise ValueError('Outside recording window; never backdate pairwise forecasts.')
    m = bundle['metadata']
    frame['recorded_at'], frame['model_trained_at'] = now.isoformat(), m['trained_at']
    frame['model_dataset_sha256'], frame['target_version'] = m['dataset_sha256'], TARGET_VERSION
    frame['horizon_sessions'], frame['cost_assumption'], frame['validation_base_rate'] = 5, .003, m['baseline_probability']
    frame['source_manifest_sha256'] = hashlib.sha256((Path(data_root) / 'history_manifest.json').read_bytes()).hexdigest()
    frame['prediction_id'] = [hashlib.sha256('|'.join([code, str(origin.date()), m['dataset_sha256'], m['trained_at'], 'pairwise']).encode()).hexdigest()[:24] for code in frame.stock_code]
    key = hashlib.sha256((m['dataset_sha256'] + m['trained_at']).encode()).hexdigest()[:16]
    path = Path(output_dir) / f'ml_pairwise_forward_{origin:%Y%m%d}_{key}.csv'
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('x', encoding='utf-8-sig') as handle:
        frame.to_csv(handle, index=False)
    seal_ledger(path, 'pairwise_rank', m, PRIMARY, ARMS)
    return dict(frozen_predictions=len(frame), ledger=str(path), recommendation_enabled=False)


def grade_original(path, inputs, as_of, p, now=None):
    validate_protocol(p)
    frame, summary = grade_shadow(path, inputs, as_of, 'pairwise_rank', now)
    for name, mask in selection_masks(frame, p).items():
        old = frame[name].map({True: True, False: False, 'True': True, 'False': False})
        if old.isna().any() or not np.array_equal(old.to_numpy(dtype=bool), mask):
            raise ValueError('The original fixed rank selection changed.')
    summary['ranking_diagnostics'] = evaluate_rank(frame, p)
    return frame, summary


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['train', 'fit-current', 'predict', 'freeze', 'grade'])
    parser.add_argument('--protocol', type=Path, default=ROOT / 'docs/model_experiments/pairwise_price_protocol_20261026.json')
    parser.add_argument('--data-root', type=Path)
    parser.add_argument('--model-dir', type=Path)
    parser.add_argument('--report', type=Path)
    parser.add_argument('--stock')
    parser.add_argument('--ledger', type=Path)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--output-dir', type=Path, default=ROOT / 'data/predictions')
    args = parser.parse_args()
    p = json.loads(args.protocol.read_text())
    data_root = args.data_root or ROOT / p['data_root']
    root = args.model_dir or ROOT / ('data/models/price_pairwise_rank' if args.command == 'train' else 'data/models/price_pairwise_rank_current')
    if args.command in ['train', 'fit-current']:
        report = args.report or ROOT / ('reports/daily_review/2026-10-26_pairwise_price_research.md' if args.command == 'train' else 'reports/daily_review/2026-10-26_pairwise_current_fit.md')
        summary = train(data_root, root, p, report, current=args.command == 'fit-current')
        print(json_text(dict(run_dir=summary['run_dir'], recommendation_gate_passed=False)))
    elif args.command == 'grade':
        if not args.ledger or not args.output or args.ledger.resolve() == args.output.resolve():
            parser.error('grade requires an original --ledger and separate --output')
        inputs, _ = load_inputs(data_root, completed_price_cutoff())
        frame, summary = grade_original(args.ledger, inputs, completed_price_cutoff(), p)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        frame.to_csv(args.output, index=False)
        print(json_text(summary))
    else:
        bundle = load_model(root)
        if args.command == 'freeze':
            print(json_text(freeze(bundle, data_root, args.output_dir)))
        else:
            if not args.stock:
                parser.error('predict requires --stock')
            code = resolve_stock(args.stock, [ROOT, data_root])
            frame = current_predictions(bundle, data_root)
            matched = frame[frame.stock_code.eq(code)]
            if matched.empty:
                parser.exit(2, 'No eligible current inputs for this stock.\n')
            print(json_text(matched.iloc[0].to_dict() | {'note': 'Research probabilities, not certified reliability.'}))


if __name__ == '__main__':
    main()
