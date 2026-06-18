"""
Daily pipeline for Overnight Alpha Lab.

This script:
1. Collects DART disclosures
2. Parses disclosure events
3. Generates a daily DART report
4. Selects key events
5. Collects stock price data for selected companies
6. Evaluates event-price reactions when data is available
"""

import os
import subprocess
from datetime import datetime

import pandas as pd


KEY_EVENT_TYPES = [
    "supply_contract",
    "paid_in_capital_increase",
    "bonus_issue",
    "convertible_bond",
    "bond_with_warrant",
    "major_shareholder_change",
    "earnings_guidance",
    "lawsuit",
    "disclosure_violation",
    "investment_decision",
    "merger",
    "spin_off",
]


def run_command(command: list[str]) -> None:
    """
    Run a command.
    """

    print(f"\nRunning: {' '.join(command)}")
    subprocess.run(command, check=True)


def get_latest_processed_file(processed_dir: str = "data/processed") -> str:
    """
    Find latest parsed DART disclosure file.
    """

    csv_files = [
        file for file in os.listdir(processed_dir)
        if file.startswith("parsed_dart_disclosures_") and file.endswith(".csv")
    ]

    if not csv_files:
        raise FileNotFoundError("No parsed DART disclosure CSV files found.")

    csv_files.sort(reverse=True)
    return os.path.join(processed_dir, csv_files[0])


def normalize_stock_code(value) -> str:
    """
    Normalize stock code to 6-digit string.
    """

    if pd.isna(value):
        return ""

    try:
        return str(int(float(value))).zfill(6)
    except ValueError:
        return str(value).strip().zfill(6)


def select_key_events(input_path: str) -> pd.DataFrame:
    """
    Select key disclosure events that are likely to affect stock price.
    """

    df = pd.read_csv(input_path)

    if "stock_code" not in df.columns:
        raise ValueError("stock_code column not found.")

    df["stock_code"] = df["stock_code"].apply(normalize_stock_code)

    key_df = df[
        (df["event_type"].isin(KEY_EVENT_TYPES))
        & (df["stock_code"] != "")
        & (df["stock_code"] != "000000")
    ].copy()

    key_df = key_df.drop_duplicates(subset=["stock_code", "report_nm", "rcept_dt"])

    return key_df


def save_selected_events(df: pd.DataFrame) -> str:
    """
    Save selected key events.
    """

    output_dir = "data/processed"
    os.makedirs(output_dir, exist_ok=True)

    today = datetime.today().strftime("%Y%m%d")
    output_path = f"{output_dir}/selected_key_events_{today}.csv"

    df.to_csv(output_path, index=False, encoding="utf-8-sig")

    return output_path


def collect_and_evaluate_selected_events(key_events: pd.DataFrame) -> None:
    """
    Collect price data and evaluate event-price reactions
    for selected stock codes.
    """

    stock_codes = sorted(key_events["stock_code"].dropna().unique())

    print("\nCollecting price data and evaluating reactions:")
    print(f"Selected stock codes: {stock_codes}")

    for stock_code in stock_codes:
        print(f"\nProcessing stock_code={stock_code}")

        try:
            run_command(["python", "src/crawler/price_collector.py", stock_code])
            run_command(["python", "src/evaluator/event_price_reaction.py", stock_code])
        except subprocess.CalledProcessError as error:
            print(f"Failed to process stock_code={stock_code}: {error}")
        except FileNotFoundError as error:
            print(f"Missing file for stock_code={stock_code}: {error}")

def main():
    print("Starting daily pipeline...")

    # 1. Collect DART disclosures
    run_command(["python", "src/crawler/dart_collector.py"])

    # 2. Parse DART disclosures
    run_command(["python", "src/parser/dart_parser.py"])

    # 3. Generate daily DART report
    run_command(["python", "src/report_generator/daily_dart_report.py"])

    # 4. Select key events
    latest_processed_file = get_latest_processed_file()
    key_events = select_key_events(latest_processed_file)

    print("\nSelected key events:")
    if key_events.empty:
        print("No key events selected today.")
        return

    print(
        key_events[
            ["corp_name", "stock_code", "report_nm", "event_type"]
        ].to_string(index=False)
    )

    selected_path = save_selected_events(key_events)
    print(f"\nSelected events saved to: {selected_path}")

    # 5. Score selected key events
    run_command(["python", "src/features/event_scoring.py"])

    # 6. Collect price data and evaluate reactions
    collect_and_evaluate_selected_events(key_events)

    print("\nDaily pipeline completed.")


if __name__ == "__main__":
    main()
