"""
Single stock predictor.

This script generates a focused stock-level prediction report
for a user-provided stock code.

Example:
python src/models/single_stock_predictor.py 005930

Output:
reports/single_stock/YYYY-MM-DD_005930_single_stock_report.md
"""

import os
import sys
from datetime import datetime

import pandas as pd


PROCESSED_DIR = "data/processed"
OUTPUT_DIR = "reports/single_stock"


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


def load_latest_ml_dataset():
    """
    Load latest ML dataset.
    """

    ml_dataset_path = get_latest_file(PROCESSED_DIR, "ml_dataset_")

    if ml_dataset_path is None:
        return pd.DataFrame(), ""

    try:
        df = pd.read_csv(ml_dataset_path)

        if "stock_code" in df.columns:
            df["stock_code"] = df["stock_code"].apply(normalize_stock_code)

        return df, ml_dataset_path
    except Exception:
        return pd.DataFrame(), ml_dataset_path


def safe_number(value, default=0.0) -> float:
    """
    Convert value to float safely.
    """

    try:
        if pd.isna(value):
            return default

        return float(value)
    except Exception:
        return default


def calculate_single_stock_score(row) -> float:
    """
    Calculate simple single-stock score.
    """

    event_score = safe_number(row.get("event_score", 0))
    news_sentiment_score = safe_number(row.get("news_sentiment_score", 0))
    news_attention_score = safe_number(row.get("news_attention_score", 0))
    negative_keyword_count = safe_number(row.get("negative_keyword_count", 0))

    score = event_score
    score += news_sentiment_score * 5
    score += min(news_attention_score, 10) * 2
    score -= negative_keyword_count * 3

    direction = str(row.get("prediction_direction", ""))

    if direction in POSITIVE_DIRECTIONS:
        score += 10
    elif direction in NEGATIVE_DIRECTIONS:
        score -= 10
    elif direction in VOLATILE_DIRECTIONS:
        score -= 5

    return score


def classify_risk_level(row) -> str:
    """
    Classify risk level.
    """

    event_type = str(row.get("event_type", ""))
    prediction_direction = str(row.get("prediction_direction", ""))
    negative_keywords = safe_number(row.get("negative_keyword_count", 0))
    score = safe_number(row.get("single_stock_score", 0))

    high_risk_events = [
        "paid_in_capital_increase",
        "convertible_bond",
        "bond_with_warrant",
        "lawsuit",
        "disclosure_violation",
    ]

    if event_type in high_risk_events:
        return "HIGH"

    if prediction_direction == "negative":
        return "HIGH"

    if negative_keywords >= 3:
        return "HIGH"

    if prediction_direction == "volatile":
        return "MEDIUM"

    if score < 30:
        return "MEDIUM"

    return "LOW"


def classify_single_stock_view(row) -> str:
    """
    Classify single stock view.
    """

    direction = str(row.get("prediction_direction", ""))
    risk_level = str(row.get("risk_level", ""))
    score = safe_number(row.get("single_stock_score", 0))

    if risk_level == "HIGH":
        return "RISK_REVIEW"

    if direction in POSITIVE_DIRECTIONS and score >= 60:
        return "POSITIVE_VIEW"

    if direction == "volatile":
        return "VOLATILE_WATCH"

    if score >= 40:
        return "WATCHLIST"

    return "WEAK_SIGNAL"


def format_percent(value) -> str:
    """
    Format return value as percent.
    """

    try:
        if pd.isna(value):
            return "Not available"

        return f"{float(value) * 100:.2f}%"
    except Exception:
        return "Not available"


