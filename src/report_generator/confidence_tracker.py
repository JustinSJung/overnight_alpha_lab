"""
Confidence tracker.

This script analyzes the latest ML dataset and generates a confidence report.

It checks:
- total rows
- pending rows
- success rows
- failure rows
- trainable rows
- overall prediction accuracy
- event type success rate
- prediction direction success rate
- model readiness level

Output:
reports/daily_review/YYYY-MM-DD_confidence_report.md
"""

import os
from datetime import datetime

import pandas as pd


PROCESSED_DIR = "data/processed"
REVIEW_DIR = "reports/daily_review"


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


def load_latest_ml_dataset() -> tuple[pd.DataFrame, str]:
    """
    Load latest ML dataset.
    """

    ml_dataset_path = get_latest_file(PROCESSED_DIR, "ml_dataset_")

    if ml_dataset_path is None:
        return pd.DataFrame(), ""

    try:
        df = pd.read_csv(ml_dataset_path)
        return df, ml_dataset_path
    except Exception:
        return pd.DataFrame(), ml_dataset_path


def get_prediction_counts(df: pd.DataFrame) -> dict:
    """
    Count prediction result rows.
    """

    if df.empty or "prediction_result" not in df.columns:
        return {
            "total_rows": len(df),
            "pending_rows": 0,
            "success_rows": 0,
            "failure_rows": 0,
            "trainable_rows": 0,
        }

    pending_rows = len(df[df["prediction_result"] == "pending"])
    success_rows = len(df[df["prediction_result"] == "success"])
    failure_rows = len(df[df["prediction_result"] == "failure"])

    return {
        "total_rows": len(df),
        "pending_rows": pending_rows,
        "success_rows": success_rows,
        "failure_rows": failure_rows,
        "trainable_rows": success_rows + failure_rows,
    }


def calculate_accuracy(counts: dict) -> float:
    """
    Calculate overall accuracy from success/failure rows.
    """

    trainable_rows = counts["trainable_rows"]

    if trainable_rows == 0:
        return 0.0

    return counts["success_rows"] / trainable_rows


def classify_readiness(trainable_rows: int, accuracy: float) -> str:
    """
    Classify current model readiness level.
    """

    if trainable_rows == 0:
        return "NOT_READY"

    if trainable_rows < 10:
        return "DATA_TOO_SMALL"

    if trainable_rows < 50:
        return "EARLY_STAGE"

    if accuracy < 0.5:
        return "LOW_CONFIDENCE"

    if accuracy < 0.6:
        return "WATCHLIST"

    if accuracy < 0.7:
        return "MODERATE_CONFIDENCE"

    return "HIGH_CONFIDENCE"


def calculate_group_success_rate(df: pd.DataFrame, group_column: str) -> pd.DataFrame:
    """
    Calculate success rate by group column.
    """

    if df.empty:
        return pd.DataFrame()

    if group_column not in df.columns:
        return pd.DataFrame()

    if "prediction_result" not in df.columns:
        return pd.DataFrame()

    train_df = df[df["prediction_result"].isin(["success", "failure"])].copy()

    if train_df.empty:
        return pd.DataFrame()

    grouped = (
        train_df
        .groupby(group_column)
        .agg(
            total_rows=("prediction_result", "count"),
            success_rows=("prediction_result", lambda x: (x == "success").sum()),
            failure_rows=("prediction_result", lambda x: (x == "failure").sum()),
        )
        .reset_index()
    )

    grouped["success_rate"] = grouped["success_rows"] / grouped["total_rows"]

    grouped = grouped.sort_values(
        by=["total_rows", "success_rate"],
        ascending=[False, False],
    )

    return grouped


def dataframe_to_markdown_table(df: pd.DataFrame) -> list[str]:
    """
    Convert dataframe to simple Markdown table lines.
    """

    if df.empty:
        return ["No trainable data available yet."]

    display_df = df.copy()

    if "success_rate" in display_df.columns:
        display_df["success_rate"] = display_df["success_rate"].apply(
            lambda x: f"{x:.2%}"
        )

    lines = []
    columns = display_df.columns.tolist()

    lines.append("| " + " | ".join(columns) + " |")
    lines.append("|" + "|".join(["---"] * len(columns)) + "|")

    for _, row in display_df.iterrows():
        values = [str(row[col]) for col in columns]
        lines.append("| " + " | ".join(values) + " |")

    return lines


