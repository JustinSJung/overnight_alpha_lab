import json
import os
import sys
from datetime import datetime
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.evaluation.metrics import (
    classify_confidence_status,
    reliability_score_from_wilson,
    safe_percentage,
)
from src.storage.schema import RESULT_FAILURE, RESULT_PENDING, RESULT_SUCCESS


PROCESSED_DIR = Path("data/processed")
PREDICTIONS_DIR = Path("data/predictions")
DOCS_DIR = Path("docs")
OUTPUT_PATH = DOCS_DIR / "dashboard.html"

CORE_STATE_PATTERNS = [
    (PROCESSED_DIR, "automation_history.csv"),
    (PROCESSED_DIR, "price_based_candidates_*.csv"),
    (PROCESSED_DIR, "price_signal_diagnostics_summary_*.csv"),
    (PROCESSED_DIR, "news_provider_features_*.csv"),
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


def success_series(df: pd.DataFrame, success_column: str) -> pd.Series:
    """
    Return success/failure/pending values with backward-compatible fallback.
    """

    if df.empty:
        return pd.Series(dtype=str)

    fallback = evaluation_result_series(df)

    if success_column in df.columns:
        primary = df[success_column].astype(str)
        missing = primary.isin(["", "nan", "None", "<NA>"])
        return primary.where(~missing, fallback)

    return fallback


def count_results(series: pd.Series) -> dict:
    return {
        "success": int((series == RESULT_SUCCESS).sum()),
        "failure": int((series == RESULT_FAILURE).sum()),
        "pending": int((series == RESULT_PENDING).sum()),
    }


def explicit_result_series(df: pd.DataFrame, column: str) -> pd.Series:
    if df.empty or column not in df.columns:
        return pd.Series(dtype=str)

    series = df[column].astype(str)
    return series.where(~series.isin(["", "nan", "None", "<NA>"]), "")


def rolling_success_metrics(df: pd.DataFrame, days: int) -> dict:
    if df.empty:
        return {
            "success_rate": None,
            "evaluated_count": 0,
        }

    date_source = pd.Series(pd.NaT, index=df.index, dtype="datetime64[ns]")
    for column in ["evaluation_date", "evaluated_at", "signal_date", "candidate_date"]:
        if column in df.columns:
            parsed = pd.to_datetime(df[column], errors="coerce")
            date_source = date_source.fillna(parsed)

    if date_source.notna().sum() == 0:
        return {
            "success_rate": None,
            "evaluated_count": 0,
        }

    result_series = success_series(df, "success_close_t1")
    evaluated_mask = result_series.isin([RESULT_SUCCESS, RESULT_FAILURE])

    if not evaluated_mask.any():
        return {
            "success_rate": None,
            "evaluated_count": 0,
        }

    latest_date = date_source[evaluated_mask].max()
    cutoff = latest_date - pd.Timedelta(days=days - 1)
    mask = evaluated_mask & (date_source >= cutoff) & (date_source <= latest_date)
    evaluated_count = int(mask.sum())

    if evaluated_count == 0:
        return {
            "success_rate": None,
            "evaluated_count": 0,
        }

    success_count = int((result_series[mask] == RESULT_SUCCESS).sum())
    return {
        "success_rate": round(safe_percentage(success_count, evaluated_count), 2),
        "evaluated_count": evaluated_count,
    }


def format_metric_value(value, suffix=""):
    if value is None:
        return "Insufficient data / 데이터 부족"
    return f"{value}{suffix}"


def render_kpi_value(value, suffix="", css_class=""):
    if value is None:
        return "\n".join([
            '<div class="kpi-value-small">',
            '            <span class="status-pill">Insufficient data<br>데이터 부족</span>',
            '          </div>',
        ])

    classes = "kpi-value"
    if css_class:
        classes += f" {css_class}"
    return f'<div class="{classes}">{value}{suffix}</div>'


def render_status_pill(value, ko_value="데이터 부족", css_class=""):
    if value is None or value == "":
        value = "Insufficient data"
        ko_value = "데이터 부족"

    classes = "status-pill"
    if css_class:
        classes += f" {css_class}"

    return f'<span class="{classes}">{value}<br>{ko_value}</span>'


def ranking_status_class(value):
    text = str(value or "").lower()
    if "improving" in text:
        return "badge-green"
    if "inverted" in text:
        return "badge-red"
    if "weak" in text:
        return "badge-orange"
    return "badge-gray"


def file_mtime(path):
    if path is None or not path.exists():
        return None

    try:
        return datetime.fromtimestamp(path.stat().st_mtime).strftime("%Y-%m-%d %H:%M:%S")
    except Exception:
        return None


def first_row_value(df: pd.DataFrame, column: str, default=None):
    if df.empty or column not in df.columns:
        return default
    value = df.iloc[0].get(column, default)
    if pd.isna(value):
        return default
    return value


def build_metrics():
    latest_ml_path = latest_file(PROCESSED_DIR, "ml_dataset_*.csv")
    latest_ml_df = read_csv(latest_ml_path)

    all_error_notes = read_all_csv(PREDICTIONS_DIR, "error_notes_*.csv")
    latest_market_eval = read_csv(latest_file(PREDICTIONS_DIR, "market_adjusted_evaluation_*.csv"))
    latest_volume_score = read_csv(latest_file(PROCESSED_DIR, "trading_volume_score_adjustments_*.csv"))
    latest_social_attention = read_csv(latest_file(PROCESSED_DIR, "social_attention_features_*.csv"))
    latest_learned_rules = read_csv(latest_file(PROCESSED_DIR, "learned_event_rules_*.csv"))
    latest_price_candidates = read_csv(latest_file(PROCESSED_DIR, "price_based_candidates_*.csv"))
    latest_diagnostics_path = latest_file(PROCESSED_DIR, "price_signal_diagnostics_summary_*.csv")
    latest_diagnostics = read_csv(latest_diagnostics_path)
    latest_news_items_path = latest_file(Path("data/raw"), "news_provider_items_*.csv")
    latest_news_features_path = latest_file(PROCESSED_DIR, "news_provider_features_*.csv")
    latest_news_status_path = latest_file(PROCESSED_DIR, "news_provider_status_*.csv")
    latest_naver_news_path = latest_file(Path("data/raw"), "naver_news_*.csv")
    latest_snacks_raw_path = latest_file(Path("data/raw"), "snacks_newsletters_*.csv")
    latest_news_items = read_csv(latest_news_items_path)
    latest_news_features = read_csv(latest_news_features_path)
    latest_news_status = read_csv(latest_news_status_path)
    latest_naver_news = read_csv(latest_naver_news_path)
    latest_snacks_raw = read_csv(latest_snacks_raw_path)
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
    selected_pick_rows = 0
    if not latest_price_candidates.empty and "selected_pick" in latest_price_candidates.columns:
        selected_pick_rows = int(
            latest_price_candidates["selected_pick"].astype(str).str.lower().isin(["true", "1", "yes"]).sum()
        )
    price_evaluated_count = 0
    price_success_count = 0
    price_failure_count = 0
    price_pending_count = 0
    price_success_rate = 0.0
    benchmark_evaluated_count = 0
    benchmark_success_count = 0
    benchmark_success_rate = None
    rolling_7d_success_rate = None
    rolling_30d_success_rate = None
    rolling_7d_evaluated_count = 0
    rolling_30d_evaluated_count = 0

    price_results = success_series(all_price_eval, "success_close_t1")
    if not price_results.empty:
        price_evaluated_count = int(price_results.isin(["success", "failure"]).sum())
        price_success_count = int((price_results == "success").sum())
        price_failure_count = int((price_results == "failure").sum())
        price_pending_count = int((price_results == "pending").sum())
        if price_evaluated_count > 0:
            price_success_rate = price_success_count / price_evaluated_count

    benchmark_results = explicit_result_series(all_price_eval, "success_excess_t1")
    if not benchmark_results.empty:
        benchmark_evaluated_count = int(benchmark_results.isin([RESULT_SUCCESS, RESULT_FAILURE]).sum())
        benchmark_success_count = int((benchmark_results == RESULT_SUCCESS).sum())
        if benchmark_evaluated_count > 0:
            benchmark_success_rate = round(safe_percentage(benchmark_success_count, benchmark_evaluated_count), 2)

    rolling_7d = rolling_success_metrics(all_price_eval, 7)
    rolling_30d = rolling_success_metrics(all_price_eval, 30)
    rolling_7d_success_rate = rolling_7d["success_rate"]
    rolling_30d_success_rate = rolling_30d["success_rate"]
    rolling_7d_evaluated_count = rolling_7d["evaluated_count"]
    rolling_30d_evaluated_count = rolling_30d["evaluated_count"]

    reliability_score = reliability_score_from_wilson(
        price_success_count,
        price_evaluated_count,
    )
    confidence_status, confidence_status_ko = classify_confidence_status(reliability_score)
    confidence_comment = (
        "Wilson 신뢰구간 하한값 기준의 보수적 신뢰도입니다. "
        "표본 수가 적을수록 단순 성공률보다 낮게 표시됩니다."
    )

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

    diagnostics_overall_success_rate = first_row_value(
        latest_diagnostics,
        "raw_success_rate",
        None,
    )
    diagnostics_reliability_score = first_row_value(
        latest_diagnostics,
        "wilson_reliability_score",
        None,
    )
    top_10_success_rate = first_row_value(latest_diagnostics, "top_10_success_rate", None)
    top_20_success_rate = first_row_value(latest_diagnostics, "top_20_success_rate", None)
    top_50_success_rate = first_row_value(latest_diagnostics, "top_50_success_rate", None)
    top_100_success_rate = first_row_value(latest_diagnostics, "top_100_success_rate", None)
    top_10_evaluated_count = first_row_value(latest_diagnostics, "top_10_evaluated_count", None)
    top_20_evaluated_count = first_row_value(latest_diagnostics, "top_20_evaluated_count", None)
    top_50_evaluated_count = first_row_value(latest_diagnostics, "top_50_evaluated_count", None)
    top_100_evaluated_count = first_row_value(latest_diagnostics, "top_100_evaluated_count", None)
    diagnostics_judgment_en = first_row_value(latest_diagnostics, "judgment_en", "")
    diagnostics_judgment_ko = first_row_value(latest_diagnostics, "judgment_ko", "")
    diagnostics_score_version = first_row_value(latest_diagnostics, "score_version", "legacy / mixed")
    v2_evaluated_count = first_row_value(latest_diagnostics, "v2_evaluated_count", 0)
    ranking_diagnosis_en = first_row_value(latest_diagnostics, "ranking_diagnosis_en", "Insufficient v2 data")
    ranking_diagnosis_ko = first_row_value(latest_diagnostics, "ranking_diagnosis_ko", "v2 데이터 부족")

    google_status_en = None
    google_status_ko = "데이터 부족"
    google_item_count = len(latest_news_items)
    news_feature_count = len(latest_news_features)
    last_news_provider_update = file_mtime(latest_news_features_path) or file_mtime(latest_news_items_path)

    if not latest_news_status.empty and "source_provider" in latest_news_status.columns:
        google_rows = latest_news_status[
            latest_news_status["source_provider"].astype(str) == "google_news_rss"
        ]
        if not google_rows.empty:
            if "updated_at" in google_rows.columns:
                last_news_provider_update = str(google_rows.iloc[-1].get("updated_at", last_news_provider_update))
            item_total = int(pd.to_numeric(google_rows.get("item_count", 0), errors="coerce").fillna(0).sum())
            if item_total > 0:
                google_status_en = "Available"
                google_status_ko = "수집 가능"
            elif "status" in google_rows.columns and (google_rows["status"].astype(str) == "failed").any():
                google_status_en = "Provider failed"
                google_status_ko = "수집 실패"
            else:
                google_status_en = "No items"
                google_status_ko = "수집 항목 없음"

    naver_status_en = "Available" if len(latest_naver_news) > 0 else None
    naver_status_ko = "수집 가능" if len(latest_naver_news) > 0 else "데이터 부족"
    snacks_status_en = "Available" if len(latest_snacks_raw) > 0 or len(latest_snacks_market := read_csv(latest_file(PROCESSED_DIR, "snacks_market_features_*.csv"))) > 0 else None
    snacks_status_ko = "수집 가능" if snacks_status_en else "데이터 부족"

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
        "confidence_status_ko": confidence_status_ko,
        "confidence_comment": confidence_comment,
        "market_rows": market_rows,
        "volume_rows": volume_rows,
        "social_rows": social_rows,
        "price_candidate_rows": price_candidate_rows,
        "selected_pick_rows": selected_pick_rows,
        "price_evaluated_count": price_evaluated_count,
        "price_success_count": price_success_count,
        "price_failure_count": price_failure_count,
        "price_pending_count": price_pending_count,
        "price_success_rate": round(price_success_rate * 100, 2),
        "reliability_score": round(reliability_score, 1),
        "benchmark_evaluated_count": benchmark_evaluated_count,
        "benchmark_success_count": benchmark_success_count,
        "benchmark_success_rate": benchmark_success_rate,
        "rolling_7d_success_rate": rolling_7d_success_rate,
        "rolling_30d_success_rate": rolling_30d_success_rate,
        "rolling_7d_evaluated_count": rolling_7d_evaluated_count,
        "rolling_30d_evaluated_count": rolling_30d_evaluated_count,
	"high_attention_count": high_attention_count,
	"rumor_noise_count": rumor_noise_count,
	"risk_noise_count": risk_noise_count,
	"learned_rule_count": learned_rule_count,
	"active_learned_rule_count": active_learned_rule_count,
	"positive_learned_rule_count": positive_learned_rule_count,
	"negative_learned_rule_count": negative_learned_rule_count,
        "diagnostics_overall_success_rate": diagnostics_overall_success_rate,
        "diagnostics_reliability_score": diagnostics_reliability_score,
        "top_10_success_rate": top_10_success_rate,
        "top_20_success_rate": top_20_success_rate,
        "top_50_success_rate": top_50_success_rate,
        "top_100_success_rate": top_100_success_rate,
        "top_10_evaluated_count": top_10_evaluated_count,
        "top_20_evaluated_count": top_20_evaluated_count,
        "top_50_evaluated_count": top_50_evaluated_count,
        "top_100_evaluated_count": top_100_evaluated_count,
        "diagnostics_judgment_en": diagnostics_judgment_en,
        "diagnostics_judgment_ko": diagnostics_judgment_ko,
        "diagnostics_score_version": diagnostics_score_version,
        "v2_evaluated_count": v2_evaluated_count,
        "ranking_diagnosis_en": ranking_diagnosis_en,
        "ranking_diagnosis_ko": ranking_diagnosis_ko,
        "naver_status_en": naver_status_en,
        "naver_status_ko": naver_status_ko,
        "google_status_en": google_status_en,
        "google_status_ko": google_status_ko,
        "snacks_status_en": snacks_status_en,
        "snacks_status_ko": snacks_status_ko,
        "last_news_provider_update": last_news_provider_update,
        "news_provider_item_count": google_item_count,
        "news_provider_feature_count": news_feature_count,
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
    reliability_width = min(max(safe_float(metrics.get("reliability_score", 0)), 0), 100)
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
        "HIGH CONFIDENCE": "badge-green",
        "EARLY STAGE": "badge-orange",
        "NOT READY": "badge-orange",
        "LOW CONFIDENCE": "badge-red",
    }.get(str(metrics.get("confidence_status", "")).upper(), "badge-gray")
    ranking_class = ranking_status_class(metrics.get("ranking_diagnosis_en"))
    benchmark_helper = ""
    if metrics.get("benchmark_success_rate") is None:
        benchmark_helper = "\n".join([
            '<div class="muted-helper">',
            '            Benchmark evaluation will appear after benchmark-matched candidate results are available.<br>',
            '            시장 기준 평가 데이터가 쌓이면 표시됩니다.',
            '          </div>',
        ])

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

    .hero-rate-unit {{
      font-size: clamp(22px, 4vw, 34px);
      color: rgba(255, 255, 255, 0.68);
    }}

    .hero-stats {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 8px;
      margin-top: 18px;
      padding-top: 16px;
      border-top: 1px solid rgba(255, 255, 255, 0.16);
    }}

    .hero-stat {{
      display: flex;
      align-items: baseline;
      justify-content: space-between;
      gap: 16px;
      color: rgba(255, 255, 255, 0.74);
      font-size: 13px;
    }}

    .hero-stat b {{
      color: white;
      font-size: 15px;
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

    .heading-ko {{
      display: inline-block;
      margin-left: 8px;
      color: var(--muted);
      font-size: 14px;
      font-weight: 650;
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

    .value,
    .kpi-value {{
      font-size: clamp(28px, 4vw, 40px);
      line-height: 1;
      font-weight: 850;
      color: var(--ink);
    }}

    .value.success,
    .kpi-value.success {{
      color: var(--green);
    }}

    .value.warning,
    .kpi-value.warning {{
      color: var(--orange);
    }}

    .value.risk,
    .kpi-value.risk {{
      color: var(--red);
    }}

    .kpi-value-small {{
      min-height: 42px;
      display: flex;
      align-items: center;
    }}

    .status-pill {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      max-width: 100%;
      padding: 8px 11px;
      border-radius: 999px;
      background: var(--gray-soft);
      color: #5b6678;
      font-size: 12px;
      font-weight: 800;
      line-height: 1.25;
      text-align: center;
      white-space: normal;
    }}

    .status-pill.badge-green {{
      color: var(--green);
      background: var(--green-soft);
    }}

    .status-pill.badge-orange {{
      color: var(--orange);
      background: var(--orange-soft);
    }}

    .status-pill.badge-red {{
      color: var(--red);
      background: var(--red-soft);
    }}

    .status-pill.badge-gray {{
      color: var(--gray);
      background: var(--gray-soft);
    }}

    .muted-helper {{
      margin-top: 10px;
      color: var(--muted);
      font-size: 12px;
      line-height: 1.45;
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
        <div class="subtitle">KIS Price-Based Learning Dashboard / KIS 가격 기반 학습 대시보드</div>
        <p class="hero-copy">
          Primary learning is based on Korea Investment API price-candidate evaluation.
          DART, news, Snacks, and social attention are supplementary signals.
        </p>
      </div>
      <div class="hero-panel">
        <div>
          <span class="badge {status_class}">{metrics["confidence_status"]} / {metrics["confidence_status_ko"]}</span>
          <div class="hero-rate-label">Reliability Score<br>신뢰도 점수</div>
          <div class="hero-rate">{metrics["reliability_score"]}<span class="hero-rate-unit"> / 100</span></div>
          <div class="progress" aria-label="Reliability score">
            <span style="width: {reliability_width:.0f}%"></span>
          </div>
          <div class="hero-stats">
            <div class="hero-stat">
              <span>Price Success Rate / 가격 후보 성공률</span>
              <b>{metrics["price_success_rate"]}%</b>
            </div>
            <div class="hero-stat">
              <span>Price Evaluated Cases / 가격 후보 평가 완료</span>
              <b>{metrics["price_evaluated_count"]}</b>
            </div>
            <div class="hero-stat">
              <span>Price Pending Candidates / 가격 후보 평가 대기</span>
              <b>{metrics["price_pending_count"]}</b>
            </div>
          </div>
        </div>
        <p class="hero-note">{metrics["confidence_status_ko"]}. {metrics["confidence_comment"]}</p>
      </div>
    </section>

    <section class="section">
      <div class="section-heading">
        <div>
          <h2>KIS Price-Based Learning <span class="heading-ko">KIS 가격 기반 학습</span></h2>
          <p class="section-subtitle">Primary learning metrics are cumulative across historical price candidate evaluations. KIS 가격 후보 평가 데이터를 누적 기준으로 집계합니다.</p>
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
        <div class="card kpi-card">
          <div class="label">Benchmark-Adjusted Success Rate</div>
          <div class="ko-desc">시장 대비 성공률</div>
          {render_kpi_value(metrics["benchmark_success_rate"], "%")}
          {benchmark_helper}
        </div>
        <div class="card kpi-card">
          <div class="label">Benchmark-Adjusted Evaluated Cases</div>
          <div class="ko-desc">시장 대비 평가 완료</div>
          <div class="value">{metrics["benchmark_evaluated_count"]}</div>
        </div>
      </div>
      <div class="note section">
        Reliability Score uses the Wilson lower confidence bound, so it is more conservative than raw success rate when sample size is small.<br>
        신뢰도 점수는 Wilson 신뢰구간 하한값을 사용하므로, 표본 수가 적을 때 단순 성공률보다 보수적으로 계산됩니다.
      </div>
    </section>

    <section class="section">
      <div class="section-heading">
        <div>
          <h2>Rolling Performance <span class="heading-ko">최근 성과 추이</span></h2>
          <p class="section-subtitle">Rolling metrics use evaluation date, or signal date when evaluation date is unavailable. 최근 평가일 기준의 단기 성과를 확인합니다.</p>
        </div>
      </div>
      <div class="signal-grid">
        <div class="card">
          <div class="label">Rolling 7-Day Success Rate</div>
          <div class="ko-desc">최근 7일 성공률</div>
          {render_kpi_value(metrics["rolling_7d_success_rate"], "%")}
        </div>
        <div class="card">
          <div class="label">Rolling 30-Day Success Rate</div>
          <div class="ko-desc">최근 30일 성공률</div>
          {render_kpi_value(metrics["rolling_30d_success_rate"], "%")}
        </div>
        <div class="card">
          <div class="label">Rolling 7-Day Evaluated Cases</div>
          <div class="ko-desc">최근 7일 평가 수</div>
          {render_kpi_value(metrics["rolling_7d_evaluated_count"] or None)}
        </div>
        <div class="card">
          <div class="label">Rolling 30-Day Evaluated Cases</div>
          <div class="ko-desc">최근 30일 평가 수</div>
          {render_kpi_value(metrics["rolling_30d_evaluated_count"] or None)}
        </div>
      </div>
    </section>

    <section class="section">
      <div class="section-heading">
        <div>
          <h2>Signal Quality Diagnostics <span class="heading-ko">신호 품질 진단</span></h2>
          <p class="section-subtitle">Rank buckets are recalculated within each signal/prediction day, then aggregated across evaluated days. 랭킹 구간은 각 일자 안에서 다시 계산한 뒤 전체 평가일에 걸쳐 누적 집계합니다.</p>
        </div>
      </div>
      <div class="kpi-grid">
        <div class="card kpi-card primary">
          <div class="label">Overall Price Success Rate</div>
          <div class="ko-desc">전체 가격 후보 성공률</div>
          {render_kpi_value(metrics["diagnostics_overall_success_rate"], "%", "success")}
        </div>
        <div class="card kpi-card">
          <div class="label">Current Ranking Diagnosis</div>
          <div class="ko-desc">현재 랭킹 진단</div>
          <div class="kpi-value-small">{render_status_pill(metrics["ranking_diagnosis_en"], metrics["ranking_diagnosis_ko"], ranking_class)}</div>
          <div class="muted-helper">V2 evaluated cases: {format_metric_value(metrics["v2_evaluated_count"])}<br>v2 평가 완료: {format_metric_value(metrics["v2_evaluated_count"])}</div>
        </div>
        <div class="card kpi-card">
          <div class="label">Score Version</div>
          <div class="ko-desc">점수 산식 버전</div>
          <div class="kpi-value-small">{render_status_pill(metrics["diagnostics_score_version"], "보수적 v2 랭커", "badge-gray")}</div>
          <div class="muted-helper">V2 scoring impact should be judged after several new daily runs.<br>v2 점수 산식 효과는 며칠 이상 신규 데이터가 쌓인 뒤 판단해야 합니다.</div>
        </div>
        <div class="card kpi-card">
          <div class="label">Top 10 Cumulative Success Rate</div>
          <div class="ko-desc">일별 Top 10 누적 성공률</div>
          {render_kpi_value(metrics["top_10_success_rate"], "%")}
          <div class="muted-helper">Evaluated cases: {format_metric_value(metrics["top_10_evaluated_count"])}<br>평가 완료: {format_metric_value(metrics["top_10_evaluated_count"])}</div>
        </div>
        <div class="card kpi-card">
          <div class="label">Top 20 Cumulative Success Rate</div>
          <div class="ko-desc">일별 Top 20 누적 성공률</div>
          {render_kpi_value(metrics["top_20_success_rate"], "%")}
          <div class="muted-helper">Evaluated cases: {format_metric_value(metrics["top_20_evaluated_count"])}<br>평가 완료: {format_metric_value(metrics["top_20_evaluated_count"])}</div>
        </div>
        <div class="card kpi-card">
          <div class="label">Top 50 Cumulative Success Rate</div>
          <div class="ko-desc">일별 Top 50 누적 성공률</div>
          {render_kpi_value(metrics["top_50_success_rate"], "%")}
          <div class="muted-helper">Evaluated cases: {format_metric_value(metrics["top_50_evaluated_count"])}<br>평가 완료: {format_metric_value(metrics["top_50_evaluated_count"])}</div>
        </div>
        <div class="card kpi-card">
          <div class="label">Top 100 Cumulative Success Rate</div>
          <div class="ko-desc">일별 Top 100 누적 성공률</div>
          {render_kpi_value(metrics["top_100_success_rate"], "%")}
          <div class="muted-helper">Evaluated cases: {format_metric_value(metrics["top_100_evaluated_count"])}<br>평가 완료: {format_metric_value(metrics["top_100_evaluated_count"])}</div>
        </div>
        <div class="card kpi-card">
          <div class="label">Candidate Pool Today</div>
          <div class="ko-desc">오늘 평가 후보 풀</div>
          <div class="value">{metrics["price_candidate_rows"]}</div>
        </div>
        <div class="card kpi-card">
          <div class="label">Selected Picks Today</div>
          <div class="ko-desc">오늘 선별 후보 수</div>
          <div class="value success">{metrics["selected_pick_rows"]}</div>
        </div>
      </div>
      <div class="note section">
        Large candidate pools improve statistical reliability. Selected picks are a smaller top-ranked subset for focused monitoring.<br>
        큰 후보 풀은 통계적 신뢰도 측정에 도움이 되며, 선별 후보는 집중 모니터링용 상위 후보입니다.<br>
        Top N rates are cumulative per signal/prediction day, then aggregated across historical evaluations.<br>
        Top N 성공률은 각 signal/prediction 일자별 누적 구간을 과거 평가 전체에 걸쳐 집계한 값입니다.<br>
        V2 scoring impact should be judged after several new daily runs.<br>
        V2 점수 산식 효과는 며칠 이상 신규 데이터가 쌓인 뒤 판단해야 합니다.<br>
        <span class="small">{metrics["diagnostics_judgment_en"]}<br>{metrics["diagnostics_judgment_ko"]}</span>
      </div>
    </section>

    <section class="section">
      <div class="section-heading">
        <div>
          <h2>News Source Status <span class="heading-ko">뉴스 소스 상태</span></h2>
          <p class="section-subtitle">News providers are supplementary context and should not block the primary KIS price loop. 뉴스 provider는 보조 신호이며 KIS 가격 학습 파이프라인을 중단시키지 않습니다.</p>
        </div>
      </div>
      <div class="signal-grid">
        <div class="card">
          <div class="label">Naver Status</div>
          <div class="ko-desc">네이버 뉴스 상태</div>
          <div class="kpi-value-small">{render_status_pill(metrics["naver_status_en"], metrics["naver_status_ko"])}</div>
        </div>
        <div class="card">
          <div class="label">Google News RSS Status</div>
          <div class="ko-desc">Google News RSS 상태</div>
          <div class="kpi-value-small">{render_status_pill(metrics["google_status_en"], metrics["google_status_ko"])}</div>
        </div>
        <div class="card">
          <div class="label">Snacks Digest Status</div>
          <div class="ko-desc">Snacks 시장 요약 상태</div>
          <div class="kpi-value-small">{render_status_pill(metrics["snacks_status_en"], metrics["snacks_status_ko"])}</div>
        </div>
        <div class="card">
          <div class="label">Last News Provider Update</div>
          <div class="ko-desc">마지막 뉴스 provider 업데이트</div>
          <div class="kpi-value-small">{render_status_pill(metrics["last_news_provider_update"], "업데이트 시각")}</div>
        </div>
        <div class="card">
          <div class="label">News Provider Items</div>
          <div class="ko-desc">뉴스 provider 원문 항목 수</div>
          <div class="value">{metrics["news_provider_item_count"]}</div>
        </div>
        <div class="card">
          <div class="label">News Provider Features</div>
          <div class="ko-desc">뉴스 provider 특징 행 수</div>
          <div class="value">{metrics["news_provider_feature_count"]}</div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="section-heading">
        <div>
          <h2>Supplementary Signals <span class="heading-ko">보조 신호</span></h2>
          <p class="section-subtitle">DART, news, Snacks, social attention, and learned rules provide context around the primary price loop. DART, 뉴스, Snacks, 관심도 분석은 가격 기반 학습을 보조합니다.</p>
        </div>
      </div>
      <div class="signal-grid">
        <div class="card">
          <div class="label">DART Event Evaluated Cases</div>
          <div class="ko-desc">DART 이벤트 평가 완료</div>
          <div class="value">{metrics["evaluated_count"]}</div>
        </div>
        <div class="card">
          <div class="label">DART Event Pending Cases</div>
          <div class="ko-desc">DART 이벤트 평가 대기</div>
          <div class="value warning">{metrics["pending_count"]}</div>
        </div>
        <div class="card">
          <div class="label">DART Event Success Rate</div>
          <div class="ko-desc">DART 이벤트 성공률</div>
          <div class="value">{metrics["dart_success_rate"]}%</div>
        </div>
        <div class="card">
          <div class="label">Social Attention Rows</div>
          <div class="ko-desc">관심도 분석 행 수</div>
          <div class="value">{metrics["social_rows"]}</div>
        </div>
        <div class="card">
          <div class="label">High Attention Signals</div>
          <div class="ko-desc">높은 관심도 신호</div>
          <div class="value success">{metrics["high_attention_count"]}</div>
        </div>
        <div class="card">
          <div class="label">Risk Noise Signals</div>
          <div class="ko-desc">리스크성 노이즈 신호</div>
          <div class="value risk">{metrics["risk_noise_count"]}</div>
        </div>
        <div class="card">
          <div class="label">Market-Adjusted Rows</div>
          <div class="ko-desc">시장 조정 평가 행 수</div>
          <div class="value">{metrics["market_rows"]}</div>
        </div>
        <div class="card">
          <div class="label">Learned Rule Types</div>
          <div class="ko-desc">학습 대상 이벤트 유형</div>
          <div class="value">{metrics["learned_rule_count"]}</div>
        </div>
        <div class="card">
          <div class="label">Active Learned Rules</div>
          <div class="ko-desc">활성화된 학습 룰</div>
          <div class="value">{metrics["active_learned_rule_count"]}</div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="section-heading">
        <div>
          <h2>Dataset & Reports <span class="heading-ko">데이터셋 및 리포트</span></h2>
          <p class="section-subtitle">Latest generated at {metrics["generated_at"]}. Latest ML dataset rows: {metrics["total_events"]}. 최근 생성 시각과 ML 데이터셋 상태를 확인합니다.</p>
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
    print("Dashboard metric summary:")
    print(f"- cumulative price evaluated cases: {metrics['price_evaluated_count']}")
    print(f"- success count: {metrics['price_success_count']}")
    print(f"- failure count: {metrics['price_failure_count']}")
    print(f"- raw success rate: {metrics['price_success_rate']}%")
    print(f"- Wilson reliability score: {metrics['reliability_score']}")
    print(f"- benchmark-adjusted evaluated cases: {metrics['benchmark_evaluated_count']}")
    print(f"- benchmark-adjusted success rate: {format_metric_value(metrics['benchmark_success_rate'], '%')}")
    print(f"- rolling 7-day success rate: {format_metric_value(metrics['rolling_7d_success_rate'], '%')}")
    print(f"- rolling 30-day success rate: {format_metric_value(metrics['rolling_30d_success_rate'], '%')}")
    print(f"- diagnostics overall price success rate: {format_metric_value(metrics['diagnostics_overall_success_rate'], '%')}")
    print(f"- diagnostics Wilson reliability score: {format_metric_value(metrics['diagnostics_reliability_score'])}")
    print(f"- Top 10 success rate: {format_metric_value(metrics['top_10_success_rate'], '%')}")
    print(f"- Top 20 success rate: {format_metric_value(metrics['top_20_success_rate'], '%')}")
    print(f"- Top 50 success rate: {format_metric_value(metrics['top_50_success_rate'], '%')}")
    print(f"- Top 100 success rate: {format_metric_value(metrics['top_100_success_rate'], '%')}")
    print(f"- Top 10 evaluated cases: {format_metric_value(metrics['top_10_evaluated_count'])}")
    print(f"- Top 20 evaluated cases: {format_metric_value(metrics['top_20_evaluated_count'])}")
    print(f"- Top 50 evaluated cases: {format_metric_value(metrics['top_50_evaluated_count'])}")
    print(f"- Top 100 evaluated cases: {format_metric_value(metrics['top_100_evaluated_count'])}")
    print(f"- candidate pool today: {metrics['price_candidate_rows']}")
    print(f"- selected picks today: {metrics['selected_pick_rows']}")
    print(f"- Google News RSS item count: {metrics['news_provider_item_count']}")
    print(f"- news provider feature count: {metrics['news_provider_feature_count']}")


if __name__ == "__main__":
    main()
