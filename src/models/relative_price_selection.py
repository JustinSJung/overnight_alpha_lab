"""Research-only cross-sectional selection; never an absolute buy probability."""
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
from sklearn.metrics import brier_score_loss, roc_auc_score
from threadpoolctl import threadpool_limits

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from src.features.completed_price_dataset import HISTORY_FEATURE_VERSION
from src.features.price_learning_dataset import FEATURES, build_dataset, load_snapshots, make_features, temporal_partitions
from src.models.price_forecaster import classifiers, date_weights, json_text, logits

DAILY_VALUES = ['absolute_success_rate', 'relative_success_rate', 'mean_return', 'net_return_proxy', 'excess_vs_pool']


def relative_dataset(snapshots, as_of, minimum_stocks=100, cost=.003):
    if snapshots.attrs.get('feature_version') != HISTORY_FEATURE_VERSION:
        raise ValueError('Relative learning requires coherent completed OHLCV history.')
    if minimum_stocks < 2:
        raise ValueError('At least two stocks per reference date are required.')
    cutoff = pd.Timestamp(as_of).normalize()
    inputs = snapshots[(snapshots.signal_date <= cutoff) & (snapshots.snapshot_date <= cutoff)].copy()
    if inputs.duplicated(['stock_code', 'signal_date']).any():
        raise ValueError('Duplicate stock/date observations.')
    inputs[FEATURES] = make_features(inputs)
    eligible = inputs[inputs[FEATURES].notna().all(axis=1) & inputs.volume_ratio_20d.gt(0)
                      & inputs.snapshot_date.le(inputs.signal_date) & inputs.close.gt(0)].copy()
    resolved, metadata = build_dataset(snapshots, horizon=5, cost=cost, as_of=cutoff)
    coverage = eligible.groupby('signal_date').size().rename('eligible_count').to_frame()
    coverage['resolved_count'] = resolved.groupby('signal_date').size().reindex(coverage.index, fill_value=0)
    coverage['complete'] = coverage.eligible_count.eq(coverage.resolved_count)
    coverage['included'] = coverage.complete & coverage.eligible_count.ge(minimum_stocks)
    resolved = resolved[resolved.signal_date.isin(coverage.index[coverage.included])].copy()
    if resolved.empty:
        raise ValueError('No complete-outcome candidate-universe dates.')
    if resolved.groupby('signal_date').target_date.nunique().gt(1).any():
        raise ValueError('Constituents do not share the same outcome horizon.')
    resolved['universe_return'] = resolved.groupby('signal_date').target_return.transform('mean')
    resolved['relative_return'] = resolved.target_return - resolved.universe_return
    resolved['relative_target'] = resolved.relative_return.gt(0).astype(int)
    resolved['stock_label_available_date'] = resolved.label_available_date
    # The cross-sectional answer is unknown until ALL reference outcomes are known.
    resolved['label_available_date'] = resolved.groupby('signal_date').label_available_date.transform('max')
    return resolved.sort_values(['signal_date', 'stock_code']).reset_index(drop=True), coverage, metadata


def fit_models(train, calibration, as_of):
    if not train.label_available_date.max() < calibration.signal_date.min():
        raise ValueError('Training labels overlap calibration inputs.')
    if calibration.label_available_date.max() > pd.Timestamp(as_of):
        raise ValueError('Calibration includes unavailable cross-sectional labels.')
    models = {}
    with threadpool_limits(limits=2):
        for name, target in [('relative', 'relative_target'), ('absolute_control', 'target')]:
            if train[target].nunique() != 2 or calibration[target].nunique() != 2:
                raise ValueError('Training and calibration need both target classes.')
            classifier = classifiers()['hist_gradient_boosting']
            classifier.fit(train[FEATURES], train[target], sample_weight=date_weights(train))
            calibrator = LogisticRegression(C=1.0, solver='liblinear', max_iter=1000, random_state=42)
            calibrator.fit(logits(classifier, calibration[FEATURES]), calibration[target],
                           sample_weight=date_weights(calibration))
            models[name] = {'classifier': classifier, 'calibrator': calibrator,
                            'known_calibration_prior': float(np.average(calibration[target], weights=date_weights(calibration))),
                            'target_column': target}
    return models


