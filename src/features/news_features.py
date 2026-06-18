"""
News feature generator.

This script connects selected DART disclosure events with
Naver news metadata and creates simple news-based features.

Generated features:
- news_count
- positive_keyword_count
- negative_keyword_count
- news_sentiment_score
- news_attention_score
"""

import os
from datetime import datetime

import pandas as pd


POSITIVE_KEYWORDS = [
    "수주",
    "계약",
    "공급",
    "호실적",
    "성장",
    "상승",
    "확대",
    "흑자",
    "개선",
    "증가",
    "기대",
    "강세",
    "신고가",
    "투자",
    "승인",
    "인수",
    "합병",
    "협력",
    "개발",
    "성과",
]

NEGATIVE_KEYWORDS = [
    "유상증자",
    "전환사채",
    "CB",
    "BW",
    "소송",
    "적자",
    "하락",
    "감소",
    "부진",
    "리스크",
    "불확실",
    "우려",
    "급락",
    "약세",
    "손실",
    "정정",
    "불성실",
    "상장폐지",
    "거래정지",
    "압수수색",
]


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


def get_latest_news_file(raw_dir: str = "data/raw") -> str:
    """
    Find the latest Naver news CSV file.
    """

    csv_files = [
        file for file in os.listdir(raw_dir)
        if file.startswith("naver_news_") and file.endswith(".csv")
    ]

    if not csv_files:
        raise FileNotFoundError("No Naver news CSV files found.")

    csv_files.sort(reverse=True)
    return os.path.join(raw_dir, csv_files[0])


def count_keywords(text: str, keywords: list[str]) -> int:
    """
    Count how many keywords appear in text.
    """

    if not isinstance(text, str):
        return 0

    return sum(1 for keyword in keywords if keyword in text)


def build_text(row: pd.Series) -> str:
    """
    Combine news title and description.
    """

    title = row.get("title", "")
    description = row.get("description", "")

    return f"{title} {description}"


def create_news_features_for_company(company_name: str, news_df: pd.DataFrame) -> dict:
    """
    Create news features for a single company.
    """

    company_news = news_df[news_df["corp_name"] == company_name].copy()

    if company_news.empty:
        return {
            "news_count": 0,
            "positive_keyword_count": 0,
            "negative_keyword_count": 0,
            "news_sentiment_score": 0,
            "news_attention_score": 0,
            "top_news_titles": "",
        }

    positive_count = 0
    negative_count = 0

    top_titles = []

    for _, row in company_news.iterrows():
        combined_text = build_text(row)

        positive_count += count_keywords(combined_text, POSITIVE_KEYWORDS)
        negative_count += count_keywords(combined_text, NEGATIVE_KEYWORDS)

        title = row.get("title", "")
        if isinstance(title, str) and title:
            top_titles.append(title)

    news_count = len(company_news)
    sentiment_score = positive_count - negative_count

    # At this stage, attention score is simply the number of news items.
    # Later, this can be improved using recency, source quality, and duplicate filtering.
    attention_score = news_count

    return {
        "news_count": news_count,
        "positive_keyword_count": positive_count,
        "negative_keyword_count": negative_count,
        "news_sentiment_score": sentiment_score,
        "news_attention_score": attention_score,
        "top_news_titles": " | ".join(top_titles[:3]),
    }


def generate_event_news_features(selected_events: pd.DataFrame, news_df: pd.DataFrame) -> pd.DataFrame:
    """
    Add news features to selected event rows.
    """

    rows = []

    for _, event in selected_events.iterrows():
        company_name = event.get("corp_name", "")
        features = create_news_features_for_company(company_name, news_df)

        row = event.to_dict()
        row.update(features)

        rows.append(row)

    return pd.DataFrame(rows)


def save_event_news_features(df: pd.DataFrame) -> str:
    """
    Save event-news feature dataframe.
    """

    output_dir = "data/processed"
    os.makedirs(output_dir, exist_ok=True)

    today = datetime.today().strftime("%Y%m%d")
    output_path = f"{output_dir}/event_news_features_{today}.csv"

    df.to_csv(output_path, index=False, encoding="utf-8-sig")

    return output_path


def main():
    print("Generating event-news features...")

    selected_events_file = get_latest_selected_events_file()
    news_file = get_latest_news_file()

    print(f"Selected events file: {selected_events_file}")
    print(f"News file: {news_file}")

    selected_events = pd.read_csv(selected_events_file)
    news_df = pd.read_csv(news_file)

    event_news_features = generate_event_news_features(selected_events, news_df)
    output_path = save_event_news_features(event_news_features)

    print(f"Generated {len(event_news_features)} event-news feature rows.")
    print(f"Saved to: {output_path}")
    print()
    print(
        event_news_features[
            [
                "corp_name",
                "stock_code",
                "event_type",
                "news_count",
                "positive_keyword_count",
                "negative_keyword_count",
                "news_sentiment_score",
                "news_attention_score",
            ]
        ].to_string(index=False)
    )


if __name__ == "__main__":
    main()
