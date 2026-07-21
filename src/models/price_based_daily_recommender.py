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
REVIEW_DIR = Path("reports/daily_review")
SELECTED_PICK_TOP_N = 20
SCORE_VERSION = "v2_conservative_ranker"


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


def clamp(value: float, low: float, high: float) -> float:
    return min(max(value, low), high)


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


def build_news_lookup(df: pd.DataFrame) -> dict[str, dict]:
    if df.empty or "query" not in df.columns:
        return {}

    lookup = {}
    for _, row in df.iterrows():
        query = str(row.get("query", "")).strip()
        code = normalize_stock_code(query) if query.replace(".", "", 1).isdigit() else query
        if code:
            lookup[code] = row.to_dict()
    return lookup


def calculate_v1_score(row, social: dict, ml_context: dict) -> tuple[float, float, float]:
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

    supplementary_score = 0
    if str(social.get("attention_label", "")) == "high_attention":
        supplementary_score += 3
    if str(social.get("risk_label", "")) != "no_risk_noise" and social:
        supplementary_score -= 4
    if str(ml_context.get("prediction_direction", "")) in {"positive", "neutral_positive"}:
        supplementary_score += 3
    if str(ml_context.get("prediction_direction", "")) == "negative":
        supplementary_score -= 3

    return round(price_score + supplementary_score, 2), round(price_score, 2), supplementary_score


def calculate_v2_components(row, social: dict, ml_context: dict, news: dict) -> dict:
    breakout_score = safe_float(row.get("breakout_score", 0))
    return_1d = safe_float(row.get("return_1d", 0))
    return_5d = safe_float(row.get("return_5d", 0))
    return_20d = safe_float(row.get("return_20d", 0))
    volume_ratio = safe_float(row.get("volume_ratio_20d", 0))
    volatility = safe_float(row.get("volatility_20d", 0))
    close = safe_float(row.get("close", 0))
    ma20 = safe_float(row.get("ma20", 0))

    distance_ma20 = (close / ma20 - 1) if close and ma20 else 0.0

    base_momentum_score = 45
    base_momentum_score += breakout_score * 4
    base_momentum_score += clamp(return_5d * 100, -8, 8)
    base_momentum_score += clamp(return_20d * 35, -6, 6)

    # Moderate volume confirms participation; extreme volume is handled as reversal risk.
    if 1.1 <= volume_ratio <= 2.5:
        volume_confirmation_score = clamp((volume_ratio - 1.0) * 5, 0, 7)
    elif 2.5 < volume_ratio <= 3.5:
        volume_confirmation_score = 3
    elif 0 < volume_ratio < 0.8:
        volume_confirmation_score = -2
    else:
        volume_confirmation_score = 0

    liquidity_score = 2 if volume_ratio > 0 else 0
    if volume_ratio >= 1.0:
        liquidity_score += 1

    volatility_penalty = clamp(volatility * 120, 0, 10)

    overextension_penalty = 0
    if return_1d > 0.07:
        overextension_penalty += clamp((return_1d - 0.07) * 120, 0, 8)
    if return_5d > 0.18:
        overextension_penalty += clamp((return_5d - 0.18) * 80, 0, 10)
    if return_20d > 0.35:
        overextension_penalty += clamp((return_20d - 0.35) * 45, 0, 8)
    if distance_ma20 > 0.15:
        overextension_penalty += clamp((distance_ma20 - 0.15) * 60, 0, 7)

    reversal_risk_penalty = 0
    if volume_ratio >= 3 and return_1d > 0.04:
        reversal_risk_penalty += clamp((volume_ratio - 2.5) * 2.2, 0, 8)
    if volume_ratio >= 2.5 and return_1d < 0:
        reversal_risk_penalty += 4
    if volatility > 0.06:
        reversal_risk_penalty += clamp((volatility - 0.06) * 100, 0, 6)

    risk_noise = safe_float(social.get("risk_noise_score", 0))
    hype_count = safe_float(social.get("hype_keyword_count", 0))
    risk_label = str(social.get("risk_label", ""))
    attention_label = str(social.get("attention_label", ""))
    attention_noise_penalty = clamp(risk_noise * 0.9 + hype_count * 0.7, 0, 7)
    if risk_label and risk_label != "no_risk_noise":
        attention_noise_penalty += 2

    news_risk_score = safe_float(news.get("news_risk_score", 0))
    negative_count = safe_float(news.get("negative_keyword_count", 0))
    risk_keyword_count = safe_float(news.get("risk_keyword_count", 0))
    news_risk_penalty = clamp(news_risk_score * 0.6 + negative_count * 0.4 + risk_keyword_count * 0.8, 0, 6)

    market_regime = str(row.get("market_regime_bucket", ml_context.get("market_regime_bucket", ""))).lower()
    market_regime_penalty = 2 if any(term in market_regime for term in ["weak", "risk", "bear"]) else 0

    healthy_context_score = 0
    if 0.02 <= return_5d <= 0.12 and 1.1 <= volume_ratio <= 2.5:
        healthy_context_score += 3
    if attention_label in {"normal_attention", "moderate_attention"} and risk_label in {"", "no_risk_noise"}:
        healthy_context_score += 1
    if safe_float(news.get("positive_keyword_count", 0)) > safe_float(news.get("negative_keyword_count", 0)):
        healthy_context_score += 1
    if str(ml_context.get("prediction_direction", "")) in {"positive", "neutral_positive"}:
        healthy_context_score += 1
    if str(ml_context.get("prediction_direction", "")) == "negative":
        market_regime_penalty += 2

    total_penalty = (
        volatility_penalty
        + overextension_penalty
        + reversal_risk_penalty
        + attention_noise_penalty
        + news_risk_penalty
        + market_regime_penalty
    )
    final_score = clamp(
        base_momentum_score
        + volume_confirmation_score
        + liquidity_score
        + healthy_context_score
        - total_penalty,
        0,
        100,
    )

    return {
        "base_momentum_score": round(base_momentum_score, 2),
        "volume_confirmation_score": round(volume_confirmation_score, 2),
        "liquidity_score": round(liquidity_score, 2),
        "volatility_penalty": round(volatility_penalty, 2),
        "overextension_penalty": round(overextension_penalty, 2),
        "reversal_risk_penalty": round(reversal_risk_penalty, 2),
        "news_risk_penalty": round(news_risk_penalty, 2),
        "attention_noise_penalty": round(attention_noise_penalty, 2),
        "market_regime_penalty": round(market_regime_penalty, 2),
        "healthy_context_score": round(healthy_context_score, 2),
        "final_price_signal_score_v2": round(final_score, 2),
        "score_version": SCORE_VERSION,
    }


