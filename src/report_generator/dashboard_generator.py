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

    html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>Overnight Alpha Lab Dashboard</title>
  <style>
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      margin: 0;
      padding: 0;
      background: #f5f7fb;
      color: #222;
    }}
    .container {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 32px 20px;
    }}
    h1 {{
      margin-bottom: 8px;
    }}
    .subtitle {{
      color: #666;
      margin-bottom: 28px;
    }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 16px;
      margin-bottom: 28px;
    }}
    .card {{
      background: white;
      border-radius: 14px;
      padding: 18px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }}
    .label {{
      font-size: 13px;
      color: #666;
      margin-bottom: 8px;
    }}
    .value {{
      font-size: 28px;
      font-weight: 700;
    }}
    .status {{
      font-size: 24px;
      font-weight: 700;
      margin-bottom: 8px;
    }}
    .notice {{
      background: #fff8e6;
      border-left: 5px solid #f0b429;
      padding: 14px 18px;
      border-radius: 8px;
      margin-bottom: 24px;
    }}
    input {{
      padding: 12px;
      font-size: 16px;
      width: 180px;
      border: 1px solid #ccc;
      border-radius: 8px;
    }}
    button {{
      padding: 12px 16px;
      font-size: 16px;
      border: none;
      border-radius: 8px;
      cursor: pointer;
      background: #24292f;
      color: white;
      margin-left: 8px;
    }}
    .result {{
      margin-top: 18px;
      background: white;
      border-radius: 14px;
      padding: 20px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }}
    .small {{
      color: #666;
      font-size: 13px;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin-top: 12px;
    }}
    td {{
      border-bottom: 1px solid #eee;
      padding: 10px;
    }}
    td:first-child {{
      color: #666;
      width: 220px;
    }}
    .links a {{
      display: inline-block;
      margin-right: 12px;
      margin-bottom: 8px;
      color: #0969da;
      text-decoration: none;
    }}
  </style>
