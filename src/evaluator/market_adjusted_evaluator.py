"""
Market-adjusted evaluator.

This script evaluates prediction results using market-adjusted returns.

Input:
data/processed/market_adjusted_features_YYYYMMDD.csv

Output:
data/predictions/market_adjusted_evaluation_YYYYMMDD.csv
reports/daily_review/YYYY-MM-DD_market_adjusted_evaluation_report.md
"""

import os
from datetime import datetime

import pandas as pd


PROCESSED_DIR = "data/processed"
PREDICTIONS_DIR = "data/predictions"
REPORT_DIR = "reports/daily_review"


POSITIVE_DIRECTIONS = [
    "positive",
    "neutral_positive",
]

NEGATIVE_DIRECTIONS = [
    "negative",
]

VOLATILE_DIRECTIONS = [
    "volatile",
]


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


def safe_float(value, default=None):
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


def load_latest_market_adjusted_features():
    """
    Load latest market-adjusted feature file.
    """

    path = get_latest_file(PROCESSED_DIR, "market_adjusted_features_")

    if path is None:
        return pd.DataFrame(), ""

    df = pd.read_csv(path)

    return df, path


def classify_market_adjusted_result(row) -> str:
    """
    Classify prediction result using market-adjusted next close return.
    """

    prediction_direction = str(row.get("prediction_direction", "unknown"))

    stock_return = safe_float(row.get("next_close_return", None))
    market_return = safe_float(row.get("market_next_close_return", None))
    excess_return = safe_float(row.get("market_adjusted_next_close_return", None))

    if stock_return is None:
        return "pending"

    if excess_return is None:
        return "market_data_missing"

    if prediction_direction in POSITIVE_DIRECTIONS:
        if stock_return > 0 and excess_return > 0:
            return "market_adjusted_success"

        if stock_return > 0 and excess_return <= 0:
            return "market_driven_weak_success"

        if stock_return <= 0 and excess_return > 0:
            return "relative_success_but_absolute_loss"

        return "market_adjusted_failure"

    if prediction_direction in NEGATIVE_DIRECTIONS:
        if stock_return < 0 and excess_return < 0:
            return "market_adjusted_success"

        if stock_return < 0 and excess_return >= 0:
            return "market_driven_weak_success"

        if stock_return >= 0 and excess_return < 0:
            return "relative_failure_despite_absolute_gain"

        return "market_adjusted_failure"

    if prediction_direction in VOLATILE_DIRECTIONS:
        if abs(excess_return) >= 0.02:
            return "market_adjusted_volatility_success"

        if abs(stock_return) >= 0.02 and abs(excess_return) < 0.02:
            return "market_driven_volatility"

        return "volatility_overestimated"

    return "unknown"


def build_market_adjusted_reason(row) -> str:
    """
    Build explanation text for market-adjusted evaluation.
    """

    prediction_direction = str(row.get("prediction_direction", "unknown"))
    original_result = str(row.get("prediction_result", "unknown"))
    adjusted_result = str(row.get("market_adjusted_result", "unknown"))

    stock_return = row.get("next_close_return", None)
    market_return = row.get("market_next_close_return", None)
    excess_return = row.get("market_adjusted_next_close_return", None)
    market_group = row.get("market_group", "UNKNOWN")
    market_source_type = row.get("market_source_type", "unknown")

    base = (
        f"Original result was `{original_result}` and prediction direction was "
        f"`{prediction_direction}`. Stock next close return was {format_percent(stock_return)}, "
        f"{market_group} market return was {format_percent(market_return)}, "
        f"and market-adjusted return was {format_percent(excess_return)}. "
        f"Market source type was `{market_source_type}`."
    )

    mapping = {
        "market_adjusted_success": (
            "The stock moved in the predicted direction and also outperformed the market benchmark."
        ),
        "market_driven_weak_success": (
            "The stock moved in the expected absolute direction, but it did not outperform the market. This may be a market-driven move rather than a strong event-driven reaction."
        ),
        "relative_success_but_absolute_loss": (
            "The stock lost money in absolute terms, but it outperformed the market. This may indicate relative strength despite a weak market."
        ),
        "market_adjusted_failure": (
            "The stock did not move favorably after adjusting for market movement."
        ),
        "relative_failure_despite_absolute_gain": (
            "The stock gained in absolute terms, but underperformed the market. The original result may look positive, but market-adjusted performance is weak."
        ),
        "market_adjusted_volatility_success": (
            "The event produced meaningful movement relative to the market."
        ),
        "market_driven_volatility": (
            "The stock moved, but the movement appears largely explained by market-wide movement."
        ),
        "volatility_overestimated": (
            "The expected volatility did not appear strongly after market adjustment."
        ),
        "market_data_missing": (
            "Market data was not available, so market-adjusted evaluation could not be completed."
        ),
        "pending": (
            "Stock return data is not available yet, so the case remains pending."
        ),
    }

    return base + " " + mapping.get(
        adjusted_result,
        "This case requires manual review.",
    )


def build_market_adjusted_learning_point(row) -> str:
    """
    Build learning point.
    """

    result = str(row.get("market_adjusted_result", "unknown"))

    mapping = {
        "market_adjusted_success": (
            "This case should be treated as a stronger success because the stock outperformed the market."
        ),
        "market_driven_weak_success": (
            "Absolute success should be treated more conservatively when the stock fails to outperform the market."
        ),
        "relative_success_but_absolute_loss": (
            "A negative absolute return may still contain useful signal if the stock outperforms a falling market."
        ),
        "market_adjusted_failure": (
            "This case should reduce confidence because the stock failed after market adjustment."
        ),
        "relative_failure_despite_absolute_gain": (
            "A positive absolute return can still be weak if the broader market performed better."
        ),
        "market_adjusted_volatility_success": (
            "Volatility predictions should be evaluated using excess movement, not only absolute stock movement."
        ),
        "market_driven_volatility": (
            "Large absolute movement may be caused by market-wide movement and should not always count as event-driven volatility."
        ),
        "volatility_overestimated": (
            "Volatility confidence should be reduced when market-adjusted movement is small."
        ),
        "market_data_missing": (
            "Market-adjusted evaluation should be retried when market data becomes available."
        ),
        "pending": (
            "Do not update market-adjusted confidence until stock return data becomes available."
        ),
    }

    return mapping.get(
        result,
        "Review this case manually before updating market-adjusted rules.",
    )


