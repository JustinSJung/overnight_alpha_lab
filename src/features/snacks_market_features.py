"""
Snacks market feature layer.

This script reads the latest Sherwood Snacks newsletter data,
extracts global market theme signals, and generates:
- data/processed/snacks_market_features_YYYYMMDD.csv
- reports/daily_review/YYYY-MM-DD_snacks_market_digest.md

This layer is a global market context layer.
It should not be interpreted as investment advice.
"""

from collections import Counter
from datetime import datetime
from pathlib import Path

import pandas as pd


RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")
REPORT_DIR = Path("reports/daily_review")


THEME_KEYWORDS = {
    "ai_semiconductor": [
        "ai",
        "artificial intelligence",
        "chip",
        "chips",
        "semiconductor",
        "nvidia",
        "data center",
        "datacenter",
        "gpu",
        "openai",
    ],
    "ev_battery": [
        "ev",
        "electric vehicle",
        "tesla",
        "battery",
        "lithium",
        "charging",
        "automaker",
    ],
    "macro_rate_inflation": [
        "fed",
        "rate",
        "rates",
        "inflation",
        "cpi",
        "treasury",
        "yield",
        "dollar",
        "recession",
    ],
    "consumer_retail": [
        "consumer",
        "retail",
        "walmart",
        "target",
        "amazon",
        "shopping",
        "spending",
        "black friday",
    ],
    "bio_healthcare": [
        "fda",
        "drug",
        "biotech",
        "pharma",
        "healthcare",
        "clinical",
        "trial",
        "vaccine",
    ],
    "energy_commodity": [
        "oil",
        "gas",
        "energy",
        "opec",
        "crude",
        "commodity",
        "commodities",
    ],
    "meme_retail_trading": [
        "meme",
        "robinhood",
        "retail trader",
        "retail investors",
        "short squeeze",
        "reddit",
    ],
    "crypto_fintech": [
        "bitcoin",
        "crypto",
        "ethereum",
        "coinbase",
        "fintech",
        "stablecoin",
    ],
}


RISK_KEYWORDS = [
    "risk",
    "lawsuit",
    "probe",
    "investigation",
    "slowdown",
    "warning",
    "loss",
    "layoff",
    "bankruptcy",
    "default",
    "tariff",
    "sanction",
    "volatility",
    "selloff",
    "crash",
    "fraud",
]


ATTENTION_KEYWORDS = [
    "surge",
    "jump",
    "rally",
    "record",
    "boom",
    "hot",
    "viral",
    "trend",
    "hype",
    "soar",
    "spike",
    "breakout",
]


KOREA_RELEVANCE_KEYWORDS = [
    "chip",
    "semiconductor",
    "memory",
    "battery",
    "ev",
    "ai",
    "shipbuilding",
    "steel",
    "oil",
    "energy",
    "biotech",
    "healthcare",
    "consumer",
]


def latest_file(directory: Path, pattern: str):
    files = sorted(directory.glob(pattern))
    if not files:
        return None
    return files[-1]


def count_keywords(text: str, keywords: list[str]) -> int:
    text_lower = str(text).lower()
    return sum(text_lower.count(keyword.lower()) for keyword in keywords)


def detect_top_themes(text: str) -> tuple[str, int]:
    scores = {}

    for theme, keywords in THEME_KEYWORDS.items():
        scores[theme] = count_keywords(text, keywords)

    nonzero = {theme: score for theme, score in scores.items() if score > 0}

    if not nonzero:
        return "no_clear_theme", 0

    top_theme = max(nonzero, key=nonzero.get)
    return top_theme, nonzero[top_theme]


def build_features(df: pd.DataFrame) -> pd.DataFrame:
    rows = []

    for _, row in df.iterrows():
        title = str(row.get("title", ""))
        body = str(row.get("body_text", ""))
        combined_text = f"{title} {body}"

        top_theme, top_theme_score = detect_top_themes(combined_text)

        risk_score = count_keywords(combined_text, RISK_KEYWORDS)
        attention_score = count_keywords(combined_text, ATTENTION_KEYWORDS)
        korea_relevance_score = count_keywords(combined_text, KOREA_RELEVANCE_KEYWORDS)

        rows.append(
            {
                "collected_at": row.get("collected_at", ""),
                "source": row.get("source", "Sherwood Snacks"),
                "rank": row.get("rank", ""),
                "title": title,
                "url": row.get("url", ""),
                "top_global_theme": top_theme,
                "top_global_theme_score": top_theme_score,
                "us_market_attention_score": attention_score,
                "macro_risk_score": risk_score,
                "korea_relevance_score": korea_relevance_score,
                "body_length": row.get("body_length", 0),
            }
        )

    return pd.DataFrame(rows)