</head>
<body>
  <div class="container">
    <h1>Overnight Alpha Lab Dashboard</h1>
    <div class="subtitle">
      자동 실행 기반 공시 이벤트 분석 · 신뢰도 추적 · 종목 간단 조회
    </div>

    <div class="notice">
      이 대시보드는 투자 조언이 아닙니다. 현재 시스템의 데이터 축적 상태와 분석 결과를 확인하기 위한 연구용 화면입니다.
      <br>
      <span class="small">Primary learning is based on Korea Investment API price-candidate evaluation. DART/news/Snacks are supplementary signals.</span>
      <br>
      <span class="small">KIS price learning metrics are cumulative across historical price candidate evaluations.</span>
    </div>

    <div class="grid">
      <div class="card">
        <div class="label">System Confidence Status</div>
        <div class="ko-desc">현재 신뢰도 상태</div>
        <div class="status">{metrics["confidence_status"]}</div>
        <div class="small">{metrics["confidence_comment"]}</div>
      </div>
      <div class="card">
        <div class="label">Price Success Rate</div>
        <div class="ko-desc">KIS 가격 후보 성공률</div>
        <div class="value">{metrics["price_success_rate"]}%</div>
      </div>
      <div class="card">
        <div class="label">DART Event Evaluated Cases</div>
        <div class="ko-desc">DART 이벤트 평가 완료</div>
        <div class="value">{metrics["evaluated_count"]}</div>
      </div>
      <div class="card">
        <div class="label">DART Event Pending Cases</div>
        <div class="ko-desc">DART 이벤트 평가 대기</div>
        <div class="value">{metrics["pending_count"]}</div>
      </div>
    </div>

    <div class="grid">
      <div class="card">
        <div class="label">Latest ML Dataset Rows</div>
        <div class="ko-desc">최근 ML 데이터 행 수</div>
        <div class="value">{metrics["total_events"]}</div>
      </div>
      <div class="card">
        <div class="label">DART Event Successes</div>
        <div class="ko-desc">DART 이벤트 성공 수</div>
        <div class="value">{metrics["success_count"]}</div>
      </div>
      <div class="card">
        <div class="label">DART Event Failures</div>
        <div class="ko-desc">DART 이벤트 실패 수</div>
        <div class="value">{metrics["failure_count"]}</div>
      </div>
      <div class="card">
        <div class="label">Last Generated At</div>
        <div class="ko-desc">마지막 생성 시간</div>
        <div class="small">{metrics["generated_at"]}</div>
      </div>
    </div>
    <div class="grid">
      <div class="card">
        <div class="label">Price Candidates</div>
        <div class="ko-desc">가격 기반 후보</div>
        <div class="value">{metrics["price_candidate_rows"]}</div>
      </div>
      <div class="card">
        <div class="label">Price Evaluated Cases</div>
        <div class="ko-desc">가격 후보 평가 완료</div>
        <div class="value">{metrics["price_evaluated_count"]}</div>
      </div>
      <div class="card">
        <div class="label">Price Success Count</div>
        <div class="ko-desc">가격 후보 성공 수</div>
        <div class="value">{metrics["price_success_count"]}</div>
      </div>
      <div class="card">
        <div class="label">Price Failure Count</div>
        <div class="ko-desc">가격 후보 실패 수</div>
        <div class="value">{metrics["price_failure_count"]}</div>
      </div>
      <div class="card">
        <div class="label">Price Pending Candidates</div>
        <div class="ko-desc">가격 후보 평가 대기</div>
        <div class="value">{metrics["price_pending_count"]}</div>
      </div>
      <div class="card">
        <div class="label">DART Event Success Rate</div>
        <div class="ko-desc">DART 이벤트 성공률</div>
        <div class="value">{metrics["dart_success_rate"]}%</div>
      </div>
    </div>
    <div class="grid">
      <div class="card">
        <div class="label">Social Attention Rows</div>
        <div class="value">{metrics["social_rows"]}</div>
      </div>
      <div class="card">
        <div class="label">High Attention Signals</div>
        <div class="ko-desc">높은 관심도 신호</div>
        <div class="value">{metrics["high_attention_count"]}</div>
      </div>
      <div class="card">
        <div class="label">Rumor Noise Signals</div>
        <div class="ko-desc">루머성 노이즈 신호</div>
        <div class="value">{metrics["rumor_noise_count"]}</div>
      </div>
      <div class="card">
        <div class="label">Risk Noise Signals</div>
        <div class="ko-desc">리스크성 노이즈 신호</div>
        <div class="value">{metrics["risk_noise_count"]}</div>
      </div>
    </div>
    <div class="grid">
      <div class="card">
        <div class="label">Learned Rule Types</div>
        <div class="value">{metrics["learned_rule_count"]}</div>
      </div>
      <div class="card">
        <div class="label">Active Learned Rules</div>
        <div class="value">{metrics["active_learned_rule_count"]}</div>
      </div>
      <div class="card">
        <div class="label">Positive Rule Updates</div>
        <div class="value">{metrics["positive_learned_rule_count"]}</div>
      </div>
      <div class="card">
        <div class="label">Negative Rule Updates</div>
        <div class="value">{metrics["negative_learned_rule_count"]}</div>
      </div>
    </div>
    <div class="card">
      <h2>종목 간단 조회</h2>
      <p class="small">
        현재 ML 데이터셋에 포함된 종목만 즉시 조회됩니다. 예: 005930
      </p>
      <input id="stockInput" placeholder="종목코드 6자리" maxlength="6">
      <button onclick="searchStock()">조회</button>
      <div id="stockResult" class="result" style="display:none;"></div>
    </div>

    <div class="card" style="margin-top:24px;">
      <h2>주요 리포트</h2>
      <div class="links">
        <a href="https://github.com/JustinSJung/overnight_alpha_lab#readme" target="_blank">README</a>
        <a href="index.html">Development Log</a>
      </div>
      <p class="small">
        최신 리포트 파일은 GitHub 저장소의 reports/daily_prediction 및 reports/daily_review 폴더에서 확인할 수 있습니다.
      </p>
    </div>
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
