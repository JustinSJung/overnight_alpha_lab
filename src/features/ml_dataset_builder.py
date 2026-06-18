"""
Machine learning dataset builder.

This script combines:
- scored key events
- event-news features
- event-price reaction results
- error notes

and creates a machine-learning-ready dataset.
"""

import os
from datetime import datetime

import pandas as pd


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


def get_latest_file(directory: str, prefix: str) -> str:
    """
    Find latest CSV file by prefix.
    """

    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory not found: {directory}")

    csv_files = [
        file for file in os.listdir(directory)
        if file.startswith(prefix) and file.endswith(".csv")
    ]

    if not csv_files:
        raise FileNotFoundError(f"No CSV files found with prefix={prefix}")

    csv_files.sort(reverse=True)
    return os.path.join(directory, csv_files[0])


def load_reaction_results(prediction_dir: str = "data/predictions") -> pd.DataFrame:
    """
    Load all event-price reaction result files.
    """

    if not os.path.exists(prediction_dir):
        return pd.DataFrame()

    files = [
        os.path.join(prediction_dir, file)
        for file in os.listdir(prediction_dir)
        if file.startswith("event_price_reaction_") and file.endswith(".csv")
    ]

    frames = []

    for file_path in files:
        try:
            df = pd.read_csv(file_path)
            if not df.empty:
                frames.append(df)
        except Exception as error:
            print(f"Failed to read {file_path}: {error}")

    if not frames:
        return pd.DataFrame()

    return pd.concat(frames, ignore_index=True)


def prepare_merge_keys(df: pd.DataFrame) -> pd.DataFrame:
    """
    Prepare normalized merge keys.
    """

    df = df.copy()

    if "stock_code" in df.columns:
        df["stock_code"] = df["stock_code"].apply(normalize_stock_code)

    if "rcept_dt" in df.columns and "event_date" not in df.columns:
        df["event_date"] = df["rcept_dt"].astype(str)

    if "event_date" in df.columns:
        df["event_date"] = df["event_date"].astype(str)

    return df


def build_ml_dataset() -> pd.DataFrame:
    """
    Build machine learning dataset.
    """

    scored_events_file = get_latest_file(
        directory="data/processed",
        prefix="scored_key_events_",
    )

    news_features_file = get_latest_file(
        directory="data/processed",
        prefix="event_news_features_",
    )

    error_notes_file = get_latest_file(
        directory="data/predictions",
        prefix="error_notes_",
    )

    print(f"Scored events file: {scored_events_file}")
    print(f"News features file: {news_features_file}")
    print(f"Error notes file: {error_notes_file}")

    scored_events = pd.read_csv(scored_events_file)
    news_features = pd.read_csv(news_features_file)
    error_notes = pd.read_csv(error_notes_file)
    reaction_results = load_reaction_results()

    scored_events = prepare_merge_keys(scored_events)
    news_features = prepare_merge_keys(news_features)
    error_notes = prepare_merge_keys(error_notes)
    reaction_results = prepare_merge_keys(reaction_results)

    merge_keys = ["stock_code", "event_type", "event_date"]

    base_columns = [
        "stock_code",
        "corp_name",
        "report_nm",
        "event_type",
        "event_date",
        "prediction_direction",
        "event_score",
        "initial_confidence",
        "score_reason",
    ]

    scored_columns = [col for col in base_columns if col in scored_events.columns]
    dataset = scored_events[scored_columns].copy()

    news_columns = [
        "stock_code",
        "event_type",
        "event_date",
        "news_count",
        "positive_keyword_count",
        "negative_keyword_count",
        "news_sentiment_score",
        "news_attention_score",
        "top_news_titles",
    ]

    available_news_columns = [col for col in news_columns if col in news_features.columns]

    dataset = pd.merge(
        dataset,
        news_features[available_news_columns],
        on=merge_keys,
        how="left",
    )

    if not reaction_results.empty:
        reaction_columns = [
            "stock_code",
            "event_type",
            "event_date",
            "next_trade_date",
            "next_open_return",
            "next_close_return",
            "note",
        ]

        available_reaction_columns = [
            col for col in reaction_columns if col in reaction_results.columns
        ]

        dataset = pd.merge(
            dataset,
            reaction_results[available_reaction_columns],
            on=merge_keys,
            how="left",
        )

    error_columns = [
        "stock_code",
        "event_type",
        "event_date",
        "prediction_result",
        "error_reason",
        "improvement_rule",
    ]

    available_error_columns = [col for col in error_columns if col in error_notes.columns]

    dataset = pd.merge(
        dataset,
        error_notes[available_error_columns],
        on=merge_keys,
        how="left",
    )

    fill_zero_columns = [
        "news_count",
        "positive_keyword_count",
        "negative_keyword_count",
        "news_sentiment_score",
        "news_attention_score",
    ]

    for column in fill_zero_columns:
        if column in dataset.columns:
            dataset[column] = dataset[column].fillna(0)

    return dataset


def save_ml_dataset(df: pd.DataFrame) -> str:
    """
    Save ML dataset.
    """

    output_dir = "data/processed"
    os.makedirs(output_dir, exist_ok=True)

    today = datetime.today().strftime("%Y%m%d")
    output_path = f"{output_dir}/ml_dataset_{today}.csv"

    df.to_csv(output_path, index=False, encoding="utf-8-sig")

    return output_path


def main():
    print("Building machine learning dataset...")

    dataset = build_ml_dataset()
    output_path = save_ml_dataset(dataset)

    print(f"Generated ML dataset rows: {len(dataset)}")
    print(f"Saved to: {output_path}")
    print()
    print(dataset.head(20).to_string(index=False))


if __name__ == "__main__":
    main()
