"""Point-in-time features and independent forward-price labels for supervised ML."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


FEATURES = [
    "return_1d", "return_5d", "return_20d", "volume_ratio_20d",
    "volatility_20d", "breakout_score", "distance_ma5", "distance_ma20",
    "ma5_vs_ma20",
]
FEATURE_VERSION = "price_snapshot_v1"


def normalize_code(value):
    if pd.isna(value):
        return ""
    text = str(value).strip()
    if text.endswith(".0") and text[:-2].isdigit():
        text = text[:-2]
    return text.zfill(6) if text.isdigit() else text.upper()


def make_features(frame):
    """Only inputs observable at the signal close; never outcome or score columns."""
    output = pd.DataFrame(index=frame.index)
    for column in FEATURES[:6]:
        output[column] = pd.to_numeric(frame.get(column, pd.Series(np.nan, index=frame.index)), errors="coerce")
    close = pd.to_numeric(frame["close"], errors="coerce")
    ma5 = pd.to_numeric(frame["ma5"], errors="coerce").where(lambda x: x > 0)
    ma20 = pd.to_numeric(frame["ma20"], errors="coerce").where(lambda x: x > 0)
    output["distance_ma5"] = close / ma5 - 1
    output["distance_ma20"] = close / ma20 - 1
    output["ma5_vs_ma20"] = ma5 / ma20 - 1
    return output.replace([np.inf, -np.inf], np.nan)


def load_snapshots(data_root):
    """Keep the FIRST recorded stock/date observation, not retrospectively rescored rows."""
    if (Path(data_root) / 'history_manifest.json').exists():
        from src.features.completed_price_dataset import load_completed_history
        return load_completed_history(data_root)
    frames = []
    skipped = []
    paths = sorted((Path(data_root) / "data/processed").glob("daily_price_signals_*.csv"))
    for path in paths:
        try:
            frame = pd.read_csv(path, dtype={"stock_code": str})
            required = {"stock_code", "signal_date", "close", "ma5", "ma20"}
            if not required.issubset(frame.columns):
                raise ValueError("missing required price signal columns")
            frame["snapshot_date"] = pd.to_datetime(path.stem.rsplit("_", 1)[-1], format="%Y%m%d")
            frame["snapshot_file"] = path.name
            frames.append(frame)
        except (ValueError, OSError, pd.errors.ParserError) as error:
            skipped.append({"file": path.name, "error": type(error).__name__})
    if not frames:
        raise ValueError("No usable daily_price_signals snapshots found.")
    frame = pd.concat(frames, ignore_index=True)
    frame["stock_code"] = frame["stock_code"].map(normalize_code)
    frame["signal_date"] = pd.to_datetime(frame["signal_date"], errors="coerce").dt.normalize()
    frame["close"] = pd.to_numeric(frame["close"], errors="coerce")
    frame = frame.dropna(subset=["signal_date", "close"])
    frame = frame[(frame["close"] > 0) & frame["stock_code"].str.fullmatch(r"[0-9A-Z]{6}")]
    frame = frame.sort_values(["snapshot_date", "snapshot_file"], kind="stable")
    frame = frame.drop_duplicates(["stock_code", "signal_date"], keep="first")
    return frame.reset_index(drop=True), {"snapshot_files": len(paths), "skipped_files": skipped}


def build_dataset(snapshots, horizon=5, cost=0.003, as_of=None):
    if horizon < 1 or not 0 <= cost < 1:
        raise ValueError("Invalid horizon or cost.")
    frame = snapshots.copy()
    if as_of is not None:
        cutoff = pd.Timestamp(as_of).normalize()
        frame = frame[(frame["snapshot_date"] <= cutoff) & (frame["signal_date"] <= cutoff)]
    if frame.empty:
        raise ValueError("No observations available by as_of.")
    calendar = pd.DatetimeIndex(sorted(frame["signal_date"].unique()))
    frame = frame.sort_values(["stock_code", "signal_date"]).reset_index(drop=True)
    day_index = pd.Series(np.arange(len(calendar)), index=calendar)
    frame["calendar_index"] = frame["signal_date"].map(day_index)
    groups = frame.groupby("stock_code", sort=False)
    frame["target_date"] = groups["signal_date"].shift(-horizon)
    frame["label_available_date"] = groups["snapshot_date"].shift(-horizon)
    frame["future_close"] = groups["close"].shift(-horizon)
    future_index = groups["calendar_index"].shift(-horizon)
    # A missing stock quote must not silently turn five sessions into a longer horizon.
    complete_horizon = future_index.sub(frame["calendar_index"]).eq(horizon)
    frame[FEATURES] = make_features(frame)
    frame["target_return"] = frame["future_close"] / frame["close"] - 1
    frame["net_return_proxy"] = frame["target_return"] - cost
    frame["target"] = frame["net_return_proxy"].gt(0).astype(int)
    usable = (
        complete_horizon & frame["target_return"].notna()
        & frame["label_available_date"].notna()
        & frame["snapshot_date"].le(frame["signal_date"])
        & frame["target_date"].gt(frame["signal_date"])
        & frame["label_available_date"].ge(frame["target_date"])
        & frame["label_available_date"].gt(frame["signal_date"])
        & frame["volume_ratio_20d"].gt(0)
        & frame[FEATURES].notna().all(axis=1)
    )
    dataset = frame[usable].copy().reset_index(drop=True)
    if as_of is not None:
        dataset = dataset[dataset["label_available_date"] <= cutoff].copy()
    metadata = {
        "feature_version": snapshots.attrs.get('feature_version', FEATURE_VERSION), "horizon_sessions": horizon, "cost_assumption": cost,
        "unique_price_observations": len(frame), "training_rows": len(dataset),
        "signal_dates": int(dataset["signal_date"].nunique()),
        "target_definition": "close_t_plus_horizon / signal_close - 1 > cost_assumption",
        "execution_note": "Close-to-close research target; not an executable next-open trading return.",
        "universe_note": "Historical collected universe; not a survivorship-free whole-market backtest.",
    }
    if 'history_provenance' in snapshots.attrs:
        metadata['history_provenance'] = snapshots.attrs['history_provenance']
    return dataset, metadata


def temporal_partitions(dataset, calibration_start=None, test_start=None):
    days = np.array(sorted(dataset["signal_date"].unique()))
    if len(days) < 45:
        raise ValueError("At least 45 labeled signal dates are required for temporal validation.")
    if (calibration_start is None) != (test_start is None):
        raise ValueError('Both fixed temporal boundaries must be specified together.')
    calibration_start = pd.Timestamp(calibration_start if calibration_start is not None else days[int(len(days) * 0.60)])
    test_start = pd.Timestamp(test_start if test_start is not None else days[int(len(days) * 0.80)])
    if not pd.Timestamp(days[0]) < calibration_start < test_start <= pd.Timestamp(days[-1]):
        raise ValueError('Temporal boundaries must be ordered inside the labeled history.')
    train = dataset[(dataset["signal_date"] < calibration_start) & (dataset["label_available_date"] < calibration_start)]
    calibration = dataset[(dataset["signal_date"] >= calibration_start) & (dataset["signal_date"] < test_start) & (dataset["label_available_date"] < test_start)]
    test = dataset[dataset["signal_date"] >= test_start]
    for label, part, minimum in [("train", train, 15), ("calibration", calibration, 3), ("test", test, 8)]:
        if part["signal_date"].nunique() < minimum or part["target"].nunique() < 2:
            raise ValueError("Insufficient dates/classes in purged " + label + " partition.")
    return train.copy(), calibration.copy(), test.copy()
