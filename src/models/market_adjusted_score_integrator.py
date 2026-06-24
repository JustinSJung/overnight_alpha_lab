"""
Market-adjusted score integrator.

This script converts market-adjusted evaluation results into
recommendation score adjustment signals.

Input:
data/predictions/market_adjusted_evaluation_YYYYMMDD.csv

Outputs:
data/processed/market_adjusted_score_adjustments_YYYYMMDD.csv
reports/daily_review/YYYY-MM-DD_market_adjusted_score_report.md
"""

import os
from datetime import datetime

import pandas as pd


PREDICTIONS_DIR = "data/predictions"
PROCESSED_DIR = "data/processed"
REPORT_DIR = "reports/daily_review"


SCORE_RULES = {
    "market_adjusted_success": 15,
    "market_driven_weak_success": -5,
    "relative_success_but_absolute_loss": 5,
    "market_adjusted_failure": -15,
    "relative_failure_despite_absolute_gain": -10,
    "market_adjusted_volatility_success": 10,
    "market_driven_volatility": -5,
    "volatility_overestimated": -10,
    "market_data_missing": 0,
    "pending": 0,
    "unknown": 0,
}


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


def load_latest_market_adjusted_evaluation():
    """
    Load latest market-adjusted evaluation file.
    """

    path = get_latest_file(
        PREDICTIONS_DIR,
        "market_adjusted_evaluation_",
    )

    if path is None:
        return pd.DataFrame(), ""

    df = pd.read_csv(path)

    if "stock_code" in df.columns:
        df["stock_code"] = df["stock_code"].apply(normalize_stock_code)

    return df, path


def calculate_adjustment_score(row) -> int:
    """
    Calculate market-adjusted score adjustment.
    """

    result = str(row.get("market_adjusted_result", "unknown"))

    return SCORE_RULES.get(result, 0)


def calculate_strength_label(score: int) -> str:
    """
    Convert score to label.
    """

    if score >= 15:
        return "strong_positive_adjustment"

    if score >= 5:
        return "mild_positive_adjustment"

    if score <= -15:
        return "strong_negative_adjustment"

    if score <= -5:
        return "mild_negative_adjustment"

    return "neutral_adjustment"


def build_adjustment_reason(row) -> str:
    """
    Build explanation for score adjustment.
    """

    result = str(row.get("market_adjusted_result", "unknown"))
    score = row.get("market_adjusted_score_adjustment", 0)

    stock_return = row.get("next_close_return", None)
    market_return = row.get("market_next_close_return", None)
    adjusted_return = row.get("market_adjusted_next_close_return", None)

    base = (
        f"Market-adjusted result is `{result}`. "
        f"Stock return was {format_percent(stock_return)}, "
        f"market return was {format_percent(market_return)}, "
        f"and market-adjusted return was {format_percent(adjusted_return)}. "
        f"Score adjustment is {score}."
    )

    explanations = {
        "market_adjusted_success": (
            " The prediction deserves a positive adjustment because the stock outperformed the market in the expected direction."
        ),
        "market_driven_weak_success": (
            " The prediction should be treated more conservatively because the absolute move may have been driven by the broader market."
        ),
        "relative_success_but_absolute_loss": (
            " The stock fell in absolute terms but showed relative strength against the market."
        ),
        "market_adjusted_failure": (
            " The prediction deserves a negative adjustment because it failed after market movement was considered."
        ),
        "relative_failure_despite_absolute_gain": (
            " The stock gained in absolute terms but underperformed the broader market."
        ),
        "market_adjusted_volatility_success": (
            " The event produced meaningful excess movement compared with the market."
        ),
        "market_driven_volatility": (
            " The stock moved, but the movement may mostly reflect market-wide volatility."
        ),
        "volatility_overestimated": (
            " The expected volatility was not strong after adjusting for market movement."
        ),
        "market_data_missing": (
            " No score change is applied because market data is missing."
        ),
        "pending": (
            " No score change is applied because stock return data is not available yet."
        ),
    }

    return base + explanations.get(
        result,
        " This case requires manual review.",
    )


def build_score_adjustments(df: pd.DataFrame) -> pd.DataFrame:
    """
    Build market-adjusted score adjustment dataframe.
    """

    if df.empty:
        return pd.DataFrame()

    result_df = df.copy()

    if "stock_code" in result_df.columns:
        result_df["stock_code"] = result_df["stock_code"].apply(normalize_stock_code)

    if "market_adjusted_result" not in result_df.columns:
        result_df["market_adjusted_result"] = "unknown"

    result_df["market_adjusted_score_adjustment"] = result_df.apply(
        calculate_adjustment_score,
        axis=1,
    )

    result_df["market_adjusted_adjustment_label"] = result_df[
        "market_adjusted_score_adjustment"
    ].apply(calculate_strength_label)

    result_df["market_adjusted_adjustment_reason"] = result_df.apply(
        build_adjustment_reason,
        axis=1,
    )

    output_columns = [
        "event_date",
        "stock_code",
        "corp_name",
        "event_type",
        "report_nm",
        "prediction_direction",
        "prediction_result",
        "market_adjusted_result",
        "market_group",
        "market_source_type",
        "market_proxy_name",
        "next_close_return",
        "market_next_close_return",
        "market_adjusted_next_close_return",
        "market_adjusted_score_adjustment",
        "market_adjusted_adjustment_label",
        "market_adjusted_adjustment_reason",
    ]

    available_columns = [
        col for col in output_columns
        if col in result_df.columns
    ]

    return result_df[available_columns].copy()


