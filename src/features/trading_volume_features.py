"""
Trading volume feature builder.

This script calculates trading volume reaction features around disclosure events.

Input:
data/processed/ml_dataset_YYYYMMDD.csv
data/raw/price_STOCK_START_END.csv

Output:
data/processed/trading_volume_features_YYYYMMDD.csv
reports/daily_review/YYYY-MM-DD_trading_volume_feature_report.md
"""

import os
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd


PROCESSED_DIR = "data/processed"
RAW_DIR = "data/raw"
REPORT_DIR = "reports/daily_review"


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


def safe_float(value, default=0.0):
    """
    Convert value to float safely.
    """

    try:
        if pd.isna(value):
            return default

        return float(value)
    except Exception:
        return default


def format_number(value) -> str:
    """
    Format number safely.
    """

    try:
        if pd.isna(value):
            return "N/A"

        return f"{float(value):,.0f}"
    except Exception:
        return "N/A"


def format_ratio(value) -> str:
    """
    Format ratio safely.
    """

    try:
        if pd.isna(value):
            return "N/A"

        return f"{float(value):.2f}x"
    except Exception:
        return "N/A"


def load_latest_ml_dataset():
    """
    Load latest ML dataset.
    """

    path = get_latest_file(PROCESSED_DIR, "ml_dataset_")

    if path is None:
        return pd.DataFrame(), ""

    df = pd.read_csv(path)

    if "stock_code" in df.columns:
        df["stock_code"] = df["stock_code"].apply(normalize_stock_code)

    return df, path


def find_price_file(stock_code: str):
    """
    Find latest price file for a stock code.
    """

    files = sorted(
        Path(RAW_DIR).glob(f"price_{stock_code}_*.csv"),
        reverse=True,
    )

    if not files:
        return None

    return str(files[0])


