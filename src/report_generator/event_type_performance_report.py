"""
Event-type performance report.

This script summarizes historical prediction performance by disclosure event type.

Input:
data/predictions/error_notes_YYYYMMDD.csv

Output:
reports/daily_review/YYYY-MM-DD_event_type_performance_report.md
"""

import os
from datetime import datetime

import pandas as pd


PREDICTIONS_DIR = "data/predictions"
OUTPUT_DIR = "reports/daily_review"


def load_error_notes() -> pd.DataFrame:
    """
    Load all error note CSV files.
    """

    if not os.path.exists(PREDICTIONS_DIR):
        return pd.DataFrame()

    files = [
        file for file in os.listdir(PREDICTIONS_DIR)
        if file.startswith("error_notes_") and file.endswith(".csv")
    ]

    if not files:
        return pd.DataFrame()

    frames = []

    for file in files:
        path = os.path.join(PREDICTIONS_DIR, file)

        try:
            df = pd.read_csv(path)
            df["source_file"] = file
            frames.append(df)
        except Exception:
            continue

    if not frames:
        return pd.DataFrame()

    return pd.concat(frames, ignore_index=True)


def safe_float(value, default=0.0) -> float:
    """
    Convert value to float safely.
    """

    try:
        if pd.isna(value):
            return default

        return float(value)
    except Exception:
        return default


def format_percent(value) -> str:
    """
    Format decimal return as percent.
    """

    try:
        if pd.isna(value):
            return "N/A"

        return f"{float(value) * 100:.2f}%"
    except Exception:
        return "N/A"


def build_performance_table(df: pd.DataFrame) -> pd.DataFrame:
    """
    Build event-type performance table.
    """

    if df.empty:
        return pd.DataFrame()

    if "event_type" not in df.columns:
        return pd.DataFrame()

    work_df = df.copy()

    required_columns = [
        "prediction_result",
        "next_open_return",
        "next_close_return",
        "confidence_adjustment",
    ]

    for col in required_columns:
        if col not in work_df.columns:
            work_df[col] = pd.NA

    work_df["event_type"] = work_df["event_type"].astype(str)
    work_df["prediction_result"] = work_df["prediction_result"].astype(str)
    work_df["confidence_adjustment"] = work_df["confidence_adjustment"].astype(str)

    rows = []

    for event_type, group in work_df.groupby("event_type"):
        total_count = len(group)

        success_count = (group["prediction_result"] == "success").sum()
        failure_count = (group["prediction_result"] == "failure").sum()
        pending_count = (group["prediction_result"] == "pending").sum()
        unknown_count = total_count - success_count - failure_count - pending_count

        evaluated_count = success_count + failure_count

        if evaluated_count > 0:
            success_rate = success_count / evaluated_count
        else:
            success_rate = None

        next_open_values = pd.to_numeric(
            group["next_open_return"],
            errors="coerce",
        )

        next_close_values = pd.to_numeric(
            group["next_close_return"],
            errors="coerce",
        )

        avg_next_open_return = next_open_values.mean()
        avg_next_close_return = next_close_values.mean()

        increase_count = (group["confidence_adjustment"] == "increase").sum()
        decrease_count = (group["confidence_adjustment"] == "decrease").sum()
        slightly_decrease_count = (
            group["confidence_adjustment"] == "slightly_decrease"
        ).sum()
        hold_count = (group["confidence_adjustment"] == "hold").sum()

        adjustment_bias = "neutral"

        if increase_count > decrease_count + slightly_decrease_count:
            adjustment_bias = "positive"
        elif decrease_count + slightly_decrease_count > increase_count:
            adjustment_bias = "conservative"

        rows.append(
            {
                "event_type": event_type,
                "total_count": total_count,
                "evaluated_count": evaluated_count,
                "success_count": success_count,
                "failure_count": failure_count,
                "pending_count": pending_count,
                "unknown_count": unknown_count,
                "success_rate": success_rate,
                "avg_next_open_return": avg_next_open_return,
                "avg_next_close_return": avg_next_close_return,
                "increase_count": increase_count,
                "decrease_count": decrease_count,
                "slightly_decrease_count": slightly_decrease_count,
                "hold_count": hold_count,
                "adjustment_bias": adjustment_bias,
            }
        )

    result_df = pd.DataFrame(rows)

    if result_df.empty:
        return result_df

    result_df = result_df.sort_values(
        by=["evaluated_count", "total_count"],
        ascending=False,
    )

    return result_df


