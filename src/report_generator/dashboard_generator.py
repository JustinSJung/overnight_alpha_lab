import json
import os
from datetime import datetime
from pathlib import Path

import pandas as pd


PROCESSED_DIR = Path("data/processed")
PREDICTIONS_DIR = Path("data/predictions")
DOCS_DIR = Path("docs")
OUTPUT_PATH = DOCS_DIR / "dashboard.html"

CORE_STATE_PATTERNS = [
    (PROCESSED_DIR, "automation_history.csv"),
    (PROCESSED_DIR, "price_based_candidates_*.csv"),
    (PREDICTIONS_DIR, "price_candidate_evaluation_*.csv"),
    (PROCESSED_DIR, "ml_dataset_*.csv"),
    (PREDICTIONS_DIR, "error_notes_*.csv"),
    (PREDICTIONS_DIR, "market_adjusted_evaluation_*.csv"),
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
    except Exception:
        return pd.DataFrame()


def read_all_csv(directory: Path, pattern: str):
    files = sorted(directory.glob(pattern))
    frames = []

    for file in files:
        try:
            df = pd.read_csv(file)
            df["source_file"] = str(file)
            frames.append(df)
        except Exception:
            pass

    if not frames:
        return pd.DataFrame()

    return pd.concat(frames, ignore_index=True)


def has_core_state_files() -> bool:
    for directory, pattern in CORE_STATE_PATTERNS:
        if list(directory.glob(pattern)):
            return True
    return False


def normalize_stock_code(value):
    if pd.isna(value):
        return ""

    try:
        return str(int(float(value))).zfill(6)
    except Exception:
        return str(value).strip().zfill(6)


def safe_get(row, column, default="N/A"):
    if column not in row:
        return default

    value = row[column]

    if pd.isna(value):
        return default

    return value


def safe_float(value, default=0.0):
    try:
        if pd.isna(value):
            return default
        return float(value)
    except Exception:
        return default


def evaluation_result_series(df: pd.DataFrame) -> pd.Series:
    """
    Return price evaluation result values across supported schema versions.
    """

    if df.empty:
        return pd.Series(dtype=str)

    if "prediction_result" in df.columns and "price_candidate_result" in df.columns:
        primary = df["prediction_result"].astype(str)
        fallback = df["price_candidate_result"].astype(str)
        return primary.where(~primary.isin(["", "nan", "None"]), fallback)

    if "prediction_result" in df.columns:
        return df["prediction_result"].astype(str)

    if "price_candidate_result" in df.columns:
        return df["price_candidate_result"].astype(str)

    return pd.Series(dtype=str)


def build_metrics():
    latest_ml_path = latest_file(PROCESSED_DIR, "ml_dataset_*.csv")
    latest_ml_df = read_csv(latest_ml_path)

    all_error_notes = read_all_csv(PREDICTIONS_DIR, "error_notes_*.csv")
    latest_market_eval = read_csv(latest_file(PREDICTIONS_DIR, "market_adjusted_evaluation_*.csv"))
    latest_volume_score = read_csv(latest_file(PROCESSED_DIR, "trading_volume_score_adjustments_*.csv"))
    latest_social_attention = read_csv(latest_file(PROCESSED_DIR, "social_attention_features_*.csv"))
    latest_learned_rules = read_csv(latest_file(PROCESSED_DIR, "learned_event_rules_*.csv"))
    latest_price_candidates = read_csv(latest_file(PROCESSED_DIR, "price_based_candidates_*.csv"))
    all_price_eval = read_all_csv(PREDICTIONS_DIR, "price_candidate_evaluation_*.csv")

    if not latest_ml_df.empty and "stock_code" in latest_ml_df.columns:
        latest_ml_df["stock_code"] = latest_ml_df["stock_code"].apply(normalize_stock_code)

    total_events = len(latest_ml_df)

    success_count = 0
    failure_count = 0
    pending_count = 0

    if not all_error_notes.empty and "prediction_result" in all_error_notes.columns:
        result_series = all_error_notes["prediction_result"].astype(str)
        success_count = int((result_series == "success").sum())
        failure_count = int((result_series == "failure").sum())
        pending_count = int((result_series == "pending").sum())

    evaluated_count = success_count + failure_count

    if evaluated_count > 0:
        dart_success_rate = success_count / evaluated_count
    else:
        dart_success_rate = 0.0
    market_rows = len(latest_market_eval)
    volume_rows = len(latest_volume_score)
    social_rows = len(latest_social_attention)
    price_candidate_rows = len(latest_price_candidates)
    price_evaluated_count = 0
    price_success_count = 0
    price_failure_count = 0
    price_pending_count = 0
    price_success_rate = 0.0

    price_results = evaluation_result_series(all_price_eval)
    if not price_results.empty:
        price_evaluated_count = int(price_results.isin(["success", "failure"]).sum())
        price_success_count = int((price_results == "success").sum())
        price_failure_count = int((price_results == "failure").sum())
        price_pending_count = int((price_results == "pending").sum())
        if price_evaluated_count > 0:
            price_success_rate = price_success_count / price_evaluated_count

    if price_evaluated_count < 10:
        confidence_status = "NOT READY"
        confidence_comment = "KIS 가격 후보 평가 데이터가 아직 부족합니다. 가격 기반 학습 데이터 축적 단계입니다."
    elif price_success_rate >= 0.65:
        confidence_status = "WATCHLIST"
        confidence_comment = "KIS 가격 후보 평가 기준으로 초기 신뢰도 관찰 가능 단계입니다. 아직 투자 판단용은 아닙니다."
    elif price_success_rate >= 0.5:
        confidence_status = "EARLY STAGE"
        confidence_comment = "KIS 가격 후보 평가에서 일부 패턴 확인은 가능하지만 더 많은 데이터가 필요합니다."
    else:
        confidence_status = "LOW CONFIDENCE"
        confidence_comment = "KIS 가격 후보 평가 기준으로는 아직 보수적으로 해석해야 합니다."

    high_attention_count = 0
    rumor_noise_count = 0
    risk_noise_count = 0

    if not latest_social_attention.empty:
        if "attention_label" in latest_social_attention.columns:
            high_attention_count = int((latest_social_attention["attention_label"] == "high_attention").sum())

        if "rumor_label" in latest_social_attention.columns:
            rumor_noise_count = int((latest_social_attention["rumor_label"] != "no_rumor_signal").sum())

        if "risk_label" in latest_social_attention.columns:
            risk_noise_count = int((latest_social_attention["risk_label"] != "no_risk_noise").sum())
    learned_rule_count = len(latest_learned_rules)
    active_learned_rule_count = 0
    positive_learned_rule_count = 0
    negative_learned_rule_count = 0

    if not latest_learned_rules.empty and "learned_event_score_adjustment" in latest_learned_rules.columns:
        learned_scores = pd.to_numeric(
            latest_learned_rules["learned_event_score_adjustment"],
            errors="coerce",
        ).fillna(0)

        active_learned_rule_count = int((learned_scores != 0).sum())
        positive_learned_rule_count = int((learned_scores > 0).sum())
        negative_learned_rule_count = int((learned_scores < 0).sum())

    latest_ml_file = str(latest_ml_path) if latest_ml_path else "N/A"

    return {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "latest_ml_file": latest_ml_file,
        "total_events": total_events,
        "success_count": success_count,
        "failure_count": failure_count,
        "pending_count": pending_count,
        "evaluated_count": evaluated_count,
        "dart_success_rate": round(dart_success_rate * 100, 2),
        "confidence_status": confidence_status,
        "confidence_comment": confidence_comment,
        "market_rows": market_rows,
        "volume_rows": volume_rows,
        "social_rows": social_rows,
        "price_candidate_rows": price_candidate_rows,
        "price_evaluated_count": price_evaluated_count,
        "price_success_count": price_success_count,
        "price_failure_count": price_failure_count,
        "price_pending_count": price_pending_count,
        "price_success_rate": round(price_success_rate * 100, 2),
	"high_attention_count": high_attention_count,
	"rumor_noise_count": rumor_noise_count,
	"risk_noise_count": risk_noise_count,
	"learned_rule_count": learned_rule_count,
	"active_learned_rule_count": active_learned_rule_count,
	"positive_learned_rule_count": positive_learned_rule_count,
	"negative_learned_rule_count": negative_learned_rule_count,
    }, latest_ml_df


def build_stock_data(latest_ml_df):
    if latest_ml_df.empty:
        return []

    if "stock_code" in latest_ml_df.columns:
        latest_ml_df["stock_code"] = latest_ml_df["stock_code"].apply(normalize_stock_code)

    rows = []

    for _, row in latest_ml_df.iterrows():
        stock_code = str(safe_get(row, "stock_code", "")).zfill(6)

        if not stock_code:
            continue

        item = {
            "stock_code": stock_code,
            "corp_name": str(safe_get(row, "corp_name", "N/A")),
            "event_type": str(safe_get(row, "event_type", "N/A")),
            "prediction_direction": str(safe_get(row, "prediction_direction", "N/A")),
            "event_score": safe_float(safe_get(row, "event_score", 0)),
            "confidence_level": str(safe_get(row, "confidence_level", "N/A")),
            "news_count": safe_float(safe_get(row, "news_count", 0)),
            "news_sentiment_score": safe_float(safe_get(row, "news_sentiment_score", 0)),
            "prediction_result": str(safe_get(row, "prediction_result", "pending")),
            "next_close_return": safe_float(safe_get(row, "next_close_return", 0)),
            "error_category": str(safe_get(row, "error_category", "N/A")),
        }

        rows.append(item)

    deduped = {}

    for item in rows:
        deduped[item["stock_code"]] = item

    return list(deduped.values())


def build_html(metrics, stock_data):
    stock_json = json.dumps(stock_data, ensure_ascii=False)
    success_width = min(max(safe_float(metrics.get("price_success_rate", 0)), 0), 100)
    evaluated_width = 0
    price_total = metrics.get("price_evaluated_count", 0) + metrics.get("price_pending_count", 0)
    if price_total:
        evaluated_width = min(
            max(metrics.get("price_evaluated_count", 0) / price_total * 100, 0),
            100,
        )
    status_class = {
        "WATCHLIST": "badge-green",
        "MODERATE CONFIDENCE": "badge-green",
        "EARLY STAGE": "badge-orange",
        "NOT READY": "badge-orange",
        "LOW CONFIDENCE": "badge-red",
    }.get(str(metrics.get("confidence_status", "")).upper(), "badge-gray")

    html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Daily Price-Signal Learning System</title>
  <style>
    :root {{
      --bg: #f4f7fb;
      --ink: #172033;
      --muted: #647086;
      --line: #e2e8f0;
      --panel: #ffffff;
      --panel-soft: #f8fafc;
      --green: #168a5b;
      --green-soft: #e7f6ef;
      --orange: #b76b00;
      --orange-soft: #fff4df;
      --red: #be3144;
      --red-soft: #ffe9ed;
      --gray: #526070;
      --gray-soft: #edf1f5;
      --blue: #2454a6;
      --blue-soft: #e8efff;
      --shadow: 0 16px 42px rgba(23, 32, 51, 0.10);
    }}

    * {{
      box-sizing: border-box;
    }}

    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      margin: 0;
      padding: 0;
      background: var(--bg);
      color: var(--ink);
    }}

    .container {{
      max-width: 1180px;
      margin: 0 auto;
      padding: 28px 20px 44px;
    }}

    .hero {{
      display: grid;
      grid-template-columns: minmax(0, 1.45fr) minmax(280px, 0.75fr);
      gap: 28px;
      align-items: stretch;
      padding: 34px;
      border-radius: 28px;
      background:
        radial-gradient(circle at top left, rgba(79, 122, 255, 0.26), transparent 34%),
        linear-gradient(135deg, #111827 0%, #1d3557 52%, #235a67 100%);
      color: white;
      box-shadow: var(--shadow);
      overflow: hidden;
    }}

    .eyebrow {{
      margin: 0 0 12px;
      color: rgba(255, 255, 255, 0.72);
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
    }}

    h1 {{
      margin: 0;
      font-size: clamp(34px, 6vw, 58px);
      line-height: 1.02;
      letter-spacing: 0;
    }}

    .subtitle {{
      margin: 14px 0 0;
      color: rgba(255, 255, 255, 0.86);
      font-size: 20px;
      font-weight: 650;
    }}

    .hero-copy {{
      margin: 18px 0 0;
      max-width: 760px;
      color: rgba(255, 255, 255, 0.76);
      font-size: 15px;
      line-height: 1.7;
    }}

    .hero-panel {{
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      min-height: 248px;
      padding: 24px;
      border: 1px solid rgba(255, 255, 255, 0.18);
      border-radius: 22px;
      background: rgba(255, 255, 255, 0.12);
      backdrop-filter: blur(10px);
    }}

    .badge {{
      display: inline-flex;
      align-items: center;
      width: fit-content;
      padding: 8px 12px;
      border-radius: 999px;
      font-size: 12px;
      font-weight: 800;
      letter-spacing: 0.06em;
      text-transform: uppercase;
    }}

    .badge-green {{
      color: var(--green);
      background: var(--green-soft);
    }}

    .badge-orange {{
      color: var(--orange);
      background: var(--orange-soft);
    }}

    .badge-red {{
      color: var(--red);
      background: var(--red-soft);
    }}

    .badge-gray {{
      color: var(--gray);
      background: var(--gray-soft);
    }}

    .hero-rate-label {{
      margin-top: 30px;
      color: rgba(255, 255, 255, 0.68);
      font-size: 12px;
      font-weight: 750;
      letter-spacing: 0.08em;
      text-transform: uppercase;
    }}

    .hero-rate {{
      margin-top: 8px;
      font-size: clamp(44px, 8vw, 72px);
      line-height: 0.95;
      font-weight: 850;
    }}

    .progress {{
      height: 10px;
      margin-top: 18px;
      border-radius: 999px;
      overflow: hidden;
      background: rgba(255, 255, 255, 0.18);
    }}

    .progress > span {{
      display: block;
      height: 100%;
      border-radius: inherit;
      background: linear-gradient(90deg, #46d39a, #9ee6be);
    }}

    .hero-note {{
      margin-top: 12px;
      color: rgba(255, 255, 255, 0.72);
      font-size: 13px;
      line-height: 1.55;
    }}

    .section {{
      margin-top: 28px;
    }}

    .section-heading {{
      display: flex;
      align-items: end;
      justify-content: space-between;
      gap: 18px;
      margin-bottom: 14px;
    }}

    h2 {{
      margin: 0;
      font-size: 22px;
      letter-spacing: 0;
    }}

    .section-subtitle {{
      margin: 6px 0 0;
      color: var(--muted);
      font-size: 14px;
      line-height: 1.5;
    }}

    .kpi-grid {{
      display: grid;
      grid-template-columns: repeat(6, minmax(0, 1fr));
      gap: 16px;
    }}

    .signal-grid {{
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 14px;
    }}

    .card {{
      min-width: 0;
      background: var(--panel);
      border: 1px solid rgba(226, 232, 240, 0.9);
      border-radius: 8px;
      padding: 18px;
      box-shadow: 0 10px 26px rgba(23, 32, 51, 0.06);
    }}

    .kpi-card {{
      min-height: 146px;
      background: linear-gradient(180deg, #ffffff 0%, #f7fbff 100%);
      border-color: #dbeafe;
    }}

    .kpi-card.primary {{
      grid-column: span 2;
      background: linear-gradient(180deg, #f1fff7 0%, #ffffff 100%);
      border-color: #bcebd4;
    }}

    .label {{
      color: var(--muted);
      font-size: 11px;
      font-weight: 800;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      line-height: 1.35;
      margin-bottom: 10px;
    }}

    .ko-desc {{
      margin-top: -4px;
      margin-bottom: 12px;
      color: #8190a3;
      font-size: 12px;
    }}

    .value {{
      font-size: clamp(28px, 4vw, 40px);
      line-height: 1;
      font-weight: 850;
      color: var(--ink);
    }}

    .value.success {{
      color: var(--green);
    }}

    .value.warning {{
      color: var(--orange);
    }}

    .value.risk {{
      color: var(--red);
    }}

    .mini-bar {{
      height: 8px;
      margin-top: 16px;
      border-radius: 999px;
      overflow: hidden;
      background: #e7edf5;
    }}

    .mini-bar > span {{
      display: block;
      height: 100%;
      border-radius: inherit;
      background: var(--blue);
    }}

    .note {{
      padding: 15px 18px;
      border-radius: 8px;
      border: 1px solid #dbeafe;
      background: var(--blue-soft);
      color: #28446d;
      font-size: 13px;
      line-height: 1.6;
    }}

    .tool-card {{
      margin-top: 18px;
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 22px;
      box-shadow: 0 10px 26px rgba(23, 32, 51, 0.06);
    }}

    .lookup-row {{
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
      margin-top: 14px;
    }}

    input {{
      width: min(240px, 100%);
      padding: 12px 14px;
      font-size: 16px;
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      outline: none;
      background: white;
    }}

    input:focus {{
      border-color: var(--blue);
      box-shadow: 0 0 0 3px rgba(36, 84, 166, 0.12);
    }}

    button {{
      padding: 12px 16px;
      font-size: 15px;
      font-weight: 750;
      border: none;
      border-radius: 8px;
      cursor: pointer;
      background: #172033;
      color: white;
    }}

    .result {{
      margin-top: 18px;
      background: var(--panel-soft);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 18px;
    }}

    .small {{
      color: var(--muted);
      font-size: 13px;
      line-height: 1.5;
    }}

    table {{
      width: 100%;
      border-collapse: collapse;
      margin-top: 12px;
    }}

    td {{
      border-bottom: 1px solid var(--line);
      padding: 10px;
    }}

    td:first-child {{
      color: var(--muted);
      width: 220px;
    }}

    .links a {{
      display: inline-block;
      margin: 10px 10px 0 0;
      padding: 10px 12px;
      border-radius: 999px;
      background: var(--gray-soft);
      color: #24435f;
      text-decoration: none;
      font-size: 13px;
      font-weight: 750;
    }}

    @media (max-width: 920px) {{
      .hero {{
        grid-template-columns: 1fr;
        padding: 26px;
      }}

      .kpi-grid {{
        grid-template-columns: repeat(2, minmax(0, 1fr));
      }}

      .kpi-card.primary {{
        grid-column: span 2;
      }}

      .signal-grid {{
        grid-template-columns: repeat(2, minmax(0, 1fr));
      }}
    }}

    @media (max-width: 620px) {{
      .container {{
        padding: 14px 12px 34px;
      }}

      .hero {{
        border-radius: 22px;
        padding: 22px;
      }}

      .hero-panel {{
        min-height: auto;
      }}

      .kpi-grid,
      .signal-grid {{
        grid-template-columns: 1fr;
      }}

      .kpi-card.primary {{
        grid-column: span 1;
      }}

      .section-heading {{
        display: block;
      }}

      td:first-child {{
        width: 45%;
      }}
    }}
  </style>
</head>
<body>
  <div class="container">
    <section class="hero">
      <div>
        <p class="eyebrow">Overnight Alpha Lab</p>
        <h1>Daily Price-Signal Learning System</h1>
        <div class="subtitle">KIS Price-Based Learning Dashboard</div>
        <p class="hero-copy">
          Primary learning is based on Korea Investment API price-candidate evaluation.
          DART, news, Snacks, and social attention are supplementary signals.
        </p>
      </div>
      <div class="hero-panel">
        <div>
          <span class="badge {status_class}">{metrics["confidence_status"]}</span>
          <div class="hero-rate-label">Cumulative Price Success Rate</div>
          <div class="hero-rate">{metrics["price_success_rate"]}%</div>
          <div class="progress" aria-label="Price success rate">
            <span style="width: {success_width:.0f}%"></span>
          </div>
        </div>
        <p class="hero-note">{metrics["confidence_comment"]}</p>
      </div>
    </section>

    <section class="section">
      <div class="section-heading">
        <div>
          <h2>KIS Price-Based Learning</h2>
          <p class="section-subtitle">Primary learning metrics are cumulative across historical price candidate evaluations.</p>
        </div>
      </div>
      <div class="kpi-grid">
        <div class="card kpi-card primary">
          <div class="label">Price Success Rate</div>
          <div class="ko-desc">KIS 가격 후보 성공률</div>
          <div class="value success">{metrics["price_success_rate"]}%</div>
          <div class="mini-bar"><span style="width: {success_width:.0f}%"></span></div>
        </div>
        <div class="card kpi-card">
          <div class="label">Price Evaluated Cases</div>
          <div class="ko-desc">가격 후보 평가 완료</div>
          <div class="value">{metrics["price_evaluated_count"]}</div>
          <div class="mini-bar"><span style="width: {evaluated_width:.0f}%"></span></div>
        </div>
        <div class="card kpi-card">
          <div class="label">Price Success Count</div>
          <div class="ko-desc">가격 후보 성공 수</div>
          <div class="value success">{metrics["price_success_count"]}</div>
        </div>
        <div class="card kpi-card">
          <div class="label">Price Failure Count</div>
          <div class="ko-desc">가격 후보 실패 수</div>
          <div class="value risk">{metrics["price_failure_count"]}</div>
        </div>
        <div class="card kpi-card">
          <div class="label">Price Pending Candidates</div>
          <div class="ko-desc">가격 후보 평가 대기</div>
          <div class="value warning">{metrics["price_pending_count"]}</div>
        </div>
        <div class="card kpi-card">
          <div class="label">Price Candidates</div>
          <div class="ko-desc">오늘 가격 기반 후보</div>
          <div class="value">{metrics["price_candidate_rows"]}</div>
        </div>
      </div>
      <div class="note section">
        KIS price learning metrics are cumulative across historical price candidate evaluations. This dashboard is for research monitoring only and is not investment advice.
      </div>
    </section>

    <section class="section">
      <div class="section-heading">
        <div>
          <h2>Supplementary Signals</h2>
          <p class="section-subtitle">DART, news, Snacks, social attention, and learned rules provide context around the primary price loop.</p>
        </div>
      </div>
      <div class="signal-grid">
        <div class="card">
          <div class="label">DART Event Evaluated Cases</div>
          <div class="value">{metrics["evaluated_count"]}</div>
        </div>
        <div class="card">
          <div class="label">DART Event Pending Cases</div>
          <div class="value warning">{metrics["pending_count"]}</div>
        </div>
        <div class="card">
          <div class="label">DART Event Success Rate</div>
          <div class="value">{metrics["dart_success_rate"]}%</div>
        </div>
        <div class="card">
          <div class="label">Social Attention Rows</div>
          <div class="value">{metrics["social_rows"]}</div>
        </div>
        <div class="card">
          <div class="label">High Attention Signals</div>
          <div class="value success">{metrics["high_attention_count"]}</div>
        </div>
        <div class="card">
          <div class="label">Risk Noise Signals</div>
          <div class="value risk">{metrics["risk_noise_count"]}</div>
        </div>
        <div class="card">
          <div class="label">Market-Adjusted Rows</div>
          <div class="value">{metrics["market_rows"]}</div>
        </div>
        <div class="card">
          <div class="label">Learned Rule Types</div>
          <div class="value">{metrics["learned_rule_count"]}</div>
        </div>
        <div class="card">
          <div class="label">Active Learned Rules</div>
          <div class="value">{metrics["active_learned_rule_count"]}</div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="section-heading">
        <div>
          <h2>Dataset & Reports</h2>
          <p class="section-subtitle">Latest generated at {metrics["generated_at"]}. Latest ML dataset rows: {metrics["total_events"]}.</p>
        </div>
      </div>
      <div class="tool-card">
        <h2>Stock Quick Lookup <span class="small">종목 간단 조회</span></h2>
        <p class="small">
          Enter a 6-digit Korean stock code to check the latest available event summary.
          현재 ML 데이터셋에 포함된 종목만 즉시 조회됩니다. 예: 005930
        </p>
        <div class="lookup-row">
          <input id="stockInput" placeholder="6-digit stock code" maxlength="6">
          <button onclick="searchStock()">Search / 조회</button>
        </div>
        <div id="stockResult" class="result" style="display:none;"></div>
      </div>

      <div class="tool-card">
        <h2>Key Reports <span class="small">주요 리포트</span></h2>
        <div class="links">
          <a href="https://github.com/JustinSJung/overnight_alpha_lab#readme" target="_blank">README</a>
          <a href="index.html">Development Log</a>
          <a href="https://github.com/JustinSJung/overnight_alpha_lab/tree/main/reports/daily_prediction" target="_blank">Key Reports</a>
        </div>
        <p class="small">
          Latest generated reports are available in the GitHub repository under reports/daily_prediction and reports/daily_review.
          최신 리포트 파일은 GitHub 저장소의 reports/daily_prediction 및 reports/daily_review 폴더에서 확인할 수 있습니다.
        </p>
      </div>
    </section>
  </div>

  <script>
    const STOCK_DATA = {stock_json};

    function fmt(value) {{
      if (value === null || value === undefined || value === "") return "N/A";
      return value;
    }}

    function searchStock() {{
      const input = document.getElementById("stockInput").value.trim().padStart(6, "0");
      const box = document.getElementById("stockResult");

      if (!input || input.length !== 6) {{
        box.style.display = "block";
        box.innerHTML = "<b>종목코드 6자리를 입력하세요.</b>";
        return;
      }}

      const item = STOCK_DATA.find(x => x.stock_code === input);

      if (!item) {{
        box.style.display = "block";
        box.innerHTML = `
          <h3>조회 결과 없음</h3>
          <p>현재 최신 ML 데이터셋에 이 종목이 없습니다.</p>
          <p class="small">GitHub Actions 또는 로컬에서 single_stock_predictor를 별도로 실행하면 개별 리포트를 만들 수 있습니다.</p>
        `;
        return;
      }}

      box.style.display = "block";
      box.innerHTML = `
        <h3>${{item.corp_name}} (${{item.stock_code}})</h3>
        <table>
          <tr><td>이벤트 유형</td><td>${{fmt(item.event_type)}}</td></tr>
          <tr><td>예측 방향</td><td>${{fmt(item.prediction_direction)}}</td></tr>
          <tr><td>이벤트 점수</td><td>${{fmt(item.event_score)}}</td></tr>
          <tr><td>신뢰도 등급</td><td>${{fmt(item.confidence_level)}}</td></tr>
          <tr><td>뉴스 수</td><td>${{fmt(item.news_count)}}</td></tr>
          <tr><td>뉴스 감성 점수</td><td>${{fmt(item.news_sentiment_score)}}</td></tr>
          <tr><td>현재 평가 결과</td><td>${{fmt(item.prediction_result)}}</td></tr>
          <tr><td>다음 종가 수익률</td><td>${{fmt(item.next_close_return)}}</td></tr>
          <tr><td>오답/평가 분류</td><td>${{fmt(item.error_category)}}</td></tr>
        </table>
      `;
    }}
  </script>
</body>
</html>
"""


    # Final bilingual label normalization
    # Rule: English main label + short Korean sublabel
    label_replacements = {
        '<div class="label">DART Event Evaluated Cases</div>\n        <div class="value">':
        '<div class="label">DART Event Evaluated Cases</div>\n        <div class="ko-desc">DART 이벤트 평가 완료</div>\n        <div class="value">',

        '<div class="label">DART Event Pending Cases</div>\n        <div class="value">':
        '<div class="label">DART Event Pending Cases</div>\n        <div class="ko-desc">DART 이벤트 평가 대기</div>\n        <div class="value">',

        '<div class="label">DART Event Successes</div>\n        <div class="value">':
        '<div class="label">DART Event Successes</div>\n        <div class="ko-desc">DART 이벤트 성공 수</div>\n        <div class="value">',

        '<div class="label">DART Event Failures</div>\n        <div class="value">':
        '<div class="label">DART Event Failures</div>\n        <div class="ko-desc">DART 이벤트 실패 수</div>\n        <div class="value">',

        '<div class="label">Social Attention Rows</div>\n        <div class="value">':
        '<div class="label">Social Attention Rows</div>\n        <div class="ko-desc">관심도 분석 행 수</div>\n        <div class="value">',

        '<div class="label">High Attention</div>\n        <div class="value">':
        '<div class="label">High Attention Signals</div>\n        <div class="ko-desc">높은 관심도 신호</div>\n        <div class="value">',

        '<div class="label">High Attention Signals</div>\n        <div class="value">':
        '<div class="label">High Attention Signals</div>\n        <div class="ko-desc">높은 관심도 신호</div>\n        <div class="value">',

        '<div class="label">Rumor Noise</div>\n        <div class="value">':
        '<div class="label">Rumor Noise Signals</div>\n        <div class="ko-desc">루머성 노이즈 신호</div>\n        <div class="value">',

        '<div class="label">Rumor Noise Signals</div>\n        <div class="value">':
        '<div class="label">Rumor Noise Signals</div>\n        <div class="ko-desc">루머성 노이즈 신호</div>\n        <div class="value">',

        '<div class="label">Risk Noise</div>\n        <div class="value">':
        '<div class="label">Risk Noise Signals</div>\n        <div class="ko-desc">리스크성 노이즈 신호</div>\n        <div class="value">',

        '<div class="label">Risk Noise Signals</div>\n        <div class="value">':
        '<div class="label">Risk Noise Signals</div>\n        <div class="ko-desc">리스크성 노이즈 신호</div>\n        <div class="value">',

        '<div class="label">Learned Rule Types</div>\n        <div class="value">':
        '<div class="label">Learned Rule Types</div>\n        <div class="ko-desc">학습 대상 이벤트 유형</div>\n        <div class="value">',

        '<div class="label">Active Learned Rules</div>\n        <div class="value">':
        '<div class="label">Active Learned Rules</div>\n        <div class="ko-desc">활성화된 학습 룰</div>\n        <div class="value">',

        '<div class="label">Positive Rule Updates</div>\n        <div class="value">':
        '<div class="label">Positive Rule Updates</div>\n        <div class="ko-desc">점수 상향 룰</div>\n        <div class="value">',

        '<div class="label">Negative Rule Updates</div>\n        <div class="value">':
        '<div class="label">Negative Rule Updates</div>\n        <div class="ko-desc">점수 하향 룰</div>\n        <div class="value">',
    }

    for old, new in label_replacements.items():
        html = html.replace(old, new)

    text_replacements = {
        '자동 실행 기반 공시 이벤트 분석 · 신뢰도 추적 · 종목 간단 조회':
        'Automated disclosure-event analysis · confidence monitoring · stock quick lookup<br><span class="small">자동 실행 기반 공시 이벤트 분석 · 신뢰도 추적 · 종목 간단 조회</span>',

        '이 대시보드는 투자 조언이 아닙니다. 현재 시스템의 데이터 축적 상태와 분석 결과를 확인하기 위한 연구용 화면입니다.':
        '<b>Research dashboard only. Not investment advice.</b><br><span class="small">이 대시보드는 투자 조언이 아닙니다. 현재 시스템의 데이터 축적 상태와 분석 결과를 확인하기 위한 연구용 화면입니다.</span>',

        '<h2>종목 간단 조회</h2>':
        '<h2>Stock Quick Lookup <span class="tag">종목 간단 조회</span></h2>',

        '현재 ML 데이터셋에 포함된 종목만 즉시 조회됩니다. 예: 005930':
        'Enter a 6-digit Korean stock code to check the latest available event summary.<br><span class="small">현재 ML 데이터셋에 포함된 종목만 즉시 조회됩니다. 예: 005930</span>',

        'placeholder="종목코드 6자리"':
        'placeholder="6-digit stock code"',

        '>조회</button>':
        '>Search / 조회</button>',

        '<h2>주요 리포트</h2>':
        '<h2>Key Reports <span class="tag">주요 리포트</span></h2>',

        '최신 리포트 파일은 GitHub 저장소의 reports/daily_prediction 및 reports/daily_review 폴더에서 확인할 수 있습니다.':
        'Latest generated reports are available in the GitHub repository under reports/daily_prediction and reports/daily_review.<br><span class="small">최신 리포트 파일은 GitHub 저장소의 reports/daily_prediction 및 reports/daily_review 폴더에서 확인할 수 있습니다.</span>',
    }

    for old, new in text_replacements.items():
        html = html.replace(old, new)

    return html



def main():
    print("Generating dashboard...")

    DOCS_DIR.mkdir(exist_ok=True)

    if not has_core_state_files():
        print("No core state files found. Dashboard generation skipped to avoid all-zero overwrite.")
        return

    metrics, latest_ml_df = build_metrics()
    stock_data = build_stock_data(latest_ml_df)

    html = build_html(metrics, stock_data)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as file:
        file.write(html)

    print(f"Dashboard saved to: {OUTPUT_PATH}")
    print(f"Embedded stock count: {len(stock_data)}")


if __name__ == "__main__":
    main()
