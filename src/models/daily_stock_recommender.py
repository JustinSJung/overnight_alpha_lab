"""
Daily stock recommender.

This script generates a daily stock candidate report from the latest ML dataset.
It applies historical confidence adjustments from advanced error notes and
event-type performance adjustments from historical success rates and returns.

Output:
reports/daily_prediction/YYYY-MM-DD_daily_stock_candidates.md
"""

import os
from datetime import datetime

import pandas as pd


PROCESSED_DIR = "data/processed"
PREDICTIONS_DIR = "data/predictions"
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


def normalize_stock_code(value) -> str:
    """
    Normalize stock code to 6-digit string.
    """

    if pd.isna(value):
        return ""

    try:
        return str(int(float(value))).zfill(6)
    except Exception:
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

    path = get_latest_file(PROCESSED_DIR, "ml_dataset_")

    if path is None:
        return pd.DataFrame(), ""

    try:
        df = pd.read_csv(path)

        if "stock_code" in df.columns:
            df["stock_code"] = df["stock_code"].apply(normalize_stock_code)

        return df, path
    except Exception:
        return pd.DataFrame(), path


def load_error_notes():
    """
    Load all available advanced error note files.
    """

    if not os.path.exists(PREDICTIONS_DIR):
        return pd.DataFrame()

    files = [
        file for file in os.listdir(PREDICTIONS_DIR)
        if file.startswith("error_notes_") and file.endswith(".csv")
    ]

    if not files:
        return pd.DataFrame()

    frames = []

    for file in files:
        path = os.path.join(PREDICTIONS_DIR, file)

        try:
            df = pd.read_csv(path)

            if "stock_code" in df.columns:
                df["stock_code"] = df["stock_code"].apply(normalize_stock_code)

            frames.append(df)
        except Exception:
            continue

    if not frames:
        return pd.DataFrame()

    return pd.concat(frames, ignore_index=True)


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


def build_error_note_adjustment_table(error_notes_df: pd.DataFrame) -> pd.DataFrame:
    """
    Build event-type level confidence adjustment table from error notes.
    """

    if error_notes_df.empty:
        return pd.DataFrame()

    required_columns = [
        "event_type",
        "confidence_adjustment",
    ]

    for col in required_columns:
        if col not in error_notes_df.columns:
            return pd.DataFrame()

    df = error_notes_df.copy()

    df["event_type"] = df["event_type"].astype(str)
    df["confidence_adjustment"] = df["confidence_adjustment"].astype(str)

    rows = []

    for event_type, group in df.groupby("event_type"):
        total_count = len(group)

        increase_count = (group["confidence_adjustment"] == "increase").sum()
        decrease_count = (group["confidence_adjustment"] == "decrease").sum()
        slightly_decrease_count = (
            group["confidence_adjustment"] == "slightly_decrease"
        ).sum()
        hold_count = (group["confidence_adjustment"] == "hold").sum()

        success_count = 0
        failure_count = 0
        pending_count = 0

        if "prediction_result" in group.columns:
            success_count = (group["prediction_result"] == "success").sum()
            failure_count = (group["prediction_result"] == "failure").sum()
            pending_count = (group["prediction_result"] == "pending").sum()

        adjustment_score = 0
        adjustment_score += increase_count * 5
        adjustment_score -= decrease_count * 7
        adjustment_score -= slightly_decrease_count * 3

        if total_count > 0:
            adjustment_score = adjustment_score / total_count

        rows.append(
            {
                "event_type": event_type,
                "historical_error_note_count": total_count,
                "historical_success_count": success_count,
                "historical_failure_count": failure_count,
                "historical_pending_count": pending_count,
                "historical_increase_count": increase_count,
                "historical_decrease_count": decrease_count,
                "historical_slightly_decrease_count": slightly_decrease_count,
                "historical_hold_count": hold_count,
                "error_note_adjustment_score": round(adjustment_score, 2),
            }
        )

    return pd.DataFrame(rows)


