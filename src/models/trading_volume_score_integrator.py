"""
Trading volume score integrator.

This script converts trading volume reaction labels into
recommendation score adjustment signals.

Input:
data/processed/trading_volume_features_YYYYMMDD.csv

Outputs:
data/processed/trading_volume_score_adjustments_YYYYMMDD.csv
reports/daily_review/YYYY-MM-DD_trading_volume_score_report.md
"""

import os
from datetime import datetime

import pandas as pd


PROCESSED_DIR = "data/processed"
REPORT_DIR = "reports/daily_review"


POSITIVE_DIRECTIONS = ["positive", "neutral_positive"]
NEGATIVE_DIRECTIONS = ["negative"]
VOLATILE_DIRECTIONS = ["volatile"]


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


def format_ratio(value) -> str:
    """
    Format volume ratio safely.
    """

    try:
        if pd.isna(value):
            return "N/A"

        return f"{float(value):.2f}x"
    except Exception:
        return "N/A"


def load_latest_trading_volume_features():
    """
    Load latest trading volume feature file.
    """

    path = get_latest_file(
        PROCESSED_DIR,
        "trading_volume_features_",
    )

    if path is None:
        return pd.DataFrame(), ""

    df = pd.read_csv(path)

    if "stock_code" in df.columns:
        df["stock_code"] = df["stock_code"].apply(normalize_stock_code)

    return df, path


def calculate_volume_score_adjustment(row) -> int:
    """
    Convert volume reaction into a score adjustment.

    The rule depends on both prediction direction and volume reaction.
    """

    direction = str(row.get("prediction_direction", "unknown"))
    label = str(row.get("volume_reaction_label", "unknown"))

    if label in [
        "price_file_missing",
        "insufficient_volume_baseline",
        "invalid_event",
        "empty_price_data",
        "no_price_after_event",
        "unknown",
    ]:
        return 0

    if direction in POSITIVE_DIRECTIONS:
        if label == "extreme_volume_spike":
            return 12
        if label == "strong_volume_spike":
            return 10
        if label == "moderate_volume_increase":
            return 5
        if label == "normal_or_weak_volume":
            return -3

    if direction in NEGATIVE_DIRECTIONS:
        if label == "extreme_volume_spike":
            return -12
        if label == "strong_volume_spike":
            return -10
        if label == "moderate_volume_increase":
            return -5
        if label == "normal_or_weak_volume":
            return 0

    if direction in VOLATILE_DIRECTIONS:
        if label == "extreme_volume_spike":
            return 8
        if label == "strong_volume_spike":
            return 6
        if label == "moderate_volume_increase":
            return 3
        if label == "normal_or_weak_volume":
            return -2

    return 0


def calculate_volume_adjustment_label(score: int) -> str:
    """
    Convert score to label.
    """

    if score >= 10:
        return "strong_positive_volume_adjustment"

    if score >= 3:
        return "mild_positive_volume_adjustment"

    if score <= -10:
        return "strong_negative_volume_adjustment"

    if score <= -3:
        return "mild_negative_volume_adjustment"

    return "neutral_volume_adjustment"


def build_volume_adjustment_reason(row) -> str:
    """
    Build explanation for volume score adjustment.
    """

    direction = str(row.get("prediction_direction", "unknown"))
    label = str(row.get("volume_reaction_label", "unknown"))
    score = row.get("trading_volume_score_adjustment", 0)

    event_ratio_20d = row.get("event_volume_ratio_20d", None)
    next_ratio_20d = row.get("next_volume_ratio_20d", None)

    base = (
        f"Prediction direction was `{direction}` and volume reaction label was `{label}`. "
        f"Event-day volume ratio was {format_ratio(event_ratio_20d)} and "
        f"next-day volume ratio was {format_ratio(next_ratio_20d)}. "
        f"Trading volume score adjustment is {score}."
    )

    if direction in POSITIVE_DIRECTIONS:
        if score > 0:
            return base + " A positive event with increased volume may indicate stronger market attention."
        if score < 0:
            return base + " A positive event with weak volume should be treated more conservatively."
        return base + " No meaningful volume-based adjustment is applied."

    if direction in NEGATIVE_DIRECTIONS:
        if score < 0:
            return base + " A negative event with increased volume may indicate stronger risk attention."
        return base + " No meaningful negative volume confirmation is observed."

    if direction in VOLATILE_DIRECTIONS:
        if score > 0:
            return base + " A volatile event with increased volume may support the volatility signal."
        if score < 0:
            return base + " A volatile event with weak volume may indicate that volatility was overestimated."
        return base + " No meaningful volume-based volatility signal is observed."

    return base + " This case requires manual review."


def build_trading_volume_score_adjustments(df: pd.DataFrame) -> pd.DataFrame:
    """
    Build trading volume score adjustment dataframe.
    """

    if df.empty:
        return pd.DataFrame()

    result_df = df.copy()

    if "stock_code" in result_df.columns:
        result_df["stock_code"] = result_df["stock_code"].apply(normalize_stock_code)

    if "volume_reaction_label" not in result_df.columns:
        result_df["volume_reaction_label"] = "unknown"

    result_df["trading_volume_score_adjustment"] = result_df.apply(
        calculate_volume_score_adjustment,
        axis=1,
    )

    result_df["trading_volume_adjustment_label"] = result_df[
        "trading_volume_score_adjustment"
    ].apply(calculate_volume_adjustment_label)

    result_df["trading_volume_adjustment_reason"] = result_df.apply(
        build_volume_adjustment_reason,
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
        "volume_reaction_label",
        "event_day_volume",
        "next_day_volume",
        "avg_volume_20d_before",
        "event_volume_ratio_20d",
        "next_volume_ratio_20d",
        "trading_volume_score_adjustment",
        "trading_volume_adjustment_label",
        "trading_volume_adjustment_reason",
    ]

    available_columns = [
        col for col in output_columns
        if col in result_df.columns
    ]

    return result_df[available_columns].copy()