def score_candidate(row, social_lookup: dict[str, dict], ml_lookup: dict[str, dict], news_lookup: dict[str, dict]) -> dict:
    stock_code = normalize_stock_code(row.get("stock_code", ""))
    social = social_lookup.get(stock_code, {})
    ml_context = ml_lookup.get(stock_code, {})
    news = news_lookup.get(stock_code, {})
    v1_score, price_score, supplementary_score = calculate_v1_score(row, social, ml_context)
    components = calculate_v2_components(row, social, ml_context, news)
    final_score = components["final_price_signal_score_v2"]

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
        "candidate_pool_date": row.get("signal_date", datetime.today().strftime("%Y-%m-%d")),
        "signal_date": row.get("signal_date", datetime.today().strftime("%Y-%m-%d")),
        "prediction_date": datetime.today().strftime("%Y-%m-%d"),
        "candidate_action": action,
        "prediction_direction": direction,
        "prediction_score": final_score,
        "final_price_signal_score": final_score,
        "price_candidate_score": final_score,
        "price_signal_score_v1": v1_score,
        "price_score_base": round(price_score, 2),
        "supplementary_score": supplementary_score,
        **components,
        "signal_label": row.get("signal_label", "neutral"),
        "close": row.get("close", pd.NA),
        "return_1d": row.get("return_1d", pd.NA),
        "return_5d": row.get("return_5d", pd.NA),
        "return_20d": row.get("return_20d", pd.NA),
        "ma5": row.get("ma5", pd.NA),
        "ma20": row.get("ma20", pd.NA),
        "volume_ratio_20d": row.get("volume_ratio_20d", pd.NA),
        "volatility_20d": row.get("volatility_20d", pd.NA),
        "price_source": row.get("price_source", "unknown"),
        "corp_name": ml_context.get("corp_name", ""),
        "stock_name": ml_context.get("corp_name", ""),
        "event_type": ml_context.get("event_type", ""),
        "social_attention_label": social.get("attention_label", ""),
        "social_risk_label": social.get("risk_label", ""),
        "news_risk_score": news.get("news_risk_score", pd.NA),
        "news_negative_keyword_count": news.get("negative_keyword_count", pd.NA),
        "news_risk_keyword_count": news.get("risk_keyword_count", pd.NA),
        "source_file": row.get("source_file", ""),
    }


