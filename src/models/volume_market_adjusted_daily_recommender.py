"""
Volume and market-adjusted daily recommender.

This script creates a v3-style daily candidate report that includes:
1. Base recommendation score
2. Market-adjusted score adjustment
3. Trading volume score adjustment

Inputs:
data/processed/ml_dataset_YYYYMMDD.csv
data/processed/market_adjusted_score_adjustments_YYYYMMDD.csv
data/processed/trading_volume_score_adjustments_YYYYMMDD.csv

Output:
reports/daily_prediction/YYYY-MM-DD_volume_market_adjusted_daily_candidates.md
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

    path = get_latest_file(
        PROCESSED_DIR,
        "market_adjusted_score_adjustments_",
    )

    if path is None:
        return pd.DataFrame(), ""

    df = pd.read_csv(path)

    if "stock_code" in df.columns:
        df["stock_code"] = df["stock_code"].apply(normalize_stock_code)

    return df, path


def load_latest_volume_adjustments():
    """
    Load latest trading volume score adjustment file.
    """

    path = get_latest_file(
        PROCESSED_DIR,
        "trading_volume_score_adjustments_",
    )

    if path is None:
        return pd.DataFrame(), ""

    df = pd.read_csv(path)

    if "stock_code" in df.columns:
        df["stock_code"] = df["stock_code"].apply(normalize_stock_code)

    return df, path


def calculate_base_score(row) -> float:
    """
    Build conservative base score from available ML dataset columns.
    """

    score = 0.0

    event_score = safe_float(row.get("event_score", 0.0))
    news_sentiment_score = safe_float(row.get("news_sentiment_score", 0.0))
    news_attention_score = safe_float(row.get("news_attention_score", 0.0))

    prediction_direction = str(row.get("prediction_direction", "unknown"))
    prediction_result = str(row.get("prediction_result", "unknown"))

    score += event_score
    score += news_sentiment_score * 5
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

    return score


def prepare_event_date(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize event date and stock code for joining.
    """

    result_df = df.copy()

    if "stock_code" not in result_df.columns:
        result_df["stock_code"] = ""

    result_df["stock_code"] = result_df["stock_code"].apply(normalize_stock_code)

    if "event_date" in result_df.columns:
        result_df["event_date"] = pd.to_datetime(
            result_df["event_date"],
            errors="coerce",
        ).dt.strftime("%Y-%m-%d")
    else:
        result_df["event_date"] = ""

    return result_df


def join_market_adjustments(base_df: pd.DataFrame, market_df: pd.DataFrame) -> pd.DataFrame:
    """
    Join market-adjusted score adjustment.
    """

    df = base_df.copy()

    if market_df.empty:
        df["market_adjusted_score_adjustment"] = 0
        df["market_adjusted_result"] = "market_adjustment_missing"
        df["market_adjusted_adjustment_label"] = "neutral_adjustment"
        df["market_adjusted_next_close_return"] = pd.NA
        return df

    market = prepare_event_date(market_df)

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
    ]

    keep_columns = [col for col in keep_columns if col in market.columns]

    market = market[keep_columns].drop_duplicates(
        subset=["event_date", "stock_code"],
        keep="first",
    )

    df = df.merge(
        market,
        on=["event_date", "stock_code"],
        how="left",
    )

    df["market_adjusted_score_adjustment"] = pd.to_numeric(
        df.get("market_adjusted_score_adjustment", 0),
        errors="coerce",
    ).fillna(0)

    df["market_adjusted_result"] = df.get(
        "market_adjusted_result",
        "market_adjustment_missing",
    )

    df["market_adjusted_adjustment_label"] = df.get(
        "market_adjusted_adjustment_label",
        "neutral_adjustment",
    )

    return df


