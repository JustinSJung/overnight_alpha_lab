"""
Market index collector.

This script collects:
1. KOSPI / KOSDAQ market index data
2. Fallback ETF proxy data if direct index collection fails
3. Stock market group lookup table from pykrx ticker lists

Outputs:
data/raw/market_index_YYYYMMDD.csv
data/raw/stock_market_lookup_YYYYMMDD.csv
"""

import os
from datetime import datetime, timedelta

import pandas as pd
from pykrx import stock


RAW_DIR = "data/raw"


INDEX_CODES = {
    "KOSPI": "1001",
    "KOSDAQ": "2001",
}


MARKET_PROXY_TICKERS = {
    "KOSPI": {
        "ticker": "069500",
        "name": "KODEX 200",
    },
    "KOSDAQ": {
        "ticker": "229200",
        "name": "KODEX KOSDAQ 150",
    },
}


def get_date_range(days: int = 60):
    """
    Return start and end date strings in YYYYMMDD format.
    """

    end_date = datetime.today()
    start_date = end_date - timedelta(days=days)

    return start_date.strftime("%Y%m%d"), end_date.strftime("%Y%m%d")


def normalize_ohlcv_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize pykrx OHLCV columns to English names.
    """

    df = df.reset_index()

    rename_map = {
        "날짜": "date",
        "시가": "open",
        "고가": "high",
        "저가": "low",
        "종가": "close",
        "거래량": "volume",
        "거래대금": "trading_value",
        "상장시가총액": "market_cap",
        "등락률": "change_rate",
    }

    df = df.rename(columns=rename_map)

    if "date" not in df.columns:
        df = df.rename(columns={df.columns[0]: "date"})

    required_columns = [
        "date",
        "open",
        "high",
        "low",
        "close",
        "volume",
        "trading_value",
    ]

    for col in required_columns:
        if col not in df.columns:
            df[col] = pd.NA

    df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

    return df


def collect_direct_index_data(days: int = 60) -> pd.DataFrame:
    """
    Try to collect actual KOSPI / KOSDAQ index data.
    """

    start_date, end_date = get_date_range(days)

    frames = []

    for index_name, index_code in INDEX_CODES.items():
        try:
            df = stock.get_index_ohlcv_by_date(
                start_date,
                end_date,
                index_code,
            )

            if df.empty:
                print(f"No direct index data for {index_name}")
                continue

            df = normalize_ohlcv_columns(df)

            df["index_name"] = index_name
            df["index_code"] = index_code
            df["source_type"] = "direct_index"
            df["proxy_name"] = ""

            output_columns = [
                "date",
                "index_name",
                "index_code",
                "proxy_name",
                "source_type",
                "open",
                "high",
                "low",
                "close",
                "volume",
                "trading_value",
            ]

            frames.append(df[output_columns])

        except Exception as error:
            print(f"Direct index collection failed for {index_name}: {error}")

    if not frames:
        return pd.DataFrame()

    return pd.concat(frames, ignore_index=True)


def collect_proxy_index_data(days: int = 60) -> pd.DataFrame:
    """
    Collect ETF proxy data if direct index collection fails.
    """

    start_date, end_date = get_date_range(days)

    frames = []

    for index_name, info in MARKET_PROXY_TICKERS.items():
        ticker = info["ticker"]
        proxy_name = info["name"]

        try:
            df = stock.get_market_ohlcv_by_date(
                start_date,
                end_date,
                ticker,
            )

            if df.empty:
                print(f"No proxy data for {index_name}: {ticker}")
                continue

            df = normalize_ohlcv_columns(df)

            df["index_name"] = index_name
            df["index_code"] = ticker
            df["source_type"] = "etf_proxy"
            df["proxy_name"] = proxy_name

            output_columns = [
                "date",
                "index_name",
                "index_code",
                "proxy_name",
                "source_type",
                "open",
                "high",
                "low",
                "close",
                "volume",
                "trading_value",
            ]

            frames.append(df[output_columns])

        except Exception as error:
            print(f"Proxy collection failed for {index_name} {ticker}: {error}")

    if not frames:
        return pd.DataFrame()

    return pd.concat(frames, ignore_index=True)


def collect_market_index_data(days: int = 60) -> pd.DataFrame:
    """
    Collect market index data with fallback.
    """

    print("Trying direct KOSPI/KOSDAQ index collection...")
    direct_df = collect_direct_index_data(days=days)

    if not direct_df.empty:
        print("Direct index collection succeeded.")
        return direct_df

    print("Direct index collection failed. Trying ETF proxy fallback...")
    proxy_df = collect_proxy_index_data(days=days)

    if not proxy_df.empty:
        print("ETF proxy fallback succeeded.")
        return proxy_df

    return pd.DataFrame()

def get_latest_error_note_stock_codes():
    """
    Get stock codes from latest error note file as fallback universe.
    """

    predictions_dir = "data/predictions"

    if not os.path.exists(predictions_dir):
        return []

    files = [
        file for file in os.listdir(predictions_dir)
        if file.startswith("error_notes_") and file.endswith(".csv")
    ]

    if not files:
        return []

    files.sort(reverse=True)
    latest_path = os.path.join(predictions_dir, files[0])

    try:
        df = pd.read_csv(latest_path)

        if "stock_code" not in df.columns:
            return []

        codes = []

        for value in df["stock_code"].dropna().unique():
            try:
                codes.append(str(int(float(value))).zfill(6))
            except Exception:
                codes.append(str(value).strip().zfill(6))

        return sorted(set(codes))
    except Exception as error:
        print(f"Failed to read latest error notes for fallback lookup: {error}")
        return []


def estimate_market_group_from_code(stock_code: str) -> str:
    """
    Last-resort market group estimate.

    This is only used when pykrx ticker lookup fails.
    The source will be marked as heuristic_fallback.
    """

    try:
        code_num = int(stock_code)

        if code_num >= 100000:
            return "KOSDAQ"

        return "KOSPI"
    except Exception:
        return "UNKNOWN"


def collect_stock_market_lookup() -> pd.DataFrame:
    """
    Collect stock ticker market group lookup table.

    Priority:
    1. pykrx KOSPI/KOSDAQ ticker lists
    2. fallback from latest error_notes stock codes
    3. heuristic market group estimate with source label
    """

    today = datetime.today()
    candidate_dates = [
        (today - timedelta(days=offset)).strftime("%Y%m%d")
        for offset in range(0, 15)
    ]

    frames = []

    market_map = {
        "KOSPI": "KOSPI",
        "KOSDAQ": "KOSDAQ",
    }

    for date_str in candidate_dates:
        for pykrx_market, market_group in market_map.items():
            try:
                tickers = stock.get_market_ticker_list(
                    date=date_str,
                    market=pykrx_market,
                )

                if not tickers:
                    continue

                rows = []

                for ticker in tickers:
                    try:
                        corp_name = stock.get_market_ticker_name(ticker)
                    except Exception:
                        corp_name = ""

                    rows.append(
                        {
                            "stock_code": str(ticker).zfill(6),
                            "corp_name": corp_name,
                            "market_group": market_group,
                            "lookup_source": "pykrx_ticker_list",
                            "lookup_date": date_str,
                        }
                    )

                if rows:
                    frames.append(pd.DataFrame(rows))

            except Exception as error:
                print(
                    f"Failed ticker lookup for {pykrx_market} on {date_str}: {error}"
                )

        if frames:
            break

    if frames:
        lookup_df = pd.concat(frames, ignore_index=True)
        lookup_df = lookup_df.drop_duplicates(subset=["stock_code"], keep="first")
        return lookup_df

    print("pykrx ticker list lookup failed. Trying fallback from latest error notes...")

    fallback_codes = get_latest_error_note_stock_codes()

    if not fallback_codes:
        return pd.DataFrame()

    fallback_rows = []

    for stock_code in fallback_codes:
        try:
            corp_name = stock.get_market_ticker_name(stock_code)
        except Exception:
            corp_name = ""

        market_group = estimate_market_group_from_code(stock_code)

        fallback_rows.append(
            {
                "stock_code": stock_code,
                "corp_name": corp_name,
                "market_group": market_group,
                "lookup_source": "heuristic_fallback",
                "lookup_date": datetime.today().strftime("%Y%m%d"),
            }
        )

    return pd.DataFrame(fallback_rows)

def save_dataframe(df: pd.DataFrame, prefix: str) -> str:
    """
    Save dataframe to data/raw.
    """

    os.makedirs(RAW_DIR, exist_ok=True)

    today = datetime.today().strftime("%Y%m%d")
    output_path = os.path.join(
        RAW_DIR,
        f"{prefix}_{today}.csv",
    )

    df.to_csv(output_path, index=False, encoding="utf-8-sig")

    return output_path


def main():
    print("Collecting market index data...")

    index_df = collect_market_index_data(days=60)

    if index_df.empty:
        print("No market index or proxy data collected.")
    else:
        index_path = save_dataframe(index_df, "market_index")
        print(f"Market index data saved to: {index_path}")
        print(f"Rows: {len(index_df)}")
        print(index_df.tail(10))

    print("")
    print("Collecting stock market lookup...")

    lookup_df = collect_stock_market_lookup()

    if lookup_df.empty:
        print("No stock market lookup collected.")
    else:
        lookup_path = save_dataframe(lookup_df, "stock_market_lookup")
        print(f"Stock market lookup saved to: {lookup_path}")
        print(f"Rows: {len(lookup_df)}")
        print(lookup_df.head(10))


if __name__ == "__main__":
    main()
