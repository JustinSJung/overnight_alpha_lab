"""
Naver News metadata collector.

This script collects news search metadata from Naver Search API
for selected companies and saves the result under data/raw.

It stores metadata only:
- title
- description
- original link
- Naver link
- publication date
- collection time

It does not store full article bodies.
"""

import html
import os
from datetime import datetime

import pandas as pd
import requests
from dotenv import load_dotenv


NAVER_NEWS_SEARCH_URL = "https://openapi.naver.com/v1/search/news.json"


def get_naver_api_keys() -> tuple[str, str]:
    """
    Load Naver API credentials from .env file.
    """

    load_dotenv()

    client_id = os.getenv("NAVER_CLIENT_ID")
    client_secret = os.getenv("NAVER_CLIENT_SECRET")

    if not client_id:
        raise ValueError("NAVER_CLIENT_ID is missing. Please check your .env file.")

    if not client_secret:
        raise ValueError("NAVER_CLIENT_SECRET is missing. Please check your .env file.")

    return client_id, client_secret


def clean_html_text(text: str) -> str:
    """
    Remove simple HTML tags and decode HTML entities.
    """

    if not isinstance(text, str):
        return ""

    cleaned = text.replace("<b>", "").replace("</b>", "")
    cleaned = html.unescape(cleaned)

    return cleaned.strip()


def search_naver_news(query: str, display: int = 10, sort: str = "date") -> pd.DataFrame:
    """
    Search Naver News API for a query.
    """

    client_id, client_secret = get_naver_api_keys()

    headers = {
        "X-Naver-Client-Id": client_id,
        "X-Naver-Client-Secret": client_secret,
    }

    params = {
        "query": query,
        "display": display,
        "start": 1,
        "sort": sort,
    }

    response = requests.get(
        NAVER_NEWS_SEARCH_URL,
        headers=headers,
        params=params,
        timeout=10,
    )

    response.raise_for_status()

    data = response.json()
    items = data.get("items", [])

    rows = []
    collected_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for item in items:
        rows.append(
            {
                "query": query,
                "title": clean_html_text(item.get("title", "")),
                "description": clean_html_text(item.get("description", "")),
                "originallink": item.get("originallink", ""),
                "link": item.get("link", ""),
                "pubDate": item.get("pubDate", ""),
                "collected_at": collected_at,
            }
        )

    return pd.DataFrame(rows)


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


def collect_news_for_selected_events(display_per_company: int = 5) -> pd.DataFrame:
    """
    Collect Naver news for companies selected by the daily pipeline.
    """

    selected_file = get_latest_selected_events_file()
    print(f"Selected events file: {selected_file}")

    selected_events = pd.read_csv(selected_file)

    if "corp_name" not in selected_events.columns:
        raise ValueError("corp_name column not found in selected events file.")

    company_names = (
        selected_events["corp_name"]
        .dropna()
        .astype(str)
        .drop_duplicates()
        .tolist()
    )

    all_news = []

    print(f"Collecting news for {len(company_names)} companies...")

    for company_name in company_names:
        print(f"- Searching news for: {company_name}")

        try:
            news_df = search_naver_news(
                query=company_name,
                display=display_per_company,
                sort="date",
            )

            if not news_df.empty:
                news_df["corp_name"] = company_name
                all_news.append(news_df)

        except Exception as error:
            print(f"Failed to collect news for {company_name}: {error}")

    if not all_news:
        return pd.DataFrame()

    return pd.concat(all_news, ignore_index=True)


def save_news_data(df: pd.DataFrame) -> str:
    """
    Save collected news metadata to CSV.
    """

    output_dir = "data/raw"
    os.makedirs(output_dir, exist_ok=True)

    today = datetime.today().strftime("%Y%m%d")
    output_path = f"{output_dir}/naver_news_{today}.csv"

    df.to_csv(output_path, index=False, encoding="utf-8-sig")

    return output_path


def main():
    print("Collecting Naver news metadata...")

    news_df = collect_news_for_selected_events(display_per_company=5)

    if news_df.empty:
        print("No news data collected.")
        return

    output_path = save_news_data(news_df)

    print(f"Collected {len(news_df)} news items.")
    print(f"Saved to: {output_path}")
    print()
    print(news_df[["corp_name", "title", "pubDate"]].head(20).to_string(index=False))


if __name__ == "__main__":
    main()
