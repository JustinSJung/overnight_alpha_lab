"""
KIS-first daily price collector with pykrx fallback.

Outputs normalized price files compatible with the existing project:
data/raw/price_STOCK_START_END.csv
data/raw/kis_quotes_YYYYMMDD.csv
"""

import os
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

try:
    from pykrx import stock
except Exception:  # pragma: no cover - optional runtime dependency guard
    stock = None

from src.crawler.kis_client import KISClient, KISCredentialsMissing, normalize_stock_code


RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")
DEFAULT_STOCK_CODES = [
    "005930",
    "000660",
    "373220",
    "207940",
    "005380",
    "000270",
    "035420",
    "035720",
    "068270",
    "051910",
]


def date_range(days: int = 120) -> tuple[str, str]:
    end_date = datetime.today()
    start_date = end_date - timedelta(days=days)
    return start_date.strftime("%Y%m%d"), end_date.strftime("%Y%m%d")


def latest_file(directory: Path, pattern: str):
    files = sorted(directory.glob(pattern))
    if not files:
        return None
    return files[-1]


def load_stock_codes_from_csv(path: Path) -> list[str]:
    try:
        df = pd.read_csv(path)
    except Exception:
        return []

    if "stock_code" not in df.columns:
        return []

    return [
        code
        for code in df["stock_code"].apply(normalize_stock_code).dropna().unique().tolist()
        if code
    ]


def load_stock_universe() -> list[str]:
    codes: list[str] = []

    watchlist_path = PROCESSED_DIR / "price_watchlist.csv"
    if watchlist_path.exists():
        codes.extend(load_stock_codes_from_csv(watchlist_path))

    for pattern in [
        "price_based_candidates_*.csv",
        "ml_dataset_*.csv",
        "selected_key_events_*.csv",
        "social_attention_features_*.csv",
    ]:
        path = latest_file(PROCESSED_DIR, pattern)
        if path:
            codes.extend(load_stock_codes_from_csv(path))

    if not codes:
        codes.extend(DEFAULT_STOCK_CODES)

    normalized = []
    seen = set()
    for code in codes:
        code = normalize_stock_code(code)
        if code and code not in seen:
            normalized.append(code)
            seen.add(code)

    return normalized


def collect_with_pykrx(stock_code: str, start_date: str, end_date: str) -> pd.DataFrame:
    if stock is None:
        return pd.DataFrame()

    df = stock.get_market_ohlcv_by_date(start_date, end_date, stock_code)
    if df.empty:
        return pd.DataFrame()

    df = df.reset_index()
    df = df.rename(
        columns={
            "날짜": "date",
            "시가": "open",
            "고가": "high",
            "저가": "low",
            "종가": "close",
            "거래량": "volume",
            "거래대금": "trading_value",
            "등락률": "change_rate",
        }
    )
    df["stock_code"] = stock_code
    df["price_source"] = "pykrx"

    selected_columns = [
        "stock_code",
        "date",
        "open",
        "high",
        "low",
        "close",
        "volume",
        "trading_value",
        "change_rate",
        "price_source",
    ]

    for column in selected_columns:
        if column not in df.columns:
            df[column] = pd.NA

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date"]).sort_values("date")
    df["date"] = df["date"].dt.strftime("%Y-%m-%d")
    return df[selected_columns]


def save_price_data(df: pd.DataFrame, stock_code: str, start_date: str, end_date: str) -> str:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    output_path = RAW_DIR / f"price_{stock_code}_{start_date}_{end_date}.csv"
    df.to_csv(output_path, index=False, encoding="utf-8-sig")
    return str(output_path)


def save_quotes(quotes: list[dict]) -> str:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    today = datetime.today().strftime("%Y%m%d")
    output_path = RAW_DIR / f"kis_quotes_{today}.csv"
    pd.DataFrame(quotes).to_csv(output_path, index=False, encoding="utf-8-sig")
    return str(output_path)


def collect_for_stock(
    stock_code: str,
    start_date: str,
    end_date: str,
    kis_client: Optional[KISClient],
) -> tuple[pd.DataFrame, Optional[dict]]:
    stock_code = normalize_stock_code(stock_code)
    quote = None

    if kis_client is not None:
        try:
            df = kis_client.get_daily_ohlcv(stock_code, start_date, end_date)
            try:
                quote = kis_client.get_current_quote(stock_code)
            except Exception as error:
                print(f"KIS quote skipped for {stock_code}: {error}")

            if not df.empty:
                return df, quote
        except Exception as error:
            print(f"KIS price collection failed for {stock_code}: {error}")
            print(f"Falling back to pykrx for {stock_code}.")

    fallback_df = collect_with_pykrx(stock_code, start_date, end_date)
    return fallback_df, quote


def main():
    cli_codes = [normalize_stock_code(value) for value in sys.argv[1:]]
    stock_codes = [code for code in cli_codes if code] or load_stock_universe()
    start_date, end_date = date_range(days=120)

    print("Collecting daily price data with KIS primary and pykrx fallback.")
    print(f"Stock count: {len(stock_codes)}")
    print(f"Period: {start_date} ~ {end_date}")

    try:
        kis_client = KISClient()
        print("KIS credentials found. KIS quotation endpoints enabled.")
    except KISCredentialsMissing:
        kis_client = None
        print("KIS credentials missing. Skipping KIS and using pykrx fallback.")
    except Exception as error:
        kis_client = None
        print(f"KIS client initialization failed: {error}")
        print("Using pykrx fallback.")

    saved_count = 0
    quotes = []

    for stock_code in stock_codes:
        try:
            df, quote = collect_for_stock(stock_code, start_date, end_date, kis_client)
        except Exception as error:
            print(f"Price collection skipped for {stock_code}: {error}")
            continue

        if df.empty:
            print(f"No price data collected for {stock_code}.")
            continue

        output_path = save_price_data(df, stock_code, start_date, end_date)
        saved_count += 1
        print(f"Saved {len(df)} rows for {stock_code}: {output_path}")

        if quote:
            quotes.append(quote)

    if quotes:
        quote_path = save_quotes(quotes)
        print(f"Saved {len(quotes)} KIS quotes: {quote_path}")

    if saved_count == 0:
        print("No price files were saved.")
        return

    print(f"Price collection completed. Saved files: {saved_count}")


if __name__ == "__main__":
    main()
