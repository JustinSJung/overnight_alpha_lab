"""Whitelisted public next-open research forecasts, never claimed as approved."""
from __future__ import annotations

import pandas as pd

from src.crawler.market_clock import KST
from src.features.next_open_dataset import TARGET_VERSION
from src.models.next_open_price_model import ROOT, current_predictions
from src.models.price_forecaster import stock_catalog


def observed_performance(graded):
    """Actual BUY outcomes of originals, never current-fit back-predictions."""
    if graded is None or graded.empty:
        return None
    resolved = graded[graded.target.notna()]
    if not resolved.target.isin([0, 1]).all():
        raise ValueError('Invalid original forecast outcomes.')
    flags = graded.get('fixed_policy_selected', pd.Series(False, index=graded.index)).map(
        {True: True, False: False, 'True': True, 'False': False})
    if flags.isna().any():
        raise ValueError('Invalid original selection flags.')
    selected = graded[flags.astype(bool)]
    selected_resolved = selected[selected.target.notna()]
    return dict(
        evaluated_cases=len(resolved), success_count=int(resolved.target.eq(1).sum()),
        failure_count=int(resolved.target.eq(0).sum()),
        success_rate=float(resolved.target.mean()) if len(resolved) else None,
        signal_dates=int(resolved.signal_date.nunique()), selected_cases=len(selected),
        selected_evaluated_cases=len(selected_resolved), selected_pending_or_unavailable=int(selected.target.isna().sum()),
        selected_success_count=int(selected_resolved.target.eq(1).sum()),
        selected_failure_count=int(selected_resolved.target.eq(0).sum()),
        selected_success_rate=float(selected_resolved.target.mean()) if len(selected_resolved) else None,
        selected_signal_dates=int(selected_resolved.signal_date.nunique()))


def build_payload(bundle, data_root, evidence, graded, now):
    if now.tzinfo is None:
        raise ValueError('Timezone-aware publication clock required.')
    now = now.astimezone(KST)
    if bundle['metadata']['target_version'] != TARGET_VERSION:
        raise ValueError('Different prediction targets must not be mixed.')
    actual_records = 0 if graded is None else len(graded)
    actual_resolved = 0 if graded is None else int(graded.target.notna().sum())
    if actual_records != evidence['recorded_candidates'] or actual_resolved != evidence['evaluated_cases']:
        raise ValueError('Forward counts must match the actual graded original records.')
    predictions = current_predictions(bundle, data_root, now)
    latest_date = predictions.signal_date.max()
    origin_kind = 'research_snapshot'
    if graded is not None:
        original = graded[pd.to_datetime(graded.signal_date).eq(latest_date)]
        if not original.empty:
            # New learning must not rewrite a forecast already shown before open.
            predictions = original[['stock_code', 'signal_date', 'probability_above_cost']].copy()
            predictions['signal_date'] = pd.to_datetime(predictions.signal_date)
            origin_kind = 'frozen_original'
    names = {}
    for name, codes in stock_catalog([ROOT, data_root]).items():
        for code in codes:
            names.setdefault(code, []).append(name)
    latest = str(predictions.signal_date.max().date())
    stocks = []
    for row in predictions.itertuples():
        aliases = sorted(set(names.get(row.stock_code, [])))
        stocks.append(dict(stock_code=row.stock_code, stock_name=aliases[0] if aliases else row.stock_code,
                           aliases=aliases, signal_date=str(row.signal_date.date()),
                           probability=float(row.probability_above_cost), predicted_return=None,
                           stale=(now.date() - row.signal_date.date()).days > 7, recommended=False))
    stocks.sort(key=lambda row: (-row['probability'], row['stock_code']))
    resolved_dates = 0 if graded is None else int(graded.loc[graded.target.notna(), 'signal_date'].nunique())
    if evidence['recorded_candidates'] != evidence['evaluated_cases'] + evidence['unresolved_cases']:
        raise ValueError('Inconsistent future evaluation counts.')
    stale = (now.date() - pd.Timestamp(latest).date()).days > 7
    pending = int(evidence.get('states', {}).get('awaiting_future_sessions', 0))
    unavailable = int(evidence['unresolved_cases']) - pending
    if pending < 0 or unavailable < 0:
        raise ValueError('Inconsistent pending outcome states.')
    return dict(schema='public_price_forecast_v1', prediction_target=TARGET_VERSION,
                prediction_origin=origin_kind,
                generated_at=now.isoformat(), price_date=latest,
                model_state='stale' if stale else 'research', recommendation_enabled=False,
                horizon_sessions=5, cost_assumption=.003, stock_count=len(stocks), skipped_count=0,
                learned_labels_through=bundle['metadata']['as_of'],
                observed_performance=observed_performance(graded),
                forward=dict(recorded=int(evidence['recorded_candidates']), resolved=int(evidence['evaluated_cases']),
                             pending=pending, unavailable=unavailable, signal_dates=resolved_dates,
                             passed=False, integrity_issues=0, scope='learning_system'),
                recommendations=[], watchlist=[row['stock_code'] for row in stocks[:5] if not row['stale']], stocks=stocks)
