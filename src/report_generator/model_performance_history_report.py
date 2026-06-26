"""
Model performance history report.

This script builds a cumulative performance history report from
available prediction, evaluation, and score adjustment files.

Inputs:
data/processed/ml_dataset_*.csv
data/predictions/error_notes_*.csv
data/predictions/market_adjusted_evaluation_*.csv
data/processed/market_adjusted_score_adjustments_*.csv
data/processed/trading_volume_score_adjustments_*.csv
data/processed/automation_history.csv

Output:
reports/daily_review/YYYY-MM-DD_model_performance_history_report.md
"""

import os
from datetime import datetime
from pathlib import Path

import pandas as pd


PROCESSED_DIR = "data/processed"
PREDICTIONS_DIR = "data/predictions"
REPORT_DIR = "reports/daily_review"


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


def extract_date_from_filename(path: Path) -> str:
    """
    Extract date-like string from file name.
    """

    stem = path.stem
    parts = stem.split("_")

    for part in reversed(parts):
        if len(part) == 8 and part.isdigit():
            return f"{part[:4]}-{part[4:6]}-{part[6:8]}"

    return ""


def read_csv_files(directory: str, prefix: str) -> pd.DataFrame:
    """
    Read and concatenate CSV files matching prefix.
    """

    paths = sorted(Path(directory).glob(f"{prefix}*.csv"))

    frames = []

    for path in paths:
        try:
            df = pd.read_csv(path)
            df["source_file"] = str(path)
            df["source_date"] = extract_date_from_filename(path)
            frames.append(df)
        except Exception as error:
            print(f"Failed to read {path}: {error}")

    if not frames:
        return pd.DataFrame()

    result_df = pd.concat(frames, ignore_index=True)

    if "stock_code" in result_df.columns:
        result_df["stock_code"] = result_df["stock_code"].apply(normalize_stock_code)

    return result_df


def load_automation_history() -> pd.DataFrame:
    """
    Load automation history if available.
    """

    path = Path(PROCESSED_DIR) / "automation_history.csv"

    if not path.exists():
        return pd.DataFrame()

    try:
        return pd.read_csv(path)
    except Exception as error:
        print(f"Failed to read automation history: {error}")
        return pd.DataFrame()


def format_percent(value) -> str:
    """
    Format decimal value as percent.
    """

    try:
        if pd.isna(value):
            return "N/A"

        return f"{float(value) * 100:.2f}%"
    except Exception:
        return "N/A"


def safe_rate(numerator, denominator) -> float:
    """
    Calculate safe rate.
    """

    try:
        denominator = float(denominator)

        if denominator == 0:
            return 0.0

        return float(numerator) / denominator
    except Exception:
        return 0.0


def count_value(df: pd.DataFrame, column: str, value: str) -> int:
    """
    Count value in column.
    """

    if df.empty or column not in df.columns:
        return 0

    return int((df[column].astype(str) == value).sum())


def count_contains(df: pd.DataFrame, column: str, keyword: str) -> int:
    """
    Count rows where column contains keyword.
    """

    if df.empty or column not in df.columns:
        return 0

    return int(df[column].astype(str).str.contains(keyword, na=False).sum())


