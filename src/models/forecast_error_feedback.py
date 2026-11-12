"""Learn conservative probability corrections from resolved, previously issued forecasts."""
import numpy as np
import pandas as pd

from src.features.next_open_dataset import TARGET_VERSION


MIN_DATES = 5
LOOKBACK_DATES = 60
PROB = 'probability_above_cost'


def prepare(rows, cutoff):
    f = rows.copy()
    for col in ('signal_date', 'label_available_date'):
        f[col] = pd.to_datetime(f[col])
    observed = f.target.notna()
    if (f.empty or f.prediction_id.isna().any() or f.prediction_id.duplicated().any()
            or f.stock_code.isna().any() or f.signal_date.isna().any()
            or f.duplicated(['signal_date', 'stock_code']).any()
            or f.signal_date.gt(cutoff).any() or not f.target_version.eq(TARGET_VERSION).all()
            or not f.horizon_sessions.eq(5).all() or not f.cost_assumption.eq(.003).all()
            or not f[[PROB, 'validation_base_rate']].apply(lambda s: s.between(0, 1)).all().all()
            or not f.loc[observed, 'target'].isin([0, 1]).all()
            or not f.loc[observed, 'label_available_date'].gt(f.loc[observed, 'signal_date']).all()
            or f.loc[observed, 'label_available_date'].gt(cutoff).any()):
        raise ValueError('Invalid original forecast or unavailable outcome.')
    # Rank the entire issued pool before looking at outcomes. Tied forecasts share a rank.
    day = f.groupby('signal_date')[PROB]
    percentile = (day.rank(method='average') - .5) / day.transform('size')
    f['rank_bin'] = (percentile * 5).astype(int)
    return f


def fit_feedback(frame, origin):
    known = frame.target.notna() & frame.label_available_date.le(origin) & frame.signal_date.lt(origin)
    coverage = known.groupby(frame.signal_date).agg(['mean', 'size'])
    dates = coverage.index[(coverage['mean'] >= .95) & (coverage['size'] >= 100)][-LOOKBACK_DATES:]
    train = frame.loc[known & frame.signal_date.isin(dates)].copy()
    state = dict(dates=len(dates), cases=len(train), ready=len(dates) >= MIN_DATES,
                 latest_label=None if train.empty else str(train.label_available_date.max().date()),
                 offset=0., ranks={}, stocks={})
    if not state['ready']:
        return state
    # Treat a trading day, not each correlated stock, as a unit of market-level evidence.
    error = train.target - train[PROB]
    daily = error.groupby(train.signal_date)
    state['offset'] = float(daily.mean().sum() / (len(dates) + 20))
    centered = error - daily.transform('mean')
    by_band = centered.groupby([train.signal_date, train.rank_bin])
    band_days = by_band.mean().groupby(level='rank_bin')
    state['ranks'] = (band_days.sum() / (band_days.count() + 20)).to_dict()
    # Only repeated stock-specific misses beyond the day's rank group affect its ordering.
    by_stock = (centered - by_band.transform('mean')).groupby(train.stock_code)
    count = by_stock.count()
    state['stocks'] = (by_stock.sum() / (count + 40))[count >= MIN_DATES].to_dict()
    return state


def predict_feedback(frame, state):
    return (frame[PROB] + state['offset'] + frame.rank_bin.map(state['ranks']).fillna(0.)
            + frame.stock_code.map(state['stocks']).fillna(0.)).clip(0., 1.)


def band_summary(group):
    obs = group.dropna(subset=['target'])
    return dict(issued=len(group), resolved=len(obs), dates=int(obs.signal_date.nunique()),
                mean_prediction=float(obs[PROB].mean()) if len(obs) else None,
                hit_rate=float(obs.target.mean()) if len(obs) else None)


def describe_base(frame):
    # Calibration compares probability with frequency; ranking compares groups within each day.
    bands = pd.cut(frame[PROB], [0, .3, .4, .5, .6, 1], include_lowest=True)
    by_date = []
    for day, group in frame.groupby('signal_date'):
        low, high = (group[group.rank_bin.eq(i)] for i in (0, 4))
        by_date.append(dict(date=str(day.date()), all=band_summary(group),
                            top=band_summary(high), bottom=band_summary(low),
                            top_minus_bottom=float(high.target.mean() - low.target.mean())
                            if high.target.count() and low.target.count() else None))
    spreads = [r['top_minus_bottom'] for r in by_date if r['top_minus_bottom'] is not None]
    return dict(probability_bands={str(k): band_summary(v) for k, v in frame.groupby(bands, observed=False)},
                rank_by_date=by_date, mean_daily_top_minus_bottom=float(np.mean(spreads)) if spreads else None)