def build_interpretation(row) -> str:
    """
    Build human-readable interpretation.
    """

    event_type = row.get("event_type", "unknown")
    direction = row.get("prediction_direction", "unknown")
    score = safe_number(row.get("single_stock_score", 0))
    risk_level = row.get("risk_level", "UNKNOWN")
    news_sentiment_score = safe_number(row.get("news_sentiment_score", 0))
    news_attention_score = safe_number(row.get("news_attention_score", 0))

    sentences = []

    sentences.append(
        f"The latest available event is classified as `{event_type}` with expected direction `{direction}`."
    )

    sentences.append(
        f"The current rule-based single-stock score is {score:.2f}, and the risk level is {risk_level}."
    )

    if news_attention_score > 0:
        sentences.append(
            f"Related news attention is present with a score of {news_attention_score:.0f}."
        )
    else:
        sentences.append(
            "There is little or no related news attention in the current dataset."
        )

    if news_sentiment_score > 0:
        sentences.append(
            f"News sentiment is positive with a score of {news_sentiment_score:.0f}."
        )
    elif news_sentiment_score < 0:
        sentences.append(
            f"News sentiment is negative with a score of {news_sentiment_score:.0f}."
        )
    else:
        sentences.append(
            "News sentiment is neutral or unavailable."
        )

    if risk_level == "HIGH":
        sentences.append(
            "This stock should be treated as a risk-review case rather than a positive candidate."
        )
    elif direction in POSITIVE_DIRECTIONS:
        sentences.append(
            "The current rule-based view is relatively favorable, but return prediction data may still be insufficient."
        )
    elif direction == "volatile":
        sentences.append(
            "The event may be important, but direction is uncertain."
        )
    else:
        sentences.append(
            "The current signal is not strong enough for a positive view."
        )

    return " ".join(sentences)


def select_latest_stock_row(df: pd.DataFrame, stock_code: str):
    """
    Select latest row for the requested stock code.
    """

    stock_df = df[df["stock_code"] == stock_code].copy()

    if stock_df.empty:
        return None, pd.DataFrame()

    if "event_date" in stock_df.columns:
        stock_df["event_date"] = stock_df["event_date"].astype(str)
        stock_df = stock_df.sort_values("event_date", ascending=False)

    stock_df["single_stock_score"] = stock_df.apply(
        calculate_single_stock_score,
        axis=1,
    )

    stock_df["risk_level"] = stock_df.apply(
        classify_risk_level,
        axis=1,
    )

    stock_df["single_stock_view"] = stock_df.apply(
        classify_single_stock_view,
        axis=1,
    )

    latest_row = stock_df.iloc[0]

    return latest_row, stock_df


