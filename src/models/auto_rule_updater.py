"""
Auto rule updater.

This script learns event-type score adjustment rules from accumulated
prediction success/failure results.

It does not overwrite the original event scoring rules.
Instead, it creates a learned rule adjustment table that can be safely
combined with the existing recommender later.

Inputs:
- data/predictions/error_notes_*.csv
- data/predictions/market_adjusted_evaluation_*.csv
- data/processed/social_attention_features_*.csv

Outputs:
- data/processed/learned_event_rules_YYYYMMDD.csv
- reports/daily_review/YYYY-MM-DD_auto_rule_update_report.md
"""

import os
from datetime import datetime
from pathlib import Path

import pandas as pd


PREDICTIONS_DIR = Path("data/predictions")
PROCESSED_DIR = Path("data/processed")
REPORT_DIR = Path("reports/daily_review")


MIN_EVALUATED_COUNT = 5


def read_all_csv(directory: Path, pattern: str) -> pd.DataFrame:
    files = sorted(directory.glob(pattern))
    frames = []

    for file in files:
        try:
            df = pd.read_csv(file)
            df["source_file"] = str(file)
            frames.append(df)
        except Exception as error:
            print(f"Failed to read {file}: {error}")

    if not frames:
        return pd.DataFrame()

    return pd.concat(frames, ignore_index=True)


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


def normalize_result(value: str) -> str:
    if pd.isna(value):
        return "pending"

    value = str(value).strip().lower()

    if value in ["success", "correct", "positive_signal_confirmed", "negative_signal_confirmed"]:
        return "success"

    if value in ["failure", "wrong", "general_prediction_failure"]:
        return "failure"

    if value == "pending":
        return "pending"

    return value


def safe_float(value, default=0.0):
    try:
        if pd.isna(value):
            return default
        return float(value)
    except Exception:
        return default


def calculate_adjustment(success_rate: float, evaluated_count: int) -> tuple:
    """
    Convert success rate into learned score adjustment.

    This is intentionally conservative.
    """

    if evaluated_count < MIN_EVALUATED_COUNT:
        return 0, "hold_insufficient_data", "평가 완료 데이터가 부족하여 자동 조정을 보류합니다."

    if success_rate >= 0.75:
        return 15, "strong_positive_learning", "성공률이 매우 높아 해당 이벤트 유형 점수를 강하게 상향합니다."

    if success_rate >= 0.65:
        return 10, "positive_learning", "성공률이 높아 해당 이벤트 유형 점수를 상향합니다."

    if success_rate >= 0.55:
        return 5, "mild_positive_learning", "성공률이 기준보다 약간 높아 소폭 상향합니다."

    if success_rate >= 0.45:
        return 0, "neutral_learning", "성공률이 중립 구간이므로 조정하지 않습니다."

    if success_rate >= 0.35:
        return -5, "mild_negative_learning", "성공률이 낮아 해당 이벤트 유형 점수를 소폭 하향합니다."

    if success_rate >= 0.25:
        return -10, "negative_learning", "성공률이 낮아 해당 이벤트 유형 점수를 하향합니다."

    return -15, "strong_negative_learning", "성공률이 매우 낮아 해당 이벤트 유형 점수를 강하게 하향합니다."


def summarize_market_adjusted(market_df: pd.DataFrame) -> pd.DataFrame:
    if market_df.empty or "event_type" not in market_df.columns:
        return pd.DataFrame()

    if "market_adjusted_result" not in market_df.columns:
        return pd.DataFrame()

    rows = []

    for event_type, group in market_df.groupby("event_type"):
        result_series = group["market_adjusted_result"].astype(str)

        success_count = int(result_series.str.contains("success", na=False).sum())
        failure_count = int(result_series.str.contains("failure", na=False).sum())
        pending_count = int((result_series == "pending").sum())

        evaluated_count = success_count + failure_count
        success_rate = success_count / evaluated_count if evaluated_count > 0 else 0

        rows.append(
            {
                "event_type": event_type,
                "market_adjusted_success_count": success_count,
                "market_adjusted_failure_count": failure_count,
                "market_adjusted_pending_count": pending_count,
                "market_adjusted_evaluated_count": evaluated_count,
                "market_adjusted_success_rate": round(success_rate, 4),
            }
        )

    return pd.DataFrame(rows)


