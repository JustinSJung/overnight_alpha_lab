import json
import os
from datetime import datetime
from pathlib import Path

import pandas as pd


PROCESSED_DIR = Path("data/processed")
PREDICTIONS_DIR = Path("data/predictions")
DOCS_DIR = Path("docs")
OUTPUT_PATH = DOCS_DIR / "dashboard.html"


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


def build_metrics():
    latest_ml_path = latest_file(PROCESSED_DIR, "ml_dataset_*.csv")
    latest_ml_df = read_csv(latest_ml_path)

    all_error_notes = read_all_csv(PREDICTIONS_DIR, "error_notes_*.csv")
    latest_market_eval = read_csv(latest_file(PREDICTIONS_DIR, "market_adjusted_evaluation_*.csv"))
    latest_volume_score = read_csv(latest_file(PROCESSED_DIR, "trading_volume_score_adjustments_*.csv"))

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
        success_rate = success_count / evaluated_count
    else:
        success_rate = 0.0

    if evaluated_count < 10:
        confidence_status = "NOT READY"
        confidence_comment = "아직 평가 완료 데이터가 부족합니다. 데이터 축적 단계입니다."
    elif success_rate >= 0.65:
        confidence_status = "WATCHLIST"
        confidence_comment = "초기 신뢰도 관찰 가능 단계입니다. 아직 투자 판단용은 아닙니다."
    elif success_rate >= 0.5:
        confidence_status = "EARLY STAGE"
        confidence_comment = "일부 패턴 확인은 가능하지만 더 많은 데이터가 필요합니다."
    else:
        confidence_status = "LOW CONFIDENCE"
        confidence_comment = "현재 성과 기준으로는 보수적으로 해석해야 합니다."

    market_rows = len(latest_market_eval)
    volume_rows = len(latest_volume_score)

    latest_ml_file = str(latest_ml_path) if latest_ml_path else "N/A"

    return {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "latest_ml_file": latest_ml_file,
        "total_events": total_events,
        "success_count": success_count,
        "failure_count": failure_count,
        "pending_count": pending_count,
        "evaluated_count": evaluated_count,
        "success_rate": round(success_rate * 100, 2),
        "confidence_status": confidence_status,
        "confidence_comment": confidence_comment,
        "market_rows": market_rows,
        "volume_rows": volume_rows,
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
    </div>

    <div class="grid">
      <div class="card">
        <div class="label">현재 신뢰도 상태</div>
        <div class="status">{metrics["confidence_status"]}</div>
        <div class="small">{metrics["confidence_comment"]}</div>
      </div>
      <div class="card">
        <div class="label">누적 성공률</div>
        <div class="value">{metrics["success_rate"]}%</div>
      </div>
      <div class="card">
        <div class="label">평가 완료</div>
        <div class="value">{metrics["evaluated_count"]}</div>
      </div>
      <div class="card">
        <div class="label">Pending</div>
        <div class="value">{metrics["pending_count"]}</div>
      </div>
    </div>

    <div class="grid">
      <div class="card">
        <div class="label">최근 ML 데이터 행 수</div>
        <div class="value">{metrics["total_events"]}</div>
      </div>
      <div class="card">
        <div class="label">성공</div>
        <div class="value">{metrics["success_count"]}</div>
      </div>
      <div class="card">
        <div class="label">실패</div>
        <div class="value">{metrics["failure_count"]}</div>
      </div>
      <div class="card">
        <div class="label">마지막 생성 시간</div>
        <div class="small">{metrics["generated_at"]}</div>
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

    return html


def main():
    print("Generating dashboard...")

    DOCS_DIR.mkdir(exist_ok=True)

    metrics, latest_ml_df = build_metrics()
    stock_data = build_stock_data(latest_ml_df)

    html = build_html(metrics, stock_data)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as file:
        file.write(html)

    print(f"Dashboard saved to: {OUTPUT_PATH}")
    print(f"Embedded stock count: {len(stock_data)}")


if __name__ == "__main__":
    main()

