"""
Market-adjusted feature builder.

This script joins advanced error notes with market index/proxy data
and calculates market-adjusted returns.

Inputs:
data/predictions/error_notes_YYYYMMDD.csv
data/raw/market_index_YYYYMMDD.csv
data/raw/stock_market_lookup_YYYYMMDD.csv

Output:
data/processed/market_adjusted_features_YYYYMMDD.csv
"""

import os
from datetime import datetime

import pandas as pd


PREDICTIONS_DIR = "data/predictions"
RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"


def get_latest_file(directory: str, prefix: str, suffix: str = ".csv"):
    """
    Find latest file by prefix and suffix.
    """

    if not os.path.exists(directory):
        return None

    files = [
        file for file in os.listdir(directory)
        if file.startswith(prefix) and file.endswith(suffix)
    ]

    if not files:
        return None

    files.sort(reverse=True)
    return os.path.join(directory, files[0])


def normalize_stock_code(value) -> str:
    """
    Normalize stock code to 6 digits.
    """

    if pd.isna(value):
        return ""

    try:
        return str(int(float(value))).zfill(6)
    except Exception:
        return str(value).strip().zfill(6)


def load_latest_error_notes():
    """
    Load latest error notes.
    """

    path = get_latest_file(PREDICTIONS_DIR, "error_notes_")

    if path is None:
        return pd.DataFrame(), ""

    df = pd.read_csv(path)

    if "stock_code" in df.columns:
        df["stock_code"] = df["stock_code"].apply(normalize_stock_code)

    return df, path


def load_latest_market_index():
    """
    Load latest market index file.
    """

    path = get_latest_file(RAW_DIR, "market_index_")

    if path is None:
        return pd.DataFrame(), ""

    df = pd.read_csv(path)

    return df, path


def load_latest_stock_market_lookup():
    """
    Load latest stock market lookup file.
    """

    path = get_latest_file(RAW_DIR, "stock_market_lookup_")

    if path is None:
        return pd.DataFrame(), ""

    df = pd.read_csv(path)

    if "stock_code" in df.columns:
        df["stock_code"] = df["stock_code"].apply(normalize_stock_code)

    return df, path


def build_index_returns(index_df: pd.DataFrame) -> pd.DataFrame:
    """
    Build next-day index return table.
    """

    if index_df.empty:
        return pd.DataFrame()

    required_columns = [
        "date",
        "index_name",
        "open",
        "close",
    ]

    for col in required_columns:
        if col not in index_df.columns:
            return pd.DataFrame()

    df = index_df.copy()

    df["date"] = pd.to_datetime(df["date"])
    df["open"] = pd.to_numeric(df["open"], errors="coerce")
    df["close"] = pd.to_numeric(df["close"], errors="coerce")

    if "source_type" not in df.columns:
        df["source_type"] = "unknown"

    if "proxy_name" not in df.columns:
        df["proxy_name"] = ""

    result_frames = []

    for index_name, group in df.groupby("index_name"):
        group = group.sort_values("date").copy()

        group["next_market_date"] = group["date"].shift(-1)
        group["next_market_open"] = group["open"].shift(-1)
        group["next_market_close"] = group["close"].shift(-1)

        group["market_next_open_return"] = (
            group["next_market_open"] - group["close"]
        ) / group["close"]

        group["market_next_close_return"] = (
            group["next_market_close"] - group["close"]
        ) / group["close"]

        group["event_date"] = group["date"].dt.strftime("%Y-%m-%d")
        group["next_market_date"] = group["next_market_date"].dt.strftime("%Y-%m-%d")

        result_frames.append(
            group[
                [
                    "event_date",
                    "index_name",
                    "source_type",
                    "proxy_name",
                    "next_market_date",
                    "market_next_open_return",
                    "market_next_close_return",
                ]
            ]
        )

    if not result_frames:
        return pd.DataFrame()

    return pd.concat(result_frames, ignore_index=True)


