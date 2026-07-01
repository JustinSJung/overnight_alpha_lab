"""
Sherwood Snacks newsletter collector.

This script collects the latest public Snacks newsletter articles
from the Sherwood Snacks archive and saves the latest 3 article summaries.

This is used as a global market context layer, not as direct investment advice.
"""

from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin

import pandas as pd
import requests
from bs4 import BeautifulSoup


ARCHIVE_URL = "https://sherwood.news/snacks/newsletters/"
RAW_DIR = Path("data/raw")


def fetch_html(url: str) -> str:
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (compatible; OvernightAlphaLab/1.0; "
            "+https://github.com/JustinSJung/overnight_alpha_lab)"
        )
    }

    response = requests.get(url, headers=headers, timeout=20)
    response.raise_for_status()
    return response.text


def extract_latest_links(html: str, limit: int = 3) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")

    candidates = []

    for link in soup.find_all("a", href=True):
        href = link.get("href", "")
        text = " ".join(link.get_text(" ", strip=True).split())

        if not href:
            continue

        full_url = urljoin(ARCHIVE_URL, href)

        if "sherwood.news" not in full_url:
            continue

        if "/snacks/" not in full_url:
            continue

        if "/newsletters/" in full_url and full_url.rstrip("/") == ARCHIVE_URL.rstrip("/"):
            continue

        if len(text) < 8:
            continue

        candidates.append(
            {
                "title": text,
                "url": full_url.split("?")[0],
            }
        )

    unique = []
    seen_urls = set()

    for item in candidates:
        if item["url"] in seen_urls:
            continue

        seen_urls.add(item["url"])
        unique.append(item)

        if len(unique) >= limit:
            break

    return unique


def extract_article_text(url: str) -> dict:
    html = fetch_html(url)
    soup = BeautifulSoup(html, "html.parser")

    title = ""

    if soup.find("h1"):
        title = soup.find("h1").get_text(" ", strip=True)

    if not title and soup.title:
        title = soup.title.get_text(" ", strip=True)

    paragraphs = []

    for paragraph in soup.find_all("p"):
        text = " ".join(paragraph.get_text(" ", strip=True).split())

        if len(text) >= 40:
            paragraphs.append(text)

    body_text = " ".join(paragraphs)
    body_text = body_text[:6000]

    return {
        "title": title,
        "url": url,
        "body_text": body_text,
        "body_length": len(body_text),
    }


def collect_latest_snacks(limit: int = 3) -> pd.DataFrame:
    archive_html = fetch_html(ARCHIVE_URL)
    links = extract_latest_links(archive_html, limit=limit)

    rows = []

    for rank, item in enumerate(links, start=1):
        try:
            article = extract_article_text(item["url"])
        except Exception as error:
            print(f"Failed to collect Snacks article: {item['url']}")
            print(f"Reason: {error}")
            continue

        rows.append(
            {
                "collected_at": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
                "source": "Sherwood Snacks",
                "rank": rank,
                "title": article.get("title") or item["title"],
                "url": item["url"],
                "body_text": article.get("body_text", ""),
                "body_length": article.get("body_length", 0),
            }
        )

    return pd.DataFrame(rows)


def main():
    print("Collecting latest Sherwood Snacks newsletters...")

    RAW_DIR.mkdir(parents=True, exist_ok=True)

    today = datetime.today().strftime("%Y%m%d")
    output_path = RAW_DIR / f"snacks_newsletters_{today}.csv"

    try:
        df = collect_latest_snacks(limit=3)
    except Exception as error:
        print("Snacks collector failed.")
        print(f"Reason: {error}")
        print("Collector will stop gracefully without error.")
        return

    if df.empty:
        print("No Snacks newsletter rows collected.")
        return

    df.to_csv(output_path, index=False)
    print(f"Saved Snacks newsletters to: {output_path}")
    print(f"Rows: {len(df)}")


if __name__ == "__main__":
    main()