def score_inputs(models, frame):
    with threadpool_limits(limits=2):
        return {name: model['calibrator'].predict_proba(logits(model['classifier'], frame[FEATURES]))[:, 1]
                for name, model in models.items()}


def rank_candidates(frame, score_column, top_k):
    if top_k < 1 or frame.duplicated(['stock_code', 'signal_date']).any():
        raise ValueError('Ranking requires positive k and unique stock/date rows.')
    if frame[score_column].isna().any() or not np.isfinite(frame[score_column]).all():
        raise ValueError('Ranking scores must be finite.')
    # Ties never depend on future labels or the incoming CSV order.
    ordered = frame.sort_values(['signal_date', score_column, 'stock_code'], ascending=[True, False, True], kind='stable')
    return ordered[ordered.groupby('signal_date').cumcount() < top_k].copy()


def daily_portfolio(frame, pool_returns):
    grouped = frame.groupby('signal_date')
    daily = grouped.agg(selected_count=('stock_code', 'size'), absolute_success_rate=('target', 'mean'),
                        relative_success_rate=('relative_target', 'mean'), mean_return=('target_return', 'mean'),
                        net_return_proxy=('net_return_proxy', 'mean'))
    daily['excess_vs_pool'] = daily.mean_return - pool_returns.reindex(daily.index)
    if daily.isna().any(axis=None):
        raise ValueError('Portfolio and universe dates do not align.')
    return daily


def random_portfolios(frame, top_ks, replicates=100, seed_start=42):
    if replicates < 1:
        raise ValueError('Random comparison needs at least one replicate.')
    daily_rows = {k: [] for k in top_ks}
    replicate_means = {k: np.zeros((replicates, len(DAILY_VALUES))) for k in top_ks}
    for day, part in frame.groupby('signal_date', sort=True):
        part = part.sort_values('stock_code')
        if len(part) < max(top_ks):
            raise ValueError('A reference date has fewer candidates than top_k.')
        pool_return = part.target_return.mean()
        outcomes = np.column_stack([part.target, part.relative_target, part.target_return,
                                    part.net_return_proxy, part.target_return - pool_return])
        samples = {k: [] for k in top_ks}
        for replicate in range(replicates):
            # Date-specific seeds keep draws stable if unrelated dates are appended.
            seed = np.random.SeedSequence([seed_start + replicate, int(pd.Timestamp(day).strftime('%Y%m%d'))])
            order = np.random.default_rng(seed).permutation(len(part))
            for k in top_ks:
                values = outcomes[order[:k]].mean(axis=0)
                samples[k].append(values)
                replicate_means[k][replicate] += values
        for k in top_ks:
            daily_rows[k].append(dict(signal_date=day, selected_count=k,
                                      **dict(zip(DAILY_VALUES, np.mean(samples[k], axis=0)))))
    dates = frame.signal_date.nunique()
    daily = {k: pd.DataFrame(rows).set_index('signal_date') for k, rows in daily_rows.items()}
    dispersion = {str(k): {'replicates': replicates,
                           'mean_return_seed_quantiles': np.quantile(values[:, 2] / dates, [.025, .5, .975]).tolist()}
                  for k, values in replicate_means.items()}
    return daily, dispersion