def save_adjustments(df: pd.DataFrame) -> str:
    """
    Save adjustment CSV.
    """

    os.makedirs(PROCESSED_DIR, exist_ok=True)

    today = datetime.today().strftime("%Y%m%d")
    output_path = os.path.join(
        PROCESSED_DIR,
        f"market_adjusted_score_adjustments_{today}.csv",
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

    lines.append(f"# Market-Adjusted Score Integration Report - {today}")
    lines.append("")
    lines.append(f"Generated at: {generated_at}")
    lines.append("")
    lines.append(f"Source evaluation file: `{source_path if source_path else 'Not found'}`")
    lines.append("")

    lines.append("## Purpose")
    lines.append("")
    lines.append(
        "This report converts market-adjusted evaluation results into recommendation score adjustment signals."
    )
    lines.append("")
    lines.append(
        "The goal is to reward predictions that outperform the market and penalize results that only appear successful because of broader market movement."
    )
    lines.append("")

    lines.append("## Score Rules")
    lines.append("")
    lines.append("| Market-Adjusted Result | Score Adjustment |")
    lines.append("|---|---:|")

    for result, score in SCORE_RULES.items():
        lines.append(f"| {result} | {score} |")

    lines.append("")

    if df.empty:
        lines.append("## Status")
        lines.append("")
        lines.append("No market-adjusted score adjustment data is available yet.")
        lines.append("")
        return "\n".join(lines)

    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Total rows: **{len(df)}**")

    if "market_adjusted_score_adjustment" in df.columns:
        total_score = df["market_adjusted_score_adjustment"].sum()
        avg_score = df["market_adjusted_score_adjustment"].mean()

        lines.append(f"- Total adjustment score: **{total_score:.2f}**")
        lines.append(f"- Average adjustment score: **{avg_score:.2f}**")

    lines.append("")

    if "market_adjusted_adjustment_label" in df.columns:
        lines.append("## Adjustment Label Counts")
        lines.append("")

        counts = df["market_adjusted_adjustment_label"].value_counts(dropna=False)

        for label, count in counts.items():
            lines.append(f"- {label}: **{count}**")

        lines.append("")

    if "market_adjusted_result" in df.columns:
        lines.append("## Market-Adjusted Result Counts")
        lines.append("")

        counts = df["market_adjusted_result"].value_counts(dropna=False)

        for result, count in counts.items():
            lines.append(f"- {result}: **{count}**")

        lines.append("")

    lines.append("## Sample Rows")
    lines.append("")

    sample_columns = [
        "event_date",
        "stock_code",
        "corp_name",
        "prediction_direction",
        "market_adjusted_result",
        "market_adjusted_score_adjustment",
        "market_adjusted_next_close_return",
    ]

    available_columns = [
        col for col in sample_columns
        if col in df.columns
    ]

    if not available_columns:
        lines.append("No displayable columns available.")
        lines.append("")
    else:
        sample_df = df[available_columns].head(20)

        lines.append("| " + " | ".join(available_columns) + " |")
        lines.append("|" + "|".join(["---"] * len(available_columns)) + "|")

        for _, row in sample_df.iterrows():
            values = []

            for col in available_columns:
                value = row[col]

                if col.endswith("return"):
                    values.append(format_percent(value))
                else:
                    values.append(str(value))

            lines.append("| " + " | ".join(values) + " |")

        lines.append("")

    lines.append("## Next Step")
    lines.append("")
    lines.append(
        "The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score."
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
        f"{today}_market_adjusted_score_report.md",
    )

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(report_text)

    return output_path


def main():
    print("Generating market-adjusted score adjustments...")

    evaluation_df, source_path = load_latest_market_adjusted_evaluation()

    print(f"Latest market-adjusted evaluation: {source_path if source_path else 'Not found'}")

    adjustment_df = build_score_adjustments(evaluation_df)

    if adjustment_df.empty:
        print("No market-adjusted score adjustments generated.")
    else:
        output_path = save_adjustments(adjustment_df)
        print(f"Market-adjusted score adjustments saved to: {output_path}")
        print(f"Rows: {len(adjustment_df)}")

        if "market_adjusted_adjustment_label" in adjustment_df.columns:
            print("")
            print("Adjustment label counts:")
            print(adjustment_df["market_adjusted_adjustment_label"].value_counts(dropna=False))

    report_text = build_report(adjustment_df, source_path)
    report_path = save_report(report_text)

    print(f"Market-adjusted score report saved to: {report_path}")


if __name__ == "__main__":
    main()
