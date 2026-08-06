"""
DeepSearch news provider.

Uses the official DeepSearch API when DEEPSEARCH_API_KEY is available. The
provider is supplementary and must not block the KIS price learning loop.
"""

import json
import os
from typing import Any
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from src.news_providers.base import NewsProvider


class DeepSearchNewsProvider(NewsProvider):
    provider_name = "deepsearch_news"

    def __init__(self, api_key: str | None = None, timeout: int = 6):
        self.api_key = api_key or os.getenv("DEEPSEARCH_API_KEY", "").strip()
        self.timeout = timeout

    def is_available(self) -> bool:
        return bool(self.api_key)

    def build_url(self, query: str, max_items: int) -> str:
        params = urlencode(
            {
                "keyword": query,
                "page_size": max_items,
                "api_key": self.api_key,
            }
        )
        return f"https://api-v2.deepsearch.com/v1/articles?{params}"

    def fetch(self, query: str, max_items: int = 5) -> list[dict[str, Any]]:
        if not self.is_available():
            return []

        request = Request(
            self.build_url(query, max_items),
            headers={
                "Accept": "application/json",
                "User-Agent": "overnight-alpha-lab/1.0 (+research-dashboard)",
            },
        )

        with urlopen(request, timeout=self.timeout) as response:
            payload = response.read().decode("utf-8")

        data = json.loads(payload)
        articles = data.get("data", data.get("articles", data if isinstance(data, list) else []))
        if isinstance(articles, dict):
            articles = articles.get("items", articles.get("results", []))
        if not isinstance(articles, list):
            articles = []

        rows = []
        for item in articles[:max_items]:
            if not isinstance(item, dict):
                continue
            rows.append(
                self.normalize_item(
                    query=query,
                    item={
                        "title": first_present(item, ["title", "title_ko", "headline", "name"]),
                        "link": first_present(item, ["content_url", "url", "link", "news_url"]),
                        "published_at": first_present(item, ["published_at", "published_date", "created_at", "date"]),
                        "summary": first_present(item, ["summary", "description", "briefing", "content"]),
                        "raw_source": first_present(
                            item,
                            ["publisher", "publisher_name", "provider", "source", "press"],
                        ),
                    },
                )
            )
        return rows


def first_present(item: dict[str, Any], keys: list[str]) -> str:
    for key in keys:
        value = item.get(key)
        if isinstance(value, dict):
            value = value.get("name") or value.get("title") or value.get("value")
        if value not in [None, "", [], {}]:
            return str(value).strip()
    return ""
