"""
Market-adjusted daily recommender.

This script creates a daily candidate report that includes
market-adjusted score adjustment signals.

It does not replace the existing daily_stock_recommender.py yet.
Instead, it creates a safer v2-style report for review.

Inputs:
data/processed/ml_dataset_YYYYMMDD.csv
data/processed/market_adjusted_score_adjustments_YYYYMMDD.csv

Output:
reports/daily_prediction/YYYY-MM-DD_market_adjusted_daily_candidates.md
"""

import os
from datetime import datetime

import pandas as pd


PROCESSED_DIR = "data/processed"
REPORT_DIR = "reports/daily_prediction"


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


def load_latest_ml_dataset():
    """
    Load latest ML dataset.
    """

    path = get_latest_file(PROCESSED_DIR, "ml_dataset_")

    if path is None:
        return pd.DataFrame(), ""

    df = pd.read_csv(path)

    if "stock_code" in df.columns:
        df["stock_code"] = df["stock_code"].apply(normalize_stock_code)

    return df, path


def load_latest_market_adjustments():
    """
    Load latest market-adjusted score adjustment file.
    """

    path = get_latest_file(PROCESSED_DIR, "market_adjusted_score_adjustments_")

    if path is None:
        return pd.DataFrame(), ""

    df = pd.read_csv(path)

    if "stock_code" in df.columns:
        df["stock_code"] = df["stock_code"].apply(normalize_stock_code)

    return df, path


def calculate_base_score(row) -> float:
    """
    Build a simple base score from available ML dataset columns.

    This is intentionally conservative.
    The existing daily_stock_recommender.py remains the main recommender.
    """

    score = 0.0

    event_score = safe_float(row.get("event_score", 0.0))
    news_sentiment_score = safe_float(row.get("news_sentiment_score", 0.0))
    news_attention_score = safe_float(row.get("news_attention_score", 0.0))

    prediction_direction = str(row.get("prediction_direction", "unknown"))
    prediction_result = str(row.get("prediction_result", "unknown"))

    score += event_score

    # News sentiment is usually small, so give it a moderate weight.
    score += news_sentiment_score * 5

    # News attention is useful, but should not dominate.
    score += news_attention_score * 2

    if prediction_direction == "positive":
        score += 5
    elif prediction_direction == "neutral_positive":
        score += 3
    elif prediction_direction == "negative":
        score -= 5
    elif prediction_direction == "volatile":
        score += 1

    if prediction_result == "success":
        score += 5
    elif prediction_result == "failure":
        score -= 5
    elif prediction_result == "pending":
        score += 0

    return score