def build_summary_metrics(
    ml_df: pd.DataFrame,
    error_df: pd.DataFrame,
    market_eval_df: pd.DataFrame,
    market_score_df: pd.DataFrame,
    volume_score_df: pd.DataFrame,
) -> dict:
    """
    Build top-level summary metrics.
    """

    metrics = {}

    metrics["ml_dataset_rows"] = len(ml_df)
    metrics["error_note_rows"] = len(error_df)
    metrics["market_evaluation_rows"] = len(market_eval_df)
    metrics["market_score_rows"] = len(market_score_df)
    metrics["volume_score_rows"] = len(volume_score_df)

    if not error_df.empty and "prediction_result" in error_df.columns:
        metrics["prediction_success"] = count_value(error_df, "prediction_result", "success")
        metrics["prediction_failure"] = count_value(error_df, "prediction_result", "failure")
        metrics["prediction_pending"] = count_value(error_df, "prediction_result", "pending")

        evaluated = metrics["prediction_success"] + metrics["prediction_failure"]
        metrics["prediction_evaluated"] = evaluated
        metrics["prediction_success_rate"] = safe_rate(metrics["prediction_success"], evaluated)
    else:
        metrics["prediction_success"] = 0
        metrics["prediction_failure"] = 0
        metrics["prediction_pending"] = 0
        metrics["prediction_evaluated"] = 0
        metrics["prediction_success_rate"] = 0.0

    if not market_eval_df.empty and "market_adjusted_result" in market_eval_df.columns:
        metrics["market_adjusted_success"] = count_value(
            market_eval_df,
            "market_adjusted_result",
            "market_adjusted_success",
        )
        metrics["market_adjusted_failure"] = count_value(
            market_eval_df,
            "market_adjusted_result",
            "market_adjusted_failure",
        )
        metrics["market_driven_weak_success"] = count_value(
            market_eval_df,
            "market_adjusted_result",
            "market_driven_weak_success",
        )
        metrics["market_pending"] = count_value(
            market_eval_df,
            "market_adjusted_result",
            "pending",
        )
    else:
        metrics["market_adjusted_success"] = 0
        metrics["market_adjusted_failure"] = 0
        metrics["market_driven_weak_success"] = 0
        metrics["market_pending"] = 0

    if not market_score_df.empty and "market_adjusted_score_adjustment" in market_score_df.columns:
        score = pd.to_numeric(
            market_score_df["market_adjusted_score_adjustment"],
            errors="coerce",
        ).fillna(0)

        metrics["market_score_total"] = float(score.sum())
        metrics["market_score_average"] = float(score.mean())
    else:
        metrics["market_score_total"] = 0.0
        metrics["market_score_average"] = 0.0

    if not volume_score_df.empty and "trading_volume_score_adjustment" in volume_score_df.columns:
        score = pd.to_numeric(
            volume_score_df["trading_volume_score_adjustment"],
            errors="coerce",
        ).fillna(0)

        metrics["volume_score_total"] = float(score.sum())
        metrics["volume_score_average"] = float(score.mean())
    else:
        metrics["volume_score_total"] = 0.0
        metrics["volume_score_average"] = 0.0

    return metrics


def build_daily_counts(df: pd.DataFrame, date_col: str = "source_date") -> pd.DataFrame:
    """
    Build daily row counts.
    """

    if df.empty or date_col not in df.columns:
        return pd.DataFrame()

    result_df = (
        df.groupby(date_col)
        .size()
        .reset_index(name="row_count")
        .sort_values(date_col)
    )

    return result_df


def build_prediction_result_table(error_df: pd.DataFrame) -> pd.DataFrame:
    """
    Build prediction result count table.
    """

    if error_df.empty or "prediction_result" not in error_df.columns:
        return pd.DataFrame()

    return (
        error_df["prediction_result"]
        .value_counts(dropna=False)
        .reset_index()
        .rename(columns={"index": "prediction_result", "prediction_result": "count"})
    )


def build_market_result_table(market_eval_df: pd.DataFrame) -> pd.DataFrame:
    """
    Build market-adjusted result count table.
    """

    if market_eval_df.empty or "market_adjusted_result" not in market_eval_df.columns:
        return pd.DataFrame()

    return (
        market_eval_df["market_adjusted_result"]
        .value_counts(dropna=False)
        .reset_index()
        .rename(columns={"index": "market_adjusted_result", "market_adjusted_result": "count"})
    )


def build_volume_result_table(volume_score_df: pd.DataFrame) -> pd.DataFrame:
    """
    Build trading volume adjustment label count table.
    """

    if volume_score_df.empty or "trading_volume_adjustment_label" not in volume_score_df.columns:
        return pd.DataFrame()

    return (
        volume_score_df["trading_volume_adjustment_label"]
        .value_counts(dropna=False)
        .reset_index()
        .rename(columns={"index": "trading_volume_adjustment_label", "trading_volume_adjustment_label": "count"})
    )


