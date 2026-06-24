"""
Stock-specific historical pattern report.

This script summarizes historical prediction and event-reaction patterns
by stock code.

Input:
data/predictions/error_notes_YYYYMMDD.csv

Output:
reports/daily_review/YYYY-MM-DD_stock_pattern_report.md
"""

import os
from datetime import datetime

import pandas as pd


PREDICTIONS_DIR = "data/predictions"
OUTPUT_DIR = "reports/daily_review"


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

            if "stock_code" in df.columns:
                df["stock_code"] = df["stock_code"].apply(normalize_stock_code)

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


def most_common_value(series: pd.Series) -> str:
    """
    Return most common non-empty value.
    """

    if series.empty:
        return "N/A"

    cleaned = series.dropna().astype(str)
    cleaned = cleaned[cleaned.str.strip() != ""]

    if cleaned.empty:
        return "N/A"

    return cleaned.value_counts().index[0]


def build_stock_pattern_table(df: pd.DataFrame) -> pd.DataFrame:
    """
    Build stock-level historical pattern table.
    """

    if df.empty:
        return pd.DataFrame()

    required_columns = [
        "stock_code",
        "prediction_result",
        "next_open_return",
        "next_close_return",
        "event_type",
    ]

    for col in required_columns:
        if col not in df.columns:
            df[col] = pd.NA

    work_df = df.copy()

    work_df["stock_code"] = work_df["stock_code"].apply(normalize_stock_code)
    work_df["prediction_result"] = work_df["prediction_result"].astype(str)
    work_df["next_open_return"] = pd.to_numeric(
        work_df["next_open_return"],
        errors="coerce",
    )
    work_df["next_close_return"] = pd.to_numeric(
        work_df["next_close_return"],
        errors="coerce",
    )

    if "corp_name" not in work_df.columns:
        work_df["corp_name"] = "Unknown"

    if "confidence_adjustment" not in work_df.columns:
        work_df["confidence_adjustment"] = "unknown"

    rows = []

    for stock_code, group in work_df.groupby("stock_code"):
        if not stock_code:
            continue

        corp_name = most_common_value(group["corp_name"])

        total_count = len(group)
        success_count = (group["prediction_result"] == "success").sum()
        failure_count = (group["prediction_result"] == "failure").sum()
        pending_count = (group["prediction_result"] == "pending").sum()
        evaluated_count = success_count + failure_count

        if evaluated_count > 0:
            success_rate = success_count / evaluated_count
        else:
            success_rate = None

        avg_next_open_return = group["next_open_return"].mean()
        avg_next_close_return = group["next_close_return"].mean()

        most_common_event_type = most_common_value(group["event_type"])

        increase_count = (group["confidence_adjustment"] == "increase").sum()
        decrease_count = (group["confidence_adjustment"] == "decrease").sum()
        slightly_decrease_count = (
            group["confidence_adjustment"] == "slightly_decrease"
        ).sum()
        hold_count = (group["confidence_adjustment"] == "hold").sum()

        risk_note = "not_enough_data"

        if pending_count == total_count:
            risk_note = "mostly_pending"
        elif evaluated_count > 0 and failure_count > success_count:
            risk_note = "weak_historical_reaction"
        elif evaluated_count > 0 and success_count > failure_count:
            risk_note = "relatively_positive_history"
        elif decrease_count + slightly_decrease_count > increase_count:
            risk_note = "conservative_confidence_bias"

        rows.append(
            {
                "stock_code": stock_code,
                "corp_name": corp_name,
                "total_count": total_count,
                "evaluated_count": evaluated_count,
                "success_count": success_count,
                "failure_count": failure_count,
                "pending_count": pending_count,
                "success_rate": success_rate,
                "avg_next_open_return": avg_next_open_return,
                "avg_next_close_return": avg_next_close_return,
                "most_common_event_type": most_common_event_type,
                "increase_count": increase_count,
                "decrease_count": decrease_count,
                "slightly_decrease_count": slightly_decrease_count,
                "hold_count": hold_count,
                "risk_note": risk_note,
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


def build_summary(error_notes_df: pd.DataFrame, stock_pattern_df: pd.DataFrame) -> list:
    """
    Build summary section.
    """

    lines = []

    total_rows = len(error_notes_df)
    total_stocks = 0 if stock_pattern_df.empty else len(stock_pattern_df)

    lines.append("## Overall Summary")
    lines.append("")
    lines.append(f"- Total error-note rows: **{total_rows}**")
    lines.append(f"- Number of stocks in history: **{total_stocks}**")

    if stock_pattern_df.empty:
        lines.append("- Evaluated stock patterns: **0**")
        lines.append("")
        return lines

    evaluated_stocks = stock_pattern_df[
        stock_pattern_df["evaluated_count"] > 0
    ]

    pending_only_stocks = stock_pattern_df[
        stock_pattern_df["pending_count"] == stock_pattern_df["total_count"]
    ]

    lines.append(f"- Stocks with evaluated reactions: **{len(evaluated_stocks)}**")
    lines.append(f"- Stocks with pending-only reactions: **{len(pending_only_stocks)}**")
    lines.append("")

    if evaluated_stocks.empty:
        lines.append(
            "Most stock-level rows are still pending. Stock-level success rates will become meaningful after next-day price reactions are evaluated."
        )
        lines.append("")
        return lines

    best_stocks = evaluated_stocks.sort_values(
        by=["success_rate", "evaluated_count"],
        ascending=False,
    ).head(5)

    weak_stocks = evaluated_stocks.sort_values(
        by=["success_rate", "evaluated_count"],
        ascending=[True, False],
    ).head(5)

    lines.append("## Stronger Stock Patterns So Far")
    lines.append("")

    for _, row in best_stocks.iterrows():
        success_rate = row.get("success_rate", None)

        if pd.isna(success_rate) or success_rate is None:
            success_rate_text = "N/A"
        else:
            success_rate_text = f"{success_rate * 100:.2f}%"

        lines.append(
            f"- {row['corp_name']} ({row['stock_code']}): success rate "
            f"{success_rate_text}, evaluated cases {int(row['evaluated_count'])}."
        )

    lines.append("")
    lines.append("## Weaker Stock Patterns So Far")
    lines.append("")

    for _, row in weak_stocks.iterrows():
        success_rate = row.get("success_rate", None)

        if pd.isna(success_rate) or success_rate is None:
            success_rate_text = "N/A"
        else:
            success_rate_text = f"{success_rate * 100:.2f}%"

        lines.append(
            f"- {row['corp_name']} ({row['stock_code']}): success rate "
            f"{success_rate_text}, evaluated cases {int(row['evaluated_count'])}."
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
    stock_pattern_df = build_stock_pattern_table(error_notes_df)

    lines = []

    lines.append(f"# Stock-Specific Historical Pattern Report - {today}")
    lines.append("")
    lines.append(f"Generated at: {generated_at}")
    lines.append("")

    lines.append("## Purpose")
    lines.append("")
    lines.append(
        "This report summarizes historical prediction and event-reaction patterns by stock code. "
        "It helps identify whether specific stocks tend to react differently to disclosure events."
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

    lines.extend(build_summary(error_notes_df, stock_pattern_df))

    lines.append("## Stock Pattern Table")
    lines.append("")

    if stock_pattern_df.empty:
        lines.append("No stock pattern table is available.")
        lines.append("")
        return "\n".join(lines)

    lines.append(
        "| Stock | Company | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Common Event | Risk Note |"
    )
    lines.append("|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|")

    for _, row in stock_pattern_df.iterrows():
        success_rate = row.get("success_rate", None)

        if pd.isna(success_rate) or success_rate is None:
            success_rate_text = "N/A"
        else:
            success_rate_text = f"{success_rate * 100:.2f}%"

        lines.append(
            f"| {row.get('stock_code', '')} "
            f"| {row.get('corp_name', '')} "
            f"| {int(row.get('total_count', 0))} "
            f"| {int(row.get('evaluated_count', 0))} "
            f"| {int(row.get('success_count', 0))} "
            f"| {int(row.get('failure_count', 0))} "
            f"| {int(row.get('pending_count', 0))} "
            f"| {success_rate_text} "
            f"| {format_percent(row.get('avg_next_open_return', None))} "
            f"| {format_percent(row.get('avg_next_close_return', None))} "
            f"| {row.get('most_common_event_type', 'N/A')} "
            f"| {row.get('risk_note', 'N/A')} |"
        )

    lines.append("")
    lines.append("## How to Read This Report")
    lines.append("")
    lines.append("- Total: total error-note rows for the stock.")
    lines.append("- Evaluated: rows with success or failure status.")
    lines.append("- Pending: rows waiting for next trading day price data.")
    lines.append("- Success Rate: success / evaluated rows.")
    lines.append("- Avg Next Open: average next-day open return for the stock.")
    lines.append("- Avg Next Close: average next-day close return for the stock.")
    lines.append("- Common Event: most frequent event type for the stock.")
    lines.append("- Risk Note: simple stock-level historical interpretation.")
    lines.append("")

    lines.append("## Next Step")
    lines.append("")
    lines.append(
        "The next step is to use stock-specific patterns as another adjustment layer in the daily recommender."
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
        f"{today}_stock_pattern_report.md",
    )

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(report_text)

    return output_path


def main():
    print("Generating stock-specific historical pattern report...")

    report_text = build_report()
    output_path = save_report(report_text)

    print(f"Stock-specific historical pattern report saved to: {output_path}")


if __name__ == "__main__":
    main()