def build_confidence_report() -> str:
    """
    Build confidence report Markdown text.
    """

    today = datetime.today().strftime("%Y-%m-%d")
    generated_at = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

    df, ml_dataset_path = load_latest_ml_dataset()
    counts = get_prediction_counts(df)
    accuracy = calculate_accuracy(counts)
    readiness = classify_readiness(counts["trainable_rows"], accuracy)

    event_type_rates = calculate_group_success_rate(df, "event_type")
    direction_rates = calculate_group_success_rate(df, "prediction_direction")

    lines = []

    lines.append(f"# Confidence Report - {today}")
    lines.append("")
    lines.append(f"Generated at: {generated_at}")
    lines.append("")
    lines.append(f"ML dataset: `{ml_dataset_path if ml_dataset_path else 'Not found'}`")
    lines.append("")

    lines.append("## Overall Status")
    lines.append("")
    lines.append("| Metric | Value |")
    lines.append("|---|---:|")
    lines.append(f"| Total rows | {counts['total_rows']} |")
    lines.append(f"| Pending rows | {counts['pending_rows']} |")
    lines.append(f"| Success rows | {counts['success_rows']} |")
    lines.append(f"| Failure rows | {counts['failure_rows']} |")
    lines.append(f"| Trainable rows | {counts['trainable_rows']} |")
    lines.append(f"| Overall accuracy | {accuracy:.2%} |")
    lines.append("")
    lines.append(f"Current readiness level: **{readiness}**")
    lines.append("")

    lines.append("## Readiness Interpretation")
    lines.append("")

    if readiness == "NOT_READY":
        lines.append(
            "The model is not ready yet because there are no success/failure rows. "
            "Most rows are still pending."
        )
    elif readiness == "DATA_TOO_SMALL":
        lines.append(
            "Some trainable rows exist, but the dataset is still too small to trust the result."
        )
    elif readiness == "EARLY_STAGE":
        lines.append(
            "The model has started accumulating trainable data, but confidence is still early-stage."
        )
    elif readiness == "LOW_CONFIDENCE":
        lines.append(
            "The model has enough samples to evaluate, but current accuracy is weak."
        )
    elif readiness == "WATCHLIST":
        lines.append(
            "The model is showing some predictive signal, but it still needs monitoring."
        )
    elif readiness == "MODERATE_CONFIDENCE":
        lines.append(
            "The model is showing moderate confidence, but more data is needed before relying on it."
        )
    else:
        lines.append(
            "The model is showing high confidence based on current data. Continue monitoring for stability."
        )

    lines.append("")

    lines.append("## Success Rate by Event Type")
    lines.append("")
    lines.extend(dataframe_to_markdown_table(event_type_rates))
    lines.append("")

    lines.append("## Success Rate by Prediction Direction")
    lines.append("")
    lines.extend(dataframe_to_markdown_table(direction_rates))
    lines.append("")

    lines.append("## Next Step")
    lines.append("")
    lines.append(
        "Continue running the daily pipeline and catch-up script. "
        "As pending rows become success/failure rows, the confidence report will become more meaningful."
    )
    lines.append("")

    return "\n".join(lines)


def save_report(report_text: str) -> str:
    """
    Save confidence report.
    """

    os.makedirs(REVIEW_DIR, exist_ok=True)

    today = datetime.today().strftime("%Y-%m-%d")
    output_path = os.path.join(REVIEW_DIR, f"{today}_confidence_report.md")

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(report_text)

    return output_path


def main():
    print("Generating confidence report...")

    report_text = build_confidence_report()
    output_path = save_report(report_text)

    print(f"Confidence report saved to: {output_path}")


if __name__ == "__main__":
    main()
