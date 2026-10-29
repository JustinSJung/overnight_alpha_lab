"""Causal, completed-close universe proxies; these are not exchange index returns."""
from __future__ import annotations

import numpy as np
import pandas as pd

MARKET_FEATURE_VERSION = 'price_market_context_v1'
MARKET_FEATURES = [
    'market_return_1d', 'market_return_5d', 'market_return_20d',
    'market_volatility_20d', 'market_up_fraction', 'market_above_ma20_fraction',
    'market_dispersion_1d', 'market_volume_ratio_20d',
    'relative_return_5d', 'relative_return_20d',
]


def add_market_context(snapshots, min_stocks=100):
    if min_stocks < 2:
        raise ValueError('Market context requires at least two stocks.')
    attrs = snapshots.attrs.copy()
    frame = snapshots.copy()
    if frame.duplicated(['stock_code', 'signal_date']).any():
        raise ValueError('Market context requires unique stock/date observations.')
    numeric = ['close', 'volume', 'return_1d', 'return_5d', 'return_20d', 'ma20', 'volume_ratio_20d']
    frame[numeric] = frame[numeric].apply(pd.to_numeric, errors='coerce')
    frame['signal_date'] = pd.to_datetime(frame['signal_date']).dt.normalize()
    available = pd.to_datetime(frame['snapshot_date']).le(frame['signal_date'])
    active = frame[available & frame['volume'].gt(0) & frame['close'].gt(0)
                   & np.isfinite(frame['return_1d'])].copy()
    active['up'] = active['return_1d'].gt(0).astype(float)
    active['above_ma20'] = (active['close'] > active['ma20']).astype(float).where(active['ma20'].gt(0))
    daily = active.groupby('signal_date').agg(
        market_return_1d=('return_1d', 'mean'), market_up_fraction=('up', 'mean'),
        market_dispersion_1d=('return_1d', 'std'),
        market_above_ma20_fraction=('above_ma20', 'mean'),
        market_volume_ratio_20d=('volume_ratio_20d', 'median'),
        market_context_stocks=('stock_code', 'nunique'),
        ma20_stocks=('above_ma20', 'count'), volume_stocks=('volume_ratio_20d', 'count'),
    )
    calendar = pd.DatetimeIndex(sorted(frame['signal_date'].unique()), name='signal_date')
    daily = daily.reindex(calendar)
    daily.loc[daily['market_context_stocks'].fillna(0) < min_stocks, list(daily.columns[:5])] = np.nan
    daily.loc[daily['ma20_stocks'].fillna(0) < min_stocks, 'market_above_ma20_fraction'] = np.nan
    daily.loc[daily['volume_stocks'].fillna(0) < min_stocks, 'market_volume_ratio_20d'] = np.nan
    log_return = np.log1p(daily['market_return_1d'].where(daily['market_return_1d'] > -1))
    for days in [5, 20]:
        daily[f'market_return_{days}d'] = np.expm1(log_return.rolling(days, min_periods=days).sum())
    daily['market_volatility_20d'] = daily['market_return_1d'].rolling(20, min_periods=20).std()
    daily = daily.drop(columns=['ma20_stocks', 'volume_stocks']).reset_index()
    frame = frame.merge(daily, on='signal_date', how='left', validate='many_to_one')
    for days in [5, 20]:
        frame[f'relative_return_{days}d'] = frame[f'return_{days}d'] - frame[f'market_return_{days}d']
    frame.attrs = attrs
    frame.attrs['feature_version'] = MARKET_FEATURE_VERSION
    frame.attrs['market_context'] = {
        'min_stocks': min_stocks, 'features': MARKET_FEATURES,
        'definition': 'Same-day active current-universe equal-weight return/breadth proxy; not KOSPI/KOSDAQ.',
        'availability': 'Completed signal-close observations only; no future returns or labels.',
        'limitations': 'Retrospective current universe; suspension/composition changes can affect the proxy.',
    }
    return frame


def model_features(frame, columns):
    from src.features.price_learning_dataset import FEATURES, make_features
    allowed = set(FEATURES + MARKET_FEATURES)
    if not columns or not set(columns).issubset(allowed) or len(set(columns)) != len(columns):
        raise ValueError('Unsupported price-model feature schema.')
    output = make_features(frame)
    for column in columns:
        if column not in output:
            output[column] = pd.to_numeric(frame.get(column, pd.Series(np.nan, index=frame.index)), errors='coerce')
    return output[columns].replace([np.inf, -np.inf], np.nan)
