"""
Learned-rule daily recommender.

This script creates a daily candidate report that integrates:
- base event score
- market-adjusted score adjustment
- trading volume score adjustment
- learned event-rule score adjustment

It does not overwrite existing recommenders.
It creates a separate v4-style report.
"""

from datetime import datetime
from pathlib import Path

import pandas as pd


PROCESSED_DIR = Path("data/processed")
REPORT_DIR = Path("reports/daily_prediction")


def latest_file(directory: Path, pattern: str):
    files = sorted(directory.glob(pattern))
    if not files:
        return None
    return files[-1]


def read_csv(path):
    if path is None or not path.exists():
        return pd.DataFrame()

    try:
        return pd.read_csv(path)
    except Exception as error:
        print(f"Failed to read {path}: {error}")
        return pd.DataFrame()


def normalize_stock_code(value):
    if pd.isna(value):
        return ""

    try:
        return str(int(float(value))).zfill(6)
    except Exception:
        return str(value).strip().zfill(6)


def safe_float(value, default=0.0):
    try:
        if pd.isna(value):
            return default
        return float(value)
    except Exception:
        return default


def normalize_event_date(df):
    result_df = df.copy()

    if "event_date" not in result_df.columns:
        result_df["event_date"] = ""
        return result_df

    result_df["event_date"] = pd.to_datetime(
        result_df["event_date"],
        errors="coerce",
    ).dt.strftime("%Y-%m-%d")
    result_df["event_date"] = result_df["event_date"].fillna("")

    return result_df


def prepare_adjustment_for_join(source_df, keep_columns, join_columns):
    existing_columns = [column for column in keep_columns if column in source_df.columns]

    if not existing_columns:
        return pd.DataFrame(columns=join_columns)

    result_df = source_df[existing_columns].copy()

    missing_join_columns = [column for column in join_columns if column not in result_df.columns]
    for column in missing_join_columns:
        result_df[column] = ""

    result_df = result_df.drop_duplicates(
        subset=join_columns,
        keep="first",
    )

    return result_df


def make_bucket(final_score, prediction_direction):
    direction = str(prediction_direction)

    if final_score >= 85:
        return "strong_learned_rule_candidate"

    if final_score >= 65:
        return "positive_candidate"

    if "volatile" in direction and final_score >= 35:
        return "volatile_watchlist"

    if final_score >= 30:
        return "watchlist_candidate"

    if final_score <= -60:
        return "risk_or_avoid_review"

    return "general_review"


def load_inputs():
    ml_path = latest_file(PROCESSED_DIR, "ml_dataset_*.csv")
    market_path = latest_file(PROCESSED_DIR, "market_adjusted_score_adjustments_*.csv")
    volume_path = latest_file(PROCESSED_DIR, "trading_volume_score_adjustments_*.csv")
    learned_path = latest_file(PROCESSED_DIR, "learned_event_rules_*.csv")

    ml_df = read_csv(ml_path)
    market_df = read_csv(market_path)
    volume_df = read_csv(volume_path)
    learned_df = read_csv(learned_path)

    print(f"Latest ML dataset: {ml_path}")
    print(f"Latest market score adjustment: {market_path}")
    print(f"Latest volume score adjustment: {volume_path}")
    print(f"Latest learned rules: {learned_path}")

    return ml_df, market_df, volume_df, learned_df


def build_recommendations(ml_df, market_df, volume_df, learned_df):
    if ml_df.empty:
        return pd.DataFrame()

    df = ml_df.copy()

    if "stock_code" in df.columns:
        df["stock_code"] = df["stock_code"].apply(normalize_stock_code)

    df = normalize_event_date(df)

    if not market_df.empty and "stock_code" in market_df.columns:
        market_df = market_df.copy()
        market_df["stock_code"] = market_df["stock_code"].apply(normalize_stock_code)
        market_df = normalize_event_date(market_df)

        market_cols = [
            column
            for column in [
                "event_date",
                "stock_code",
                "market_adjusted_score_adjustment",
                "market_adjusted_adjustment_label",
                "market_adjusted_adjustment_reason",
            ]
            if column in market_df.columns
        ]

        market_df = prepare_adjustment_for_join(
            source_df=market_df,
            keep_columns=market_cols,
            join_columns=["event_date", "stock_code"],
        )

        df = df.merge(
            market_df,
            on=["event_date", "stock_code"],
            how="left",
            validate="m:1",
        )

    if not volume_df.empty and "stock_code" in volume_df.columns:
        volume_df = volume_df.copy()
        volume_df["stock_code"] = volume_df["stock_code"].apply(normalize_stock_code)
        volume_df = normalize_event_date(volume_df)

        volume_cols = [
            column
            for column in [
                "event_date",
                "stock_code",
                "trading_volume_score_adjustment",
                "trading_volume_adjustment_label",
                "trading_volume_adjustment_reason",
            ]
            if column in volume_df.columns
        ]

        volume_df = prepare_adjustment_for_join(
            source_df=volume_df,
            keep_columns=volume_cols,
            join_columns=["event_date", "stock_code"],
        )

        df = df.merge(
            volume_df,
            on=["event_date", "stock_code"],
            how="left",
            validate="m:1",
        )

    if not learned_df.empty and "event_type" in learned_df.columns:
        learned_cols = [
            column
            for column in [
                "event_type",
                "learned_event_score_adjustment",
                "learning_label",
                "learning_reason",
                "evaluated_count",
                "success_rate",
            ]
            if column in learned_df.columns
        ]

        learned_df = prepare_adjustment_for_join(
            source_df=learned_df,
            keep_columns=learned_cols,
            join_columns=["event_type"],
        )

        df = df.merge(
            learned_df,
            on="event_type",
            how="left",
            validate="m:1",
        )

    df["base_event_score_v4"] = df.get("event_score", 0).apply(safe_float)

    if "market_adjusted_score_adjustment" not in df.columns:
        df["market_adjusted_score_adjustment"] = 0

    if "trading_volume_score_adjustment" not in df.columns:
        df["trading_volume_score_adjustment"] = 0

    if "learned_event_score_adjustment" not in df.columns:
        df["learned_event_score_adjustment"] = 0

    df["market_adjusted_score_adjustment"] = df["market_adjusted_score_adjustment"].apply(safe_float)
    df["trading_volume_score_adjustment"] = df["trading_volume_score_adjustment"].apply(safe_float)
    df["learned_event_score_adjustment"] = df["learned_event_score_adjustment"].apply(safe_float)

    df["final_learned_rule_score"] = (
        df["base_event_score_v4"]
        + df["market_adjusted_score_adjustment"]
        + df["trading_volume_score_adjustment"]
        + df["learned_event_score_adjustment"]
    )

    df["candidate_bucket"] = df.apply(
        lambda row: make_bucket(
            row["final_learned_rule_score"],
            row.get("prediction_direction", ""),
        ),
        axis=1,
    )

    df = df.sort_values(
        by=["final_learned_rule_score"],
        ascending=False,
    )

    return df