def build_market_adjusted_confidence(row) -> str:
    """
    Suggest confidence adjustment using market-adjusted result.
    """

    result = str(row.get("market_adjusted_result", "unknown"))

    if result == "market_adjusted_success":
        return "increase"

    if result in [
        "market_driven_weak_success",
        "relative_success_but_absolute_loss",
        "market_adjusted_volatility_success",
    ]:
        return "slightly_increase"

    if result in [
        "market_adjusted_failure",
        "relative_failure_despite_absolute_gain",
        "volatility_overestimated",
    ]:
        return "decrease"

    if result in [
        "market_driven_volatility",
        "market_data_missing",
        "pending",
    ]:
        return "hold"

    return "hold"


def generate_market_adjusted_evaluation():
    """
    Generate market-adjusted evaluation dataframe.
    """

    df, source_path = load_latest_market_adjusted_features()

    if df.empty:
        return pd.DataFrame(), source_path

    df = df.copy()

    df["market_adjusted_result"] = df.apply(
        classify_market_adjusted_result,
        axis=1,
    )

    df["market_adjusted_reason"] = df.apply(
        build_market_adjusted_reason,
        axis=1,
    )

    df["market_adjusted_learning_point"] = df.apply(
        build_market_adjusted_learning_point,
        axis=1,
    )

    df["market_adjusted_confidence_adjustment"] = df.apply(
        build_market_adjusted_confidence,
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
        "market_group_source",
        "market_source_type",
        "market_proxy_name",
        "next_close_return",
        "market_next_close_return",
        "market_adjusted_next_close_return",
        "market_adjusted_reason",
        "market_adjusted_learning_point",
        "confidence_adjustment",
        "market_adjusted_confidence_adjustment",
    ]

    available_columns = [
        col for col in output_columns
        if col in df.columns
    ]

    return df[available_columns].copy(), source_path


def save_evaluation(df: pd.DataFrame) -> str:
    """
    Save evaluation CSV.
    """

    os.makedirs(PREDICTIONS_DIR, exist_ok=True)

    today = datetime.today().strftime("%Y%m%d")
    output_path = os.path.join(
        PREDICTIONS_DIR,
        f"market_adjusted_evaluation_{today}.csv",
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

    lines.append(f"# Market-Adjusted Evaluation Report - {today}")
    lines.append("")
    lines.append(f"Generated at: {generated_at}")
    lines.append("")
    lines.append(f"Source feature file: `{source_path if source_path else 'Not found'}`")
    lines.append("")

    lines.append("## Purpose")
    lines.append("")
    lines.append(
        "This report evaluates prediction results using market-adjusted returns. "
        "It helps distinguish event-driven stock reactions from broader market movement."
    )
    lines.append("")

    lines.append("## Important Notice")
    lines.append("")
    lines.append(
        "This report is generated for research and portfolio purposes only. "
        "It is not financial advice or a buy/sell recommendation."
    )
    lines.append("")

    if df.empty:
        lines.append("## Status")
        lines.append("")
        lines.append("No market-adjusted evaluation data is available yet.")
        lines.append("")
        return "\n".join(lines)

    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Total rows: **{len(df)}**")

    if "market_adjusted_result" in df.columns:
        counts = df["market_adjusted_result"].value_counts(dropna=False)
        for result, count in counts.items():
            lines.append(f"- {result}: **{count}**")

    lines.append("")

    lines.append("## Interpretation")
    lines.append("")
    lines.append("- `market_adjusted_success`: stock moved correctly and outperformed the market.")
    lines.append("- `market_driven_weak_success`: stock moved correctly but did not outperform the market.")
    lines.append("- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.")
    lines.append("- `market_adjusted_failure`: stock failed after adjusting for market movement.")
    lines.append("- `market_driven_volatility`: movement may be mostly explained by market-wide movement.")
    lines.append("")

    lines.append("## Sample Rows")
    lines.append("")

    sample_columns = [
        "event_date",
        "stock_code",
        "corp_name",
        "prediction_direction",
        "prediction_result",
        "market_adjusted_result",
        "next_close_return",
        "market_next_close_return",
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
        "The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring."
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
        f"{today}_market_adjusted_evaluation_report.md",
    )

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(report_text)

    return output_path


def main():
    print("Generating market-adjusted evaluation...")

    df, source_path = generate_market_adjusted_evaluation()

    if df.empty:
        print("No market-adjusted evaluation generated.")
        print(f"Source feature file: {source_path if source_path else 'Not found'}")

    else:
        evaluation_path = save_evaluation(df)
        print(f"Market-adjusted evaluation saved to: {evaluation_path}")
        print(f"Rows: {len(df)}")

        if "market_adjusted_result" in df.columns:
            print("")
            print("Market-adjusted result counts:")
            print(df["market_adjusted_result"].value_counts(dropna=False))

    report_text = build_report(df, source_path)
    report_path = save_report(report_text)

    print(f"Market-adjusted evaluation report saved to: {report_path}")


if __name__ == "__main__":
    main()