def add_market_group(
    error_notes_df: pd.DataFrame,
    lookup_df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Add market group to error notes using real KOSPI/KOSDAQ ticker lookup.
    """

    df = error_notes_df.copy()

    if "stock_code" not in df.columns:
        df["stock_code"] = ""

    df["stock_code"] = df["stock_code"].apply(normalize_stock_code)

    if lookup_df.empty:
        df["market_group"] = "UNKNOWN"
        df["market_group_source"] = "missing_lookup"
        return df

    lookup_cols = [
        col for col in ["stock_code", "market_group"]
        if col in lookup_df.columns
    ]

    if "stock_code" not in lookup_cols or "market_group" not in lookup_cols:
        df["market_group"] = "UNKNOWN"
        df["market_group_source"] = "invalid_lookup"
        return df

    lookup = lookup_df[lookup_cols].drop_duplicates(subset=["stock_code"])

    merged_df = df.merge(
        lookup,
        on="stock_code",
        how="left",
    )

    merged_df["market_group"] = merged_df["market_group"].fillna("UNKNOWN")
    merged_df["market_group_source"] = merged_df["market_group"].apply(
        lambda value: "pykrx_lookup" if value != "UNKNOWN" else "not_found"
    )

    return merged_df


def build_market_adjusted_features(
    error_notes_df: pd.DataFrame,
    index_returns_df: pd.DataFrame,
    lookup_df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Join error notes with market returns and calculate excess returns.
    """

    if error_notes_df.empty:
        return pd.DataFrame()

    df = add_market_group(error_notes_df, lookup_df)

    if "event_date" not in df.columns:
        return pd.DataFrame()

    df["event_date"] = pd.to_datetime(df["event_date"]).dt.strftime("%Y-%m-%d")

    if index_returns_df.empty:
        df["market_source_type"] = pd.NA
        df["market_proxy_name"] = pd.NA
        df["market_next_open_return"] = pd.NA
        df["market_next_close_return"] = pd.NA
        df["market_adjusted_next_open_return"] = pd.NA
        df["market_adjusted_next_close_return"] = pd.NA
        return df

    market_df = index_returns_df.rename(
        columns={
            "index_name": "market_group",
            "source_type": "market_source_type",
            "proxy_name": "market_proxy_name",
        }
    )

    merged_df = df.merge(
        market_df,
        on=["event_date", "market_group"],
        how="left",
    )

    numeric_columns = [
        "next_open_return",
        "next_close_return",
        "market_next_open_return",
        "market_next_close_return",
    ]

    for col in numeric_columns:
        if col not in merged_df.columns:
            merged_df[col] = pd.NA

        merged_df[col] = pd.to_numeric(
            merged_df[col],
            errors="coerce",
        )

    merged_df["market_adjusted_next_open_return"] = (
        merged_df["next_open_return"]
        - merged_df["market_next_open_return"]
    )

    merged_df["market_adjusted_next_close_return"] = (
        merged_df["next_close_return"]
        - merged_df["market_next_close_return"]
    )

    return merged_df


def save_features(df: pd.DataFrame) -> str:
    """
    Save market-adjusted feature file.
    """

    os.makedirs(PROCESSED_DIR, exist_ok=True)

    today = datetime.today().strftime("%Y%m%d")
    output_path = os.path.join(
        PROCESSED_DIR,
        f"market_adjusted_features_{today}.csv",
    )

    df.to_csv(output_path, index=False, encoding="utf-8-sig")

    return output_path


def main():
    print("Building market-adjusted features...")

    error_notes_df, error_notes_path = load_latest_error_notes()
    index_df, index_path = load_latest_market_index()
    lookup_df, lookup_path = load_latest_stock_market_lookup()

    print(f"Latest error notes: {error_notes_path if error_notes_path else 'Not found'}")
    print(f"Latest market index: {index_path if index_path else 'Not found'}")
    print(f"Latest stock market lookup: {lookup_path if lookup_path else 'Not found'}")

    index_returns_df = build_index_returns(index_df)

    result_df = build_market_adjusted_features(
        error_notes_df,
        index_returns_df,
        lookup_df,
    )

    if result_df.empty:
        print("No market-adjusted features generated.")
        return

    output_path = save_features(result_df)

    print(f"Market-adjusted features saved to: {output_path}")
    print(f"Rows: {len(result_df)}")

    columns_to_show = [
        "event_date",
        "stock_code",
        "corp_name",
        "market_group",
        "market_group_source",
        "market_source_type",
        "market_proxy_name",
        "next_close_return",
        "market_next_close_return",
        "market_adjusted_next_close_return",
    ]

    available_columns = [
        col for col in columns_to_show
        if col in result_df.columns
    ]

    print(result_df[available_columns].head(10))


if __name__ == "__main__":
    main()
