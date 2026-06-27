"""
Pending event re-evaluator.

This script finds pending rows in the latest ML dataset,
re-collects price data for those stock codes, re-runs event reaction
evaluation, regenerates error notes, rebuilds the ML dataset, and
runs the baseline model again.

Purpose:
- Convert old pending rows into success/failure when next trading day
  price data becomes available.
"""

import os
import subprocess

import pandas as pd


def run_command(command):
    """
    Run a command and stop if it fails.
    """

    print()
    print("Running:", " ".join(command))

    result = subprocess.run(command)

    if result.returncode != 0:
        raise RuntimeError(f"Command failed: {' '.join(command)}")


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


def get_latest_ml_dataset(processed_dir: str = "data/processed") -> str:
    """
    Find the latest ML dataset file.
    """

    files = [
        file for file in os.listdir(processed_dir)
        if file.startswith("ml_dataset_") and file.endswith(".csv")
    ]

    if not files:
        raise FileNotFoundError("No ML dataset file found.")

    files.sort(reverse=True)

    return os.path.join(processed_dir, files[0])


def load_pending_events(ml_dataset_path: str) -> pd.DataFrame:
    """
    Load pending rows from latest ML dataset.
    """

    df = pd.read_csv(ml_dataset_path)

    if "prediction_result" not in df.columns:
        raise ValueError("prediction_result column not found in ML dataset.")

    pending_df = df[df["prediction_result"] == "pending"].copy()

    if "stock_code" in pending_df.columns:
        pending_df["stock_code"] = pending_df["stock_code"].apply(normalize_stock_code)

    pending_df = pending_df[pending_df["stock_code"] != ""]

    return pending_df


def get_pending_stock_codes(pending_df: pd.DataFrame) -> list[str]:
    """
    Extract unique stock codes from pending rows.
    """

    if pending_df.empty:
        return []

    stock_codes = sorted(pending_df["stock_code"].dropna().unique().tolist())

    return stock_codes


def main():
    print("Starting pending event re-evaluation...")

    try:
        ml_dataset_path = get_latest_ml_dataset()
    except FileNotFoundError:
        print("No ML dataset file found.")
        print("This can happen on weekends, holidays, or days with no DART data.")
        print("Pending re-evaluator will stop gracefully without error.")
        return    

    print("Latest ML dataset:", ml_dataset_path)

    pending_df = load_pending_events(ml_dataset_path)
    pending_count = len(pending_df)

    print("Pending rows:", pending_count)

    if pending_count == 0:
        print("No pending rows found. Nothing to re-evaluate.")
        return

    stock_codes = get_pending_stock_codes(pending_df)

    print("Pending stock codes:", stock_codes)

    for stock_code in stock_codes:
        run_command(["python", "src/crawler/price_collector.py", stock_code])
        run_command(["python", "src/evaluator/event_price_reaction.py", stock_code])

    run_command(["python", "src/evaluator/error_note_generator.py"])
    run_command(["python", "src/features/ml_dataset_builder.py"])
    run_command(["python", "src/models/baseline_model.py"])

    print()
    print("Pending re-evaluation completed.")


if __name__ == "__main__":
    main()