def block_interval(values, samples=5000, block=5, alpha=.05, seed=42):
    values = np.asarray(values, dtype=float)
    if values.ndim != 1 or not len(values) or not np.isfinite(values).all():
        raise ValueError('Block intervals require a nonempty finite daily vector.')
    if samples < 1 or block < 1 or not 0 < alpha < 1:
        raise ValueError('Invalid bootstrap parameters.')
    if len(values) < max(20, block):
        return {'mean': float(values.mean()), 'lower': None, 'upper': None}
    starts = np.random.default_rng(seed).integers(0, len(values), (samples, int(np.ceil(len(values) / block))))
    indices = ((starts[:, :, None] + np.arange(block)) % len(values)).reshape(samples, -1)[:, :len(values)]
    bounds = np.quantile(values[indices].mean(axis=1), [alpha / 2, 1 - alpha / 2])
    return {'mean': float(values.mean()), 'lower': float(bounds[0]), 'upper': float(bounds[1])}


def paired_returns(candidate, reference, protocol, alpha=.05):
    if not candidate.index.equals(reference.index):
        raise ValueError('Paired return dates must match exactly.')
    return block_interval(candidate.mean_return - reference.mean_return, protocol['bootstrap_samples'],
                          protocol['bootstrap_block_sessions'], alpha, protocol['bootstrap_seed'])


def probability_metrics(frame, probability, target, prior):
    weights = date_weights(frame)
    daily_auc = [roc_auc_score(part[target], probability[part.index])
                 for _, part in frame.groupby('signal_date') if part[target].nunique() == 2]
    return {'target': target, 'date_brier': float(brier_score_loss(frame[target], probability, sample_weight=weights)),
            'known_constant_date_brier': float(brier_score_loss(frame[target], np.full(len(frame), prior), sample_weight=weights)),
            'mean_daily_auc': float(np.mean(daily_auc)) if daily_auc else None,
            'auc_dates': len(daily_auc), 'known_calibration_prior': prior}


