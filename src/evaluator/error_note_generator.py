"""
Error note generator.

This script compares rule-based event predictions
with actual next-day stock price reactions and creates
a daily review/error-note dataset.

At this stage, the system supports:
- success
- failure
- pending
"""

import os
from datetime import datetime

import pandas as pd


def get_latest_scored_events_file(processed_dir: str = "data/processed") -> str:
    """
    Find the latest scored key events CSV file.
    """

    csv_files = [
        file for file in os.listdir(processed_dir)
        if file.startswith("scored_key_events_") and file.endswith(".csv")
    ]

    if not csv_files:
        raise FileNotFoundError("No scored key events CSV files found.")

    csv_files.sort(reverse=True)
    return os.path.join(processed_dir, csv_files[0])


def get_prediction_files(prediction_dir: str = "data/predictions") -> list[str]:
    """
    Find all event-price reaction CSV files.
    """

    if not os.path.exists(prediction_dir):
        raise FileNotFoundError(f"Prediction directory not found: {prediction_dir}")

    csv_files = [
        os.path.join(prediction_dir, file)
        for file in os.listdir(prediction_dir)
        if file.startswith("event_price_reaction_") and file.endswith(".csv")
    ]

    return csv_files


def load_all_reaction_results(prediction_files: list[str]) -> pd.DataFrame:
    """
    Load all event-price reaction files into a single dataframe.
    """

    frames = []

    for file_path in prediction_files:
        try:
            df = pd.read_csv(file_path)
            if not df.empty:
                frames.append(df)
        except Exception as error:
            print(f"Failed to read {file_path}: {error}")

    if not frames:
        return pd.DataFrame()

    return pd.concat(frames, ignore_index=True)


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


def classify_prediction_result(prediction_direction: str, next_open_return) -> str:
    """
    Classify result as success, failure, or pending.
    """

    if pd.isna(next_open_return):
        return "pending"

    try:
        return_value = float(next_open_return)
    except ValueError:
        return "pending"

    if prediction_direction in ["positive", "neutral_positive"]:
        return "success" if return_value > 0 else "failure"

    if prediction_direction == "negative":
        return "success" if return_value < 0 else "failure"

    if prediction_direction == "volatile":
        return "success" if abs(return_value) >= 0.03 else "failure"

    return "pending"


def generate_error_reason(row: pd.Series) -> str:
    """
    Generate a simple error-note reason.
    """

    result = row.get("prediction_result", "")
    direction = row.get("prediction_direction", "")
    event_type = row.get("event_type", "")
    next_open_return = row.get("next_open_return", None)

    if result == "pending":
        return "Next trading day price data is not available yet."

    if result == "success":
        return "Prediction direction matched the next-day opening reaction."

    if direction in ["positive", "neutral_positive"] and result == "failure":
        return (
            "The event was initially scored as positive, but the next-day opening reaction was negative. "
            "Possible causes include prior price run-up, weak market conditions, low event surprise, or overestimated event strength."
        )

    if direction == "negative" and result == "failure":
        return (
            "The event was initially scored as negative, but the next-day opening reaction was positive. "
            "Possible causes include already-priced-in bad news, strong market conditions, short covering, or underestimated positive context."
        )

    if direction == "volatile" and result == "failure":
        return (
            "The event was expected to create volatility, but the next-day opening reaction was limited. "
            "Possible causes include low investor attention, weak liquidity, or limited material impact."
        )

    return f"No detailed error rule is available yet for event_type={event_type}."


def generate_improvement_rule(row: pd.Series) -> str:
    """
    Generate a simple future improvement rule.
    """

    result = row.get("prediction_result", "")
    direction = row.get("prediction_direction", "")

    if result == "pending":
        return "Re-evaluate after next trading day price data becomes available."

    if result == "success":
        return "Keep current scoring rule and collect more samples."

    if direction in ["positive", "neutral_positive"]:
        return (
            "Add prior price run-up, market index trend, sector trend, and event-size factors "
            "before increasing positive event confidence."
        )

    if direction == "negative":
        return (
            "Check whether the negative event was already priced in and whether market sentiment offset the event risk."
        )

    if direction == "volatile":
        return (
            "Add liquidity, trading volume, and investor attention indicators to volatility scoring."
        )

    return "Add more contextual features before updating the scoring rule."


def build_error_notes(scored_events: pd.DataFrame, reaction_results: pd.DataFrame) -> pd.DataFrame:
    """
    Merge scored events with reaction results and create error notes.
    """

    scored_events = scored_events.copy()
    reaction_results = reaction_results.copy()

    scored_events["stock_code"] = scored_events["stock_code"].apply(normalize_stock_code)
    reaction_results["stock_code"] = reaction_results["stock_code"].apply(normalize_stock_code)

    scored_events["event_date"] = scored_events["rcept_dt"].astype(str)
    reaction_results["event_date"] = reaction_results["event_date"].astype(str)

    merge_keys = ["stock_code", "event_type", "event_date"]

    merged = pd.merge(
        scored_events,
        reaction_results[
            [
                "stock_code",
                "event_type",
                "event_date",
                "next_trade_date",
                "next_open_return",
                "next_close_return",
                "note",
            ]
        ],
        on=merge_keys,
        how="left",
    )

    merged["prediction_result"] = merged.apply(
        lambda row: classify_prediction_result(
            row.get("prediction_direction", ""),
            row.get("next_open_return", None),
        ),
        axis=1,
    )

    merged["error_reason"] = merged.apply(generate_error_reason, axis=1)
    merged["improvement_rule"] = merged.apply(generate_improvement_rule, axis=1)

    selected_columns = [
        "corp_name",
        "stock_code",
        "report_nm",
        "event_type",
        "event_date",
        "prediction_direction",
        "event_score",
        "initial_confidence",
        "next_trade_date",
        "next_open_return",
        "next_close_return",
        "prediction_result",
        "error_reason",
        "improvement_rule",
    ]

    existing_columns = [col for col in selected_columns if col in merged.columns]

    return merged[existing_columns].copy()


def save_error_notes(df: pd.DataFrame) -> str:
    """
    Save error notes as CSV.
    """

    output_dir = "data/predictions"
    os.makedirs(output_dir, exist_ok=True)

    today = datetime.today().strftime("%Y%m%d")
    output_path = f"{output_dir}/error_notes_{today}.csv"

    df.to_csv(output_path, index=False, encoding="utf-8-sig")

    return output_path


def main():
    print("Generating prediction review and error notes...")

    scored_file = get_latest_scored_events_file()
    prediction_files = get_prediction_files()

    print(f"Scored events file: {scored_file}")
    print(f"Prediction files found: {len(prediction_files)}")

    scored_events = pd.read_csv(scored_file)
    reaction_results = load_all_reaction_results(prediction_files)

    if reaction_results.empty:
        print("No reaction results found. Error notes cannot be generated yet.")
        return

    error_notes = build_error_notes(scored_events, reaction_results)
    output_path = save_error_notes(error_notes)

    print(f"Generated {len(error_notes)} error-note rows.")
    print(f"Saved to: {output_path}")
    print()
    print(
        error_notes[
            [
                "corp_name",
                "stock_code",
                "event_type",
                "prediction_direction",
                "event_score",
                "next_open_return",
                "prediction_result",
            ]
        ].to_string(index=False)
    )


if __name__ == "__main__":
    main()