def save_report(candidates: pd.DataFrame, output_csv: Path) -> str:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    today_display = datetime.today().strftime("%Y-%m-%d")
    output_path = REPORT_DIR / f"{today_display}_price_based_daily_candidates.md"

    selected = candidates[candidates.get("selected_pick", False) == True].copy()

    lines = [
        f"# {today_display} Price-Based Daily Candidates",
        "",
        "Price action is the primary signal. DART, Naver news, Snacks, and social attention are supplementary context.",
        "",
        f"Source CSV: `{output_csv}`",
        "",
        "## Candidate Pool Summary",
        "",
        f"- Broad candidate pool count: **{len(candidates)}**",
        f"- Selected pick count: **{len(selected)}**",
        f"- Score version: **{SCORE_VERSION}**",
        "",
        "> All candidates remain in the evaluation pool. Selected picks are top-ranked monitoring candidates, not trades.",
        "> 전체 후보는 평가 풀에 유지되며, 선별 후보는 거래 추천이 아니라 집중 모니터링용 상위 후보입니다.",
        "",
        "## Selected Top Candidates",
        "",
        "| Rank | Stock | Name | Action | Score | Signal | 5D Return | Volume Ratio | Selection Reason |",
        "|---:|---|---|---|---:|---|---:|---:|---|",
    ]

    for _, row in selected.head(SELECTED_PICK_TOP_N).iterrows():
        lines.append(
            "| {rank} | {stock} | {name} | {action} | {score:.2f} | {signal} | {ret:.2f}% | {volume:.2f}x | {reason} |".format(
                rank=int(safe_float(row.get("candidate_rank", 0))),
                stock=row.get("stock_code", ""),
                name=row.get("stock_name", row.get("corp_name", "")),
                action=row.get("candidate_action", ""),
                score=safe_float(row.get("final_price_signal_score_v2", row.get("price_candidate_score", 0))),
                signal=row.get("signal_label", ""),
                ret=safe_float(row.get("return_5d", 0)) * 100,
                volume=safe_float(row.get("volume_ratio_20d", 0)),
                reason=row.get("selection_reason", ""),
            )
        )

    lines.extend(
        [
            "",
            "## Notes",
            "",
            "- This report is for research and automation monitoring only.",
            "- Selected picks are top-ranked monitoring candidates, not trades.",
            "- 선별 후보는 거래 추천이 아니라 집중 모니터링용 상위 후보입니다.",
            "- No order placement or trading action is performed by this project.",
        ]
    )

    output_path.write_text("\n".join(lines), encoding="utf-8")
    return str(output_path)