def build_market_adjusted_candidates(
    ml_df: pd.DataFrame,
    adjustment_df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Join ML dataset with market-adjusted score adjustment and build final score.
    """

    if ml_df.empty:
        return pd.DataFrame()

    df = ml_df.copy()

    if "stock_code" not in df.columns:
        df["stock_code"] = ""

    df["stock_code"] = df["stock_code"].apply(normalize_stock_code)

    if "event_date" in df.columns:
        df["event_date"] = pd.to_datetime(df["event_date"]).dt.strftime("%Y-%m-%d")
    else:
        df["event_date"] = ""

    df["base_recommendation_score_v2"] = df.apply(calculate_base_score, axis=1)

    if adjustment_df.empty:
        df["market_adjusted_score_adjustment"] = 0
        df["market_adjusted_adjustment_label"] = "neutral_adjustment"
        df["market_adjusted_adjustment_reason"] = "No market-adjusted score adjustment file was available."
    else:
        adj = adjustment_df.copy()

        if "stock_code" not in adj.columns:
            adj["stock_code"] = ""

        adj["stock_code"] = adj["stock_code"].apply(normalize_stock_code)

        if "event_date" in adj.columns:
            adj["event_date"] = pd.to_datetime(adj["event_date"]).dt.strftime("%Y-%m-%d")
        else:
            adj["event_date"] = ""

        join_columns = ["event_date", "stock_code"]

        keep_columns = [
            "event_date",
            "stock_code",
            "market_adjusted_result",
            "market_group",
            "market_source_type",
            "market_proxy_name",
            "market_adjusted_next_close_return",
            "market_adjusted_score_adjustment",
            "market_adjusted_adjustment_label",
            "market_adjusted_adjustment_reason",
        ]

        keep_columns = [
            col for col in keep_columns
            if col in adj.columns
        ]

        adj = adj[keep_columns].drop_duplicates(
            subset=join_columns,
            keep="first",
        )

        df = df.merge(
            adj,
            on=join_columns,
            how="left",
        )

        df["market_adjusted_score_adjustment"] = pd.to_numeric(
            df.get("market_adjusted_score_adjustment", 0),
            errors="coerce",
        ).fillna(0)

        df["market_adjusted_adjustment_label"] = df.get(
            "market_adjusted_adjustment_label",
            "neutral_adjustment",
        )

        df["market_adjusted_adjustment_reason"] = df.get(
            "market_adjusted_adjustment_reason",
            "No market-adjusted adjustment was matched.",
        )

    df["final_market_adjusted_score"] = (
        df["base_recommendation_score_v2"]
        + df["market_adjusted_score_adjustment"]
    )

    df["candidate_bucket"] = df.apply(classify_candidate_bucket, axis=1)

    df = df.sort_values(
        by="final_market_adjusted_score",
        ascending=False,
    )

    return df


def classify_candidate_bucket(row) -> str:
    """
    Classify candidate bucket using final market-adjusted score.
    """

    score = safe_float(row.get("final_market_adjusted_score", 0))
    direction = str(row.get("prediction_direction", "unknown"))
    market_result = str(row.get("market_adjusted_result", "unknown"))

    if direction == "negative":
        return "risk_or_avoid_review"

    if market_result == "market_adjusted_success" and score >= 50:
        return "strong_market_adjusted_candidate"

    if score >= 40:
        return "positive_candidate"

    if score >= 20:
        return "watchlist_candidate"

    if direction == "volatile":
        return "volatile_watchlist"

    return "general_review"


def build_report(df: pd.DataFrame, ml_path: str, adjustment_path: str) -> str:
    """
    Build Markdown report.
    """

    today = datetime.today().strftime("%Y-%m-%d")
    generated_at = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

    lines = []

    lines.append(f"# Market-Adjusted Daily Candidate Report - {today}")
    lines.append("")
    lines.append(f"Generated at: {generated_at}")
    lines.append("")
    lines.append(f"ML dataset source: `{ml_path if ml_path else 'Not found'}`")
    lines.append(f"Market-adjusted score source: `{adjustment_path if adjustment_path else 'Not found'}`")
    lines.append("")

    lines.append("## Purpose")
    lines.append("")
    lines.append(
        "This report applies market-adjusted score adjustments to daily candidate scoring."
    )
    lines.append("")
    lines.append(
        "It is a safer v2 report and does not replace the existing daily stock recommender yet."
    )
    lines.append("")

    lines.append("## Important Notice")
    lines.append("")
    lines.append(
        "This report is generated for research and portfolio purposes only. "
        "It is not financial advice or a buy/sell recommendation."
    )
    lines.append("")

    lines.append("## Score Formula")
    lines.append("")
    lines.append("```text")
    lines.append("base_recommendation_score_v2")
    lines.append("+ market_adjusted_score_adjustment")
    lines.append("= final_market_adjusted_score")
    lines.append("```")
    lines.append("")

    if df.empty:
        lines.append("## Status")
        lines.append("")
        lines.append("No market-adjusted daily candidate data is available yet.")
        lines.append("")
        return "\n".join(lines)

    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Total rows: **{len(df)}**")

    if "candidate_bucket" in df.columns:
        counts = df["candidate_bucket"].value_counts(dropna=False)
        for bucket, count in counts.items():
            lines.append(f"- {bucket}: **{count}**")

    lines.append("")

    add_bucket_section(
        lines,
        df,
        "strong_market_adjusted_candidate",
        "Strong Market-Adjusted Candidates",
    )

    add_bucket_section(
        lines,
        df,
        "positive_candidate",
        "Positive Candidates",
    )

    add_bucket_section(
        lines,
        df,
        "watchlist_candidate",
        "Watchlist Candidates",
    )

    add_bucket_section(
        lines,
        df,
        "volatile_watchlist",
        "Volatile Watchlist",
    )

    add_bucket_section(
        lines,
        df,
        "risk_or_avoid_review",
        "Risk / Avoid Review",
    )

    add_bucket_section(
        lines,
        df,
        "general_review",
        "General Review",
    )

    lines.append("## Next Step")
    lines.append("")
    lines.append(
        "The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender."
    )
    lines.append("")

    return "\n".join(lines)


def add_bucket_section(lines, df: pd.DataFrame, bucket: str, title: str):
    """
    Add a candidate bucket section.
    """

    if "candidate_bucket" not in df.columns:
        return

    subset = df[df["candidate_bucket"] == bucket].copy()

    lines.append(f"## {title}")
    lines.append("")

    if subset.empty:
        lines.append("No candidates in this section.")
        lines.append("")
        return

    sample_columns = [
        "event_date",
        "stock_code",
        "corp_name",
        "event_type",
        "prediction_direction",
        "prediction_result",
        "market_adjusted_result",
        "base_recommendation_score_v2",
        "market_adjusted_score_adjustment",
        "final_market_adjusted_score",
        "market_adjusted_next_close_return",
    ]

    available_columns = [
        col for col in sample_columns
        if col in subset.columns
    ]

    subset = subset[available_columns].head(20)

    lines.append("| " + " | ".join(available_columns) + " |")
    lines.append("|" + "|".join(["---"] * len(available_columns)) + "|")

    for _, row in subset.iterrows():
        values = []

        for col in available_columns:
            value = row[col]

            if col.endswith("return"):
                values.append(format_percent(value))
            elif "score" in col:
                try:
                    values.append(f"{float(value):.2f}")
                except Exception:
                    values.append(str(value))
            else:
                values.append(str(value))

        lines.append("| " + " | ".join(values) + " |")

    lines.append("")


def save_report(report_text: str) -> str:
    """
    Save Markdown report.
    """

    os.makedirs(REPORT_DIR, exist_ok=True)

    today = datetime.today().strftime("%Y-%m-%d")
    output_path = os.path.join(
        REPORT_DIR,
        f"{today}_market_adjusted_daily_candidates.md",
    )

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(report_text)

    return output_path


def main():
    print("Generating market-adjusted daily candidate report...")

    ml_df, ml_path = load_latest_ml_dataset()
    adjustment_df, adjustment_path = load_latest_market_adjustments()

    print(f"Latest ML dataset: {ml_path if ml_path else 'Not found'}")
    print(f"Latest market-adjusted score adjustments: {adjustment_path if adjustment_path else 'Not found'}")

    result_df = build_market_adjusted_candidates(
        ml_df,
        adjustment_df,
    )

    if result_df.empty:
        print("No market-adjusted daily candidates generated.")
    else:
        print(f"Rows: {len(result_df)}")

        if "candidate_bucket" in result_df.columns:
            print("")
            print("Candidate bucket counts:")
            print(result_df["candidate_bucket"].value_counts(dropna=False))

    report_text = build_report(
        result_df,
        ml_path,
        adjustment_path,
    )

    report_path = save_report(report_text)

    print(f"Market-adjusted daily candidate report saved to: {report_path}")


if __name__ == "__main__":
    main()
