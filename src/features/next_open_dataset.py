"""Separate next-open research labels, retaining every input-eligible candidate."""
from __future__ import annotations

import numpy as np
import pandas as pd

from src.features.ohlcv_information import OHLCV_FEATURES
from src.features.price_learning_dataset import FEATURES

COLUMNS = FEATURES + OHLCV_FEATURES

TARGET_VERSION = 'next_open_to_fifth_close_v1'


def valid_candle(frame):
    values = frame[['open', 'high', 'low', 'close', 'volume']]
    return (np.isfinite(values).all(axis=1) & values.volume.gt(0)
            & values.open.gt(0) & values.low.gt(0)
            & values.high.ge(values[['open', 'close']].max(axis=1))
            & values.low.le(values[['open', 'close']].min(axis=1)))


def build_next_open_dataset(inputs, as_of, horizon=5, cost=.003, candidate_keys=None):
    """Outcomes may be unavailable; eligibility/ranks must never depend on them.

    The observed whole-universe session calendar is used, not a stock's next
    available row. Missing/suspended execution bars do not become failed calls.
    Exceptional price discontinuities require corporate-action review, not clipping.
    """
    if horizon < 1 or not 0 <= cost < 1:
        raise ValueError('Invalid horizon or cost.')
    cutoff = pd.Timestamp(as_of).normalize()
    frame = inputs[inputs.signal_date.le(cutoff) & inputs.snapshot_date.le(cutoff)].copy()
    if frame.empty or frame.duplicated(['stock_code', 'signal_date']).any():
        raise ValueError('Unique stock/date input history is required.')
    if frame.snapshot_date.gt(frame.signal_date).any():
        raise ValueError('Input observation was recorded after its signal date.')
    calendar = pd.DatetimeIndex(sorted(frame.signal_date.unique()))
    frame = frame.sort_values(['stock_code', 'signal_date']).reset_index(drop=True)
    index = pd.Series(np.arange(len(calendar)), index=calendar)
    frame['session_index'] = frame.signal_date.map(index)
    frame['bar_valid'] = valid_candle(frame)
    groups = frame.groupby('stock_code', sort=False)
    frame['entry_date'] = groups.signal_date.shift(-1)
    frame['entry_open'] = groups.open.shift(-1)
    frame['entry_bar_valid'] = groups.bar_valid.shift(-1).eq(True)
    frame['target_date'] = groups.signal_date.shift(-horizon)
    frame['label_available_date'] = groups.snapshot_date.shift(-horizon)
    frame['future_close'] = groups.close.shift(-horizon)
    frame['exit_bar_valid'] = groups.bar_valid.shift(-horizon).eq(True)
    entry_index = groups.session_index.shift(-1)
    exit_index = groups.session_index.shift(-horizon)
    continuous = entry_index.sub(frame.session_index).eq(1) & exit_index.sub(frame.session_index).eq(horizon)
    expected_exit = pd.Series(calendar, index=np.arange(len(calendar))).reindex(
        (frame.session_index + horizon).to_numpy()).reset_index(drop=True)
    frame['expected_target_date'] = expected_exit
    # A large one-session change is a review flag, NOT proof of bad prices and
    # NOT a statutory price-limit assertion. Multi-session gains are not clipped.
    one_day = groups.close.pct_change(fill_method=None).abs().gt(.305)
    exceptional = pd.Series(False, index=frame.index)
    for step in range(2, horizon + 1):
        exceptional |= one_day.groupby(frame.stock_code, sort=False).shift(-step).eq(True)
    entry_intraday = groups.close.shift(-1) / frame.entry_open.where(frame.entry_open.gt(0)) - 1
    exceptional |= entry_intraday.abs().gt(.305)
    frame['exceptional_price_move'] = exceptional
    frame['label_status'] = 'resolved'
    frame.loc[~continuous, 'label_status'] = 'missing_session_prices'
    frame.loc[continuous & ~frame.entry_bar_valid, 'label_status'] = 'entry_price_unavailable'
    frame.loc[continuous & frame.entry_bar_valid & ~frame.exit_bar_valid, 'label_status'] = 'exit_price_unavailable'
    frame.loc[continuous & frame.entry_bar_valid & frame.exit_bar_valid & exceptional,
              'label_status'] = 'price_discontinuity_requires_review'
    frame.loc[frame.expected_target_date.isna(), 'label_status'] = 'awaiting_future_sessions'
    resolved = frame.label_status.eq('resolved') & frame.label_available_date.le(cutoff)
    frame['target_return'] = (frame.future_close / frame.entry_open.where(frame.entry_open.gt(0)) - 1).where(resolved)
    frame['net_return_proxy'] = frame.target_return - cost
    frame['target'] = frame.net_return_proxy.gt(0).astype(float).where(resolved)
    frame['same_close_return_reference'] = frame.future_close / frame.close - 1
    eligible = (np.isfinite(frame[COLUMNS]).all(axis=1) & frame.close.gt(0)
                & frame.volume.gt(0) & frame.volume_ratio_20d.gt(0))
    if candidate_keys is not None:
        # Only grading previously frozen candidates may bypass current eligibility;
        # a revised historical input must not remove an originally issued call.
        keys = candidate_keys[['stock_code', 'signal_date']].copy()
        if keys.duplicated().any():
            raise ValueError('Frozen candidate keys must be unique.')
        eligible = pd.MultiIndex.from_frame(frame[['stock_code', 'signal_date']]).isin(pd.MultiIndex.from_frame(keys))
    result = frame[eligible].copy().reset_index(drop=True)
    metadata = {
        'target_version': TARGET_VERSION, 'horizon_sessions': horizon, 'cost_assumption': cost,
        'target_definition': 'close_on_fifth_session / next_session_open - 1 > cost',
        'execution_note': 'Hypothetical next-open entry / fifth-close exit; not guaranteed fills. '
                          'Fixed round-trip cost does not model queueing, taxes by product, impact or delisting proceeds.',
        'calendar_note': 'Union of observed universe dates, not an authoritative exchange calendar.',
        'discontinuity_rule': 'Absolute one-session close change above 30.5% inside holding interval, '
                              'or entry intraday change above 30.5%, requires review. Not proof of error.',
        'input_candidates': len(result), 'resolved_candidates': int(result.target.notna().sum()),
        'label_status_counts': {str(k): int(v) for k, v in result.label_status.value_counts().items()},
        'universe_note': 'Current observed universe and retrospectively adjusted prices; survivorship bias remains.',
    }
    return result, metadata
