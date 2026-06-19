"""
Automation history tracker.

This script creates and updates a cumulative CSV file that tracks
daily automation status metrics over time.

Output:
data/processed/automation_history.csv

Tracked metrics:
- raw DART rows
- parsed DART rows
- selected key event rows
- scored event rows
- news feature rows
- error note rows
- ML dataset rows
- pending rows
- success rows
- failure rows
- trainable rows
"""

import os
from datetime import datetime

import pandas as pd


RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"
PREDICTION_DIR = "data/predictions"
REVIEW_DIR = "reports/daily_review"

HISTORY_PATH = "data/processed/automation_history.csv"


def get_latest_file(directory: str, prefix: str, suffix: str = ".csv"):
    """
    Find the latest file by prefix and suffix.
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


def count_rows(file_path: str) -> int:
    """
    Count rows in a CSV file safely.
    """

    if file_path is None:
        return 0

    try:
        df = pd.read_csv(file_path)
        return len(df)
    except Exception:
        return 0


def load_csv(file_path: str) -> pd.DataFrame:
    """
    Load CSV safely.
    """

    if file_path is None:
        return pd.DataFrame()

    try:
        return pd.read_csv(file_path)
    except Exception:
        return pd.DataFrame()


def get_prediction_counts(ml_dataset_path: str) -> dict:
    """
    Count pending, success, failure, and trainable rows.
    """

    df = load_csv(ml_dataset_path)

    if df.empty or "prediction_result" not in df.columns:
        return {
            "ml_dataset_rows": len(df),
            "pending_rows": 0,
            "success_rows": 0,
            "failure_rows": 0,
            "trainable_rows": 0,
        }

    pending_rows = len(df[df["prediction_result"] == "pending"])
    success_rows = len(df[df["prediction_result"] == "success"])
    failure_rows = len(df[df["prediction_result"] == "failure"])

    return {
        "ml_dataset_rows": len(df),
        "pending_rows": pending_rows,
        "success_rows": success_rows,
        "failure_rows": failure_rows,
        "trainable_rows": success_rows + failure_rows,
    }


def baseline_report_exists() -> bool:
    """
    Check whether today's baseline model report exists.
    """

    today = datetime.today().strftime("%Y-%m-%d")
    report_path = os.path.join(REVIEW_DIR, f"{today}_baseline_model_report.md")

    return os.path.exists(report_path)


def automation_status_report_exists() -> bool:
    """
    Check whether today's automation status report exists.
    """

    today = datetime.today().strftime("%Y-%m-%d")
    report_path = os.path.join(REVIEW_DIR, f"{today}_automation_status_report.md")

    return os.path.exists(report_path)


def build_today_history_row() -> dict:
    """
    Build one daily history row.
    """

    run_date = datetime.today().strftime("%Y-%m-%d")
    generated_at = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

    raw_dart_file = get_latest_file(RAW_DIR, "dart_disclosures_")
    parsed_dart_file = get_latest_file(PROCESSED_DIR, "parsed_dart_disclosures_")
    selected_events_file = get_latest_file(PROCESSED_DIR, "selected_key_events_")
    scored_events_file = get_latest_file(PROCESSED_DIR, "scored_key_events_")
    news_features_file = get_latest_file(PROCESSED_DIR, "event_news_features_")
    error_notes_file = get_latest_file(PREDICTION_DIR, "error_notes_")
    ml_dataset_file = get_latest_file(PROCESSED_DIR, "ml_dataset_")

    prediction_counts = get_prediction_counts(ml_dataset_file)

    row = {
        "run_date": run_date,
        "generated_at": generated_at,
        "raw_dart_rows": count_rows(raw_dart_file),
        "parsed_dart_rows": count_rows(parsed_dart_file),
        "selected_event_rows": count_rows(selected_events_file),
        "scored_event_rows": count_rows(scored_events_file),
        "news_feature_rows": count_rows(news_features_file),
        "error_note_rows": count_rows(error_notes_file),
        "ml_dataset_rows": prediction_counts["ml_dataset_rows"],
        "pending_rows": prediction_counts["pending_rows"],
        "success_rows": prediction_counts["success_rows"],
        "failure_rows": prediction_counts["failure_rows"],
        "trainable_rows": prediction_counts["trainable_rows"],
        "baseline_model_report_exists": baseline_report_exists(),
        "automation_status_report_exists": automation_status_report_exists(),
        "raw_dart_file": raw_dart_file if raw_dart_file else "",
        "ml_dataset_file": ml_dataset_file if ml_dataset_file else "",
    }

    return row


def update_history(today_row: dict) -> pd.DataFrame:
    """
    Append or replace today's row in automation history.
    """

    os.makedirs(PROCESSED_DIR, exist_ok=True)

    if os.path.exists(HISTORY_PATH):
        history_df = pd.read_csv(HISTORY_PATH)
    else:
        history_df = pd.DataFrame()

    today = today_row["run_date"]

    if not history_df.empty and "run_date" in history_df.columns:
        history_df = history_df[history_df["run_date"] != today]

    today_df = pd.DataFrame([today_row])
    history_df = pd.concat([history_df, today_df], ignore_index=True)

    history_df = history_df.sort_values("run_date").reset_index(drop=True)

    history_df.to_csv(HISTORY_PATH, index=False, encoding="utf-8-sig")

    return history_df


def main():
    print("Updating automation history...")

    today_row = build_today_history_row()
    history_df = update_history(today_row)

    print(f"Automation history saved to: {HISTORY_PATH}")
    print(f"Total history rows: {len(history_df)}")
    print()
    print(history_df.tail(10).to_string(index=False))


if __name__ == "__main__":
    main()
