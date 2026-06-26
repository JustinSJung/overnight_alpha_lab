"""
Social attention feature generator.

This script creates simple social / rumor / retail attention features
from existing disclosure and news text data.

It does not scrape private communities or login-required websites.
It only uses already collected local project data.

Inputs:
- data/processed/selected_key_events_YYYYMMDD.csv
- data/processed/event_news_features_YYYYMMDD.csv

Outputs:
- data/processed/social_attention_features_YYYYMMDD.csv
- reports/daily_review/YYYY-MM-DD_social_attention_report.md
"""

import os
from datetime import datetime
from pathlib import Path

import pandas as pd


PROCESSED_DIR = Path("data/processed")
REPORT_DIR = Path("reports/daily_review")


HYPE_KEYWORDS = [
    "급등",
    "폭등",
    "상한가",
    "강세",
    "신고가",
    "테마",
    "수급",
    "매수세",
    "관심",
    "주목",
    "기대감",
    "랠리",
]

RUMOR_KEYWORDS = [
    "찌라시",
    "루머",
    "소문",
    "단독",
    "추정",
    "가능성",
    "검토",
    "논의",
    "물밑",
    "미확인",
]

RETAIL_KEYWORDS = [
    "개미",
    "개인투자자",
    "투자자",
    "종토방",
    "커뮤니티",
    "인기",
    "검색",
    "관심종목",
]

POSITIVE_CATALYST_KEYWORDS = [
    "수주",
    "계약",
    "공급",
    "인수",
    "합병",
    "투자",
    "승인",
    "개발",
    "성과",
    "흑자",
    "호실적",
    "확대",
]

RISK_NOISE_KEYWORDS = [
    "급락",
    "하락",
    "약세",
    "우려",
    "리스크",
    "적자",
    "손실",
    "소송",
    "유상증자",
    "전환사채",
    "CB",
    "BW",
    "거래정지",
    "상장폐지",
    "불성실",
    "압수수색",
]


def latest_file(directory: Path, pattern: str):
    files = sorted(directory.glob(pattern))

    if not files:
        return None

    return files[-1]


def read_csv(path):
    if path is None or not path.exists():
        return pd.DataFrame()

    try:
        return pd.read_csv(path)
    except Exception as error:
        print(f"Failed to read {path}: {error}")
        return pd.DataFrame()


def normalize_stock_code(value):
    if pd.isna(value):
        return ""

    try:
        return str(int(float(value))).zfill(6)
    except Exception:
        return str(value).strip().zfill(6)


def count_keywords(text: str, keywords: list) -> int:
    if not isinstance(text, str):
        return 0

    text_upper = text.upper()
    count = 0

    for keyword in keywords:
        keyword_upper = keyword.upper()
        if keyword_upper in text_upper:
            count += 1

    return count


def combine_text(row) -> str:
    parts = []

    for column in [
        "corp_name",
        "report_nm",
        "event_type",
        "top_news_titles",
    ]:
        if column in row and not pd.isna(row[column]):
            parts.append(str(row[column]))

    return " ".join(parts)


def build_social_features(events_df: pd.DataFrame, news_df: pd.DataFrame) -> pd.DataFrame:
    if events_df.empty:
        return pd.DataFrame()

    if "stock_code" in events_df.columns:
        events_df["stock_code"] = events_df["stock_code"].apply(normalize_stock_code)

    if not news_df.empty and "stock_code" in news_df.columns:
        news_df["stock_code"] = news_df["stock_code"].apply(normalize_stock_code)

    if not news_df.empty:
        merge_columns = [
            column
            for column in [
                "stock_code",
                "news_count",
                "news_sentiment_score",
                "news_attention_score",
                "top_news_titles",
            ]
            if column in news_df.columns
        ]

        merged_df = events_df.merge(
            news_df[merge_columns],
            on="stock_code",
            how="left",
        )
    else:
        merged_df = events_df.copy()

    rows = []

    for _, row in merged_df.iterrows():
        text = combine_text(row)

        hype_count = count_keywords(text, HYPE_KEYWORDS)
        rumor_count = count_keywords(text, RUMOR_KEYWORDS)
        retail_count = count_keywords(text, RETAIL_KEYWORDS)
        positive_catalyst_count = count_keywords(text, POSITIVE_CATALYST_KEYWORDS)
        risk_noise_count = count_keywords(text, RISK_NOISE_KEYWORDS)

        news_count = 0
        news_attention_score = 0
        news_sentiment_score = 0

        if "news_count" in row and not pd.isna(row["news_count"]):
            news_count = float(row["news_count"])

        if "news_attention_score" in row and not pd.isna(row["news_attention_score"]):
            news_attention_score = float(row["news_attention_score"])

        if "news_sentiment_score" in row and not pd.isna(row["news_sentiment_score"]):
            news_sentiment_score = float(row["news_sentiment_score"])

        social_attention_score = (
            hype_count * 3
            + retail_count * 2
            + positive_catalyst_count * 2
            + min(news_count, 10) * 0.5
            + news_attention_score * 0.2
        )

        rumor_noise_score = rumor_count * 4

        risk_noise_score = risk_noise_count * 3

        if social_attention_score >= 12:
            attention_label = "high_attention"
        elif social_attention_score >= 6:
            attention_label = "medium_attention"
        elif social_attention_score > 0:
            attention_label = "low_attention"
        else:
            attention_label = "no_attention_signal"

        if rumor_noise_score >= 8:
            rumor_label = "high_rumor_noise"
        elif rumor_noise_score >= 4:
            rumor_label = "medium_rumor_noise"
        elif rumor_noise_score > 0:
            rumor_label = "low_rumor_noise"
        else:
            rumor_label = "no_rumor_signal"

        if risk_noise_score >= 9:
            risk_label = "high_risk_noise"
        elif risk_noise_score >= 3:
            risk_label = "risk_noise_detected"
        else:
            risk_label = "no_risk_noise"

        rows.append(
            {
                "stock_code": normalize_stock_code(row.get("stock_code", "")),
                "corp_name": row.get("corp_name", "N/A"),
                "event_type": row.get("event_type", "N/A"),
                "report_nm": row.get("report_nm", "N/A"),
                "news_count": news_count,
                "news_sentiment_score": news_sentiment_score,
                "hype_keyword_count": hype_count,
                "rumor_keyword_count": rumor_count,
                "retail_keyword_count": retail_count,
                "positive_catalyst_keyword_count": positive_catalyst_count,
                "risk_noise_keyword_count": risk_noise_count,
                "social_attention_score": round(social_attention_score, 2),
                "rumor_noise_score": round(rumor_noise_score, 2),
                "risk_noise_score": round(risk_noise_score, 2),
                "attention_label": attention_label,
                "rumor_label": rumor_label,
                "risk_label": risk_label,
                "source_text_sample": text[:300],
            }
        )

    return pd.DataFrame(rows)


