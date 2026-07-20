"""
Base interface for supplementary news providers.
"""

from abc import ABC, abstractmethod
from typing import Any


NORMALIZED_COLUMNS = [
    "source_provider",
    "query",
    "title",
    "link",
    "published_at",
    "summary",
    "raw_source",
]


class NewsProvider(ABC):
    provider_name: str

    @abstractmethod
    def fetch(self, query: str, max_items: int = 5) -> list[dict[str, Any]]:
        """
        Fetch normalized news items for a query.
        """

    def normalize_item(self, query: str, item: dict[str, Any]) -> dict[str, Any]:
        return {
            "source_provider": self.provider_name,
            "query": query,
            "title": item.get("title", ""),
            "link": item.get("link", ""),
            "published_at": item.get("published_at", ""),
            "summary": item.get("summary", ""),
            "raw_source": item.get("raw_source", ""),
        }