def save_audit_report(candidates: pd.DataFrame) -> str:
    REVIEW_DIR.mkdir(parents=True, exist_ok=True)
    today_display = datetime.today().strftime("%Y-%m-%d")
    output_path = REVIEW_DIR / f"{today_display}_price_scoring_audit_report.md"

    selected = candidates[candidates.get("selected_pick", False) == True].copy()
    avg = {}
    for column in [
        "final_price_signal_score_v2",
        "base_momentum_score",
        "volume_confirmation_score",
        "volatility_penalty",
        "overextension_penalty",
        "reversal_risk_penalty",
        "news_risk_penalty",
        "attention_noise_penalty",
        "market_regime_penalty",
    ]:
        avg[column] = safe_float(pd.to_numeric(candidates.get(column, pd.Series(dtype=float)), errors="coerce").mean())

    lines = [
        f"# Price Scoring Audit Report - {today_display}",
        "",
        "This audit documents the conservative v2 price ranker. It is diagnostic only and is not investment advice.",
        "이 문서는 보수적인 v2 가격 랭커를 점검하기 위한 진단 자료이며 투자 조언이 아닙니다.",
        "",
        "## Current Score Components",
        "",
        "- v1 score: breakout score, 5-day return, 20-day return, volume ratio, volatility penalty, and small social/ML context adjustments.",
        "- v2 score: base momentum plus moderate volume/liquidity confirmation, minus volatility, overextension, reversal, news risk, attention noise, and market regime penalties.",
        f"- Score version: **{SCORE_VERSION}**",
        f"- Broad candidate pool count: **{len(candidates)}**",
        f"- Selected monitoring picks: **{len(selected)}**",
        "",
        "## Suspected Failure Modes",
        "",
        "- v1 can over-reward volume spikes and already-exhausted short-term moves.",
        "- v1 has limited penalties for pullback risk after sharp moves.",
        "- News, attention, and social risk are supplementary and may have been too lightly penalized when risk/noise is high.",
        "- Top-ranked buckets have recently underperformed the broad pool, so rank quality needs several more daily observations after v2.",
        "",
        "## Conservative Fixes",
        "",
        "- Preserve the broad candidate pool for statistical learning.",
        "- Rank selected picks by `final_price_signal_score_v2`, mirrored into existing score columns for evaluator compatibility.",
        "- Reward moderate momentum with volume confirmation instead of automatically favoring the most extreme mover.",
        "- Penalize overextension, reversal risk, attention noise, and risk-heavy news without making news the main engine.",
        "- Avoid stock-specific thresholds, future leakage, or complex ML.",
        "",
        "## Component Averages",
        "",
        "| Component | Average |",
        "|---|---:|",
    ]
    for column, value in avg.items():
        lines.append(f"| {column} | {value:.2f} |")

    lines.extend(
        [
            "",
            "## Notes",
            "",
            "V2 scoring impact should be judged after several new daily runs.",
            "V2 점수 산식 효과는 며칠 이상 신규 데이터가 쌓인 뒤 판단해야 합니다.",
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
    news_df = read_csv(latest_file(PROCESSED_DIR, "news_provider_features_*.csv"))
    social_lookup = build_context_lookup(social_df)
    ml_lookup = build_context_lookup(ml_df)
    news_lookup = build_news_lookup(news_df)

    rows = [
        score_candidate(row, social_lookup, ml_lookup, news_lookup)
        for _, row in signals_df.iterrows()
    ]

    if not rows:
        print("No price-based candidates generated.")
        return

    candidates = pd.DataFrame(rows).sort_values(
        ["final_price_signal_score_v2", "return_5d", "volume_ratio_20d"],
        ascending=[False, False, False],
    ).reset_index(drop=True)

    candidates["candidate_rank"] = range(1, len(candidates) + 1)
    candidates["selected_pick"] = candidates["candidate_rank"] <= SELECTED_PICK_TOP_N
    candidates["selection_reason"] = candidates["candidate_rank"].apply(
        lambda rank: f"Top {SELECTED_PICK_TOP_N} by conservative v2 price signal score"
        if rank <= SELECTED_PICK_TOP_N
        else "Broad evaluation pool candidate"
    )

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    today = datetime.today().strftime("%Y%m%d")
    output_csv = PROCESSED_DIR / f"price_based_candidates_{today}.csv"
    candidates.to_csv(output_csv, index=False, encoding="utf-8-sig")
    report_path = save_report(candidates, output_csv)
    audit_path = save_audit_report(candidates)

    print(f"Saved {len(candidates)} price-based candidates: {output_csv}")
    print(f"Saved report: {report_path}")
    print(f"Saved scoring audit report: {audit_path}")
    print(f"score_version: {SCORE_VERSION}")
    print(f"selected picks today: {int(candidates['selected_pick'].sum())}")


if __name__ == "__main__":
    main()
