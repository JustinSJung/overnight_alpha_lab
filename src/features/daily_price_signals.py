"""
Build daily price signals from normalized price files.

Input:
data/raw/price_STOCK_START_END.csv

Output:
data/processed/daily_price_signals_YYYYMMDD.csv
"""

from datetime import datetime
from pathlib import Path

import pandas as pd


RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")


def normalize_stock_code(value) -> str:
    if value is None or pd.isna(value):
        return ""

    try:
        return str(int(float(value))).zfill(6)
    except Exception:
        return str(value).strip().zfill(6)


def safe_float(value, default=0.0) -> float:
    try:
        if pd.isna(value):
            return default
        return float(value)
    except Exception:
        return default


def latest_price_files() -> list[Path]:
    latest_by_stock: dict[str, Path] = {}

    for path in sorted(RAW_DIR.glob("price_*.csv")):
        parts = path.name.split("_")
        if len(parts) < 4:
            continue
        stock_code = normalize_stock_code(parts[1])
        if stock_code:
            latest_by_stock[stock_code] = path

    return sorted(latest_by_stock.values())


def normalize_price_df(df: pd.DataFrame) -> pd.DataFrame:
    rename_map = {
        "날짜": "date",
        "시가": "open",
        "고가": "high",
        "저가": "low",
        "종가": "close",
        "거래량": "volume",
        "거래대금": "trading_value",
        "등락률": "change_rate",
    }
    df = df.rename(columns=rename_map).copy()

    for column in ["stock_code", "date", "open", "high", "low", "close", "volume"]:
        if column not in df.columns:
            df[column] = pd.NA

    df["stock_code"] = df["stock_code"].apply(normalize_stock_code)
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    for column in ["open", "high", "low", "close", "volume", "trading_value", "change_rate"]:
        if column in df.columns:
            df[column] = pd.to_numeric(df[column], errors="coerce")

    df = df.dropna(subset=["stock_code", "date", "close"])
    return df.sort_values("date")


def calculate_signal(price_df: pd.DataFrame, source_file: Path) -> dict:
    df = normalize_price_df(price_df)

    if len(df) < 20:
        return {}

    latest = df.iloc[-1]
    previous = df.iloc[-2]
    close = safe_float(latest["close"])
    previous_close = safe_float(previous["close"])

    returns = df["close"].pct_change()
    volume = df["volume"]
    avg_volume_20 = volume.tail(20).mean()

    ma5 = df["close"].tail(5).mean()
    ma20 = df["close"].tail(20).mean()
    high_20 = df["high"].tail(20).max()
    low_20 = df["low"].tail(20).min()
    return_1d = (close - previous_close) / previous_close if previous_close else 0.0
    return_5d = close / df["close"].iloc[-6] - 1 if len(df) >= 6 else 0.0
    return_20d = close / df["close"].iloc[-21] - 1 if len(df) >= 21 else 0.0
    volatility_20d = returns.tail(20).std()
    volume_ratio_20d = safe_float(latest["volume"]) / avg_volume_20 if avg_volume_20 else 0.0

    breakout_score = 0
    if high_20 and close >= high_20 * 0.98:
        breakout_score += 2
    if ma20 and ma5 > ma20:
        breakout_score += 1
    if volume_ratio_20d >= 1.5:
        breakout_score += 1
    if return_5d > 0:
        breakout_score += 1

    if breakout_score >= 4:
        signal_label = "strong_price_momentum"
    elif breakout_score >= 2:
        signal_label = "price_momentum"
    elif return_5d < -0.05 and close <= low_20 * 1.05:
        signal_label = "price_weakness"
    else:
        signal_label = "neutral"

    price_source = latest.get("price_source", "unknown")

    return {
        "stock_code": normalize_stock_code(latest["stock_code"]),
        "signal_date": latest["date"].strftime("%Y-%m-%d"),
        "close": round(close, 4),
        "return_1d": round(return_1d, 4),
        "return_5d": round(return_5d, 4),
        "return_20d": round(return_20d, 4),
        "ma5": round(safe_float(ma5), 4),
        "ma20": round(safe_float(ma20), 4),
        "volume_ratio_20d": round(safe_float(volume_ratio_20d), 4),
        "volatility_20d": round(safe_float(volatility_20d), 4),
        "breakout_score": breakout_score,
        "signal_label": signal_label,
        "price_source": price_source,
        "source_file": str(source_file),
    }


def main():
    print("Building daily price signals...")
    files = latest_price_files()

    if not files:
        print("No price files found. Daily price signal generation skipped.")
        return

    rows = []

    for path in files:
        try:
            df = pd.read_csv(path)
            signal = calculate_signal(df, path)
        except Exception as error:
            print(f"Price signal skipped for {path}: {error}")
            continue

        if signal:
            rows.append(signal)

    if not rows:
        print("No daily price signals generated.")
        return

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    today = datetime.today().strftime("%Y%m%d")
    output_path = PROCESSED_DIR / f"daily_price_signals_{today}.csv"
    signal_df = pd.DataFrame(rows).sort_values(
        ["breakout_score", "return_5d", "volume_ratio_20d"],
        ascending=[False, False, False],
    )
    signal_df.to_csv(output_path, index=False, encoding="utf-8-sig")

    print(f"Saved {len(signal_df)} daily price signals: {output_path}")


if __name__ == "__main__":
    main()
