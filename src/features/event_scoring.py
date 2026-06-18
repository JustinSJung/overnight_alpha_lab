"""
Event scoring module.

This script assigns initial direction, event score,
and confidence level to selected DART disclosure events.

At this stage, the scoring model is rule-based.
Later, these scores will be improved through backtesting,
error notes, and machine learning.
"""

import os
from datetime import datetime

import pandas as pd


EVENT_SCORE_RULES = {
    "supply_contract": {
        "direction": "positive",
        "score": 70,
        "confidence": "C",
        "reason": "Supply contract disclosures may indicate future revenue growth.",
    },
    "bonus_issue": {
        "direction": "positive",
        "score": 60,
        "confidence": "C",
        "reason": "Bonus issues may increase investor attention, but actual value impact can vary.",
    },
    "earnings_guidance": {
        "direction": "neutral_positive",
        "score": 50,
        "confidence": "C",
        "reason": "Earnings guidance can affect price depending on whether results exceed expectations.",
    },
    "paid_in_capital_increase": {
        "direction": "negative",
        "score": -70,
        "confidence": "C",
        "reason": "Paid-in capital increases can create dilution concerns.",
    },
    "convertible_bond": {
        "direction": "negative",
        "score": -60,
        "confidence": "C",
        "reason": "Convertible bonds may create future dilution risk.",
    },
    "bond_with_warrant": {
        "direction": "negative",
        "score": -60,
        "confidence": "C",
        "reason": "Bonds with warrants may create future dilution risk.",
    },
    "lawsuit": {
        "direction": "negative",
        "score": -75,
        "confidence": "C",
        "reason": "Lawsuits may increase uncertainty and downside risk.",
    },
    "disclosure_violation": {
        "direction": "negative",
        "score": -80,
        "confidence": "C",
        "reason": "Disclosure violations may damage investor trust.",
    },
    "major_shareholder_change": {
        "direction": "volatile",
        "score": 10,
        "confidence": "C",
        "reason": "Major shareholder changes can increase volatility depending on context.",
    },
    "investment_decision": {
        "direction": "volatile",
        "score": 30,
        "confidence": "C",
        "reason": "Investment decisions can be positive or negative depending on scale and funding source.",
    },
    "merger": {
        "direction": "volatile",
        "score": 30,
        "confidence": "C",
        "reason": "Mergers can create major price movement, but direction depends on deal terms.",
    },
    "spin_off": {
        "direction": "volatile",
        "score": 30,
        "confidence": "C",
        "reason": "Spin-offs can create volatility depending on market interpretation.",
    },
}


def get_latest_selected_events_file(processed_dir: str = "data/processed") -> str:
    """
    Find the latest selected key events CSV file.
    """

    csv_files = [
        file for file in os.listdir(processed_dir)
        if file.startswith("selected_key_events_") and file.endswith(".csv")
    ]

    if not csv_files:
        raise FileNotFoundError("No selected key events CSV files found.")

    csv_files.sort(reverse=True)
    return os.path.join(processed_dir, csv_files[0])


def score_event_type(event_type: str) -> dict:
    """
    Score a single event type.
    """

    default_rule = {
        "direction": "unknown",
        "score": 0,
        "confidence": "D",
        "reason": "No scoring rule is available for this event type yet.",
    }

    return EVENT_SCORE_RULES.get(event_type, default_rule)


def add_event_scores(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add event scoring columns to selected event dataframe.
    """

    scored_rows = []

    for _, row in df.iterrows():
        event_type = row.get("event_type", "")
        rule = score_event_type(event_type)

        scored_row = row.to_dict()
        scored_row["prediction_direction"] = rule["direction"]
        scored_row["event_score"] = rule["score"]
        scored_row["initial_confidence"] = rule["confidence"]
        scored_row["score_reason"] = rule["reason"]

        scored_rows.append(scored_row)

    return pd.DataFrame(scored_rows)


def save_scored_events(df: pd.DataFrame) -> str:
    """
    Save scored event dataframe.
    """

    output_dir = "data/processed"
    os.makedirs(output_dir, exist_ok=True)

    today = datetime.today().strftime("%Y%m%d")
    output_path = f"{output_dir}/scored_key_events_{today}.csv"

    df.to_csv(output_path, index=False, encoding="utf-8-sig")

    return output_path


def main():
    print("Scoring selected key events...")

    input_path = get_latest_selected_events_file()
    print(f"Input file: {input_path}")

    selected_events = pd.read_csv(input_path)
    scored_events = add_event_scores(selected_events)

    output_path = save_scored_events(scored_events)

    print(f"Scored {len(scored_events)} events.")
    print(f"Saved to: {output_path}")
    print()
    print(
        scored_events[
            [
                "corp_name",
                "stock_code",
                "report_nm",
                "event_type",
                "prediction_direction",
                "event_score",
                "initial_confidence",
            ]
        ].to_string(index=False)
    )


if __name__ == "__main__":
    main()
