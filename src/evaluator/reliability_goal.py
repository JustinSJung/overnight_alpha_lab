"""Prespecified prospective-only goal checks, never a displayed confidence shortcut."""
from __future__ import annotations

import numpy as np
import pandas as pd

from src.crawler.market_clock import completed_price_cutoff
from src.evaluator.forward_price_forecast import valid_record_time
from src.features.next_open_dataset import TARGET_VERSION


def date_block_bounds(values, alpha, samples=10000, block=5):
    values = np.asarray(values, dtype=float)
    if values.ndim != 1 or len(values) < 20 or np.isfinite(values).sum() < 20:
        return None
    rng = np.random.default_rng(42)
    starts = rng.integers(0, len(values), (samples, int(np.ceil(len(values) / block))))
    index = ((starts[:, :, None] + np.arange(block)) % len(values)).reshape(samples, -1)[:, :len(values)]
    drawn = values[index]
    n = np.isfinite(drawn).sum(axis=1)
    means = np.nansum(drawn, axis=1)[n > 0] / n[n > 0]
    return float(np.quantile(means, alpha))


def certify_goal(graded, calendar, selected_column, goal, now, evidence_role, policy_id, benchmark=None):
    """Caller must grade HASH-VERIFIED originals; this function rechecks their timing.

    Recent not-yet-mature issue dates are excluded by scheduled session time,
    not by which outcomes happen to be available. Mature missing results fail.
    """
    if (evidence_role != 'hash_verified_timely_originals' or goal['schema'] != 'price_reliability_goal_v1'
            or goal['target_version'] != TARGET_VERSION or pd.Timestamp(now).tzinfo is None
            or policy_id not in goal['registered_policy_ids']
            or len(goal['registered_policy_ids']) > goal['maximum_policy_families']):
        raise ValueError('Only separately verified prospective originals may certify the goal.')
    result = dict(status='insufficient_future_evidence', goal_passed=False, policy_id=policy_id,
                  success_rate_target=goal['success_rate_minimum'], success_lower_target=goal['success_lower_minimum'],
                  evaluated_cases=0, selected_cases=0, selected_signal_dates=0, mature_issue_dates=0,
                  outcome_coverage=None, issue_date_coverage=None, pooled_success_rate=None,
                  date_equal_success_rate=None, success_lower=None, net_return_lower=None,
                  benchmark_excess_lower=None, certification_look=None, reasons=[])
    if graded.empty:
        result['reasons'] = ['no_timely_originals']
        return result
    f = graded.copy()
    f['signal_date'] = pd.to_datetime(f.signal_date, format='mixed').dt.normalize()
    if (f.signal_date.isna().any() or f.duplicated(['stock_code', 'signal_date']).any()
            or f.prediction_id.duplicated().any() or not f.target_version.eq(TARGET_VERSION).all() or not f.horizon_sessions.eq(5).all()
            or not f.cost_assumption.eq(.003).all()):
        raise ValueError('Duplicate or incompatible future evidence.')
    flags = f[selected_column].map({True: True, False: False, 'True': True, 'False': False})
    if flags.isna().any():
        raise ValueError('Missing original policy flags.')
    f['goal_selected'] = flags.astype(bool)
    for row in f.itertuples():
        recorded, trained = pd.Timestamp(row.recorded_at), pd.Timestamp(row.model_trained_at)
        if (recorded.tzinfo is None or trained.tzinfo is None or trained > recorded or recorded > now
                or not valid_record_time(row.signal_date, recorded)):
            raise ValueError('Original timing/provenance is invalid.')
    registered = f.signal_date.ge(pd.Timestamp(goal['certification_signal_start']))
    result['pre_registration_candidates'] = int((~registered).sum())
    f = f[registered].copy()
    if f.empty:
        result['reasons'] = ['no_post_registration_originals']
        return result
    if f[f.goal_selected].groupby('signal_date').size().gt(5).any():
        raise ValueError('The certified policy cannot silently change its daily cap.')
    cutoff = pd.Timestamp(completed_price_cutoff(pd.Timestamp(now).to_pydatetime()))
    calendar = pd.DatetimeIndex(sorted(pd.to_datetime(calendar).unique()))
    calendar = calendar[calendar <= cutoff]
    positions = calendar.get_indexer(f.signal_date)
    if np.any(positions < 0):
        raise ValueError('An original signal date is missing from the observed session calendar.')
    mature = positions + 5 < len(calendar)
    f = f[mature].copy()
    if f.empty:
        result['reasons'] = ['no_scheduled_mature_originals']
        return result
    # Missing issuances are still calendar time, not independent adjacent bets.
    # Keep those sessions in both the frequency denominator and block resampling.
    dates = calendar[:-5]
    dates = dates[dates >= pd.Timestamp(goal['certification_signal_start'])]
    health_source = f.copy()
    selected_counts = f[f.goal_selected].groupby('signal_date').size().reindex(dates, fill_value=0)
    cumulative = selected_counts.cumsum()
    looks = [n for n in goal['certification_case_looks'] if n <= int(cumulative.iloc[-1])]
    look_number = len(looks)
    if looks:
        end = cumulative.index[cumulative.ge(looks[-1])][0]
        # Always retain the complete issue batch; never choose individual winners.
        f = f[f.signal_date.le(end)].copy()
        dates = dates[dates <= end]
        result['certification_look'] = looks[-1]
    selected = f[f.goal_selected].copy()
    observed = selected[selected.target.notna()]
    if not observed.target.isin([0, 1]).all() or not np.isfinite(observed.net_return_proxy).all():
        raise ValueError('Resolved evidence contains invalid BUY outcomes.')
    result.update(selected_cases=len(selected), evaluated_cases=len(observed),
                  selected_signal_dates=int(selected.signal_date.nunique()), mature_issue_dates=len(dates),
                  recorded_mature_issue_dates=int(f.signal_date.nunique()),
                  outcome_coverage=len(observed) / len(selected) if len(selected) else None,
                  issue_date_coverage=selected.signal_date.nunique() / len(dates),
                  pooled_success_rate=float(observed.target.mean()) if len(observed) else None)
    if len(observed):
        result['date_equal_success_rate'] = float(observed.groupby('signal_date').target.mean().mean())
    reasons = []
    if len(observed) < goal['minimum_evaluated_cases']:
        reasons.append('fewer_than_minimum_evaluated_cases')
    if selected.signal_date.nunique() < goal['minimum_signal_dates']:
        reasons.append('fewer_than_minimum_selected_signal_dates')
    if result['issue_date_coverage'] < goal['minimum_issue_date_coverage']:
        reasons.append('recommendation_frequency_too_low')
    if result['outcome_coverage'] is None or result['outcome_coverage'] < goal['minimum_outcome_coverage']:
        reasons.append('mature_selected_outcomes_missing')
    if not looks:
        reasons.append('no_prespecified_certification_look_reached')
    if result['pooled_success_rate'] is None or result['pooled_success_rate'] < goal['success_rate_minimum']:
        reasons.append('observed_success_below_target')
    # Spend alpha only at fixed case-count looks, with a fixed family budget.
    alpha = goal['confidence_alpha'] / goal['maximum_policy_families'] / (max(1, look_number) * (max(1, look_number) + 1))
    result['one_sided_alpha_at_look'] = alpha
    daily = selected.groupby('signal_date').agg(success=('target', 'mean'), resolved=('target', 'count'),
                                               count=('stock_code', 'size'), net=('net_return_proxy', 'mean')).reindex(dates)
    complete = daily.resolved.eq(daily['count'])
    success = daily.success.where(complete)
    net = daily.net.where(complete | daily['count'].isna()).fillna(0)
    if result['outcome_coverage'] == 1 and looks:
        bootstrap_lower = date_block_bounds(success, alpha, block=goal['bootstrap_block_sessions'])
        # A perfect small sample must not produce a spurious 100% lower bound.
        # Bounded-outcome guard treats non-overlapping session blocks as units;
        # independence across those blocks remains an explicit research assumption.
        units = max(1, int(np.isfinite(success).sum()) // goal['bootstrap_block_sessions'])
        finite_guard = max(0., float(success.mean()) - np.sqrt(np.log(1 / alpha) / (2 * units)))
        result['success_bootstrap_lower'] = bootstrap_lower
        result['success_finite_block_guard'] = finite_guard
        result['effective_success_blocks'] = units
        result['success_lower'] = min(bootstrap_lower, finite_guard) if bootstrap_lower is not None else None
        result['net_return_lower'] = date_block_bounds(net, alpha, block=goal['bootstrap_block_sessions'])
    if result['success_lower'] is None or result['success_lower'] < goal['success_lower_minimum']:
        reasons.append('success_statistical_lower_below_target')
    if result['net_return_lower'] is None or result['net_return_lower'] <= goal['minimum_net_return_lower']:
        reasons.append('net_return_lower_not_positive')
    if benchmark is not None and len(selected):
        b = benchmark.copy()
        b['signal_date'] = pd.to_datetime(b.signal_date).dt.normalize()
        if b.signal_date.duplicated().any():
            raise ValueError('Benchmark dates must be unique.')
        b = b.set_index('signal_date').reindex(dates)
        active = selected_counts.reindex(dates).gt(0)
        expected_entry = pd.Series(calendar[calendar.get_indexer(dates) + 1], index=dates)
        expected_exit = pd.Series(calendar[calendar.get_indexer(dates) + 5], index=dates)
        matched = (pd.to_datetime(b.entry_date).eq(expected_entry) & pd.to_datetime(b.exit_date).eq(expected_exit)
                   & np.isfinite(b.net_return) & b.source.eq(goal['benchmark_source_id']))
        if matched[active].all() and result['outcome_coverage'] == 1 and looks:
            excess = (net - b.net_return).where(active, 0)
            result['benchmark_excess_lower'] = date_block_bounds(excess, alpha, block=goal['bootstrap_block_sessions'])
    if result['benchmark_excess_lower'] is None or result['benchmark_excess_lower'] <= goal['minimum_benchmark_excess_lower']:
        reasons.append('benchmark_coverage_or_excess_lower_failed')
    health = health_source[health_source.goal_selected]
    health_dates = sorted(health.signal_date.unique())[-goal['recent_health_dates']:]
    health = health[health.signal_date.isin(health_dates)]
    result['recent_health_success'] = float(health.groupby('signal_date').target.mean().mean()) if len(health) else None
    if (len(health_dates) < goal['recent_health_dates'] or health.target.isna().any()
            or result['recent_health_success'] is None or result['recent_health_success'] < goal['success_rate_minimum']):
        reasons.append('recent_health_not_adequate')
    result['reasons'] = reasons
    result['goal_passed'] = not reasons
    result['status'] = 'goal_criteria_passed' if not reasons else ('goal_not_met' if looks else 'insufficient_future_evidence')
    result['scope'] = 'Fixed-policy prospective learning-system evidence; not a guarantee of future returns'
    return result