def save_adjustments(df: pd.DataFrame) -> str:
    """
    Save score adjustment CSV.
    """

    os.makedirs(PROCESSED_DIR, exist_ok=True)

    today = datetime.today().strftime("%Y%m%d")
    output_path = os.path.join(
        PROCESSED_DIR,
        f"trading_volume_score_adjustments_{today}.csv",
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

    lines.append(f"# Trading Volume Score Integration Report - {today}")
    lines.append("")
    lines.append(f"Generated at: {generated_at}")
    lines.append("")
    lines.append(f"Source trading volume feature file: `{source_path if source_path else 'Not found'}`")
    lines.append("")

    lines.append("## Purpose")
    lines.append("")
    lines.append(
        "This report converts trading volume reaction labels into recommendation score adjustment signals."
    )
    lines.append("")
    lines.append(
        "The goal is to reward positive events with strong volume confirmation and penalize negative events with strong volume confirmation."
    )
    lines.append("")

    lines.append("## Important Notice")
    lines.append("")
    lines.append(
        "This report is generated for research and portfolio purposes only. "
        "It is not financial advice or a buy/sell recommendation."
    )
    lines.append("")

    lines.append("## Score Logic")
    lines.append("")
    lines.append("- Positive event + strong volume spike: positive adjustment")
    lines.append("- Positive event + weak volume: conservative negative adjustment")
    lines.append("- Negative event + strong volume spike: negative risk adjustment")
    lines.append("- Volatile event + strong volume spike: volatility confirmation adjustment")
    lines.append("")

    if df.empty:
        lines.append("## Status")
        lines.append("")
        lines.append("No trading volume score adjustment data is available yet.")
        lines.append("")
        return "\n".join(lines)

    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Total rows: **{len(df)}**")

    if "trading_volume_score_adjustment" in df.columns:
        total_score = df["trading_volume_score_adjustment"].sum()
        avg_score = df["trading_volume_score_adjustment"].mean()

        lines.append(f"- Total volume adjustment score: **{total_score:.2f}**")
        lines.append(f"- Average volume adjustment score: **{avg_score:.2f}**")

    lines.append("")

    if "trading_volume_adjustment_label" in df.columns:
        lines.append("## Adjustment Label Counts")
        lines.append("")

        counts = df["trading_volume_adjustment_label"].value_counts(dropna=False)

        for label, count in counts.items():
            lines.append(f"- {label}: **{count}**")

        lines.append("")

    if "volume_reaction_label" in df.columns:
        lines.append("## Volume Reaction Counts")
        lines.append("")

        counts = df["volume_reaction_label"].value_counts(dropna=False)

        for label, count in counts.items():
            lines.append(f"- {label}: **{count}**")

        lines.append("")

    lines.append("## Sample Rows")
    lines.append("")

    sample_columns = [
        "event_date",
        "stock_code",
        "corp_name",
        "prediction_direction",
        "volume_reaction_label",
        "event_volume_ratio_20d",
        "next_volume_ratio_20d",
        "trading_volume_score_adjustment",
        "trading_volume_adjustment_label",
    ]

    available_columns = [
        col for col in sample_columns
        if col in df.columns
    ]

    if not available_columns:
        lines.append("No displayable columns available.")
        lines.append("")
    else:
        sample_df = df[available_columns].head(30)

        lines.append("| " + " | ".join(available_columns) + " |")
        lines.append("|" + "|".join(["---"] * len(available_columns)) + "|")

        for _, row in sample_df.iterrows():
            values = []

            for col in available_columns:
                value = row[col]

                if "ratio" in col:
                    values.append(format_ratio(value))
                elif "score" in col:
                    try:
                        values.append(f"{float(value):.2f}")
                    except Exception:
                        values.append(str(value))
                else:
                    values.append(str(value))

            lines.append("| " + " | ".join(values) + " |")

        lines.append("")

    lines.append("## Next Step")
    lines.append("")
    lines.append(
        "The next step is to connect trading volume score adjustment to the market-adjusted daily candidate report."
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
        f"{today}_trading_volume_score_report.md",
    )

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(report_text)

    return output_path


def main():
    print("Generating trading volume score adjustments...")

    feature_df, source_path = load_latest_trading_volume_features()

    print(f"Latest trading volume features: {source_path if source_path else 'Not found'}")

    adjustment_df = build_trading_volume_score_adjustments(feature_df)

    if adjustment_df.empty:
        print("No trading volume score adjustments generated.")
    else:
        output_path = save_adjustments(adjustment_df)
        print(f"Trading volume score adjustments saved to: {output_path}")
        print(f"Rows: {len(adjustment_df)}")

        if "trading_volume_adjustment_label" in adjustment_df.columns:
            print("")
            print("Trading volume adjustment label counts:")
            print(adjustment_df["trading_volume_adjustment_label"].value_counts(dropna=False))

    report_text = build_report(adjustment_df, source_path)
    report_path = save_report(report_text)

    print(f"Trading volume score report saved to: {report_path}")


if __name__ == "__main__":
    main()