def join_volume_adjustments(base_df: pd.DataFrame, volume_df: pd.DataFrame) -> pd.DataFrame:
    """
    Join trading volume score adjustment.
    """

    df = base_df.copy()

    if volume_df.empty:
        df["trading_volume_score_adjustment"] = 0
        df["volume_reaction_label"] = "volume_adjustment_missing"
        df["trading_volume_adjustment_label"] = "neutral_volume_adjustment"
        return df

    volume = prepare_event_date(volume_df)

    keep_columns = [
        "event_date",
        "stock_code",
        "volume_reaction_label",
        "event_volume_ratio_20d",
        "next_volume_ratio_20d",
        "trading_volume_score_adjustment",
        "trading_volume_adjustment_label",
    ]

    keep_columns = [col for col in keep_columns if col in volume.columns]

    volume = volume[keep_columns].drop_duplicates(
        subset=["event_date", "stock_code"],
        keep="first",
    )

    df = df.merge(
        volume,
        on=["event_date", "stock_code"],
        how="left",
    )

    df["trading_volume_score_adjustment"] = pd.to_numeric(
        df.get("trading_volume_score_adjustment", 0),
        errors="coerce",
    ).fillna(0)

    df["volume_reaction_label"] = df.get(
        "volume_reaction_label",
        "volume_adjustment_missing",
    )

    df["trading_volume_adjustment_label"] = df.get(
        "trading_volume_adjustment_label",
        "neutral_volume_adjustment",
    )

    return df


def classify_candidate_bucket(row) -> str:
    """
    Classify candidate bucket using final volume + market-adjusted score.
    """

    score = safe_float(row.get("final_volume_market_adjusted_score", 0))
    direction = str(row.get("prediction_direction", "unknown"))
    market_result = str(row.get("market_adjusted_result", "unknown"))
    volume_label = str(row.get("volume_reaction_label", "unknown"))

    if direction == "negative":
        if volume_label in ["strong_volume_spike", "extreme_volume_spike"]:
            return "high_attention_risk_review"
        return "risk_or_avoid_review"

    if score >= 60:
        return "strong_volume_market_adjusted_candidate"

    if market_result == "market_adjusted_success" and score >= 45:
        return "strong_market_adjusted_candidate"

    if volume_label in ["strong_volume_spike", "extreme_volume_spike"] and score >= 35:
        return "volume_confirmed_candidate"

    if score >= 35:
        return "positive_candidate"

    if score >= 20:
        return "watchlist_candidate"

    if direction == "volatile":
        return "volatile_watchlist"

    return "general_review"


def build_candidates(
    ml_df: pd.DataFrame,
    market_df: pd.DataFrame,
    volume_df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Build final volume + market-adjusted candidate dataframe.
    """

    if ml_df.empty:
        return pd.DataFrame()

    df = prepare_event_date(ml_df)

    df["base_recommendation_score_v3"] = df.apply(calculate_base_score, axis=1)

    df = join_market_adjustments(df, market_df)
    df = join_volume_adjustments(df, volume_df)

    df["final_volume_market_adjusted_score"] = (
        df["base_recommendation_score_v3"]
        + df["market_adjusted_score_adjustment"]
        + df["trading_volume_score_adjustment"]
    )

    df["candidate_bucket"] = df.apply(classify_candidate_bucket, axis=1)

    df = df.sort_values(
        by="final_volume_market_adjusted_score",
        ascending=False,
    )

    return df


def add_bucket_section(lines, df: pd.DataFrame, bucket: str, title: str):
    """
    Add a candidate bucket section to report.
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
        "volume_reaction_label",
        "base_recommendation_score_v3",
        "market_adjusted_score_adjustment",
        "trading_volume_score_adjustment",
        "final_volume_market_adjusted_score",
        "market_adjusted_next_close_return",
        "event_volume_ratio_20d",
        "next_volume_ratio_20d",
    ]

    available_columns = [col for col in sample_columns if col in subset.columns]

    subset = subset[available_columns].head(20)

    lines.append("| " + " | ".join(available_columns) + " |")
    lines.append("|" + "|".join(["---"] * len(available_columns)) + "|")

    for _, row in subset.iterrows():
        values = []

        for col in available_columns:
            value = row[col]

            if col.endswith("return"):
                values.append(format_percent(value))
            elif "ratio" in col:
                try:
                    if pd.isna(value):
                        values.append("N/A")
                    else:
                        values.append(f"{float(value):.2f}x")
                except Exception:
                    values.append(str(value))
            elif "score" in col:
                try:
                    values.append(f"{float(value):.2f}")
                except Exception:
                    values.append(str(value))
            else:
                values.append(str(value))

        lines.append("| " + " | ".join(values) + " |")

    lines.append("")