def build_event_type_performance_adjustment_table(
    error_notes_df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Build event-type success-rate and return adjustment table.

    This table uses evaluated historical rows only.
    Pending rows are counted but not used for success-rate calculation.
    """

    if error_notes_df.empty:
        return pd.DataFrame()

    required_columns = [
        "event_type",
        "prediction_result",
        "next_close_return",
    ]

    for col in required_columns:
        if col not in error_notes_df.columns:
            return pd.DataFrame()

    df = error_notes_df.copy()

    df["event_type"] = df["event_type"].astype(str)
    df["prediction_result"] = df["prediction_result"].astype(str)
    df["next_close_return"] = pd.to_numeric(
        df["next_close_return"],
        errors="coerce",
    )

    if "next_open_return" in df.columns:
        df["next_open_return"] = pd.to_numeric(
            df["next_open_return"],
            errors="coerce",
        )
    else:
        df["next_open_return"] = pd.NA

    rows = []

    for event_type, group in df.groupby("event_type"):
        total_count = len(group)

        success_count = (group["prediction_result"] == "success").sum()
        failure_count = (group["prediction_result"] == "failure").sum()
        pending_count = (group["prediction_result"] == "pending").sum()

        evaluated_count = success_count + failure_count

        if evaluated_count > 0:
            success_rate = success_count / evaluated_count
        else:
            success_rate = None

        avg_next_open_return = group["next_open_return"].mean()
        avg_next_close_return = group["next_close_return"].mean()

        success_rate_adjustment = 0.0
        return_adjustment = 0.0

        if success_rate is not None:
            if evaluated_count >= 3:
                if success_rate >= 0.65:
                    success_rate_adjustment = 6.0
                elif success_rate >= 0.55:
                    success_rate_adjustment = 3.0
                elif success_rate <= 0.35:
                    success_rate_adjustment = -6.0
                elif success_rate <= 0.45:
                    success_rate_adjustment = -3.0
            else:
                # Small sample: adjust very lightly.
                if success_rate >= 0.70:
                    success_rate_adjustment = 2.0
                elif success_rate <= 0.30:
                    success_rate_adjustment = -2.0

        if not pd.isna(avg_next_close_return):
            if avg_next_close_return >= 0.03:
                return_adjustment = 4.0
            elif avg_next_close_return >= 0.01:
                return_adjustment = 2.0
            elif avg_next_close_return <= -0.03:
                return_adjustment = -4.0
            elif avg_next_close_return <= -0.01:
                return_adjustment = -2.0

        event_type_performance_adjustment_score = (
            success_rate_adjustment + return_adjustment
        )

        rows.append(
            {
                "event_type": event_type,
                "event_type_total_count": total_count,
                "event_type_evaluated_count": evaluated_count,
                "event_type_success_count": success_count,
                "event_type_failure_count": failure_count,
                "event_type_pending_count": pending_count,
                "event_type_success_rate": success_rate,
                "event_type_avg_next_open_return": avg_next_open_return,
                "event_type_avg_next_close_return": avg_next_close_return,
                "event_type_success_rate_adjustment": success_rate_adjustment,
                "event_type_return_adjustment": return_adjustment,
                "event_type_performance_adjustment_score": round(
                    event_type_performance_adjustment_score,
                    2,
                ),
            }
        )

    return pd.DataFrame(rows)


def calculate_base_recommendation_score(row) -> float:
    """
    Calculate base recommendation score before historical adjustment.
    """

    event_score = safe_number(row.get("event_score", 0))
    news_sentiment_score = safe_number(row.get("news_sentiment_score", 0))
    news_attention_score = safe_number(row.get("news_attention_score", 0))
    negative_keyword_count = safe_number(row.get("negative_keyword_count", 0))

    score = event_score
    score += news_sentiment_score * 5
    score += min(news_attention_score, 10) * 2
    score -= negative_keyword_count * 3

    prediction_direction = str(row.get("prediction_direction", ""))

    if prediction_direction in POSITIVE_DIRECTIONS:
        score += 10
    elif prediction_direction in NEGATIVE_DIRECTIONS:
        score -= 10
    elif prediction_direction in VOLATILE_DIRECTIONS:
        score -= 5

    return score


def classify_risk_level(row) -> str:
    """
    Classify risk level.
    """

    event_type = str(row.get("event_type", ""))
    prediction_direction = str(row.get("prediction_direction", ""))
    negative_keywords = safe_number(row.get("negative_keyword_count", 0))
    adjusted_score = safe_number(row.get("adjusted_recommendation_score", 0))

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

    if adjusted_score < 30:
        return "MEDIUM"

    return "LOW"


def classify_candidate_type(row) -> str:
    """
    Classify candidate type.
    """

    prediction_direction = str(row.get("prediction_direction", ""))
    risk_level = str(row.get("risk_level", ""))
    adjusted_score = safe_number(row.get("adjusted_recommendation_score", 0))

    if risk_level == "HIGH":
        return "AVOID_OR_RISK_REVIEW"

    if prediction_direction in POSITIVE_DIRECTIONS and adjusted_score >= 60:
        return "POSITIVE_CANDIDATE"

    if prediction_direction == "volatile":
        return "WATCHLIST_VOLATILE"

    if adjusted_score >= 40:
        return "WATCHLIST"

    return "WATCHLIST"


def build_recommendation_reason(row) -> str:
    """
    Build recommendation reason text.
    """

    event_type = row.get("event_type", "unknown")
    prediction_direction = row.get("prediction_direction", "unknown")
    event_score = safe_number(row.get("event_score", 0))
    news_attention_score = safe_number(row.get("news_attention_score", 0))
    news_sentiment_score = safe_number(row.get("news_sentiment_score", 0))
    negative_keyword_count = safe_number(row.get("negative_keyword_count", 0))
    error_note_adjustment_score = safe_number(
        row.get("error_note_adjustment_score", 0)
    )
    performance_adjustment_score = safe_number(
        row.get("event_type_performance_adjustment_score", 0)
    )

    reason_parts = []

    reason_parts.append(f"Event type is {event_type}.")
    reason_parts.append(f"Initial direction is {prediction_direction}.")
    reason_parts.append(f"Event score is {event_score:.0f}.")
    reason_parts.append(f"News attention score is {news_attention_score:.0f}.")
    reason_parts.append(f"News sentiment score is {news_sentiment_score:.0f}.")

    if negative_keyword_count > 0:
        reason_parts.append(
            f"Negative keyword count is {negative_keyword_count:.0f}."
        )

    if error_note_adjustment_score > 0:
        reason_parts.append(
            f"Historical error notes added {error_note_adjustment_score:.2f} points."
        )
    elif error_note_adjustment_score < 0:
        reason_parts.append(
            f"Historical error notes subtracted {abs(error_note_adjustment_score):.2f} points."
        )
    else:
        reason_parts.append(
            "Historical error notes did not change the score."
        )

    if performance_adjustment_score > 0:
        reason_parts.append(
            f"Event-type performance added {performance_adjustment_score:.2f} points."
        )
    elif performance_adjustment_score < 0:
        reason_parts.append(
            f"Event-type performance subtracted {abs(performance_adjustment_score):.2f} points."
        )
    else:
        reason_parts.append(
            "Event-type performance did not change the score."
        )

    return " ".join(reason_parts)


def prepare_candidates(df: pd.DataFrame, top_n: int = 30) -> pd.DataFrame:
    """
    Prepare candidate dataframe.
    """

    if df.empty:
        return pd.DataFrame()

    candidates = df.copy()

    candidates["base_recommendation_score"] = candidates.apply(
        calculate_base_recommendation_score,
        axis=1,
    )

    score_columns = [
        "error_note_adjustment_score",
        "event_type_success_rate_adjustment",
        "event_type_return_adjustment",
        "event_type_performance_adjustment_score",
    ]

    for col in score_columns:
        if col not in candidates.columns:
            candidates[col] = 0.0

        candidates[col] = candidates[col].fillna(0.0)

    candidates["adjusted_recommendation_score"] = (
        candidates["base_recommendation_score"]
        + candidates["error_note_adjustment_score"]
        + candidates["event_type_performance_adjustment_score"]
    )

    candidates["risk_level"] = candidates.apply(
        classify_risk_level,
        axis=1,
    )

    candidates["candidate_type"] = candidates.apply(
        classify_candidate_type,
        axis=1,
    )

    candidates["recommendation_reason"] = candidates.apply(
        build_recommendation_reason,
        axis=1,
    )

    candidates = candidates.sort_values(
        by="adjusted_recommendation_score",
        ascending=False,
    )

    return candidates.head(top_n)


def build_report() -> str:
    """
    Build daily stock candidate Markdown report.
    """

    today = datetime.today().strftime("%Y-%m-%d")
    generated_at = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

    df, ml_dataset_path = load_latest_ml_dataset()
    error_notes_df = load_error_notes()

    adjustment_table = build_error_note_adjustment_table(error_notes_df)
    performance_adjustment_table = build_event_type_performance_adjustment_table(
        error_notes_df,
    )

    if not df.empty and "event_type" in df.columns:
        df["event_type"] = df["event_type"].astype(str)

    if not adjustment_table.empty:
        df = df.merge(
            adjustment_table,
            on="event_type",
            how="left",
        )

    if not performance_adjustment_table.empty:
        df = df.merge(
            performance_adjustment_table,
            on="event_type",
            how="left",
        )

    adjustment_columns = [
        "historical_error_note_count",
        "historical_success_count",
        "historical_failure_count",
        "historical_pending_count",
        "historical_increase_count",
        "historical_decrease_count",
        "historical_slightly_decrease_count",
        "historical_hold_count",
        "error_note_adjustment_score",
        "event_type_total_count",
        "event_type_evaluated_count",
        "event_type_success_count",
        "event_type_failure_count",
        "event_type_pending_count",
        "event_type_success_rate",
        "event_type_avg_next_open_return",
        "event_type_avg_next_close_return",
        "event_type_success_rate_adjustment",
        "event_type_return_adjustment",
        "event_type_performance_adjustment_score",
    ]

    for col in adjustment_columns:
        if col not in df.columns:
            df[col] = 0

    fill_zero_columns = [
        "historical_error_note_count",
        "historical_success_count",
        "historical_failure_count",
        "historical_pending_count",
        "historical_increase_count",
        "historical_decrease_count",
        "historical_slightly_decrease_count",
        "historical_hold_count",
        "error_note_adjustment_score",
        "event_type_total_count",
        "event_type_evaluated_count",
        "event_type_success_count",
        "event_type_failure_count",
        "event_type_pending_count",
        "event_type_success_rate_adjustment",
        "event_type_return_adjustment",
        "event_type_performance_adjustment_score",
    ]

    for col in fill_zero_columns:
        df[col] = df[col].fillna(0)

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
        "news sentiment, news attention, prediction direction, simple risk filters, "
        "historical confidence adjustments from advanced error notes, and event-type "
        "performance adjustments based on historical success rates and returns."
    )
    lines.append("")

    lines.append("## Event-Type Success Rate Adjustment")
    lines.append("")
    lines.append(
        "The recommender now applies a direct event-type performance adjustment. "
        "Event types with stronger historical success rates or positive average next-day "
        "returns can receive a small positive adjustment. Event types with weak success "
        "rates or negative average returns can receive a conservative penalty."
    )
    lines.append("")

    if performance_adjustment_table.empty:
        lines.append("No event-type performance adjustment data is available yet.")
        lines.append("")
    else:
        lines.append(
            "| Event Type | Total | Evaluated | Success Rate | Avg Next Close | Success Adj | Return Adj | Total Adj |"
        )
        lines.append("|---|---:|---:|---:|---:|---:|---:|---:|")

        view = performance_adjustment_table.sort_values(
            by="event_type_performance_adjustment_score",
            ascending=False,
        ).head(12)

        for _, row in view.iterrows():
            success_rate = row.get("event_type_success_rate", None)

            if pd.isna(success_rate) or success_rate is None:
                success_rate_text = "N/A"
            else:
                success_rate_text = f"{safe_number(success_rate) * 100:.2f}%"

            lines.append(
                f"| {row.get('event_type', '')} "
                f"| {int(safe_number(row.get('event_type_total_count', 0)))} "
                f"| {int(safe_number(row.get('event_type_evaluated_count', 0)))} "
                f"| {success_rate_text} "
                f"| {format_percent(row.get('event_type_avg_next_close_return', None))} "
                f"| {safe_number(row.get('event_type_success_rate_adjustment', 0)):.2f} "
                f"| {safe_number(row.get('event_type_return_adjustment', 0)):.2f} "
                f"| {safe_number(row.get('event_type_performance_adjustment_score', 0)):.2f} |"
            )

        lines.append("")

    lines.append("## Error-Note Learning Adjustment")
    lines.append("")
    lines.append(
        "The recommender also reads past error notes and applies event-type level "
        "confidence adjustments from `confidence_adjustment` values."
    )
    lines.append("")

    if adjustment_table.empty:
        lines.append("No historical error-note adjustment data is available yet.")
        lines.append("")
    else:
        lines.append("| Event Type | Notes | Success | Failure | Pending | Adjustment |")
        lines.append("|---|---:|---:|---:|---:|---:|")

        adjustment_view = adjustment_table.sort_values(
            by="error_note_adjustment_score",
            ascending=False,
        ).head(10)

        for _, row in adjustment_view.iterrows():
            lines.append(
                f"| {row.get('event_type', '')} "
                f"| {int(safe_number(row.get('historical_error_note_count', 0)))} "
                f"| {int(safe_number(row.get('historical_success_count', 0)))} "
                f"| {int(safe_number(row.get('historical_failure_count', 0)))} "
                f"| {int(safe_number(row.get('historical_pending_count', 0)))} "
                f"| {safe_number(row.get('error_note_adjustment_score', 0)):.2f} |"
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

    watchlist_candidates = candidates[
        candidates["candidate_type"] == "WATCHLIST"
    ].copy()

    risk_candidates = candidates[
        candidates["candidate_type"] == "AVOID_OR_RISK_REVIEW"
    ].copy()

    def append_candidate_section(section_title: str, section_df: pd.DataFrame, max_rows: int):
        lines.append(f"## {section_title}")
        lines.append("")

        if section_df.empty:
            lines.append("No candidates in this section.")
            lines.append("")
            return

        if section_title == "Risk / Avoid Review List":
            section_df = section_df.sort_values(
                by="adjusted_recommendation_score",
                ascending=True,
            ).head(max_rows)
        else:
            section_df = section_df.sort_values(
                by="adjusted_recommendation_score",
                ascending=False,
            ).head(max_rows)

        for rank, (_, row) in enumerate(section_df.iterrows(), start=1):
            corp_name = row.get("corp_name", "Unknown")
            stock_code = str(row.get("stock_code", "")).zfill(6)
            event_type = row.get("event_type", "unknown")
            report_nm = row.get("report_nm", "")
            prediction_direction = row.get("prediction_direction", "unknown")
            base_score = safe_number(row.get("base_recommendation_score", 0))
            error_note_score = safe_number(row.get("error_note_adjustment_score", 0))
            performance_score = safe_number(
                row.get("event_type_performance_adjustment_score", 0)
            )
            adjusted_score = safe_number(row.get("adjusted_recommendation_score", 0))
            risk_level = row.get("risk_level", "UNKNOWN")
            candidate_type = row.get("candidate_type", "WATCHLIST")
            reason = row.get("recommendation_reason", "")
            top_news_titles = row.get("top_news_titles", "")

            next_open_return = row.get("next_open_return", None)
            next_close_return = row.get("next_close_return", None)

            event_type_evaluated_count = safe_number(
                row.get("event_type_evaluated_count", 0)
            )
            event_type_success_rate = row.get("event_type_success_rate", None)
            event_type_avg_close = row.get("event_type_avg_next_close_return", None)

            if pd.isna(event_type_success_rate):
                event_type_success_rate_text = "N/A"
            else:
                event_type_success_rate_text = (
                    f"{safe_number(event_type_success_rate) * 100:.2f}%"
                )

            lines.append(f"### {rank}. {corp_name} ({stock_code})")
            lines.append("")
            lines.append(f"- Candidate type: **{candidate_type}**")
            lines.append(f"- Expected direction: **{prediction_direction}**")
            lines.append(f"- Base recommendation score: **{base_score:.2f}**")
            lines.append(f"- Error-note adjustment score: **{error_note_score:.2f}**")
            lines.append(f"- Event-type performance adjustment score: **{performance_score:.2f}**")
            lines.append(f"- Adjusted recommendation score: **{adjusted_score:.2f}**")
            lines.append(f"- Risk level: **{risk_level}**")
            lines.append(f"- Event type: `{event_type}`")
            lines.append(
                f"- Event-type evaluated cases: {event_type_evaluated_count:.0f}, "
                f"success rate: {event_type_success_rate_text}, "
                f"avg next close: {format_percent(event_type_avg_close)}"
            )

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
        risk_candidates,
        max_rows=10,
    )

    lines.append("## Data Readiness")
    lines.append("")
    lines.append(
        "At this stage, candidates are still generated using rule-based scoring. "
        "The system now also uses historical error-note patterns and event-type "
        "performance statistics as conservative confidence adjustment layers. "
        "These adjustments will become more meaningful after enough evaluated "
        "event-reaction samples are accumulated."
    )
    lines.append("")

    lines.append("## How to Read This Report")
    lines.append("")
    lines.append("- Positive Candidates: relatively favorable event and news conditions.")
    lines.append("- Volatile Watchlist: potentially important events with uncertain direction.")
    lines.append("- General Watchlist: events worth monitoring but not strong enough for positive classification.")
    lines.append("- Risk / Avoid Review List: negative or high-risk events such as capital increases, CB/BW, lawsuits, or disclosure violations.")
    lines.append("- Error-note adjustment score: learning signal from previous advanced error notes.")
    lines.append("- Event-type performance adjustment score: success-rate and average-return based adjustment.")
    lines.append("")

    lines.append("## Next Step")
    lines.append("")
    lines.append(
        "The next step is to add stock-specific historical reaction patterns, so the system can distinguish between event-type level behavior and stock-level behavior."
    )
    lines.append("")

    return "\n".join(lines)


def save_report(report_text: str) -> str:
    """
    Save daily stock candidate report.
    """

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    today = datetime.today().strftime("%Y-%m-%d")
    output_path = os.path.join(
        OUTPUT_DIR,
        f"{today}_daily_stock_candidates.md",
    )

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