def build_summary(df: pd.DataFrame, performance_df: pd.DataFrame) -> list:
    """
    Build summary lines.
    """

    lines = []

    total_rows = len(df)

    if "prediction_result" in df.columns:
        success_count = (df["prediction_result"] == "success").sum()
        failure_count = (df["prediction_result"] == "failure").sum()
        pending_count = (df["prediction_result"] == "pending").sum()
    else:
        success_count = 0
        failure_count = 0
        pending_count = 0

    evaluated_count = success_count + failure_count

    if evaluated_count > 0:
        overall_success_rate = success_count / evaluated_count
    else:
        overall_success_rate = None

    lines.append("## Overall Summary")
    lines.append("")
    lines.append(f"- Total error-note rows: **{total_rows}**")
    lines.append(f"- Evaluated rows: **{evaluated_count}**")
    lines.append(f"- Success rows: **{success_count}**")
    lines.append(f"- Failure rows: **{failure_count}**")
    lines.append(f"- Pending rows: **{pending_count}**")

    if overall_success_rate is None:
        lines.append("- Overall success rate: **N/A**")
    else:
        lines.append(f"- Overall success rate: **{overall_success_rate * 100:.2f}%**")

    lines.append("")

    if performance_df.empty:
        lines.append("No event-type performance data is available yet.")
        lines.append("")
        return lines

    evaluated_df = performance_df[performance_df["evaluated_count"] > 0].copy()

    if evaluated_df.empty:
        lines.append(
            "Most rows are still pending. Event-type success rates will become meaningful after next-day price reactions are evaluated."
        )
        lines.append("")
        return lines

    best_df = evaluated_df.sort_values(
        by=["success_rate", "evaluated_count"],
        ascending=False,
    ).head(3)

    weak_df = evaluated_df.sort_values(
        by=["success_rate", "evaluated_count"],
        ascending=[True, False],
    ).head(3)

    lines.append("## Best Event Types So Far")
    lines.append("")

    for _, row in best_df.iterrows():
        lines.append(
            f"- `{row['event_type']}`: success rate "
            f"{row['success_rate'] * 100:.2f}% "
            f"from {int(row['evaluated_count'])} evaluated cases."
        )

    lines.append("")
    lines.append("## Weak Event Types So Far")
    lines.append("")

    for _, row in weak_df.iterrows():
        lines.append(
            f"- `{row['event_type']}`: success rate "
            f"{row['success_rate'] * 100:.2f}% "
            f"from {int(row['evaluated_count'])} evaluated cases."
        )

    lines.append("")

    return lines


def build_report() -> str:
    """
    Build Markdown report.
    """

    today = datetime.today().strftime("%Y-%m-%d")
    generated_at = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

    error_notes_df = load_error_notes()
    performance_df = build_performance_table(error_notes_df)

    lines = []

    lines.append(f"# Event-Type Performance Report - {today}")
    lines.append("")
    lines.append(f"Generated at: {generated_at}")
    lines.append("")

    lines.append("## Purpose")
    lines.append("")
    lines.append(
        "This report summarizes prediction performance by disclosure event type. "
        "It helps identify which event types have historically produced stronger or weaker prediction results."
    )
    lines.append("")

    lines.append("## Important Notice")
    lines.append("")
    lines.append(
        "This report is generated for research and portfolio purposes only. "
        "It is not financial advice or a buy/sell recommendation."
    )
    lines.append("")

    if error_notes_df.empty:
        lines.append("## Status")
        lines.append("")
        lines.append("No error-note data is available yet.")
        lines.append("")
        return "\n".join(lines)

    lines.extend(build_summary(error_notes_df, performance_df))

    lines.append("## Event-Type Performance Table")
    lines.append("")

    if performance_df.empty:
        lines.append("No performance table is available.")
        lines.append("")
        return "\n".join(lines)

    lines.append(
        "| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |"
    )
    lines.append("|---|---:|---:|---:|---:|---:|---:|---:|---:|---|")

    for _, row in performance_df.iterrows():
        success_rate = row.get("success_rate", None)

        if pd.isna(success_rate) or success_rate is None:
            success_rate_text = "N/A"
        else:
            success_rate_text = f"{success_rate * 100:.2f}%"

        lines.append(
            f"| {row.get('event_type', '')} "
            f"| {int(row.get('total_count', 0))} "
            f"| {int(row.get('evaluated_count', 0))} "
            f"| {int(row.get('success_count', 0))} "
            f"| {int(row.get('failure_count', 0))} "
            f"| {int(row.get('pending_count', 0))} "
            f"| {success_rate_text} "
            f"| {format_percent(row.get('avg_next_open_return', None))} "
            f"| {format_percent(row.get('avg_next_close_return', None))} "
            f"| {row.get('adjustment_bias', 'neutral')} |"
        )

    lines.append("")
    lines.append("## How to Read This Report")
    lines.append("")
    lines.append("- Total: total error-note rows for the event type.")
    lines.append("- Evaluated: rows with success or failure status.")
    lines.append("- Pending: rows waiting for next trading day price data.")
    lines.append("- Success Rate: success / evaluated rows.")
    lines.append("- Avg Next Open: average next-day open return.")
    lines.append("- Avg Next Close: average next-day close return.")
    lines.append("- Bias: confidence adjustment direction based on historical error notes.")
    lines.append("")

    lines.append("## Next Step")
    lines.append("")
    lines.append(
        "The next step is to use this report to improve event-type weights in the daily recommender."
    )
    lines.append("")

    return "\n".join(lines)


def save_report(report_text: str) -> str:
    """
    Save report to Markdown file.
    """

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    today = datetime.today().strftime("%Y-%m-%d")
    output_path = os.path.join(
        OUTPUT_DIR,
        f"{today}_event_type_performance_report.md",
    )

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(report_text)

    return output_path


def main():
    print("Generating event-type performance report...")

    report_text = build_report()
    output_path = save_report(report_text)

    print(f"Event-type performance report saved to: {output_path}")


if __name__ == "__main__":
    main()
