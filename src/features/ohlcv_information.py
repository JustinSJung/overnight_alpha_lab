"""Causal OHLCV inputs not present in the initial nine-feature price model."""
import numpy as np
import pandas as pd

OHLCV_FEATURES = [
    'overnight_gap', 'intraday_return', 'intraday_range', 'close_position',
    'downside_volatility_20d', 'up_day_fraction_20d', 'volume_trend_5_20',
    'log_traded_value_proxy_20d', 'range_mean_20d', 'gap_volatility_20d',
]


def add_ohlcv_information(snapshots):
    if snapshots.duplicated(['stock_code', 'signal_date']).any():
        raise ValueError('Duplicate stock/date OHLCV inputs.')
    parts = []
    for _, frame in snapshots.groupby('stock_code', sort=False):
        frame = frame.sort_values('signal_date').copy()
        close, volume = frame.close, frame.volume
        previous = close.shift(1)
        valid = (frame.open.gt(0) & frame.low.gt(0) & frame.high.ge(frame[['open', 'close']].max(axis=1))
                 & frame.low.le(frame[['open', 'close']].min(axis=1)))
        inactive = volume.eq(0)
        gap = (frame.open / previous - 1).where(valid, 0.0).where(valid | inactive)
        ranges = ((frame.high - frame.low) / previous).where(valid, 0.0).where(valid | inactive)
        frame['overnight_gap'] = gap
        frame['intraday_return'] = (close / frame.open.where(frame.open.gt(0)) - 1).where(valid, 0.0).where(valid | inactive)
        frame['intraday_range'] = ranges
        spread = (frame.high - frame.low).where(lambda value: value.gt(0))
        frame['close_position'] = ((close - frame.low) / spread).fillna(.5).where(valid | inactive)
        returns = close.pct_change(fill_method=None)
        frame['downside_volatility_20d'] = returns.clip(upper=0).pow(2).rolling(20, min_periods=20).mean().pow(.5)
        frame['up_day_fraction_20d'] = returns.gt(0).astype(float).where(returns.notna()).rolling(20, min_periods=20).mean()
        mean_volume = volume.rolling(20, min_periods=20).mean().replace(0, np.nan)
        frame['volume_trend_5_20'] = volume.rolling(5, min_periods=5).mean() / mean_volume - 1
        frame['log_traded_value_proxy_20d'] = np.log1p((volume * close).rolling(20, min_periods=20).mean())
        frame['range_mean_20d'] = ranges.rolling(20, min_periods=20).mean()
        frame['gap_volatility_20d'] = gap.rolling(20, min_periods=20).std()
        frame[OHLCV_FEATURES] = frame[OHLCV_FEATURES].replace([np.inf, -np.inf], np.nan)
        parts.append(frame)
    if not parts:
        raise ValueError('No OHLCV inputs.')
    result = pd.concat(parts, ignore_index=True)
    result.attrs = snapshots.attrs.copy()
    return result