def build_event_type_performance(error_df: pd.DataFrame) -> pd.DataFrame:
    """
    Build simple event-type performance table.
    """

    if error_df.empty:
        return pd.DataFrame()

    required = ["event_type", "prediction_result"]

    for col in required:
        if col not in error_df.columns:
            return pd.DataFrame()

    rows = []

    for event_type, group in error_df.groupby("event_type"):
        success = count_value(group, "prediction_result", "success")
        failure = count_value(group, "prediction_result", "failure")
        pending = count_value(group, "prediction_result", "pending")
        evaluated = success + failure

        rows.append(
            {
                "event_type": event_type,
                "total": len(group),
                "success": success,
                "failure": failure,
                "pending": pending,
                "evaluated": evaluated,
                "success_rate": safe_rate(success, evaluated),
            }
        )

    result_df = pd.DataFrame(rows)

    if not result_df.empty:
        result_df = result_df.sort_values(
            by=["evaluated", "success_rate"],
            ascending=[False, False],
        )

    return result_df


def add_markdown_table(lines: list, df: pd.DataFrame, columns: list, max_rows: int = 20):
    """
    Add dataframe as Markdown table.
    """

    if df.empty:
        lines.append("No data available.")
        lines.append("")
        return

    available_columns = [col for col in columns if col in df.columns]

    if not available_columns:
        lines.append("No displayable columns available.")
        lines.append("")
        return

    sample_df = df[available_columns].head(max_rows)

    lines.append("| " + " | ".join(available_columns) + " |")
    lines.append("|" + "|".join(["---"] * len(available_columns)) + "|")

    for _, row in sample_df.iterrows():
        values = []

        for col in available_columns:
            value = row[col]

            if "rate" in col:
                values.append(format_percent(value))
            elif isinstance(value, float):
                values.append(f"{value:.2f}")
            else:
                values.append(str(value))

        lines.append("| " + " | ".join(values) + " |")

    lines.append("")