def summarize_social_attention(social_df: pd.DataFrame) -> pd.DataFrame:
    if social_df.empty or "event_type" not in social_df.columns:
        return pd.DataFrame()

    rows = []

    for event_type, group in social_df.groupby("event_type"):
        high_attention = 0
        rumor_noise = 0
        risk_noise = 0

        avg_social_attention_score = 0
        avg_rumor_noise_score = 0
        avg_risk_noise_score = 0

        if "attention_label" in group.columns:
            high_attention = int((group["attention_label"] == "high_attention").sum())

        if "rumor_label" in group.columns:
            rumor_noise = int((group["rumor_label"] != "no_rumor_signal").sum())

        if "risk_label" in group.columns:
            risk_noise = int((group["risk_label"] != "no_risk_noise").sum())

        if "social_attention_score" in group.columns:
            avg_social_attention_score = group["social_attention_score"].apply(safe_float).mean()

        if "rumor_noise_score" in group.columns:
            avg_rumor_noise_score = group["rumor_noise_score"].apply(safe_float).mean()

        if "risk_noise_score" in group.columns:
            avg_risk_noise_score = group["risk_noise_score"].apply(safe_float).mean()

        rows.append(
            {
                "event_type": event_type,
                "social_rows": len(group),
                "high_attention_count": high_attention,
                "rumor_noise_count": rumor_noise,
                "risk_noise_count": risk_noise,
                "avg_social_attention_score": round(avg_social_attention_score, 2),
                "avg_rumor_noise_score": round(avg_rumor_noise_score, 2),
                "avg_risk_noise_score": round(avg_risk_noise_score, 2),
            }
        )

    return pd.DataFrame(rows)


def build_learned_rules(
    error_df: pd.DataFrame,
    market_summary_df: pd.DataFrame,
    social_summary_df: pd.DataFrame,
) -> pd.DataFrame:
    if error_df.empty:
        return pd.DataFrame()

    required_columns = ["event_type", "prediction_result"]

    for column in required_columns:
        if column not in error_df.columns:
            print(f"Missing required column: {column}")
            return pd.DataFrame()

    df = error_df.copy()
    df["normalized_prediction_result"] = df["prediction_result"].apply(normalize_result)

    rows = []

    for event_type, group in df.groupby("event_type"):
        success_count = int((group["normalized_prediction_result"] == "success").sum())
        failure_count = int((group["normalized_prediction_result"] == "failure").sum())
        pending_count = int((group["normalized_prediction_result"] == "pending").sum())

        evaluated_count = success_count + failure_count
        total_count = len(group)

        success_rate = success_count / evaluated_count if evaluated_count > 0 else 0
        failure_rate = failure_count / evaluated_count if evaluated_count > 0 else 0
        pending_rate = pending_count / total_count if total_count > 0 else 0

        learned_adjustment, learning_label, learning_reason = calculate_adjustment(
            success_rate,
            evaluated_count,
        )

        confidence_multiplier = 1.0

        if evaluated_count < MIN_EVALUATED_COUNT:
            confidence_multiplier = 0.0
        elif evaluated_count < 10:
            confidence_multiplier = 0.5
        elif evaluated_count < 30:
            confidence_multiplier = 0.75

        final_learned_adjustment = round(learned_adjustment * confidence_multiplier, 2)

        rows.append(
            {
                "event_type": event_type,
                "total_count": total_count,
                "success_count": success_count,
                "failure_count": failure_count,
                "pending_count": pending_count,
                "evaluated_count": evaluated_count,
                "success_rate": round(success_rate, 4),
                "failure_rate": round(failure_rate, 4),
                "pending_rate": round(pending_rate, 4),
                "raw_learned_adjustment": learned_adjustment,
                "confidence_multiplier": confidence_multiplier,
                "learned_event_score_adjustment": final_learned_adjustment,
                "learning_label": learning_label,
                "learning_reason": learning_reason,
                "minimum_required_evaluated_count": MIN_EVALUATED_COUNT,
            }
        )

    rules_df = pd.DataFrame(rows)

    if rules_df.empty:
        return rules_df

    if not market_summary_df.empty:
        rules_df = rules_df.merge(
            market_summary_df,
            on="event_type",
            how="left",
        )

    if not social_summary_df.empty:
        rules_df = rules_df.merge(
            social_summary_df,
            on="event_type",
            how="left",
        )

    fill_zero_columns = [
        "market_adjusted_success_count",
        "market_adjusted_failure_count",
        "market_adjusted_pending_count",
        "market_adjusted_evaluated_count",
        "market_adjusted_success_rate",
        "social_rows",
        "high_attention_count",
        "rumor_noise_count",
        "risk_noise_count",
        "avg_social_attention_score",
        "avg_rumor_noise_score",
        "avg_risk_noise_score",
    ]

    for column in fill_zero_columns:
        if column in rules_df.columns:
            rules_df[column] = rules_df[column].fillna(0)

    rules_df = rules_df.sort_values(
        by=["evaluated_count", "success_rate"],
        ascending=[False, False],
    )

    return rules_df


