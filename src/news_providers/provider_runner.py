"""
Run supplementary news providers and build compact news features.
"""

import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import json

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.news_providers.base import NORMALIZED_COLUMNS, NewsProvider
from src.news_providers.deepsearch_news_provider import DeepSearchNewsProvider
from src.news_providers.gdelt_news_provider import GdeltNewsProvider
from src.news_providers.google_news_rss_provider import GoogleNewsRssProvider


RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")
MAX_QUERIES = 20
MAX_ITEMS_PER_QUERY = 5
MAX_CONSECUTIVE_PROVIDER_FAILURES = 3

POSITIVE_KEYWORDS = [
    "수주", "공급계약", "공급", "흑자", "실적개선", "승인", "투자", "증설", "협력",
    "계약", "호실적", "성장", "상승", "확대", "개선", "증가", "강세", "개발", "성과",
]
NEGATIVE_KEYWORDS = [
    "유상증자", "전환사채", "CB", "BW", "소송", "적자", "하락", "감소", "부진", "리스크",
    "불확실", "우려", "급락", "약세", "손실", "정정", "불성실", "상장폐지", "거래정지", "압수수색",
]
RISK_KEYWORDS = [
    "거래정지", "상장폐지", "불성실공시", "불성실", "소송", "압수수색", "적자", "급락", "CB", "BW", "유상증자",
]
ATTENTION_KEYWORDS = [
    "급등", "폭등", "상한가", "테마", "수급", "매수세", "관심", "주목", "기대감", "랠리", "단독",
]
RUMOR_NOISE_KEYWORDS = [
    "풍문", "루머", "사실무근", "조회공시", "인수설", "매각설", "단독", "관련주", "테마", "급등",
    "상한가", "수혜", "기대감",
]


def latest_file(directory: Path, pattern: str):
    files = sorted(directory.glob(pattern))
    return files[-1] if files else None


def read_csv(path):
    if path is None or not path.exists():
        return pd.DataFrame()

    try:
        return pd.read_csv(path)
    except Exception as error:
        print(f"Failed to read {path}: {error}")
        return pd.DataFrame()


def keyword_count(text: str, keywords: list[str]) -> int:
    text = str(text)
    return sum(1 for keyword in keywords if keyword.lower() in text.lower())


def now_string() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def build_queries(candidates: pd.DataFrame) -> list[str]:
    if candidates.empty:
        return ["코스피", "코스닥", "한국 주식"]

    df = candidates.copy()

    if "selected_pick" in df.columns:
        selected_mask = df["selected_pick"].astype(str).str.lower().isin(["true", "1", "yes"])
        selected = df[selected_mask].copy()
    else:
        selected = pd.DataFrame()

    if selected.empty:
        score_column = next(
            (column for column in ["candidate_rank", "final_price_signal_score", "prediction_score", "price_candidate_score"] if column in df.columns),
            None,
        )
        if score_column == "candidate_rank":
            df[score_column] = pd.to_numeric(df[score_column], errors="coerce")
            selected = df.sort_values(score_column, ascending=True).head(MAX_QUERIES)
        elif score_column:
            df[score_column] = pd.to_numeric(df[score_column], errors="coerce")
            selected = df.sort_values(score_column, ascending=False).head(MAX_QUERIES)
        else:
            selected = df.head(MAX_QUERIES)

    queries = []
    for _, row in selected.head(MAX_QUERIES).iterrows():
        name = str(row.get("stock_name", row.get("corp_name", ""))).strip()
        code = str(row.get("stock_code", "")).strip()
        if name and name.lower() != "nan":
            queries.append(name)
        elif code and code.lower() != "nan":
            queries.append(code)

    deduped = []
    seen = set()
    for query in queries:
        if query not in seen:
            deduped.append(query)
            seen.add(query)

    return deduped[:MAX_QUERIES] or ["코스피", "코스닥", "한국 주식"]


