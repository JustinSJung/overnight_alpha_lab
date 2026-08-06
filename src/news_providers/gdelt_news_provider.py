"""
GDELT news provider.

Uses the public GDELT DOC 2.0 API as a broad fallback signal. Results are
compact and supplementary, never a blocking dependency for price learning.
"""

import json
from typing import Any
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from src.news_providers.base import NewsProvider


class GdeltNewsProvider(NewsProvider):
    provider_name = "gdelt"

    def __init__(self, timeout: int = 6):
        self.timeout = timeout

    def is_available(self) -> bool:
        return True

    def build_url(self, query: str, max_items: int) -> str:
        params = urlencode(
            {
                "query": query,
                "mode": "ArtList",
                "format": "json",
                "maxrecords": max_items,
                "sort": "HybridRel",
            }
        )
        return f"https://api.gdeltproject.org/api/v2/doc/doc?{params}"

    def fetch(self, query: str, max_items: int = 5) -> list[dict[str, Any]]:
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
        articles = data.get("articles", [])
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
                        "title": item.get("title", ""),
                        "link": item.get("url", ""),
                        "published_at": item.get("seendate", ""),
                        "summary": item.get("summary", ""),
                        "raw_source": item.get("domain", item.get("sourceCountry", "")),
                    },
                )
            )
        return rows
