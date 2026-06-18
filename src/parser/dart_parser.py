"""
DART disclosure parser.

This script reads raw DART disclosure CSV files,
classifies disclosure events, and saves processed data.
"""

import os
from datetime import datetime

import pandas as pd


def classify_event(report_name: str) -> str:
    """
    Classify disclosure event type based on report title.
    """

    if not isinstance(report_name, str):
        return "unknown"

    if "단일판매" in report_name or "공급계약" in report_name:
        return "supply_contract"

    if "유상증자" in report_name:
        return "paid_in_capital_increase"

    if "무상증자" in report_name:
        return "bonus_issue"

    if "전환사채" in report_name or "CB" in report_name:
        return "convertible_bond"

    if "신주인수권부사채" in report_name or "BW" in report_name:
        return "bond_with_warrant"

    if "최대주주" in report_name:
        return "major_shareholder_change"

    if "임원" in report_name or "주요주주" in report_name:
        return "insider_or_major_holder"

    if "영업실적" in report_name or "잠정실적" in report_name:
        return "earnings_guidance"

    if "소송" in report_name:
        return "lawsuit"

    if "불성실공시" in report_name:
        return "disclosure_violation"

    if "투자판단" in report_name:
        return "investment_decision"

    if "합병" in report_name:
        return "merger"

    if "분할" in report_name:
        return "spin_off"

    return "other"


def get_latest_raw_file(raw_dir: str = "data/raw") -> str:
    """
    Find the latest DART raw CSV file.
    """

    if not os.path.exists(raw_dir):
        raise FileNotFoundError(f"Raw data directory not found: {raw_dir}")

    csv_files = [
        file for file in os.listdir(raw_dir)
        if file.startswith("dart_disclosures_") and file.endswith(".csv")
    ]

    if not csv_files:
        raise FileNotFoundError("No raw DART disclosure CSV files found.")

    csv_files.sort(reverse=True)
    return os.path.join(raw_dir, csv_files[0])


def parse_disclosures(input_path: str) -> pd.DataFrame:
    """
    Read raw DART CSV and add event classification columns.
    """

    df = pd.read_csv(input_path)

    if "report_nm" not in df.columns:
        raise ValueError("Column 'report_nm' not found in raw DART data.")

    df["event_type"] = df["report_nm"].apply(classify_event)

    selected_columns = [
        "corp_name",
        "corp_code",
        "stock_code",
        "report_nm",
        "event_type",
        "rcept_dt",
        "rcept_no",
    ]

    existing_columns = [col for col in selected_columns if col in df.columns]
    parsed_df = df[existing_columns].copy()

    return parsed_df


def save_processed_data(df: pd.DataFrame, input_path: str) -> str:
    """
    Save processed DART data to CSV.
    """

    output_dir = "data/processed"
    os.makedirs(output_dir, exist_ok=True)

    date_part = os.path.basename(input_path).replace("dart_disclosures_", "").replace(".csv", "")
    output_path = f"{output_dir}/parsed_dart_disclosures_{date_part}.csv"

    df.to_csv(output_path, index=False, encoding="utf-8-sig")

    return output_path


def main():
    print("Parsing latest DART disclosure file...")

    input_path = get_latest_raw_file()
    print(f"Input file: {input_path}")

    parsed_df = parse_disclosures(input_path)
    output_path = save_processed_data(parsed_df, input_path)

    print(f"Parsed {len(parsed_df)} disclosures.")
    print(f"Saved to: {output_path}")
    print()
    print("Event type summary:")
    print(parsed_df["event_type"].value_counts())
    print()
    print(parsed_df[["corp_name", "report_nm", "event_type"]].head(10))


if __name__ == "__main__":
    main()
