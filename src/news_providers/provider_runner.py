"""
Run supplementary news providers and build compact news features.
"""

import sys
from datetime import datetime
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.news_providers.base import NORMALIZED_COLUMNS
from src.news_providers.google_news_rss_provider import GoogleNewsRssProvider


RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")
MAX_QUERIES = 20
MAX_ITEMS_PER_QUERY = 5

POSITIVE_KEYWORDS = [
    "수주", "계약", "공급", "호실적", "성장", "상승", "확대", "흑자", "개선", "증가",
    "기대", "강세", "신고가", "투자", "승인", "인수", "합병", "협력", "개발", "성과",
]
NEGATIVE_KEYWORDS = [
    "유상증자", "전환사채", "CB", "BW", "소송", "적자", "하락", "감소", "부진", "리스크",
    "불확실", "우려", "급락", "약세", "손실", "정정", "불성실", "상장폐지", "거래정지", "압수수색",
]
RISK_KEYWORDS = [
    "소송", "리스크", "불확실", "우려", "손실", "정정", "불성실", "상장폐지", "거래정지", "압수수색",
]
ATTENTION_KEYWORDS = [
    "급등", "폭등", "상한가", "테마", "수급", "매수세", "관심", "주목", "기대감", "랠리", "단독",
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
    if items.empty:
        return pd.DataFrame(
            columns=[
                "source_provider",
                "query",
                "news_count",
                "unique_source_count",
                "positive_keyword_count",
                "negative_keyword_count",
                "risk_keyword_count",
                "attention_keyword_count",
                "news_attention_score",
                "news_risk_score",
                "top_titles",
            ]
        )

    rows = []
    for (provider, query), group in items.groupby(["source_provider", "query"], dropna=False):
        text = " ".join((group["title"].fillna("") + " " + group["summary"].fillna("")).astype(str))
        positive_count = keyword_count(text, POSITIVE_KEYWORDS)
        negative_count = keyword_count(text, NEGATIVE_KEYWORDS)
        risk_count = keyword_count(text, RISK_KEYWORDS)
        attention_count = keyword_count(text, ATTENTION_KEYWORDS)
        domains = group["link"].astype(str).str.extract(r"https?://([^/]+)")[0].fillna("")
        rows.append(
            {
                "source_provider": provider,
                "query": query,
                "news_count": len(group),
                "unique_source_count": int(domains.nunique()),
                "positive_keyword_count": positive_count,
                "negative_keyword_count": negative_count,
                "risk_keyword_count": risk_count,
                "attention_keyword_count": attention_count,
                "news_attention_score": len(group) + attention_count * 2 + positive_count,
                "news_risk_score": risk_count * 2 + negative_count,
                "top_titles": " | ".join(group["title"].dropna().astype(str).head(3)),
            }
        )

    return pd.DataFrame(rows)


def main():
    print("Running supplementary news providers...")
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    today = datetime.today().strftime("%Y%m%d")
    candidates = read_csv(latest_file(PROCESSED_DIR, "price_based_candidates_*.csv"))
    queries = build_queries(candidates)
    provider = GoogleNewsRssProvider()
    status_rows = []
    all_items = []

    for query in queries:
        try:
            rows = provider.fetch(query, max_items=MAX_ITEMS_PER_QUERY)
            all_items.extend(rows)
            status_rows.append(
                {
                    "source_provider": provider.provider_name,
                    "query": query,
                    "status": "success",
                    "item_count": len(rows),
                    "error_message": "",
                    "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                }
            )
        except Exception as error:
            print(f"Google News RSS failed for query '{query}': {error}")
            status_rows.append(
                {
                    "source_provider": provider.provider_name,
                    "query": query,
                    "status": "failed",
                    "item_count": 0,
                    "error_message": str(error)[:220],
                    "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                }
            )

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
    print(f"Google News RSS item count: {len(raw_df)}")
    print(f"News provider feature count: {len(features_df)}")


if __name__ == "__main__":
    main()
