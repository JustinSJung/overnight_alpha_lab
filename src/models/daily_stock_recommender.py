"""
Daily stock recommender.

This script generates rule-based daily stock recommendation candidates
from the latest ML dataset.

It is not a financial advice system.
It is a research/portfolio project module that ranks event-driven
stock candidates based on disclosure event score, news sentiment,
news attention, and confidence readiness.

Output:
reports/daily_prediction/YYYY-MM-DD_daily_stock_candidates.md
"""

import os
from datetime import datetime

import pandas as pd


PROCESSED_DIR = "data/processed"
OUTPUT_DIR = "reports/daily_prediction"

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


def load_latest_ml_dataset():
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


def safe_numeric(series, default=0):
    """
    Convert a pandas series to numeric safely.
    """

    return pd.to_numeric(series, errors="coerce").fillna(default)


def calculate_recommendation_score(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate rule-based recommendation score.
    """

    df = df.copy()

    for column in [
        "event_score",
        "news_count",
        "positive_keyword_count",
        "negative_keyword_count",
        "news_sentiment_score",
        "news_attention_score",
    ]:
        if column not in df.columns:
            df[column] = 0

        df[column] = safe_numeric(df[column])

    # Base score starts from event score.
    df["recommendation_score"] = df["event_score"]

    # News sentiment contributes to score.
    df["recommendation_score"] += df["news_sentiment_score"] * 5

    # News attention contributes slightly.
    df["recommendation_score"] += df["news_attention_score"].clip(upper=10) * 2

    # Penalize negative keyword count.
    df["recommendation_score"] -= df["negative_keyword_count"] * 3

    # If direction is positive, give slight boost.
    if "prediction_direction" in df.columns:
        df.loc[
            df["prediction_direction"].isin(POSITIVE_DIRECTIONS),
            "recommendation_score",
        ] += 10

        df.loc[
            df["prediction_direction"].isin(NEGATIVE_DIRECTIONS),
            "recommendation_score",
        ] -= 10

        df.loc[
            df["prediction_direction"].isin(VOLATILE_DIRECTIONS),
            "recommendation_score",
        ] -= 5

    return df


def classify_risk_level(row) -> str:
    """
    Classify simple risk level.
    """

    event_type = str(row.get("event_type", ""))
    prediction_direction = str(row.get("prediction_direction", ""))
    negative_keywords = float(row.get("negative_keyword_count", 0))
    score = float(row.get("recommendation_score", 0))

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


def classify_candidate_type(row) -> str:
    """
    Classify candidate type.
    """

    direction = str(row.get("prediction_direction", ""))
    score = float(row.get("recommendation_score", 0))

    if direction in POSITIVE_DIRECTIONS and score >= 60:
        return "POSITIVE_CANDIDATE"

    if direction == "volatile":
        return "WATCHLIST_VOLATILE"

    if direction == "negative":
        return "AVOID_OR_RISK_REVIEW"

    return "WATCHLIST"


def build_reason(row) -> str:
    """
    Build human-readable recommendation reason.
    """

    event_type = row.get("event_type", "unknown")
    event_score = row.get("event_score", 0)
    news_sentiment_score = row.get("news_sentiment_score", 0)
    news_attention_score = row.get("news_attention_score", 0)
    prediction_direction = row.get("prediction_direction", "unknown")

    reasons = []

    reasons.append(f"Event type is {event_type}.")
    reasons.append(f"Initial direction is {prediction_direction}.")
    reasons.append(f"Event score is {event_score}.")

    if news_attention_score > 0:
        reasons.append(f"News attention score is {news_attention_score}.")

    if news_sentiment_score > 0:
        reasons.append(f"News sentiment is positive at {news_sentiment_score}.")
    elif news_sentiment_score < 0:
        reasons.append(f"News sentiment is negative at {news_sentiment_score}.")
    else:
        reasons.append("News sentiment is neutral or unavailable.")

    return " ".join(reasons)


def prepare_candidates(df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    """
    Prepare top recommendation candidates.
    """

    if df.empty:
        return pd.DataFrame()

    candidates = calculate_recommendation_score(df)

    candidates["risk_level"] = candidates.apply(classify_risk_level, axis=1)
    candidates["candidate_type"] = candidates.apply(classify_candidate_type, axis=1)
    candidates["recommendation_reason"] = candidates.apply(build_reason, axis=1)

    # Remove exact duplicate rows if the same event appears repeatedly.
    dedupe_columns = [
        col for col in ["stock_code", "corp_name", "event_type", "event_date"]
        if col in candidates.columns
    ]

    if dedupe_columns:
        candidates = candidates.drop_duplicates(subset=dedupe_columns)

    # Prefer higher score, but keep risk visible.
    candidates = candidates.sort_values(
        by="recommendation_score",
        ascending=False,
    )

    return candidates.head(top_n)


def format_percent(value):
    """
    Format return value as percent if available.
    """

    try:
        if pd.isna(value):
            return "Not available"

        return f"{float(value) * 100:.2f}%"
    except Exception:
        return "Not available"


def build_report() -> str:
    """
    Build daily stock candidate Markdown report.
    """

    today = datetime.today().strftime("%Y-%m-%d")
    generated_at = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

    df, ml_dataset_path = load_latest_ml_dataset()
    candidates = prepare_candidates(df, top_n=30)

    lines = []

    lines.append(f"# Daily Stock Candidate Report - {today}")
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

    lines.append("## Method")
    lines.append("")
    lines.append(
        "Candidates are ranked using a rule-based score that combines event score, "
        "news sentiment, news attention, prediction direction, and simple risk filters."
    )
    lines.append("")
    lines.append(
        "The return prediction model is still in an early stage and may report "
        "`NOT_ENOUGH_DATA` until enough evaluated return samples are accumulated."
    )
    lines.append("")

    if df.empty:
        lines.append("## Status")
        lines.append("")
        lines.append("No ML dataset is available yet.")
        lines.append("")
        return "\n".join(lines)

    if candidates.empty:
        lines.append("## Status")
        lines.append("")
        lines.append("No candidate rows are available.")
        lines.append("")
        return "\n".join(lines)

    positive_candidates = candidates[
        candidates["candidate_type"] == "POSITIVE_CANDIDATE"
    ].copy()

    volatile_candidates = candidates[
        candidates["candidate_type"] == "WATCHLIST_VOLATILE"
    ].copy()

    risk_candidates = candidates[
        candidates["candidate_type"] == "AVOID_OR_RISK_REVIEW"
    ].copy()

    watchlist_candidates = candidates[
        candidates["candidate_type"] == "WATCHLIST"
    ].copy()

    def append_candidate_section(section_title: str, section_df: pd.DataFrame, max_rows: int):
        lines.append(f"## {section_title}")
        lines.append("")

        if section_df.empty:
            lines.append("No candidates in this section.")
            lines.append("")
            return

        section_df = section_df.sort_values(
            by="recommendation_score",
            ascending=False,
        ).head(max_rows)

        for rank, (_, row) in enumerate(section_df.iterrows(), start=1):
            corp_name = row.get("corp_name", "Unknown")
            stock_code = str(row.get("stock_code", "")).zfill(6)
            event_type = row.get("event_type", "unknown")
            report_nm = row.get("report_nm", "")
            prediction_direction = row.get("prediction_direction", "unknown")
            recommendation_score = row.get("recommendation_score", 0)
            risk_level = row.get("risk_level", "UNKNOWN")
            candidate_type = row.get("candidate_type", "WATCHLIST")
            reason = row.get("recommendation_reason", "")
            top_news_titles = row.get("top_news_titles", "")

            next_open_return = row.get("next_open_return", None)
            next_close_return = row.get("next_close_return", None)

            lines.append(f"### {rank}. {corp_name} ({stock_code})")
            lines.append("")
            lines.append(f"- Candidate type: **{candidate_type}**")
            lines.append(f"- Expected direction: **{prediction_direction}**")
            lines.append(f"- Recommendation score: **{recommendation_score:.2f}**")
            lines.append(f"- Risk level: **{risk_level}**")
            lines.append(f"- Event type: `{event_type}`")

            if report_nm:
                lines.append(f"- Disclosure title: {report_nm}")

            lines.append(f"- Next open return data: {format_percent(next_open_return)}")
            lines.append(f"- Next close return data: {format_percent(next_close_return)}")
            lines.append(f"- Reason: {reason}")

            if isinstance(top_news_titles, str) and top_news_titles.strip():
                lines.append(f"- Related news examples: {top_news_titles}")

            lines.append("")

    append_candidate_section(
        "Positive Candidates",
        positive_candidates,
        max_rows=10,
    )

    append_candidate_section(
        "Volatile Watchlist",
        volatile_candidates,
        max_rows=10,
    )

    append_candidate_section(
        "General Watchlist",
        watchlist_candidates,
        max_rows=10,
    )

    append_candidate_section(
        "Risk / Avoid Review List",
        risk_candidates.sort_values(
            by="recommendation_score",
            ascending=True,
        ),
        max_rows=10,
    )

    lines.append("## Data Readiness")
    lines.append("")
    lines.append(
        "At this stage, candidates are generated using rule-based scoring. "
        "Expected return values will become more meaningful after enough evaluated "
        "event-reaction samples are accumulated."
    )
    lines.append("")

    lines.append("## How to Read This Report")
    lines.append("")
    lines.append("- Positive Candidates: relatively favorable event and news conditions.")
    lines.append("- Volatile Watchlist: potentially important events with uncertain direction.")
    lines.append("- General Watchlist: events worth monitoring but not strong enough for positive classification.")
    lines.append("- Risk / Avoid Review List: negative or high-risk events such as capital increases, CB/BW, lawsuits, or disclosure violations.")
    lines.append("")

    lines.append("## Next Step")
    lines.append("")
    lines.append(
        "The next step is to improve candidate scoring by incorporating trained return "
        "prediction outputs, event-type historical success rates, and confidence levels."
    )
    lines.append("")

    return "\n".join(lines)

def save_report(report_text: str) -> str:
    """
    Save daily stock candidate report.
    """

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    today = datetime.today().strftime("%Y-%m-%d")
    output_path = os.path.join(OUTPUT_DIR, f"{today}_daily_stock_candidates.md")

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(report_text)

    return output_path


def main():
    print("Generating daily stock candidate report...")

    report_text = build_report()
    output_path = save_report(report_text)

    print(f"Daily stock candidate report saved to: {output_path}")


if __name__ == "__main__":
    main()