def build_features(items: pd.DataFrame) -> pd.DataFrame:
    feature_columns = [
        "source_provider",
        "query",
        "provider_mix",
        "news_count",
        "unique_source_count",
        "positive_keyword_count",
        "negative_keyword_count",
        "risk_keyword_count",
        "rumor_noise_keyword_count",
        "attention_keyword_count",
        "news_attention_score",
        "rumor_noise_score",
        "news_risk_score",
        "top_titles",
    ]
    if items.empty:
        return pd.DataFrame(columns=feature_columns)

    rows = []
    for query, group in items.groupby("query", dropna=False):
        text = " ".join((group["title"].fillna("") + " " + group["summary"].fillna("")).astype(str))
        positive_count = keyword_count(text, POSITIVE_KEYWORDS)
        negative_count = keyword_count(text, NEGATIVE_KEYWORDS)
        risk_count = keyword_count(text, RISK_KEYWORDS)
        rumor_noise_count = keyword_count(text, RUMOR_NOISE_KEYWORDS)
        attention_count = keyword_count(text, ATTENTION_KEYWORDS)
        domains = group["link"].astype(str).str.extract(r"https?://([^/]+)")[0].fillna("")
        providers = sorted(
            provider
            for provider in group["source_provider"].dropna().astype(str).unique()
            if provider and provider != "nan"
        )
        rows.append(
            {
                "source_provider": "mixed" if len(providers) > 1 else (providers[0] if providers else "unknown"),
                "query": query,
                "provider_mix": ", ".join(providers),
                "news_count": len(group),
                "unique_source_count": int(domains.nunique()),
                "positive_keyword_count": positive_count,
                "negative_keyword_count": negative_count,
                "risk_keyword_count": risk_count,
                "rumor_noise_keyword_count": rumor_noise_count,
                "attention_keyword_count": attention_count,
                "news_attention_score": len(group) + rumor_noise_count * 2 + positive_count,
                "rumor_noise_score": rumor_noise_count * 2 + max(int(domains.nunique()) - 1, 0),
                "news_risk_score": risk_count * 2 + negative_count,
                "top_titles": " | ".join(group["title"].dropna().astype(str).head(3)),
            }
        )

    return pd.DataFrame(rows, columns=feature_columns)


def fetch_naver_news(query: str, max_items: int = 3) -> list[dict[str, Any]]:
    client_id = os.getenv("NAVER_CLIENT_ID", "").strip()
    client_secret = os.getenv("NAVER_CLIENT_SECRET", "").strip()
    if not client_id or not client_secret:
        return []

    params = urlencode({"query": query, "display": max_items, "sort": "date"})
    request = Request(
        f"https://openapi.naver.com/v1/search/news.json?{params}",
        headers={
            "X-Naver-Client-Id": client_id,
            "X-Naver-Client-Secret": client_secret,
            "User-Agent": "overnight-alpha-lab/1.0 (+research-dashboard)",
        },
    )
    with urlopen(request, timeout=10) as response:
        payload = response.read().decode("utf-8")
    data = json.loads(payload)
    items = data.get("items", [])
    rows = []
    provider = InlineProvider("naver_search")
    for item in items[:max_items]:
        rows.append(
            provider.normalize_item(
                query=query,
                item={
                    "title": item.get("title", ""),
                    "link": item.get("originallink", item.get("link", "")),
                    "published_at": item.get("pubDate", ""),
                    "summary": item.get("description", ""),
                    "raw_source": "Naver Search API",
                },
            )
        )
    return rows


class InlineProvider(NewsProvider):
    def __init__(self, provider_name: str):
        self.provider_name = provider_name

    def fetch(self, query: str, max_items: int = 5) -> list[dict[str, Any]]:
        return []


def provider_status_row(
    provider_name: str,
    query: str,
    status: str,
    item_count: int = 0,
    error_message: str = "",
) -> dict[str, Any]:
    return {
        "source_provider": provider_name,
        "query": query,
        "status": status,
        "provider_status": status,
        "item_count": item_count,
        "error_message": error_message[:220],
        "updated_at": now_string(),
    }


