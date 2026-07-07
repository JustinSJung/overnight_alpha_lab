"""
Generate price-based daily candidates.

Price action is the primary signal. DART, news, social attention, and learned
rules are treated as supplementary context when available.
"""

from datetime import datetime
from pathlib import Path

import pandas as pd


PROCESSED_DIR = Path("data/processed")
REPORT_DIR = Path("reports/daily_prediction")


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
    except Exception:
        return pd.DataFrame()


def normalize_stock_code(value) -> str:
    if value is None or pd.isna(value):
        return ""

    try:
        return str(int(float(value))).zfill(6)
    except Exception:
        return str(value).strip().zfill(6)


def safe_float(value, default=0.0) -> float:
    try:
        if pd.isna(value):
            return default
        return float(value)
    except Exception:
        return default


def build_context_lookup(df: pd.DataFrame) -> dict[str, dict]:
    if df.empty or "stock_code" not in df.columns:
        return {}

    df = df.copy()
    df["stock_code"] = df["stock_code"].apply(normalize_stock_code)
    lookup = {}

    for _, row in df.iterrows():
        code = row.get("stock_code", "")
        if code:
            lookup[code] = row.to_dict()

    return lookup


def score_candidate(row, social_lookup: dict[str, dict], ml_lookup: dict[str, dict]) -> dict:
    stock_code = normalize_stock_code(row.get("stock_code", ""))
    breakout_score = safe_float(row.get("breakout_score", 0))
    return_5d = safe_float(row.get("return_5d", 0))
    return_20d = safe_float(row.get("return_20d", 0))
    volume_ratio = safe_float(row.get("volume_ratio_20d", 0))
    volatility = safe_float(row.get("volatility_20d", 0))

    price_score = 50
    price_score += breakout_score * 8
    price_score += min(max(return_5d * 100, -15), 15)
    price_score += min(max(return_20d * 50, -10), 10)
    price_score += min(max((volume_ratio - 1) * 6, -6), 12)
    price_score -= min(volatility * 100, 8)

    social = social_lookup.get(stock_code, {})
    ml_context = ml_lookup.get(stock_code, {})

    supplementary_score = 0
    if str(social.get("attention_label", "")) == "high_attention":
        supplementary_score += 3
    if str(social.get("risk_label", "")) != "no_risk_noise" and social:
        supplementary_score -= 4
    if str(ml_context.get("prediction_direction", "")) in {"positive", "neutral_positive"}:
        supplementary_score += 3
    if str(ml_context.get("prediction_direction", "")) == "negative":
        supplementary_score -= 3

    final_score = round(price_score + supplementary_score, 2)

    if final_score >= 75:
        action = "BUY_CANDIDATE"
        direction = "positive"
    elif final_score >= 60:
        action = "WATCHLIST"
        direction = "neutral_positive"
    elif final_score <= 40:
        action = "AVOID"
        direction = "negative"
    else:
        action = "HOLD"
        direction = "neutral"

    return {
        "stock_code": stock_code,
        "candidate_date": row.get("signal_date", datetime.today().strftime("%Y-%m-%d")),
        "candidate_action": action,
        "prediction_direction": direction,
        "price_candidate_score": final_score,
        "price_score_base": round(price_score, 2),
        "supplementary_score": supplementary_score,
        "signal_label": row.get("signal_label", "neutral"),
        "close": row.get("close", pd.NA),
        "return_1d": row.get("return_1d", pd.NA),
        "return_5d": row.get("return_5d", pd.NA),
        "return_20d": row.get("return_20d", pd.NA),
        "volume_ratio_20d": row.get("volume_ratio_20d", pd.NA),
        "volatility_20d": row.get("volatility_20d", pd.NA),
        "price_source": row.get("price_source", "unknown"),
        "corp_name": ml_context.get("corp_name", ""),
        "event_type": ml_context.get("event_type", ""),
        "social_attention_label": social.get("attention_label", ""),
        "social_risk_label": social.get("risk_label", ""),
        "source_file": row.get("source_file", ""),
    }


def save_report(candidates: pd.DataFrame, output_csv: Path) -> str:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    today_display = datetime.today().strftime("%Y-%m-%d")
    output_path = REPORT_DIR / f"{today_display}_price_based_daily_candidates.md"

    lines = [
        f"# {today_display} Price-Based Daily Candidates",
        "",
        "Price action is the primary signal. DART, Naver news, Snacks, and social attention are supplementary context.",
        "",
        f"Source CSV: `{output_csv}`",
        "",
        "| Stock | Action | Score | Signal | 5D Return | Volume Ratio | Source |",
        "|---|---|---:|---|---:|---:|---|",
    ]

    for _, row in candidates.head(30).iterrows():
        lines.append(
            "| {stock} | {action} | {score:.2f} | {signal} | {ret:.2f}% | {volume:.2f}x | {source} |".format(
                stock=row.get("stock_code", ""),
                action=row.get("candidate_action", ""),
                score=safe_float(row.get("price_candidate_score", 0)),
                signal=row.get("signal_label", ""),
                ret=safe_float(row.get("return_5d", 0)) * 100,
                volume=safe_float(row.get("volume_ratio_20d", 0)),
                source=row.get("price_source", ""),
            )
        )

    lines.extend(
        [
            "",
            "## Notes",
            "",
            "- This report is for research and automation monitoring only.",
            "- No order placement or trading action is performed by this project.",
        ]
    )

    output_path.write_text("\n".join(lines), encoding="utf-8")
    return str(output_path)


def main():
    print("Generating price-based daily candidates...")

    signals_path = latest_file(PROCESSED_DIR, "daily_price_signals_*.csv")
    signals_df = read_csv(signals_path)

    if signals_df.empty:
        print("No daily price signals found. Price-based recommender skipped.")
        return

    if "stock_code" in signals_df.columns:
        signals_df["stock_code"] = signals_df["stock_code"].apply(normalize_stock_code)

    social_df = read_csv(latest_file(PROCESSED_DIR, "social_attention_features_*.csv"))
    ml_df = read_csv(latest_file(PROCESSED_DIR, "ml_dataset_*.csv"))
    social_lookup = build_context_lookup(social_df)
    ml_lookup = build_context_lookup(ml_df)

    rows = [
        score_candidate(row, social_lookup, ml_lookup)
        for _, row in signals_df.iterrows()
    ]

    if not rows:
        print("No price-based candidates generated.")
        return

    candidates = pd.DataFrame(rows).sort_values(
        ["price_candidate_score", "return_5d", "volume_ratio_20d"],
        ascending=[False, False, False],
    )

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    today = datetime.today().strftime("%Y%m%d")
    output_csv = PROCESSED_DIR / f"price_based_candidates_{today}.csv"
    candidates.to_csv(output_csv, index=False, encoding="utf-8-sig")
    report_path = save_report(candidates, output_csv)

    print(f"Saved {len(candidates)} price-based candidates: {output_csv}")
    print(f"Saved report: {report_path}")


if __name__ == "__main__":
    main()
