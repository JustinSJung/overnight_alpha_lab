"""
Korean stock price data collector.

This script collects daily OHLCV stock price data
and saves it under data/raw.

Usage:
    python src/crawler/price_collector.py 005930
"""

import os
import sys
from datetime import datetime, timedelta

import pandas as pd
from pykrx import stock


def normalize_stock_code(value) -> str:
    """
    Normalize stock code to 6-digit string.
    """

    if value is None:
        return ""

    return str(value).strip().zfill(6)


def get_date_range(days: int = 30) -> tuple[str, str]:
    """
    Get start and end date strings in YYYYMMDD format.
    """

    end_date = datetime.today()
    start_date = end_date - timedelta(days=days)

    return start_date.strftime("%Y%m%d"), end_date.strftime("%Y%m%d")


def collect_stock_price(
    stock_code: str,
    start_date: str,
    end_date: str,
) -> pd.DataFrame:
    """
    Collect daily OHLCV data for a Korean stock.
    """

    stock_code = normalize_stock_code(stock_code)

    df = stock.get_market_ohlcv_by_date(start_date, end_date, stock_code)

    if df.empty:
        print(f"No price data found for stock_code={stock_code}")
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

    selected_columns = [
        "stock_code",
        "date",
        "open",
        "high",
        "low",
        "close",
        "volume",
    ]

    if "trading_value" in df.columns:
        selected_columns.append("trading_value")

    if "change_rate" in df.columns:
        selected_columns.append("change_rate")

    return df[selected_columns]


def save_price_data(df: pd.DataFrame, stock_code: str, start_date: str, end_date: str) -> str:
    """
    Save price data to CSV.
    """

    output_dir = "data/raw"
    os.makedirs(output_dir, exist_ok=True)

    output_path = f"{output_dir}/price_{stock_code}_{start_date}_{end_date}.csv"
    df.to_csv(output_path, index=False, encoding="utf-8-sig")

    return output_path


def main():
    if len(sys.argv) < 2:
        print("Usage: python src/crawler/price_collector.py <stock_code>")
        print("Example: python src/crawler/price_collector.py 005930")
        return

    stock_code = normalize_stock_code(sys.argv[1])
    start_date, end_date = get_date_range(days=30)

    print(f"Collecting price data for {stock_code}")
    print(f"Period: {start_date} ~ {end_date}")

    df = collect_stock_price(stock_code, start_date, end_date)

    if df.empty:
        print("No data saved.")
        return

    output_path = save_price_data(df, stock_code, start_date, end_date)

    print(f"Collected {len(df)} rows.")
    print(f"Saved to: {output_path}")
    print()
    print(df.tail())


if __name__ == "__main__":
    main()