def build_report(stock_code: str) -> str:
    """
    Build single stock prediction report.
    """

    today = datetime.today().strftime("%Y-%m-%d")
    generated_at = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

    df, ml_dataset_path = load_latest_ml_dataset()

    lines = []

    lines.append(f"# Single Stock Prediction Report - {stock_code}")
    lines.append("")
    lines.append(f"Generated at: {generated_at}")
    lines.append("")
    lines.append(f"ML dataset: `{ml_dataset_path if ml_dataset_path else 'Not found'}`")
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
        lines.append("No ML dataset is available yet.")
        lines.append("")
        return "\n".join(lines)

    latest_row, stock_df = select_latest_stock_row(df, stock_code)

    if latest_row is None:
        lines.append("## Status")
        lines.append("")
        lines.append(
            f"No event data found for stock code `{stock_code}` in the latest ML dataset."
        )
        lines.append("")
        lines.append("## What This Means")
        lines.append("")
        lines.append(
            "The stock may not have appeared in the latest collected disclosure/event dataset. "
            "This does not mean there is no market risk or opportunity. "
            "It only means the current event-driven dataset does not contain this stock."
        )
        lines.append("")
        return "\n".join(lines)

    corp_name = latest_row.get("corp_name", "Unknown")
    event_type = latest_row.get("event_type", "unknown")
    event_date = latest_row.get("event_date", "unknown")
    report_nm = latest_row.get("report_nm", "")
    prediction_direction = latest_row.get("prediction_direction", "unknown")
    event_score = latest_row.get("event_score", 0)
    news_count = latest_row.get("news_count", 0)
    news_sentiment_score = latest_row.get("news_sentiment_score", 0)
    news_attention_score = latest_row.get("news_attention_score", 0)
    single_stock_score = latest_row.get("single_stock_score", 0)
    risk_level = latest_row.get("risk_level", "UNKNOWN")
    single_stock_view = latest_row.get("single_stock_view", "UNKNOWN")
    top_news_titles = latest_row.get("top_news_titles", "")

    next_open_return = latest_row.get("next_open_return", None)
    next_close_return = latest_row.get("next_close_return", None)
    prediction_result = latest_row.get("prediction_result", "unknown")

    interpretation = build_interpretation(latest_row)

    lines.append("## Stock Summary")
    lines.append("")
    lines.append(f"- Company: **{corp_name}**")
    lines.append(f"- Stock code: `{stock_code}`")
    lines.append(f"- Latest event date: {event_date}")
    lines.append(f"- Latest event type: `{event_type}`")
    lines.append(f"- Prediction direction: **{prediction_direction}**")
    lines.append(f"- Single-stock view: **{single_stock_view}**")
    lines.append(f"- Risk level: **{risk_level}**")
    lines.append(f"- Single-stock score: **{single_stock_score:.2f}**")
    lines.append(f"- Prediction result status: `{prediction_result}`")
    lines.append("")

    if report_nm:
        lines.append("## Latest Disclosure")
        lines.append("")
        lines.append(f"- {report_nm}")
        lines.append("")

    lines.append("## Feature Summary")
    lines.append("")
    lines.append("| Feature | Value |")
    lines.append("|---|---:|")
    lines.append(f"| Event score | {event_score} |")
    lines.append(f"| News count | {news_count} |")
    lines.append(f"| News sentiment score | {news_sentiment_score} |")
    lines.append(f"| News attention score | {news_attention_score} |")
    lines.append(f"| Next open return data | {format_percent(next_open_return)} |")
    lines.append(f"| Next close return data | {format_percent(next_close_return)} |")
    lines.append("")

    lines.append("## Interpretation")
    lines.append("")
    lines.append(interpretation)
    lines.append("")

    if isinstance(top_news_titles, str) and top_news_titles.strip():
        lines.append("## Related News Examples")
        lines.append("")
        for title in top_news_titles.split(" | "):
            if title.strip():
                lines.append(f"- {title.strip()}")
        lines.append("")

    lines.append("## Recent Rows for This Stock")
    lines.append("")
    recent_columns = [
        "event_date",
        "corp_name",
        "event_type",
        "prediction_direction",
        "event_score",
        "news_sentiment_score",
        "prediction_result",
    ]

    available_columns = [col for col in recent_columns if col in stock_df.columns]
    recent_df = stock_df[available_columns].head(5).copy()

    if recent_df.empty:
        lines.append("No recent rows available.")
    else:
        lines.append("| " + " | ".join(available_columns) + " |")
        lines.append("|" + "|".join(["---"] * len(available_columns)) + "|")

        for _, row in recent_df.iterrows():
            values = [str(row[col]) for col in available_columns]
            lines.append("| " + " | ".join(values) + " |")

    lines.append("")
    lines.append("## Data Readiness")
    lines.append("")
    lines.append(
        "This single-stock report is based on the latest event-driven ML dataset. "
        "If the stock has no recent event data, the report may be limited. "
        "Expected return prediction will become more meaningful after enough evaluated "
        "event-reaction samples are accumulated."
    )
    lines.append("")

    return "\n".join(lines)


def save_report(stock_code: str, report_text: str) -> str:
    """
    Save single stock report.
    """

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    today = datetime.today().strftime("%Y-%m-%d")
    output_path = os.path.join(
        OUTPUT_DIR,
        f"{today}_{stock_code}_single_stock_report.md",
    )

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(report_text)

    return output_path


def main():
    if len(sys.argv) < 2:
        print("Usage: python src/models/single_stock_predictor.py <stock_code>")
        print("Example: python src/models/single_stock_predictor.py 005930")
        return

    stock_code = normalize_stock_code(sys.argv[1])

    print(f"Generating single stock prediction report for {stock_code}...")

    report_text = build_report(stock_code)
    output_path = save_report(stock_code, report_text)

    print(f"Single stock prediction report saved to: {output_path}")


if __name__ == "__main__":
    main()