def normalize_price_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize possible Korean/English price columns.
    """

    rename_map = {
        "날짜": "date",
        "시가": "open",
        "고가": "high",
        "저가": "low",
        "종가": "close",
        "거래량": "volume",
        "거래대금": "trading_value",
        "등락률": "change_rate",
        "Date": "date",
        "Open": "open",
        "High": "high",
        "Low": "low",
        "Close": "close",
        "Volume": "volume",
    }

    df = df.rename(columns=rename_map)

    if "date" not in df.columns:
        first_col = df.columns[0]
        df = df.rename(columns={first_col: "date"})

    for col in ["open", "high", "low", "close", "volume"]:
        if col not in df.columns:
            df[col] = pd.NA

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["volume"] = pd.to_numeric(df["volume"], errors="coerce")

    df = df.dropna(subset=["date"])
    df = df.sort_values("date").copy()

    return df


def calculate_volume_features_for_event(row) -> dict:
    """
    Calculate volume features for one event row.
    """

    stock_code = normalize_stock_code(row.get("stock_code", ""))
    event_date_raw = row.get("event_date", None)

    result = {
        "stock_code": stock_code,
        "event_date": event_date_raw,
        "price_file_found": False,
        "volume_event_date": pd.NA,
        "event_day_volume": pd.NA,
        "next_day_volume": pd.NA,
        "avg_volume_5d_before": pd.NA,
        "avg_volume_20d_before": pd.NA,
        "event_volume_ratio_5d": pd.NA,
        "event_volume_ratio_20d": pd.NA,
        "next_volume_ratio_5d": pd.NA,
        "next_volume_ratio_20d": pd.NA,
        "volume_reaction_label": "price_file_missing",
    }

    if not stock_code or pd.isna(event_date_raw):
        result["volume_reaction_label"] = "invalid_event"
        return result

    price_path = find_price_file(stock_code)

    if price_path is None:
        return result

    result["price_file_found"] = True

    try:
        price_df = pd.read_csv(price_path)
        price_df = normalize_price_columns(price_df)
    except Exception as error:
        result["volume_reaction_label"] = f"price_file_error: {error}"
        return result

    if price_df.empty:
        result["volume_reaction_label"] = "empty_price_data"
        return result

    event_date = pd.to_datetime(event_date_raw, errors="coerce")

    if pd.isna(event_date):
        result["volume_reaction_label"] = "invalid_event_date"
        return result

    # Use the first available trading day on or after event_date.
    after_event = price_df[price_df["date"] >= event_date].copy()

    if after_event.empty:
        result["volume_reaction_label"] = "no_price_after_event"
        return result

    event_idx = after_event.index[0]
    event_row = price_df.loc[event_idx]

    result["volume_event_date"] = event_row["date"].strftime("%Y-%m-%d")
    result["event_day_volume"] = event_row["volume"]

    previous_rows = price_df[price_df["date"] < event_row["date"]].copy()
    next_rows = price_df[price_df["date"] > event_row["date"]].copy()

    if not next_rows.empty:
        result["next_day_volume"] = next_rows.iloc[0]["volume"]

    avg_5 = previous_rows.tail(5)["volume"].mean()
    avg_20 = previous_rows.tail(20)["volume"].mean()

    result["avg_volume_5d_before"] = avg_5
    result["avg_volume_20d_before"] = avg_20

    event_volume = safe_float(result["event_day_volume"], None)
    next_volume = safe_float(result["next_day_volume"], None)

    if event_volume is not None and avg_5 and avg_5 > 0:
        result["event_volume_ratio_5d"] = event_volume / avg_5

    if event_volume is not None and avg_20 and avg_20 > 0:
        result["event_volume_ratio_20d"] = event_volume / avg_20

    if next_volume is not None and avg_5 and avg_5 > 0:
        result["next_volume_ratio_5d"] = next_volume / avg_5

    if next_volume is not None and avg_20 and avg_20 > 0:
        result["next_volume_ratio_20d"] = next_volume / avg_20

    result["volume_reaction_label"] = classify_volume_reaction(result)

    return result


def classify_volume_reaction(volume_result: dict) -> str:
    """
    Classify volume reaction strength.
    """

    event_ratio_20d = safe_float(
        volume_result.get("event_volume_ratio_20d", None),
        None,
    )

    next_ratio_20d = safe_float(
        volume_result.get("next_volume_ratio_20d", None),
        None,
    )

    best_ratio = 0.0

    for value in [event_ratio_20d, next_ratio_20d]:
        if value is not None:
            best_ratio = max(best_ratio, value)

    if best_ratio >= 5:
        return "extreme_volume_spike"

    if best_ratio >= 3:
        return "strong_volume_spike"

    if best_ratio >= 1.5:
        return "moderate_volume_increase"

    if best_ratio > 0:
        return "normal_or_weak_volume"

    return "insufficient_volume_baseline"


def build_trading_volume_features(ml_df: pd.DataFrame) -> pd.DataFrame:
    """
    Build trading volume features for all ML dataset rows.
    """

    if ml_df.empty:
        return pd.DataFrame()

    base_df = ml_df.copy()

    if "stock_code" not in base_df.columns:
        base_df["stock_code"] = ""

    base_df["stock_code"] = base_df["stock_code"].apply(normalize_stock_code)

    volume_rows = []

    for _, row in base_df.iterrows():
        volume_rows.append(calculate_volume_features_for_event(row))

    volume_df = pd.DataFrame(volume_rows)

    join_columns = ["stock_code", "event_date"]

    result_df = base_df.merge(
        volume_df,
        on=join_columns,
        how="left",
    )

    return result_df


def save_features(df: pd.DataFrame) -> str:
    """
    Save trading volume features.
    """

    os.makedirs(PROCESSED_DIR, exist_ok=True)

    today = datetime.today().strftime("%Y%m%d")
    output_path = os.path.join(
        PROCESSED_DIR,
        f"trading_volume_features_{today}.csv",
    )

    df.to_csv(output_path, index=False, encoding="utf-8-sig")

    return output_path


def build_report(df: pd.DataFrame, source_path: str) -> str:
    """
    Build Markdown report.
    """

    today = datetime.today().strftime("%Y-%m-%d")
    generated_at = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

    lines = []

    lines.append(f"# Trading Volume Feature Report - {today}")
    lines.append("")
    lines.append(f"Generated at: {generated_at}")
    lines.append("")
    lines.append(f"Source ML dataset: `{source_path if source_path else 'Not found'}`")
    lines.append("")

    lines.append("## Purpose")
    lines.append("")
    lines.append(
        "This report measures whether disclosure events were followed by meaningful trading volume changes."
    )
    lines.append("")
    lines.append(
        "Trading volume helps distinguish events that attracted market attention from events that had weak market response."
    )
    lines.append("")

    lines.append("## Important Notice")
    lines.append("")
    lines.append(
        "This report is generated for research and portfolio purposes only. "
        "It is not financial advice or a buy/sell recommendation."
    )
    lines.append("")

    if df.empty:
        lines.append("## Status")
        lines.append("")
        lines.append("No trading volume feature data is available yet.")
        lines.append("")
        return "\n".join(lines)

    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Total rows: **{len(df)}**")

    if "price_file_found" in df.columns:
        found_count = int(df["price_file_found"].fillna(False).sum())
        lines.append(f"- Rows with price file found: **{found_count}**")

    if "volume_reaction_label" in df.columns:
        lines.append("")
        lines.append("## Volume Reaction Label Counts")
        lines.append("")

        counts = df["volume_reaction_label"].value_counts(dropna=False)

        for label, count in counts.items():
            lines.append(f"- {label}: **{count}**")

    lines.append("")

    lines.append("## Interpretation")
    lines.append("")
    lines.append("- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.")
    lines.append("- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.")
    lines.append("- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.")
    lines.append("- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.")
    lines.append("- `price_file_missing`: price data was not available for that stock.")
    lines.append("")

    lines.append("## Sample Rows")
    lines.append("")

    sample_columns = [
        "event_date",
        "stock_code",
        "corp_name",
        "event_type",
        "prediction_direction",
        "volume_reaction_label",
        "event_day_volume",
        "avg_volume_20d_before",
        "event_volume_ratio_20d",
        "next_day_volume",
        "next_volume_ratio_20d",
    ]

    available_columns = [
        col for col in sample_columns
        if col in df.columns
    ]

    if not available_columns:
        lines.append("No displayable columns available.")
        lines.append("")
    else:
        sample_df = df[available_columns].head(30)

        lines.append("| " + " | ".join(available_columns) + " |")
        lines.append("|" + "|".join(["---"] * len(available_columns)) + "|")

        for _, row in sample_df.iterrows():
            values = []

            for col in available_columns:
                value = row[col]

                if "volume" in col and "ratio" not in col:
                    values.append(format_number(value))
                elif "ratio" in col:
                    values.append(format_ratio(value))
                else:
                    values.append(str(value))

            lines.append("| " + " | ".join(values) + " |")

        lines.append("")

    lines.append("## Next Step")
    lines.append("")
    lines.append(
        "The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report."
    )
    lines.append("")

    return "\n".join(lines)


def save_report(report_text: str) -> str:
    """
    Save Markdown report.
    """

    os.makedirs(REPORT_DIR, exist_ok=True)

    today = datetime.today().strftime("%Y-%m-%d")
    output_path = os.path.join(
        REPORT_DIR,
        f"{today}_trading_volume_feature_report.md",
    )

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(report_text)

    return output_path


def main():
    print("Building trading volume features...")

    ml_df, source_path = load_latest_ml_dataset()

    print(f"Latest ML dataset: {source_path if source_path else 'Not found'}")

    result_df = build_trading_volume_features(ml_df)

    if result_df.empty:
        print("No trading volume features generated.")
    else:
        output_path = save_features(result_df)
        print(f"Trading volume features saved to: {output_path}")
        print(f"Rows: {len(result_df)}")

        if "volume_reaction_label" in result_df.columns:
            print("")
            print("Volume reaction label counts:")
            print(result_df["volume_reaction_label"].value_counts(dropna=False))

    report_text = build_report(result_df, source_path)
    report_path = save_report(report_text)

    print(f"Trading volume feature report saved to: {report_path}")


if __name__ == "__main__":
    main()