def build_report(feature_df: pd.DataFrame, output_path: Path):
    lines = []

    today = datetime.today().strftime("%Y-%m-%d")

    lines.append(f"# Snacks Global Market Digest - {today}")
    lines.append("")
    lines.append("## Purpose")
    lines.append("")
    lines.append(
        "This report summarizes recent public Sherwood Snacks newsletter articles as a global market context layer."
    )
    lines.append("")
    lines.append(
        "It is used as a supplementary market-attention signal, not as direct investment advice."
    )
    lines.append("")

    if feature_df.empty:
        lines.append("No Snacks market digest rows available.")
        output_path.write_text("\n".join(lines), encoding="utf-8")
        return

    total_rows = len(feature_df)
    total_attention = int(feature_df["us_market_attention_score"].sum())
    total_macro_risk = int(feature_df["macro_risk_score"].sum())
    total_korea_relevance = int(feature_df["korea_relevance_score"].sum())

    theme_counts = Counter(feature_df["top_global_theme"].tolist())

    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Snacks articles analyzed: **{total_rows}**")
    lines.append(f"- US market attention signals: **{total_attention}**")
    lines.append(f"- Macro risk signals: **{total_macro_risk}**")
    lines.append(f"- Korea relevance signals: **{total_korea_relevance}**")
    lines.append("")

    lines.append("## Top Global Themes")
    lines.append("")
    lines.append("| Theme | Count |")
    lines.append("|---|---:|")

    for theme, count in theme_counts.most_common():
        lines.append(f"| {theme} | {count} |")

    lines.append("")
    lines.append("## Latest Snacks Articles")
    lines.append("")
    lines.append(
        "| Rank | Title | Top Theme | Attention | Macro Risk | Korea Relevance | URL |"
    )
    lines.append("|---:|---|---|---:|---:|---:|---|")

    for _, row in feature_df.iterrows():
        title = str(row.get("title", "")).replace("|", " ")
        url = str(row.get("url", ""))
        lines.append(
            f"| {row.get('rank', '')} | {title} | "
            f"{row.get('top_global_theme', '')} | "
            f"{row.get('us_market_attention_score', 0)} | "
            f"{row.get('macro_risk_score', 0)} | "
            f"{row.get('korea_relevance_score', 0)} | "
            f"{url} |"
        )

    lines.append("")
    lines.append("## Interpretation")
    lines.append("")
    lines.append("- High US market attention may indicate stronger global market narrative momentum.")
    lines.append("- Macro risk signals are used only as context, not as direct trading signals.")
    lines.append("- Korea relevance signals indicate possible thematic overlap with Korean equities.")
    lines.append("- This layer should be observed before being integrated into candidate scoring.")
    lines.append("")

    output_path.write_text("\n".join(lines), encoding="utf-8")


def main():
    print("Generating Snacks market features...")

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    latest_raw = latest_file(RAW_DIR, "snacks_newsletters_*.csv")

    if latest_raw is None:
        print("No Snacks raw newsletter file found.")
        print("Snacks market feature generation will stop gracefully.")
        return

    df = pd.read_csv(latest_raw)

    if df.empty:
        print("Snacks raw newsletter file is empty.")
        return

    feature_df = build_features(df)

    today_compact = datetime.today().strftime("%Y%m%d")
    today_dash = datetime.today().strftime("%Y-%m-%d")

    output_csv = PROCESSED_DIR / f"snacks_market_features_{today_compact}.csv"
    output_report = REPORT_DIR / f"{today_dash}_snacks_market_digest.md"

    feature_df.to_csv(output_csv, index=False)
    build_report(feature_df, output_report)

    print(f"Saved Snacks market features to: {output_csv}")
    print(f"Saved Snacks market digest report to: {output_report}")
    print(f"Rows: {len(feature_df)}")


if __name__ == "__main__":
    main()
