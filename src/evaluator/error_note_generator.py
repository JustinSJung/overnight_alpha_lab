"""
Advanced error note generator.

This script compares predicted event direction with actual next-day
price reaction and generates detailed learning notes.

Output:
data/predictions/error_notes_YYYYMMDD.csv
"""

import os
from datetime import datetime

import pandas as pd


PROCESSED_DIR = "data/processed"
PREDICTIONS_DIR = "data/predictions"


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
    Find the latest file by filename.
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


def load_latest_scored_events():
    """
    Load latest scored key events.
    """

    path = get_latest_file(PROCESSED_DIR, "scored_key_events_")

    if path is None:
        return pd.DataFrame(), ""

    df = pd.read_csv(path)

    if "stock_code" in df.columns:
        df["stock_code"] = df["stock_code"].apply(normalize_stock_code)

    return df, path


def load_latest_news_features():
    """
    Load latest event-news feature file.
    """

    path = get_latest_file(PROCESSED_DIR, "event_news_features_")

    if path is None:
        return pd.DataFrame(), ""

    df = pd.read_csv(path)

    if "stock_code" in df.columns:
        df["stock_code"] = df["stock_code"].apply(normalize_stock_code)

    return df, path


def load_event_price_reactions():
    """
    Load all event-price reaction files.
    """

    if not os.path.exists(PREDICTIONS_DIR):
        return pd.DataFrame()

    files = [
        file for file in os.listdir(PREDICTIONS_DIR)
        if file.startswith("event_price_reaction_") and file.endswith(".csv")
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


def safe_float(value, default=0.0) -> float:
    """
    Convert value to float safely.
    """

    try:
        if pd.isna(value):
            return default

        return float(value)
    except Exception:
        return default


def determine_prediction_result(prediction_direction: str, next_close_return):
    """
    Determine success, failure, or pending.
    """

    if pd.isna(next_close_return):
        return "pending"

    actual_return = safe_float(next_close_return)

    if prediction_direction in POSITIVE_DIRECTIONS:
        if actual_return > 0:
            return "success"
        return "failure"

    if prediction_direction in NEGATIVE_DIRECTIONS:
        if actual_return < 0:
            return "success"
        return "failure"

    if prediction_direction in VOLATILE_DIRECTIONS:
        if abs(actual_return) >= 0.02:
            return "success"
        return "failure"

    return "unknown"


def build_error_category(row) -> str:
    """
    Build high-level error category.
    """

    prediction_result = row.get("prediction_result", "unknown")
    prediction_direction = row.get("prediction_direction", "unknown")
    event_type = row.get("event_type", "unknown")

    news_sentiment_score = safe_float(row.get("news_sentiment_score", 0))
    negative_keyword_count = safe_float(row.get("negative_keyword_count", 0))
    news_attention_score = safe_float(row.get("news_attention_score", 0))
    next_close_return = row.get("next_close_return", None)

    high_risk_events = [
        "paid_in_capital_increase",
        "convertible_bond",
        "bond_with_warrant",
        "lawsuit",
        "disclosure_violation",
    ]

    if prediction_result == "pending":
        return "pending_price_data"

    if prediction_result == "success":
        if prediction_direction in POSITIVE_DIRECTIONS:
            return "positive_signal_confirmed"
        if prediction_direction in NEGATIVE_DIRECTIONS:
            return "negative_signal_confirmed"
        if prediction_direction in VOLATILE_DIRECTIONS:
            return "volatility_signal_confirmed"
        return "success_unknown_pattern"

    if prediction_result == "failure":
        if event_type in high_risk_events and prediction_direction in POSITIVE_DIRECTIONS:
            return "risk_event_misclassified"

        if prediction_direction in POSITIVE_DIRECTIONS and news_sentiment_score <= 0:
            return "weak_positive_signal"

        if prediction_direction in POSITIVE_DIRECTIONS and negative_keyword_count >= 2:
            return "positive_signal_with_negative_noise"

        if prediction_direction in POSITIVE_DIRECTIONS and news_attention_score <= 0:
            return "low_attention_positive_signal"

        if prediction_direction in NEGATIVE_DIRECTIONS:
            return "negative_signal_reversed"

        if prediction_direction in VOLATILE_DIRECTIONS:
            actual_return = safe_float(next_close_return)
            if abs(actual_return) < 0.02:
                return "volatility_overestimated"
            return "volatility_direction_mismatch"

        return "general_prediction_failure"

    return "unknown"


def build_detailed_error_reason(row) -> str:
    """
    Build detailed reason text.
    """

    prediction_result = row.get("prediction_result", "unknown")
    prediction_direction = row.get("prediction_direction", "unknown")
    event_type = row.get("event_type", "unknown")
    report_nm = row.get("report_nm", "")

    event_score = safe_float(row.get("event_score", 0))
    news_sentiment_score = safe_float(row.get("news_sentiment_score", 0))
    news_attention_score = safe_float(row.get("news_attention_score", 0))
    negative_keyword_count = safe_float(row.get("negative_keyword_count", 0))
    next_close_return = row.get("next_close_return", None)

    if prediction_result == "pending":
        return (
            "Actual next-day price reaction is not available yet. "
            "The prediction cannot be evaluated until price data is collected."
        )

    actual_text = "not available"
    if not pd.isna(next_close_return):
        actual_text = f"{safe_float(next_close_return) * 100:.2f}%"

    if prediction_result == "success":
        return (
            f"The prediction direction `{prediction_direction}` was consistent with "
            f"the actual next close return of {actual_text}. "
            f"The event type was `{event_type}`, event score was {event_score:.2f}, "
            f"news sentiment score was {news_sentiment_score:.2f}, and news attention score was {news_attention_score:.2f}."
        )

    reasons = []

    reasons.append(
        f"The prediction direction was `{prediction_direction}`, but the actual next close return was {actual_text}."
    )

    reasons.append(
        f"The event type was `{event_type}` with event score {event_score:.2f}."
    )

    if report_nm:
        reasons.append(
            f"The disclosure title was `{report_nm}`."
        )

    if news_sentiment_score <= 0 and prediction_direction in POSITIVE_DIRECTIONS:
        reasons.append(
            "Although the event direction was positive, news sentiment was weak or neutral."
        )

    if negative_keyword_count >= 2:
        reasons.append(
            f"The event had {negative_keyword_count:.0f} negative keyword signals, which may have reduced market confidence."
        )

    if news_attention_score <= 0:
        reasons.append(
            "News attention was low, so the event may not have been strong enough to trigger a price reaction."
        )

    if prediction_direction in VOLATILE_DIRECTIONS:
        reasons.append(
            "The event was treated as volatile, but the actual price movement may have been smaller than expected."
        )

    return " ".join(reasons)


def build_learning_point(row) -> str:
    """
    Build learning point.
    """

    error_category = row.get("error_category", "unknown")
    prediction_result = row.get("prediction_result", "unknown")

    if prediction_result == "pending":
        return "Do not update model confidence until actual price reaction data becomes available."

    if prediction_result == "success":
        return "This event pattern can be treated as a useful reference case for future predictions."

    mapping = {
        "weak_positive_signal": (
            "Positive event predictions should be treated more conservatively when news sentiment is weak."
        ),
        "positive_signal_with_negative_noise": (
            "Positive events with multiple negative keywords should receive lower confidence."
        ),
        "low_attention_positive_signal": (
            "Positive events with low news attention may not produce meaningful next-day reactions."
        ),
        "risk_event_misclassified": (
            "High-risk event types should not be classified as positive without strong supporting evidence."
        ),
        "negative_signal_reversed": (
            "Some negative events can rebound if the market interprets them as already priced in or less severe than expected."
        ),
        "volatility_overestimated": (
            "Volatile event classification should require stronger attention or stronger historical movement patterns."
        ),
        "volatility_direction_mismatch": (
            "Volatile events need separate direction prediction rather than only movement prediction."
        ),
        "general_prediction_failure": (
            "The current rule set was not sufficient to explain the actual price reaction."
        ),
    }

    return mapping.get(
        error_category,
        "Review this case manually and identify whether event type, news sentiment, or attention score should be adjusted.",
    )


def build_next_rule_adjustment(row) -> str:
    """
    Suggest next rule adjustment.
    """

    error_category = row.get("error_category", "unknown")
    prediction_result = row.get("prediction_result", "unknown")

    if prediction_result == "pending":
        return "Keep this row pending and re-evaluate after next trading day price data is available."

    if prediction_result == "success":
        return "Maintain current rule weight for this pattern and use it as a positive reference sample."

    mapping = {
        "weak_positive_signal": (
            "Decrease confidence for positive events when news_sentiment_score is less than or equal to zero."
        ),
        "positive_signal_with_negative_noise": (
            "Apply a penalty when negative_keyword_count is greater than or equal to two."
        ),
        "low_attention_positive_signal": (
            "Apply a penalty when news_attention_score is zero or missing."
        ),
        "risk_event_misclassified": (
            "Force high-risk event types into risk review unless supported by strong positive news and price confirmation."
        ),
        "negative_signal_reversed": (
            "Reduce negative confidence when negative events show positive actual returns repeatedly."
        ),
        "volatility_overestimated": (
            "Require higher news_attention_score before classifying an event as a strong volatility candidate."
        ),
        "volatility_direction_mismatch": (
            "Separate volatility prediction from direction prediction in future model versions."
        ),
        "general_prediction_failure": (
            "Add more features such as market index return, trading volume, and sector movement."
        ),
    }

    return mapping.get(
        error_category,
        "Keep this case for manual review and future feature engineering.",
    )


def build_confidence_adjustment(row) -> str:
    """
    Suggest confidence adjustment.
    """

    prediction_result = row.get("prediction_result", "unknown")
    error_category = row.get("error_category", "unknown")

    if prediction_result == "pending":
        return "hold"

    if prediction_result == "success":
        return "increase"

    strong_decrease_categories = [
        "risk_event_misclassified",
        "weak_positive_signal",
        "positive_signal_with_negative_noise",
        "volatility_overestimated",
    ]

    if error_category in strong_decrease_categories:
        return "decrease"

    return "slightly_decrease"


def merge_sources(scored_df, news_df, reaction_df):
    """
    Merge scored events, news features, and price reactions.
    """

    if scored_df.empty:
        return pd.DataFrame()

    df = scored_df.copy()

    if not news_df.empty:
        merge_cols = [
            col for col in news_df.columns
            if col not in df.columns or col in ["stock_code", "corp_name", "event_date"]
        ]

        news_subset = news_df[merge_cols].copy()

        possible_keys = [
            key for key in ["stock_code", "corp_name", "event_date"]
            if key in df.columns and key in news_subset.columns
        ]

        if possible_keys:
            df = df.merge(
                news_subset,
                on=possible_keys,
                how="left",
            )

    if not reaction_df.empty:
        reaction_cols = [
            "stock_code",
            "event_date",
            "next_open_return",
            "next_close_return",
        ]

        available_reaction_cols = [
            col for col in reaction_cols
            if col in reaction_df.columns
        ]

        reaction_subset = reaction_df[available_reaction_cols].copy()

        possible_keys = [
            key for key in ["stock_code", "event_date"]
            if key in df.columns and key in reaction_subset.columns
        ]

        if possible_keys:
            df = df.merge(
                reaction_subset,
                on=possible_keys,
                how="left",
            )

    return df


def generate_error_notes():
    """
    Generate advanced error notes.
    """

    scored_df, scored_path = load_latest_scored_events()
    news_df, news_path = load_latest_news_features()
    reaction_df = load_event_price_reactions()

    merged_df = merge_sources(scored_df, news_df, reaction_df)

    if merged_df.empty:
        return pd.DataFrame(), scored_path, news_path

    if "prediction_direction" not in merged_df.columns:
        merged_df["prediction_direction"] = "unknown"

    if "next_close_return" not in merged_df.columns:
        merged_df["next_close_return"] = pd.NA

    merged_df["prediction_result"] = merged_df.apply(
        lambda row: determine_prediction_result(
            str(row.get("prediction_direction", "unknown")),
            row.get("next_close_return", pd.NA),
        ),
        axis=1,
    )

    merged_df["error_category"] = merged_df.apply(
        build_error_category,
        axis=1,
    )

    merged_df["detailed_error_reason"] = merged_df.apply(
        build_detailed_error_reason,
        axis=1,
    )

    merged_df["learning_point"] = merged_df.apply(
        build_learning_point,
        axis=1,
    )

    merged_df["next_rule_adjustment"] = merged_df.apply(
        build_next_rule_adjustment,
        axis=1,
    )

    merged_df["confidence_adjustment"] = merged_df.apply(
        build_confidence_adjustment,
        axis=1,
    )

    output_columns = [
        "event_date",
        "stock_code",
        "corp_name",
        "event_type",
        "report_nm",
        "prediction_direction",
        "event_score",
        "news_count",
        "news_sentiment_score",
        "news_attention_score",
        "negative_keyword_count",
        "next_open_return",
        "next_close_return",
        "prediction_result",
        "error_category",
        "detailed_error_reason",
        "learning_point",
        "next_rule_adjustment",
        "confidence_adjustment",
    ]

    available_columns = [
        col for col in output_columns
        if col in merged_df.columns
    ]

    result_df = merged_df[available_columns].copy()

    return result_df, scored_path, news_path


def save_error_notes(df: pd.DataFrame) -> str:
    """
    Save error notes.
    """

    os.makedirs(PREDICTIONS_DIR, exist_ok=True)

    today = datetime.today().strftime("%Y%m%d")
    output_path = os.path.join(
        PREDICTIONS_DIR,
        f"error_notes_{today}.csv",
    )

    df.to_csv(output_path, index=False, encoding="utf-8-sig")

    return output_path


def main():
    print("Generating advanced error notes...")

    df, scored_path, news_path = generate_error_notes()

    if df.empty:
        print("No error notes generated.")
        print(f"Latest scored file: {scored_path if scored_path else 'Not found'}")
        print(f"Latest news feature file: {news_path if news_path else 'Not found'}")
        return

    output_path = save_error_notes(df)

    print(f"Advanced error notes saved to: {output_path}")
    print(f"Rows: {len(df)}")

    if "prediction_result" in df.columns:
        print("")
        print("Prediction result counts:")
        print(df["prediction_result"].value_counts(dropna=False))

    if "error_category" in df.columns:
        print("")
        print("Error category counts:")
        print(df["error_category"].value_counts(dropna=False))


if __name__ == "__main__":
    main()