def save_features(features_df: pd.DataFrame) -> str:
    os.makedirs(PROCESSED_DIR, exist_ok=True)

    today = datetime.today().strftime("%Y%m%d")
    output_path = PROCESSED_DIR / f"social_attention_features_{today}.csv"

    features_df.to_csv(output_path, index=False, encoding="utf-8-sig")

    return str(output_path)


def build_report(features_df: pd.DataFrame) -> str:
    os.makedirs(REPORT_DIR, exist_ok=True)

    today_display = datetime.today().strftime("%Y-%m-%d")
    output_path = REPORT_DIR / f"{today_display}_social_attention_report.md"

    lines = []

    lines.append(f"# Social Attention Feature Report - {today_display}")
    lines.append("")
    lines.append("## Purpose")
    lines.append("")
    lines.append(
        "This report summarizes investor attention, rumor-noise, and risk-noise signals "
        "derived from existing disclosure and news text."
    )
    lines.append("")
    lines.append(
        "This layer does not treat rumors as facts. It only treats rumor-like language "
        "as a noise and attention feature for research purposes."
    )
    lines.append("")

    if features_df.empty:
        lines.append("No social attention features generated.")
        lines.append("")

        with open(output_path, "w", encoding="utf-8") as file:
            file.write("\n".join(lines))

        return str(output_path)

    total_rows = len(features_df)
    high_attention = int((features_df["attention_label"] == "high_attention").sum())
    medium_attention = int((features_df["attention_label"] == "medium_attention").sum())
    rumor_detected = int((features_df["rumor_label"] != "no_rumor_signal").sum())
    risk_detected = int((features_df["risk_label"] != "no_risk_noise").sum())

    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Total rows: **{total_rows}**")
    lines.append(f"- High attention rows: **{high_attention}**")
    lines.append(f"- Medium attention rows: **{medium_attention}**")
    lines.append(f"- Rumor-noise detected rows: **{rumor_detected}**")
    lines.append(f"- Risk-noise detected rows: **{risk_detected}**")
    lines.append("")

    lines.append("## Top Social Attention Signals")
    lines.append("")

    display_columns = [
        "stock_code",
        "corp_name",
        "event_type",
        "social_attention_score",
        "rumor_noise_score",
        "risk_noise_score",
        "attention_label",
        "rumor_label",
        "risk_label",
    ]

    top_df = features_df.sort_values(
        by=["social_attention_score", "rumor_noise_score", "risk_noise_score"],
        ascending=[False, False, False],
    ).head(20)

    lines.append("| " + " | ".join(display_columns) + " |")
    lines.append("|" + "|".join(["---"] * len(display_columns)) + "|")

    for _, row in top_df.iterrows():
        values = [str(row.get(column, "N/A")) for column in display_columns]
        lines.append("| " + " | ".join(values) + " |")

    lines.append("")
    lines.append("## Interpretation")
    lines.append("")
    lines.append("- High social attention may indicate stronger short-term investor interest.")
    lines.append("- Rumor-noise should not be interpreted as truth. It is only a noise signal.")
    lines.append("- Risk-noise may help explain why seemingly positive events fail.")
    lines.append("- This layer should be combined with event score, market-adjusted return, and trading volume reaction.")
    lines.append("")

    with open(output_path, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))

    return str(output_path)


def main():
    print("Generating social attention features...")

    events_path = latest_file(PROCESSED_DIR, "selected_key_events_*.csv")
    news_path = latest_file(PROCESSED_DIR, "event_news_features_*.csv")

    print(f"Latest selected events: {events_path}")
    print(f"Latest news features: {news_path}")

    events_df = read_csv(events_path)
    news_df = read_csv(news_path)

    features_df = build_social_features(events_df, news_df)

    feature_path = save_features(features_df)
    report_path = build_report(features_df)

    print(f"Social attention features saved to: {feature_path}")
    print(f"Social attention report saved to: {report_path}")
    print(f"Rows: {len(features_df)}")


if __name__ == "__main__":
    main()