def save_rules(rules_df: pd.DataFrame) -> str:
    os.makedirs(PROCESSED_DIR, exist_ok=True)

    today = datetime.today().strftime("%Y%m%d")
    output_path = PROCESSED_DIR / f"learned_event_rules_{today}.csv"

    rules_df.to_csv(output_path, index=False, encoding="utf-8-sig")

    return str(output_path)


def build_report(rules_df: pd.DataFrame) -> str:
    os.makedirs(REPORT_DIR, exist_ok=True)

    today_display = datetime.today().strftime("%Y-%m-%d")
    output_path = REPORT_DIR / f"{today_display}_auto_rule_update_report.md"

    lines = []

    lines.append(f"# Auto Rule Update Report - {today_display}")
    lines.append("")
    lines.append("## Purpose")
    lines.append("")
    lines.append(
        "This report summarizes automatically learned event-type score adjustments "
        "based on accumulated prediction success and failure history."
    )
    lines.append("")
    lines.append(
        "The original rule-based event scoring file is not overwritten. "
        "The learned rules are saved separately and can be safely used as an additional score layer."
    )
    lines.append("")

    if rules_df.empty:
        lines.append("No learned rules generated.")
        lines.append("")

        with open(output_path, "w", encoding="utf-8") as file:
            file.write("\n".join(lines))

        return str(output_path)

    active_rules = int((rules_df["learned_event_score_adjustment"] != 0).sum())
    positive_rules = int((rules_df["learned_event_score_adjustment"] > 0).sum())
    negative_rules = int((rules_df["learned_event_score_adjustment"] < 0).sum())
    hold_rules = int((rules_df["learning_label"] == "hold_insufficient_data").sum())

    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Total event types: **{len(rules_df)}**")
    lines.append(f"- Active learned rules: **{active_rules}**")
    lines.append(f"- Positive adjustment rules: **{positive_rules}**")
    lines.append(f"- Negative adjustment rules: **{negative_rules}**")
    lines.append(f"- Held due to insufficient data: **{hold_rules}**")
    lines.append(f"- Minimum evaluated count: **{MIN_EVALUATED_COUNT}**")
    lines.append("")

    lines.append("## Learned Event Rules")
    lines.append("")

    display_columns = [
        "event_type",
        "total_count",
        "evaluated_count",
        "success_count",
        "failure_count",
        "pending_count",
        "success_rate",
        "learned_event_score_adjustment",
        "learning_label",
    ]

    lines.append("| " + " | ".join(display_columns) + " |")
    lines.append("|" + "|".join(["---"] * len(display_columns)) + "|")

    for _, row in rules_df.iterrows():
        values = []

        for column in display_columns:
            value = row.get(column, "N/A")

            if column.endswith("rate"):
                try:
                    value = f"{float(value) * 100:.2f}%"
                except Exception:
                    value = "N/A"

            values.append(str(value))

        lines.append("| " + " | ".join(values) + " |")

    lines.append("")
    lines.append("## Interpretation")
    lines.append("")
    lines.append("- Positive adjustments mean the event type has shown stronger historical performance.")
    lines.append("- Negative adjustments mean the event type has shown weaker historical performance.")
    lines.append("- Held rules mean there are not enough evaluated cases yet.")
    lines.append("- This is a conservative learning layer and should not be interpreted as investment advice.")
    lines.append("")

    lines.append("## Next Step")
    lines.append("")
    lines.append(
        "The next step is to integrate learned_event_score_adjustment into the daily candidate scoring formula."
    )
    lines.append("")

    with open(output_path, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))

    return str(output_path)


def main():
    print("Generating learned event rules...")

    error_df = read_all_csv(PREDICTIONS_DIR, "error_notes_*.csv")
    market_df = read_all_csv(PREDICTIONS_DIR, "market_adjusted_evaluation_*.csv")

    latest_social_path = latest_file(PROCESSED_DIR, "social_attention_features_*.csv")
    social_df = read_csv(latest_social_path)

    print(f"Error-note rows: {len(error_df)}")
    print(f"Market-adjusted evaluation rows: {len(market_df)}")
    print(f"Latest social attention file: {latest_social_path}")
    print(f"Social attention rows: {len(social_df)}")

    market_summary_df = summarize_market_adjusted(market_df)
    social_summary_df = summarize_social_attention(social_df)

    rules_df = build_learned_rules(
        error_df=error_df,
        market_summary_df=market_summary_df,
        social_summary_df=social_summary_df,
    )

    rules_path = save_rules(rules_df)
    report_path = build_report(rules_df)

    print(f"Learned event rules saved to: {rules_path}")
    print(f"Auto rule update report saved to: {report_path}")
    print(f"Rows: {len(rules_df)}")


if __name__ == "__main__":
    main()