def build_report(
    ml_df: pd.DataFrame,
    error_df: pd.DataFrame,
    market_eval_df: pd.DataFrame,
    market_score_df: pd.DataFrame,
    volume_score_df: pd.DataFrame,
    automation_df: pd.DataFrame,
) -> str:
    """
    Build Markdown report.
    """

    today = datetime.today().strftime("%Y-%m-%d")
    generated_at = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

    metrics = build_summary_metrics(
        ml_df,
        error_df,
        market_eval_df,
        market_score_df,
        volume_score_df,
    )

    lines = []

    lines.append(f"# Model Performance History Report - {today}")
    lines.append("")
    lines.append(f"Generated at: {generated_at}")
    lines.append("")

    lines.append("## Purpose")
    lines.append("")
    lines.append(
        "This report summarizes cumulative model, prediction, market-adjusted, and trading-volume performance history."
    )
    lines.append("")
    lines.append(
        "It is designed to track whether the project is accumulating enough evaluated cases to support better model training and recommendation logic."
    )
    lines.append("")

    lines.append("## Important Notice")
    lines.append("")
    lines.append(
        "This report is generated for research and portfolio purposes only. "
        "It is not financial advice or a buy/sell recommendation."
    )
    lines.append("")

    lines.append("## Summary Metrics")
    lines.append("")
    lines.append(f"- ML dataset rows: **{metrics['ml_dataset_rows']}**")
    lines.append(f"- Error-note rows: **{metrics['error_note_rows']}**")
    lines.append(f"- Market-adjusted evaluation rows: **{metrics['market_evaluation_rows']}**")
    lines.append(f"- Market-adjusted score rows: **{metrics['market_score_rows']}**")
    lines.append(f"- Trading volume score rows: **{metrics['volume_score_rows']}**")
    lines.append("")
    lines.append(f"- Prediction success: **{metrics['prediction_success']}**")
    lines.append(f"- Prediction failure: **{metrics['prediction_failure']}**")
    lines.append(f"- Prediction pending: **{metrics['prediction_pending']}**")
    lines.append(f"- Prediction evaluated: **{metrics['prediction_evaluated']}**")
    lines.append(f"- Prediction success rate: **{format_percent(metrics['prediction_success_rate'])}**")
    lines.append("")
    lines.append(f"- Market-adjusted success: **{metrics['market_adjusted_success']}**")
    lines.append(f"- Market-adjusted failure: **{metrics['market_adjusted_failure']}**")
    lines.append(f"- Market-driven weak success: **{metrics['market_driven_weak_success']}**")
    lines.append(f"- Market-adjusted pending: **{metrics['market_pending']}**")
    lines.append("")
    lines.append(f"- Total market-adjusted score adjustment: **{metrics['market_score_total']:.2f}**")
    lines.append(f"- Average market-adjusted score adjustment: **{metrics['market_score_average']:.2f}**")
    lines.append(f"- Total trading-volume score adjustment: **{metrics['volume_score_total']:.2f}**")
    lines.append(f"- Average trading-volume score adjustment: **{metrics['volume_score_average']:.2f}**")
    lines.append("")

    lines.append("## Data Accumulation by File Date")
    lines.append("")

    daily_counts = build_daily_counts(ml_df)

    add_markdown_table(
        lines,
        daily_counts,
        ["source_date", "row_count"],
        max_rows=30,
    )

    lines.append("## Prediction Result Counts")
    lines.append("")

    prediction_table = build_prediction_result_table(error_df)

    add_markdown_table(
        lines,
        prediction_table,
        ["prediction_result", "count"],
        max_rows=20,
    )

    lines.append("## Market-Adjusted Result Counts")
    lines.append("")

    market_table = build_market_result_table(market_eval_df)

    add_markdown_table(
        lines,
        market_table,
        ["market_adjusted_result", "count"],
        max_rows=20,
    )

    lines.append("## Trading Volume Adjustment Counts")
    lines.append("")

    volume_table = build_volume_result_table(volume_score_df)

    add_markdown_table(
        lines,
        volume_table,
        ["trading_volume_adjustment_label", "count"],
        max_rows=20,
    )

    lines.append("## Event-Type Performance Summary")
    lines.append("")

    event_table = build_event_type_performance(error_df)

    add_markdown_table(
        lines,
        event_table,
        [
            "event_type",
            "total",
            "success",
            "failure",
            "pending",
            "evaluated",
            "success_rate",
        ],
        max_rows=30,
    )

    lines.append("## Automation History")
    lines.append("")

    if automation_df.empty:
        lines.append("No automation history data available.")
        lines.append("")
    else:
        columns = list(automation_df.columns)
        add_markdown_table(
            lines,
            automation_df.tail(30),
            columns,
            max_rows=30,
        )

    lines.append("## Interpretation")
    lines.append("")
    lines.append("- A high pending count means the system needs more next-trading-day price data before performance can be judged.")
    lines.append("- A low evaluated count means the model should remain conservative.")
    lines.append("- Market-adjusted success is more meaningful than simple absolute-return success.")
    lines.append("- Trading-volume score adjustment is useful only when enough price and volume history is available.")
    lines.append("- The main goal at this stage is data accumulation and evaluation structure, not live trading performance.")
    lines.append("")

    lines.append("## Next Step")
    lines.append("")
    lines.append(
        "The next step is to prepare the final MVP summary and clean up the README after Day 30."
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
        f"{today}_model_performance_history_report.md",
    )

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(report_text)

    return output_path


def main():
    print("Generating model performance history report...")

    ml_df = read_csv_files(PROCESSED_DIR, "ml_dataset_")
    error_df = read_csv_files(PREDICTIONS_DIR, "error_notes_")
    market_eval_df = read_csv_files(PREDICTIONS_DIR, "market_adjusted_evaluation_")
    market_score_df = read_csv_files(PROCESSED_DIR, "market_adjusted_score_adjustments_")
    volume_score_df = read_csv_files(PROCESSED_DIR, "trading_volume_score_adjustments_")
    automation_df = load_automation_history()

    print(f"ML dataset rows: {len(ml_df)}")
    print(f"Error-note rows: {len(error_df)}")
    print(f"Market-adjusted evaluation rows: {len(market_eval_df)}")
    print(f"Market-adjusted score rows: {len(market_score_df)}")
    print(f"Trading-volume score rows: {len(volume_score_df)}")
    print(f"Automation history rows: {len(automation_df)}")

    report_text = build_report(
        ml_df,
        error_df,
        market_eval_df,
        market_score_df,
        volume_score_df,
        automation_df,
    )

    report_path = save_report(report_text)

    print(f"Model performance history report saved to: {report_path}")


if __name__ == "__main__":
    main()
