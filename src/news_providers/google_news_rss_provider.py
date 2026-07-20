"""
Google News RSS provider.

Uses the public Google News RSS endpoint with conservative query volume. This
is a supplementary signal and must not block the KIS price pipeline.
"""

from email.utils import parsedate_to_datetime
from typing import Any
from urllib.parse import quote_plus
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET

from src.news_providers.base import NewsProvider


class GoogleNewsRssProvider(NewsProvider):
    provider_name = "google_news_rss"

    def __init__(self, hl: str = "ko", gl: str = "KR", ceid: str = "KR:ko", timeout: int = 10):
        self.hl = hl
        self.gl = gl
        self.ceid = ceid
        self.timeout = timeout

    def build_url(self, query: str) -> str:
        encoded_query = quote_plus(query)
        return (
            "https://news.google.com/rss/search"
            f"?q={encoded_query}&hl={self.hl}&gl={self.gl}&ceid={self.ceid}"
        )

    def fetch(self, query: str, max_items: int = 5) -> list[dict[str, Any]]:
        url = self.build_url(query)
        request = Request(
            url,
            headers={
                "User-Agent": "overnight-alpha-lab/1.0 (+research-dashboard)",
            },
        )

        with urlopen(request, timeout=self.timeout) as response:
            payload = response.read()

        root = ET.fromstring(payload)
        rows = []

        for item in root.findall("./channel/item")[:max_items]:
            title = text_or_empty(item.find("title"))
            link = text_or_empty(item.find("link"))
            published_raw = text_or_empty(item.find("pubDate"))
            summary = text_or_empty(item.find("description"))
            published_at = published_raw

            try:
                published_at = parsedate_to_datetime(published_raw).isoformat()
            except Exception:
                pass

            rows.append(
                self.normalize_item(
                    query=query,
                    item={
                        "title": title,
                        "link": link,
                        "published_at": published_at,
                        "summary": summary,
                        "raw_source": "Google News RSS",
                    },
                )
            )

        return rows


def text_or_empty(node) -> str:
    if node is None or node.text is None:
        return ""
    return str(node.text).strip()