def render_report(summary):
    def pct(value):
        return 'n/a' if value is None else f'{value:.3%}'
    lines = ['# Relative Price Selection Research', '',
             'RESEARCH_ONLY. Retrospective development experiment, not a new untouched test or a buy recommendation.', '',
             '## Meaning and Coverage', '',
             'Relative probability means beating the equal-weight input-eligible candidate universe over five quote sessions. It is NOT the chance of a profitable purchase and the universe is NOT KOSPI/KOSDAQ.',
             'The reference includes the candidate itself. Identical assumed costs cancel in relative comparisons; absolute net proxies still subtract 0.3%.',
             'Eligibility uses signal-close inputs only. Entire dates with missing constituent outcomes are excluded, never just unresolved stocks. This complete-date filter and the current-universe/retrospectively adjusted-history selection bias remain limitations.',
             f"Evaluation coverage: {summary['coverage']['included_dates']}/{summary['coverage']['eligible_dates']} dates; {summary['coverage']['evaluated_rows']} rows.",
             'All portfolio rates/returns below give each signal date equal weight. Top20 is primary; Top10 is secondary. Ranking has no probability cutoff and is NOT an activated recommendation policy.', '',
             '## Selection Results', '',
             '| Group | Dates | Cases | Absolute success | Beats universe | Five-session net proxy | Excess vs universe |',
             '|---|---:|---:|---:|---:|---:|---:|']
    for name, row in summary['portfolios'].items():
        lines.append(f"| {name} | {row['dates']} | {row['selected_cases']} | {pct(row['absolute_success_rate'])} | {pct(row['relative_success_rate'])} | {pct(row['net_return_proxy'])} | {pct(row['excess_vs_pool'])} |")
    lines += ['', 'Random is the mean of 100 pre-fixed, independent deterministic random selections (not the best seed). Portfolio outcomes overlap in time; they are not compounded or executable next-open P&L.', '',
              '## Primary Top20 Paired Comparisons', '',
              '| Reference | Relative model minus reference return | Simultaneous family-95% interval |',
              '|---|---:|---|']
    for name, row in summary['primary_paired'].items():
        lines.append(f"| {name} | {pct(row['mean'])} | [{pct(row['lower'])}, {pct(row['upper'])}] |")
    lines += ['', 'Paired circular blocks of five observed signal dates; 5,000 resamples, seed 42. Four comparisons use Bonferroni-adjusted intervals. These are approximate development diagnostics after earlier inspection of the same dates, not new independent evidence.',
              'Top20 absolute net-proxy interval: ' + str(summary['primary_net_interval']),
              'Development screen passed: ' + str(summary['development_screen_passed']),
              'Screen reasons: ' + ', '.join(summary['screen_reasons']),
              'Production recommendation gate: False (prospective validation is always required).', '',
              '## Probability Diagnostics', '',
              '| Model | Date Brier | Known past-constant Brier | Mean daily AUC | Sigmoid slope |',
              '|---|---:|---:|---:|---:|']
    for name, row in summary['probabilities'].items():
        lines.append(f"| {name} | {row['date_brier']:.6f} | {row['known_constant_date_brier']:.6f} | {row['mean_daily_auc']} | {row['calibration_slope']:.6f} |")
    lines += ['', 'The two Brier scores concern different targets; do not compare their numeric levels to claim one model is more reliable. Relative and absolute classifiers share inputs, dates, sample weights and fixed model settings.', '',
              '## Monthly Primary Results', '',
              '| Month | Dates | Relative Top20 excess | Absolute-control Top20 excess | Momentum Top20 excess | Random Top20 excess | Relative Top20 net proxy |',
              '|---|---:|---:|---:|---:|---:|---:|']
    for row in summary['monthly']:
        lines.append(f"| {row['month']} | {row['dates']} | {pct(row['relative_excess'])} | {pct(row['absolute_excess'])} | {pct(row['momentum_excess'])} | {pct(row['random_excess'])} | {pct(row['relative_net'])} |")
    lines += ['', '## Temporal Audit', '',
              'Fit as-of: ' + summary['fit_as_of'], '',
              '| Partition | Rows | Dates | Signal start | Signal end | Latest cross-sectional label |',
              '|---|---:|---:|---|---|---|']
    for name, row in summary['partitions'].items():
        lines.append(f"| {name} | {row['rows']} | {row['dates']} | {row['start']} | {row['end']} | {row['latest_label']} |")
    lines += ['', 'No future test outcomes/scores are attached to the serialized as-of model. Experimental relative bundles have a separate schema and cannot replace an absolute forecast bundle.',
              'No candidate generation, legacy evaluation, dashboard, default model, frozen forward ledger, or deployment was changed.', '',
              'Protocol SHA256: ' + summary['protocol_sha256'],
              'Dataset SHA256: ' + summary['dataset_sha256'],
              'Artifacts (ignored by Git): ' + summary['run_dir'], '']
    return '\n'.join(lines)