def run_provider(provider: NewsProvider, query: str, max_items: int) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    is_available = getattr(provider, "is_available", lambda: True)
    if not is_available():
        return [], provider_status_row(provider.provider_name, query, "skipped_missing_credentials")
    try:
        rows = provider.fetch(query, max_items=max_items)
        return rows, provider_status_row(provider.provider_name, query, "success", len(rows))
    except Exception as error:
        print(f"{provider.provider_name} failed for query '{query}': {str(error)[:160]}")
        return [], provider_status_row(provider.provider_name, query, "failed", 0, str(error))


def run_naver_provider(query: str) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    if not (os.getenv("NAVER_CLIENT_ID", "").strip() and os.getenv("NAVER_CLIENT_SECRET", "").strip()):
        if os.getenv("NAVER_API_HUB_CLIENT_ID", "").strip() or os.getenv("NAVER_API_HUB_CLIENT_SECRET", "").strip():
            return [], provider_status_row("naver_search", query, "skipped_api_hub_not_configured")
        return [], provider_status_row("naver_search", query, "skipped_missing_credentials")
    try:
        rows = fetch_naver_news(query, max_items=3)
        return rows, provider_status_row("naver_search", query, "success", len(rows))
    except Exception as error:
        print(f"naver_search failed for query '{query}': {str(error)[:160]}")
        return [], provider_status_row("naver_search", query, "failed", 0, str(error))


def main():
    print("Running supplementary news providers...")
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    today = datetime.today().strftime("%Y%m%d")
    candidates = read_csv(latest_file(PROCESSED_DIR, "price_based_candidates_*.csv"))
    queries = build_queries(candidates)
    providers = [
        DeepSearchNewsProvider(),
        GoogleNewsRssProvider(),
        GdeltNewsProvider(),
    ]
    status_rows = []
    all_items = []
    provider_failure_streaks = {provider.provider_name: 0 for provider in providers}
    disabled_providers = set()

    for query in queries:
        for provider in providers:
            if provider.provider_name in disabled_providers:
                status_rows.append(
                    provider_status_row(
                        provider.provider_name,
                        query,
                        "skipped_after_repeated_failures",
                        0,
                        "Provider disabled for this run after repeated failures.",
                    )
                )
                continue
            rows, status = run_provider(provider, query, MAX_ITEMS_PER_QUERY)
            all_items.extend(rows)
            status_rows.append(status)
            if status["status"] == "failed":
                provider_failure_streaks[provider.provider_name] += 1
                if provider_failure_streaks[provider.provider_name] >= MAX_CONSECUTIVE_PROVIDER_FAILURES:
                    disabled_providers.add(provider.provider_name)
                    print(f"{provider.provider_name} disabled after repeated failures in this run.")
            elif status["status"] == "success" and status["item_count"] > 0:
                provider_failure_streaks[provider.provider_name] = 0
        rows, status = run_naver_provider(query)
        all_items.extend(rows)
        status_rows.append(status)

    raw_df = pd.DataFrame(all_items, columns=NORMALIZED_COLUMNS)
    features_df = build_features(raw_df)
    status_df = pd.DataFrame(status_rows)

    raw_path = RAW_DIR / f"news_provider_items_{today}.csv"
    features_path = PROCESSED_DIR / f"news_provider_features_{today}.csv"
    status_path = PROCESSED_DIR / f"news_provider_status_{today}.csv"

    raw_df.to_csv(raw_path, index=False, encoding="utf-8-sig")
    features_df.to_csv(features_path, index=False, encoding="utf-8-sig")
    status_df.to_csv(status_path, index=False, encoding="utf-8-sig")

    print(f"News provider raw items saved to: {raw_path}")
    print(f"News provider features saved to: {features_path}")
    print(f"News provider status saved to: {status_path}")
    provider_counts = status_df.groupby("source_provider")["item_count"].sum().to_dict() if not status_df.empty else {}
    print(f"News provider item count: {len(raw_df)}")
    print(f"News provider feature count: {len(features_df)}")
    print(f"Provider item counts: {provider_counts}")
    if "rumor_noise_keyword_count" in features_df.columns:
        print(f"Rumor/noise keyword count: {int(features_df['rumor_noise_keyword_count'].sum())}")


if __name__ == "__main__":
    main()