def build_report(recommendations_df):
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    today = datetime.today().strftime("%Y-%m-%d")
    output_path = REPORT_DIR / f"{today}_learned_rule_daily_candidates.md"

    lines = []

    lines.append(f"# Learned-Rule Daily Candidate Report - {today}")
    lines.append("")
    lines.append("## Purpose")
    lines.append("")
    lines.append(
        "This report applies learned event-rule score adjustments to the daily candidate scoring formula."
    )
    lines.append("")
    lines.append("The current v4 score formula is:")
    lines.append("")
    lines.append("```text")
    lines.append("base_event_score")
    lines.append("+ market_adjusted_score_adjustment")
    lines.append("+ trading_volume_score_adjustment")
    lines.append("+ learned_event_score_adjustment")
    lines.append("= final_learned_rule_score")
    lines.append("```")
    lines.append("")
    lines.append(
        "This report is for research and portfolio demonstration purposes only. It is not investment advice."
    )
    lines.append("")

    if recommendations_df.empty:
        lines.append("No candidate data available.")
        lines.append("")

        output_path.write_text("\n".join(lines), encoding="utf-8")
        return str(output_path)

    total_rows = len(recommendations_df)
    active_learned_rows = int((recommendations_df["learned_event_score_adjustment"] != 0).sum())

    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Total candidate rows: **{total_rows}**")
    lines.append(f"- Rows with active learned-rule adjustment: **{active_learned_rows}**")
    lines.append("")

    bucket_counts = recommendations_df["candidate_bucket"].value_counts()

    lines.append("## Candidate Buckets")
    lines.append("")
    lines.append("| Bucket | Count |")
    lines.append("|---|---:|")

    for bucket, count in bucket_counts.items():
        lines.append(f"| {bucket} | {count} |")

    lines.append("")

    display_columns = [
        "stock_code",
        "corp_name",
        "event_type",
        "prediction_direction",
        "base_event_score_v4",
        "market_adjusted_score_adjustment",
        "trading_volume_score_adjustment",
        "learned_event_score_adjustment",
        "final_learned_rule_score",
        "candidate_bucket",
        "learning_label",
        "evaluated_count",
        "success_rate",
    ]

    existing_columns = [
        column for column in display_columns if column in recommendations_df.columns
    ]

    lines.append("## Top Candidates")
    lines.append("")
    lines.append("| " + " | ".join(existing_columns) + " |")
    lines.append("|" + "|".join(["---"] * len(existing_columns)) + "|")

    top_df = recommendations_df.head(30)

    for _, row in top_df.iterrows():
        values = []

        for column in existing_columns:
            value = row.get(column, "N/A")

            if pd.isna(value):
                value = "N/A"

            if column == "success_rate":
                try:
                    value = f"{float(value) * 100:.2f}%"
                except Exception:
                    value = "N/A"

            values.append(str(value))

        lines.append("| " + " | ".join(values) + " |")

    lines.append("")
    lines.append("## Interpretation")
    lines.append("")
    lines.append("- Positive learned-rule adjustments mean that the event type has historically performed better.")
    lines.append("- Negative learned-rule adjustments mean that the event type has historically performed worse.")
    lines.append("- If active learned-rule rows are zero, the system is still waiting for enough evaluated cases.")
    lines.append("- This layer is conservative and does not overwrite the original event scoring rules.")
    lines.append("")

    output_path.write_text("\n".join(lines), encoding="utf-8")
    return str(output_path)


def main():
    print("Generating learned-rule daily candidate report...")

    ml_df, market_df, volume_df, learned_df = load_inputs()

    recommendations_df = build_recommendations(
        ml_df=ml_df,
        market_df=market_df,
        volume_df=volume_df,
        learned_df=learned_df,
    )

    report_path = build_report(recommendations_df)

    print(f"Learned-rule candidate report saved to: {report_path}")
    print(f"Rows: {len(recommendations_df)}")


if __name__ == "__main__":
    main()