def run_experiment(data_root, output_root, protocol, report_path):
    if (protocol['features'] != FEATURES or protocol['horizon_sessions'] != 5 or protocol['cost_assumption'] != .003
            or protocol['primary_top_k'] != 20 or protocol['secondary_top_k'] != 10
            or protocol['classifier'] != 'hist_gradient_boosting' or protocol['production_promotion'] is not False
            or protocol['candidate_pool_change'] is not False):
        raise ValueError('Unsupported relative selection protocol.')
    snapshots, source = load_snapshots(data_root)
    if source.get('skipped_files') or snapshots.attrs.get('history_provenance', {}).get('failed_stocks', 0):
        raise ValueError('Do not silently narrow the input universe after collection failures.')
    dataset, coverage, metadata = relative_dataset(snapshots, protocol['labels_as_of'], protocol['minimum_stocks_per_date'])
    dataset = dataset[dataset.signal_date <= pd.Timestamp(protocol['evaluation_end'])].copy()
    train, calibration, test = temporal_partitions(dataset, protocol['calibration_start'], protocol['evaluation_start'])
    train, calibration, test = [part.reset_index(drop=True) for part in [train, calibration, test]]
    calendar = pd.DatetimeIndex(sorted(snapshots.signal_date.unique()))
    as_of = calendar[calendar < pd.Timestamp(protocol['evaluation_start'])][-1]
    models = fit_models(train, calibration, as_of)
    predicted = score_inputs(models, test)
    columns = ['stock_code', 'signal_date', 'target_date', 'label_available_date', 'target', 'relative_target',
               'target_return', 'universe_return', 'relative_return', 'net_return_proxy', 'return_20d']
    ledger = test[columns].copy()
    for name, values in predicted.items():
        ledger[name + '_probability'] = values
    ledger['origin'] = 'retrospective_development_not_prospective'
    ledger['recommendation'] = 'ABSTAIN'
    recorded_at = datetime.now(timezone.utc)
    ledger['recorded_at'] = recorded_at.isoformat()
    pool_returns = ledger.groupby('signal_date').target_return.mean()
    portfolios = {'pool': daily_portfolio(ledger, pool_returns)}
    top_ks = [protocol['primary_top_k'], protocol['secondary_top_k']]
    for k in top_ks:
        for name, score in [('relative', 'relative_probability'), ('absolute', 'absolute_control_probability'),
                            ('momentum', 'return_20d')]:
            portfolios[f'{name}_top{k}'] = daily_portfolio(rank_candidates(ledger, score, k), pool_returns)
    random_daily, random_dispersion = random_portfolios(ledger, top_ks, protocol['random_replicates'], protocol['random_seed_start'])
    portfolios.update({f'random_top{k}': frame for k, frame in random_daily.items()})
    primary = portfolios['relative_top20']
    controls = ['pool', 'absolute_top20', 'momentum_top20', 'random_top20']
    paired = {name: paired_returns(primary, portfolios[name], protocol, alpha=.05 / len(controls)) for name in controls}
    interval = block_interval(primary.net_return_proxy, protocol['bootstrap_samples'], protocol['bootstrap_block_sessions'], seed=protocol['bootstrap_seed'])
    evaluation_coverage = coverage.loc[protocol['evaluation_start']:protocol['evaluation_end']].copy()
    reasons = []
    if len(primary) < 100:
        reasons.append('fewer_than_100_complete_dates')
    if evaluation_coverage.included.mean() < .95:
        reasons.append('less_than_95_percent_complete_date_coverage')
    for name, result in paired.items():
        if result['lower'] is None or result['lower'] <= 0:
            reasons.append('no_clear_advantage_vs_' + name)
    if interval['lower'] is None or interval['lower'] <= 0:
        reasons.append('absolute_net_proxy_lower_bound_not_positive')
    protocol_hash = hashlib.sha256(json_text(protocol).encode()).hexdigest()
    dataset_hash = hashlib.sha256(pd.util.hash_pandas_object(
        dataset[['stock_code', 'signal_date', 'label_available_date', 'target_return', 'relative_target'] + FEATURES], index=False
    ).values.tobytes()).hexdigest()
    implementation = {str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
                      for path in [Path(__file__), ROOT / 'src/features/price_learning_dataset.py',
                                   ROOT / 'src/features/completed_price_dataset.py', ROOT / 'src/models/price_forecaster.py']}
    partition_audit = {name: {'rows': len(part), 'dates': int(part.signal_date.nunique()),
                             'start': str(part.signal_date.min().date()), 'end': str(part.signal_date.max().date()),
                             'latest_label': str(part.label_available_date.max().date())}
                       for name, part in [('train', train), ('calibration', calibration), ('test', test)]}
    model_metadata = {'schema': 'research_relative_selection_v1_not_absolute_forecaster', 'as_of': str(as_of.date()),
                      'features': FEATURES, 'protocol': protocol, 'protocol_sha256': protocol_hash,
                      'implementation_sha256': implementation, 'history_provenance': metadata.get('history_provenance'),
                      'fit_partitions': {name: partition_audit[name] for name in ['train', 'calibration']},
                      'trained_at': recorded_at.isoformat(), 'recommendation_gate_passed': False}
    run_dir = Path(output_root) / (recorded_at.strftime('%Y%m%dT%H%M%SZ') + '_' + uuid.uuid4().hex[:8])
    run_dir.mkdir(parents=True, exist_ok=False)
    joblib.dump({'models': models, 'metadata': model_metadata}, run_dir / 'research_models.joblib')
    (run_dir / 'model_metadata.json').write_text(json_text(model_metadata) + '\n', encoding='utf-8')
    ledger.to_csv(run_dir / 'historical_predictions.csv', index=False)
    coverage.to_csv(run_dir / 'universe_outcome_coverage.csv')
    pd.concat([frame.assign(portfolio=name).reset_index() for name, frame in portfolios.items()], ignore_index=True).to_csv(run_dir / 'daily_portfolios.csv', index=False)
    monthly = []
    for month in sorted(primary.index.to_period('M').unique()):
        part = primary.index.to_period('M') == month
        monthly.append({'month': str(month), 'dates': int(part.sum()),
                        'relative_excess': float(primary.loc[part, 'excess_vs_pool'].mean()),
                        'relative_net': float(primary.loc[part, 'net_return_proxy'].mean()),
                        **{name + '_excess': float(portfolios[name + '_top20'].loc[part, 'excess_vs_pool'].mean())
                           for name in ['absolute', 'momentum', 'random']}})
    probabilities = {name: probability_metrics(test, predicted[name], model['target_column'], model['known_calibration_prior'])
                     | {'calibration_slope': float(model['calibrator'].coef_[0, 0])} for name, model in models.items()}
    summary = {'protocol': protocol, 'protocol_sha256': protocol_hash, 'dataset_sha256': dataset_hash,
               'implementation_sha256': implementation, 'recorded_at': recorded_at.isoformat(), 'run_dir': str(run_dir),
               'fit_as_of': str(as_of.date()), 'partitions': partition_audit, 'probabilities': probabilities,
               'coverage': {'eligible_dates': len(evaluation_coverage), 'included_dates': int(evaluation_coverage.included.sum()),
                            'evaluated_rows': len(test), 'excluded_dates': evaluation_coverage.loc[~evaluation_coverage.included].reset_index().to_dict('records')},
               'portfolios': {name: dict(dates=len(frame), selected_cases=int(frame.selected_count.sum()),
                                        **{col: float(frame[col].mean()) for col in DAILY_VALUES}) for name, frame in portfolios.items()},
               'primary_paired': paired, 'primary_net_interval': interval, 'monthly': monthly,
               'random_seed_dispersion': random_dispersion, 'development_screen_passed': not reasons,
               'screen_reasons': reasons, 'recommendation_gate_passed': False}
    report_path = Path(report_path)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(render_report(summary), encoding='utf-8')
    report_path.with_suffix('.json').write_text(json_text(summary) + '\n', encoding='utf-8')
    print(json_text({'run_dir': str(run_dir), 'coverage': summary['coverage'], 'primary_paired': paired,
                     'development_screen_passed': not reasons, 'recommendation_gate_passed': False}), flush=True)
    return summary


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--protocol', type=Path, default=ROOT / 'docs/model_experiments/relative_selection_protocol_20261021.json')
    parser.add_argument('--data-root', type=Path)
    parser.add_argument('--output-root', type=Path, default=ROOT / 'data/models/price_relative_selection')
    parser.add_argument('--report-path', type=Path, default=ROOT / 'reports/daily_review/2026-10-21_relative_price_selection.md')
    args = parser.parse_args()
    protocol = json.loads(args.protocol.read_text(encoding='utf-8'))
    run_experiment(args.data_root or ROOT / protocol['data_root'], args.output_root, protocol, args.report_path)


if __name__ == '__main__':
    main()
