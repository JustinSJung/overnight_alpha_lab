"""
Automation status report generator.

This script summarizes the current project execution status:
- latest DART raw disclosure file
- latest parsed disclosure file
- latest selected key events file
- latest scored events file
- latest news feature file
- latest ML dataset file
- pending / success / failure counts
- latest baseline model report
- latest generated reports

Output:
reports/daily_review/YYYY-MM-DD_automation_status_report.md
"""

import os
from datetime import datetime

import pandas as pd


TARGET_DIRS = {
    "raw": "data/raw",
    "processed": "data/processed",
    "predictions": "data/predictions",
    "daily_prediction": "reports/daily_prediction",
    "daily_review": "reports/daily_review",
}


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
    Count rows in a CSV file.
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


def get_prediction_result_counts(ml_dataset_path: str) -> dict:
    """
    Count pending, success, and failure rows in the ML dataset.
    """

    df = load_csv(ml_dataset_path)

    if df.empty or "prediction_result" not in df.columns:
        return {
            "pending": 0,
            "success": 0,
            "failure": 0,
            "trainable": 0,
            "total": len(df),
        }

    pending_count = len(df[df["prediction_result"] == "pending"])
    success_count = len(df[df["prediction_result"] == "success"])
    failure_count = len(df[df["prediction_result"] == "failure"])
    trainable_count = success_count + failure_count

    return {
        "pending": pending_count,
        "success": success_count,
        "failure": failure_count,
        "trainable": trainable_count,
        "total": len(df),
    }


def get_latest_files_summary() -> dict:
    """
    Collect latest important files.
    """

    latest_files = {
        "raw_dart": get_latest_file(
            TARGET_DIRS["raw"],
            "dart_disclosures_",
        ),
        "parsed_dart": get_latest_file(
            TARGET_DIRS["processed"],
            "parsed_dart_disclosures_",
        ),
        "selected_events": get_latest_file(
            TARGET_DIRS["processed"],
            "selected_key_events_",
        ),
        "scored_events": get_latest_file(
            TARGET_DIRS["processed"],
            "scored_key_events_",
        ),
        "news_features": get_latest_file(
            TARGET_DIRS["processed"],
            "event_news_features_",
        ),
        "ml_dataset": get_latest_file(
            TARGET_DIRS["processed"],
            "ml_dataset_",
        ),
        "error_notes": get_latest_file(
            TARGET_DIRS["predictions"],
            "error_notes_",
        ),
        "daily_prediction_report": get_latest_file(
            TARGET_DIRS["daily_prediction"],
            "",
            ".md",
        ),
        "baseline_model_report": get_latest_file(
            TARGET_DIRS["daily_review"],
            "",
            "_baseline_model_report.md",
        ),
    }

    return latest_files


def file_exists_text(file_path: str) -> str:
    """
    Return readable file existence status.
    """

    if file_path and os.path.exists(file_path):
        return "YES"

    return "NO"


def build_report() -> str:
    """
    Build automation status report text.
    """

    today = datetime.today().strftime("%Y-%m-%d")
    generated_at = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

    latest_files = get_latest_files_summary()

    raw_dart_rows = count_rows(latest_files["raw_dart"])
    parsed_dart_rows = count_rows(latest_files["parsed_dart"])
    selected_event_rows = count_rows(latest_files["selected_events"])
    scored_event_rows = count_rows(latest_files["scored_events"])
    news_feature_rows = count_rows(latest_files["news_features"])
    error_note_rows = count_rows(latest_files["error_notes"])

    ml_counts = get_prediction_result_counts(latest_files["ml_dataset"])

    lines = []

    lines.append(f"# Automation Status Report - {today}")
    lines.append("")
    lines.append(f"Generated at: {generated_at}")
    lines.append("")

    lines.append("## Execution Summary")
    lines.append("")
    lines.append("| Item | Status |")
    lines.append("|---|---|")
    lines.append(f"| Raw DART disclosure file | {file_exists_text(latest_files['raw_dart'])} |")
    lines.append(f"| Parsed DART file | {file_exists_text(latest_files['parsed_dart'])} |")
    lines.append(f"| Selected key events file | {file_exists_text(latest_files['selected_events'])} |")
    lines.append(f"| Scored key events file | {file_exists_text(latest_files['scored_events'])} |")
    lines.append(f"| News features file | {file_exists_text(latest_files['news_features'])} |")
    lines.append(f"| Error notes file | {file_exists_text(latest_files['error_notes'])} |")
    lines.append(f"| ML dataset file | {file_exists_text(latest_files['ml_dataset'])} |")
    lines.append(f"| Baseline model report | {file_exists_text(latest_files['baseline_model_report'])} |")
    lines.append("")

    lines.append("## Data Summary")
    lines.append("")
    lines.append("| Dataset | Rows |")
    lines.append("|---|---:|")
    lines.append(f"| Raw DART disclosures | {raw_dart_rows} |")
    lines.append(f"| Parsed DART disclosures | {parsed_dart_rows} |")
    lines.append(f"| Selected key events | {selected_event_rows} |")
    lines.append(f"| Scored key events | {scored_event_rows} |")
    lines.append(f"| News feature rows | {news_feature_rows} |")
    lines.append(f"| Error note rows | {error_note_rows} |")
    lines.append(f"| ML dataset rows | {ml_counts['total']} |")
    lines.append("")

    lines.append("## Prediction Result Summary")
    lines.append("")
    lines.append("| Result | Rows |")
    lines.append("|---|---:|")
    lines.append(f"| Pending | {ml_counts['pending']} |")
    lines.append(f"| Success | {ml_counts['success']} |")
    lines.append(f"| Failure | {ml_counts['failure']} |")
    lines.append(f"| Trainable rows | {ml_counts['trainable']} |")
    lines.append("")

    lines.append("## Latest Files")
    lines.append("")
    for label, path in latest_files.items():
        display_path = path if path else "Not found"
        lines.append(f"- {label}: `{display_path}`")

    lines.append("")
    lines.append("## Interpretation")
    lines.append("")

    if ml_counts["trainable"] == 0:
        lines.append(
            "The ML dataset exists, but there are no trainable rows yet. "
            "Most events are still pending because next trading day price data may not be available."
        )
    elif ml_counts["trainable"] < 10:
        lines.append(
            "Some trainable rows exist, but the sample size is still small. "
            "The baseline model may not be reliable yet."
        )
    else:
        lines.append(
            "The dataset has enough trainable rows for baseline model training. "
            "Model performance should be reviewed carefully."
        )

    lines.append("")
    lines.append("## Next Step")
    lines.append("")
    lines.append(
        "Continue running the scheduled pipeline or catch-up script. "
        "As pending rows are converted into success or failure, the training dataset will grow."
    )
    lines.append("")

    return "\n".join(lines)


def save_report(report_text: str) -> str:
    """
    Save report to reports/daily_review.
    """

    output_dir = "reports/daily_review"
    os.makedirs(output_dir, exist_ok=True)

    today = datetime.today().strftime("%Y-%m-%d")
    output_path = os.path.join(
        output_dir,
        f"{today}_automation_status_report.md",
    )

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(report_text)

    return output_path


def main():
    print("Generating automation status report...")

    report_text = build_report()
    output_path = save_report(report_text)

    print(f"Automation status report saved to: {output_path}")


if __name__ == "__main__":
    main()