def build_report(
    df: pd.DataFrame,
    ml_path: str,
    market_path: str,
    volume_path: str,
) -> str:
    """
    Build Markdown report.
    """

    today = datetime.today().strftime("%Y-%m-%d")
    generated_at = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

    lines = []

    lines.append(f"# Volume + Market-Adjusted Daily Candidate Report - {today}")
    lines.append("")
    lines.append(f"Generated at: {generated_at}")
    lines.append("")
    lines.append(f"ML dataset source: `{ml_path if ml_path else 'Not found'}`")
    lines.append(f"Market-adjusted score source: `{market_path if market_path else 'Not found'}`")
    lines.append(f"Trading volume score source: `{volume_path if volume_path else 'Not found'}`")
    lines.append("")

    lines.append("## Purpose")
    lines.append("")
    lines.append(
        "This report applies both market-adjusted score adjustments and trading volume score adjustments to daily candidate scoring."
    )
    lines.append("")
    lines.append(
        "It is a v3 candidate report for comparison and does not replace the main recommender yet."
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
    lines.append("base_recommendation_score_v3")
    lines.append("+ market_adjusted_score_adjustment")
    lines.append("+ trading_volume_score_adjustment")
    lines.append("= final_volume_market_adjusted_score")
    lines.append("```")
    lines.append("")

    if df.empty:
        lines.append("## Status")
        lines.append("")
        lines.append("No volume + market-adjusted daily candidate data is available yet.")
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
        "strong_volume_market_adjusted_candidate",
        "Strong Volume + Market-Adjusted Candidates",
    )

    add_bucket_section(
        lines,
        df,
        "strong_market_adjusted_candidate",
        "Strong Market-Adjusted Candidates",
    )

    add_bucket_section(
        lines,
        df,
        "volume_confirmed_candidate",
        "Volume-Confirmed Candidates",
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
        "high_attention_risk_review",
        "High-Attention Risk Review",
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
        "The next step is to compare this v3 report with the existing recommender and decide which score components should be merged into the main daily stock recommender."
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
        f"{today}_volume_market_adjusted_daily_candidates.md",
    )

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(report_text)

    return output_path


def main():
    print("Generating volume + market-adjusted daily candidate report...")

    ml_df, ml_path = load_latest_ml_dataset()
    market_df, market_path = load_latest_market_adjustments()
    volume_df, volume_path = load_latest_volume_adjustments()

    print(f"Latest ML dataset: {ml_path if ml_path else 'Not found'}")
    print(f"Latest market-adjusted score adjustments: {market_path if market_path else 'Not found'}")
    print(f"Latest trading volume score adjustments: {volume_path if volume_path else 'Not found'}")

    result_df = build_candidates(
        ml_df,
        market_df,
        volume_df,
    )

    if result_df.empty:
        print("No volume + market-adjusted daily candidates generated.")
    else:
        print(f"Rows: {len(result_df)}")

        if "candidate_bucket" in result_df.columns:
            print("")
            print("Candidate bucket counts:")
            print(result_df["candidate_bucket"].value_counts(dropna=False))

    report_text = build_report(
        result_df,
        ml_path,
        market_path,
        volume_path,
    )

    report_path = save_report(report_text)

    print(f"Volume + market-adjusted daily candidate report saved to: {report_path}")


if __name__ == "__main__":
    main()
