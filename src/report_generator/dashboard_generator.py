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
    dedupe_evaluations,
    direction_series,
    normalize_stock_code,
    reliability_score_from_wilson,
    safe_percentage,
    success_series,
)
from src.storage.schema import RESULT_FAILURE, RESULT_PENDING, RESULT_SUCCESS


PROCESSED_DIR = Path("data/processed")
PREDICTIONS_DIR = Path("data/predictions")
DOCS_DIR = Path("docs")
OUTPUT_PATH = DOCS_DIR / "dashboard.html"
DIAGNOSTICS_OUTPUT_PATH = DOCS_DIR / "diagnostics.html"

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

    # signal_date first: it identifies when the trade signal actually occurred.
    # evaluation_date is when the row was last (re-)scored, which is
    # re-stamped to today on every pipeline run regardless of the signal's
    # age -- using it first collapses every rolling window onto the same
    # handful of recent evaluation runs instead of the signal's real date.
    date_source = pd.Series(pd.NaT, index=df.index, dtype="datetime64[ns]")
    for column in ["signal_date", "candidate_date", "evaluation_date", "evaluated_at"]:
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


def dedupe_price_evaluations(df: pd.DataFrame) -> pd.DataFrame:
    return dedupe_evaluations(df, key_column="dashboard_price_evaluation_key")


def summarize_direction_group(df: pd.DataFrame) -> dict:
    """
    Diagnostic-only success-rate breakdown for one candidate_direction (buy/avoid)
    slice of the deduplicated price evaluations. Does not change scoring.
    """
    if df.empty:
        return {
            "evaluated_count": 0,
            "success_count": 0,
            "failure_count": 0,
            "success_rate": None,
            "benchmark_evaluated_count": 0,
            "benchmark_success_count": 0,
            "benchmark_success_rate": None,
        }

    results = success_series(df, "success_close_t1")
    evaluated_mask = results.isin([RESULT_SUCCESS, RESULT_FAILURE])
    evaluated_count = int(evaluated_mask.sum())
    success_count = int((results == RESULT_SUCCESS).sum())
    failure_count = int((results == RESULT_FAILURE).sum())
    success_rate = round(safe_percentage(success_count, evaluated_count), 2) if evaluated_count else None

    benchmark_results = explicit_result_series(df, "success_excess_t1")
    benchmark_evaluated_mask = benchmark_results.isin([RESULT_SUCCESS, RESULT_FAILURE])
    benchmark_evaluated_count = int(benchmark_evaluated_mask.sum())
    benchmark_success_count = int((benchmark_results == RESULT_SUCCESS).sum())
    benchmark_success_rate = (
        round(safe_percentage(benchmark_success_count, benchmark_evaluated_count), 2)
        if benchmark_evaluated_count
        else None
    )

    return {
        "evaluated_count": evaluated_count,
        "success_count": success_count,
        "failure_count": failure_count,
        "success_rate": success_rate,
        "benchmark_evaluated_count": benchmark_evaluated_count,
        "benchmark_success_count": benchmark_success_count,
        "benchmark_success_rate": benchmark_success_rate,
    }


def format_metric_value(value, suffix=""):
    if value is None:
        return "Insufficient data / 데이터 부족"
    return f"{value}{suffix}"


def format_return_pct(value):
    value = safe_float(value, None)
    if value is None:
        return "N/A"
    return f"{value * 100:.2f}%"


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


def integrity_status_class(value):
    text = str(value or "").lower()
    if "clean" in text or "available" in text:
        return "badge-green"
    if "duplicate" in text or "missing" in text or "inverted" in text or "stale" in text:
        return "badge-red"
    if "weak" in text or "partial" in text:
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
    latest_price_candidate_rules_path = latest_file(PROCESSED_DIR, "price_candidate_learned_rules_*.csv")
    latest_price_candidate_rules = read_csv(latest_price_candidate_rules_path)
    latest_v2_performance_path = latest_file(PROCESSED_DIR, "v2_performance_summary_*.csv")
    latest_v2_performance = read_csv(latest_v2_performance_path)
    latest_v3_backtest_path = latest_file(PROCESSED_DIR, "v3_ranker_backtest_summary_*.csv")
    latest_v3_backtest = read_csv(latest_v3_backtest_path)
    latest_performance_audit_path = latest_file(PROCESSED_DIR, "performance_decision_audit_*.csv")
    latest_performance_audit = read_csv(latest_performance_audit_path)
    latest_price_candidates = read_csv(latest_file(PROCESSED_DIR, "price_based_candidates_*.csv"))
    latest_diagnostics_path = latest_file(PROCESSED_DIR, "price_signal_diagnostics_summary_*.csv")
    latest_diagnostics = read_csv(latest_diagnostics_path)
    latest_integrity_path = latest_file(PROCESSED_DIR, "evaluation_integrity_audit_summary_*.csv")
    latest_integrity = read_csv(latest_integrity_path)
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
    unique_price_eval = dedupe_price_evaluations(all_price_eval)

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

    price_results = success_series(unique_price_eval, "success_close_t1")
    if not price_results.empty:
        price_evaluated_count = int(price_results.isin(["success", "failure"]).sum())
        price_success_count = int((price_results == "success").sum())
        price_failure_count = int((price_results == "failure").sum())
        price_pending_count = int((price_results == "pending").sum())
        if price_evaluated_count > 0:
            price_success_rate = price_success_count / price_evaluated_count

    benchmark_results = explicit_result_series(unique_price_eval, "success_excess_t1")
    if not benchmark_results.empty:
        benchmark_evaluated_count = int(benchmark_results.isin([RESULT_SUCCESS, RESULT_FAILURE]).sum())
        benchmark_success_count = int((benchmark_results == RESULT_SUCCESS).sum())
        if benchmark_evaluated_count > 0:
            benchmark_success_rate = round(safe_percentage(benchmark_success_count, benchmark_evaluated_count), 2)

    rolling_7d = rolling_success_metrics(unique_price_eval, 7)
    rolling_30d = rolling_success_metrics(unique_price_eval, 30)
    rolling_7d_success_rate = rolling_7d["success_rate"]
    rolling_30d_success_rate = rolling_30d["success_rate"]
    rolling_7d_evaluated_count = rolling_7d["evaluated_count"]
    rolling_30d_evaluated_count = rolling_30d["evaluated_count"]

    if not unique_price_eval.empty:
        candidate_direction = direction_series(unique_price_eval)
        buy_eval = unique_price_eval[candidate_direction == "buy"]
        avoid_eval = unique_price_eval[candidate_direction == "avoid"]
    else:
        buy_eval = pd.DataFrame()
        avoid_eval = pd.DataFrame()
    buy_direction_summary = summarize_direction_group(buy_eval)
    avoid_direction_summary = summarize_direction_group(avoid_eval)

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
    integrity_total_rows = first_row_value(latest_integrity, "total_evaluation_rows", None)
    integrity_unique_keys = first_row_value(latest_integrity, "unique_evaluation_keys", None)
    integrity_duplicate_rows = first_row_value(latest_integrity, "duplicate_rows", None)
    integrity_duplicate_rate = first_row_value(latest_integrity, "duplicate_rate", None)
    integrity_v2_evaluated_count = first_row_value(latest_integrity, "v2_evaluated_count", v2_evaluated_count)
    integrity_v2_success_rate = first_row_value(latest_integrity, "v2_success_rate", None)
    integrity_benchmark_coverage = first_row_value(latest_integrity, "benchmark_adjusted_coverage_rate", None)
    integrity_benchmark_success_rate = first_row_value(latest_integrity, "benchmark_adjusted_success_rate", None)
    integrity_benchmark_evaluated = first_row_value(latest_integrity, "benchmark_adjusted_evaluated", benchmark_evaluated_count)
    integrity_benchmark_rows = first_row_value(latest_integrity, "benchmark_rows_available", None)
    benchmark_latest_date = first_row_value(latest_integrity, "benchmark_latest_date", "")
    price_signal_latest_date = first_row_value(latest_integrity, "price_signal_latest_date", "")
    integrity_duplicate_status = first_row_value(latest_integrity, "duplicate_status", "Insufficient data")
    integrity_benchmark_status = first_row_value(latest_integrity, "benchmark_status", "Insufficient data")
    integrity_ranking_status = first_row_value(latest_integrity, "ranking_status", ranking_diagnosis_en)

    price_candidate_rule_count = len(latest_price_candidate_rules)
    price_candidate_boost_rule_count = 0
    price_candidate_penalize_rule_count = 0
    price_candidate_watch_rule_count = 0
    suspicious_price_rule_count = 0
    top_suspicious_price_rule = "N/A"
    top_suspicious_price_rule_reason = "N/A"
    top_positive_price_rule = "N/A"
    top_negative_price_rule = "N/A"
    latest_price_rule_update_time = file_mtime(latest_price_candidate_rules_path)
    if not latest_price_candidate_rules.empty and "recommended_action" in latest_price_candidate_rules.columns:
        actions = latest_price_candidate_rules["recommended_action"].astype(str)
        price_candidate_boost_rule_count = int((actions == "boost").sum())
        price_candidate_penalize_rule_count = int((actions == "penalize").sum())
        price_candidate_watch_rule_count = int((actions == "watch").sum())
        if "suspicious_flag" in latest_price_candidate_rules.columns:
            suspicious_mask = latest_price_candidate_rules["suspicious_flag"].astype(str).str.lower().isin(["true", "1", "yes"])
            suspicious_price_rule_count = int(suspicious_mask.sum())
            suspicious_rules = latest_price_candidate_rules[suspicious_mask].copy()
            if not suspicious_rules.empty:
                if "lift_vs_baseline" in suspicious_rules.columns:
                    suspicious_rules["lift_vs_baseline"] = pd.to_numeric(
                        suspicious_rules["lift_vs_baseline"],
                        errors="coerce",
                    )
                    suspicious_rules = suspicious_rules.sort_values("lift_vs_baseline", ascending=False)
                top_suspicious = suspicious_rules.iloc[0]
                top_suspicious_price_rule = (
                    f"{top_suspicious.get('rule_group', '')}={top_suspicious.get('rule_value', '')}"
                )
                top_suspicious_price_rule_reason = str(top_suspicious.get("suspicious_reason", "N/A"))
        if "lift_vs_baseline" in latest_price_candidate_rules.columns:
            ranked_rules = latest_price_candidate_rules.copy()
            ranked_rules["lift_vs_baseline"] = pd.to_numeric(ranked_rules["lift_vs_baseline"], errors="coerce")
            ranked_rules = ranked_rules.dropna(subset=["lift_vs_baseline"])
            if not ranked_rules.empty:
                positive = ranked_rules.sort_values("lift_vs_baseline", ascending=False).iloc[0]
                negative = ranked_rules.sort_values("lift_vs_baseline", ascending=True).iloc[0]
                top_positive_price_rule = f"{positive.get('rule_group', '')}={positive.get('rule_value', '')} ({positive.get('lift_vs_baseline', '')}pp)"
                top_negative_price_rule = f"{negative.get('rule_group', '')}={negative.get('rule_value', '')} ({negative.get('lift_vs_baseline', '')}pp)"

    v2_monitor_evaluated = first_row_value(latest_v2_performance, "v2_evaluated_cases", 0)
    v2_monitor_raw_success_rate = first_row_value(latest_v2_performance, "v2_raw_success_rate", None)
    v2_monitor_benchmark_success_rate = first_row_value(
        latest_v2_performance,
        "v2_benchmark_adjusted_success_rate",
        None,
    )
    v2_monitor_benchmark_coverage_rate = first_row_value(latest_v2_performance, "v2_benchmark_coverage_rate", None)
    v2_monitor_selected_evaluated = first_row_value(latest_v2_performance, "v2_selected_pick_evaluated_cases", 0)
    v2_monitor_selected_success_rate = first_row_value(latest_v2_performance, "v2_selected_pick_success_rate", None)
    v2_monitor_non_selected_evaluated = first_row_value(latest_v2_performance, "v2_non_selected_evaluated_cases", 0)
    v2_monitor_non_selected_success_rate = first_row_value(latest_v2_performance, "v2_non_selected_success_rate", None)
    v2_monitor_top_10_success_rate = first_row_value(latest_v2_performance, "v2_top_10_success_rate", None)
    v2_monitor_top_20_success_rate = first_row_value(latest_v2_performance, "v2_top_20_success_rate", None)
    v2_monitor_top_10_evaluated = first_row_value(latest_v2_performance, "v2_top_10_evaluated_cases", 0)
    v2_monitor_top_20_evaluated = first_row_value(latest_v2_performance, "v2_top_20_evaluated_cases", 0)
    v2_monitor_diagnosis_en = first_row_value(latest_v2_performance, "v2_diagnosis_en", "Insufficient data")
    v2_monitor_diagnosis_ko = first_row_value(latest_v2_performance, "v2_diagnosis_ko", "데이터 부족")
    v2_monitor_benchmark_diagnosis_en = first_row_value(
        latest_v2_performance,
        "v2_benchmark_diagnosis_en",
        "Benchmark data unavailable",
    )
    v2_monitor_benchmark_diagnosis_ko = first_row_value(
        latest_v2_performance,
        "v2_benchmark_diagnosis_ko",
        "시장 기준 데이터 부족",
    )
    latest_v2_monitor_update_time = file_mtime(latest_v2_performance_path)
    v2_monitor_buy_evaluated = first_row_value(latest_v2_performance, "v2_buy_evaluated_cases", 0)
    v2_monitor_buy_success_rate = first_row_value(latest_v2_performance, "v2_buy_success_rate", None)
    v2_monitor_buy_avg_t1_return = first_row_value(latest_v2_performance, "v2_buy_avg_close_t1_return", None)
    v2_monitor_buy_avg_t3_return = first_row_value(latest_v2_performance, "v2_buy_avg_close_t3_return", None)
    v2_monitor_buy_avg_t5_return = first_row_value(latest_v2_performance, "v2_buy_avg_close_t5_return", None)
    v2_monitor_buy_benchmark_success_rate = first_row_value(latest_v2_performance, "v2_buy_benchmark_success_rate", None)
    v2_monitor_avoid_evaluated = first_row_value(latest_v2_performance, "v2_avoid_evaluated_cases", 0)
    v2_monitor_avoid_success_rate = first_row_value(latest_v2_performance, "v2_avoid_success_rate", None)
    v2_monitor_avoid_avg_t1_return = first_row_value(latest_v2_performance, "v2_avoid_avg_close_t1_return", None)
    v2_monitor_avoid_avg_t3_return = first_row_value(latest_v2_performance, "v2_avoid_avg_close_t3_return", None)
    v2_monitor_avoid_avg_t5_return = first_row_value(latest_v2_performance, "v2_avoid_avg_close_t5_return", None)
    v2_monitor_avoid_benchmark_success_rate = first_row_value(latest_v2_performance, "v2_avoid_benchmark_success_rate", None)

    v3_component_coverage_rate = first_row_value(latest_v3_backtest, "historical_component_coverage_rate", None)
    v3_has_enough_historical_data = first_row_value(latest_v3_backtest, "has_enough_historical_data", False)
    v3_coverage_note = first_row_value(latest_v3_backtest, "coverage_note", "insufficient historical component coverage")
    v3_overall_success_rate = first_row_value(latest_v3_backtest, "overall_success_rate", None)
    v3_current_selected_success_rate = first_row_value(
        latest_v3_backtest,
        "current_selected_group_success_rate",
        None,
    )
    v3_top_10_success_rate = first_row_value(latest_v3_backtest, "v3_top_10_success_rate", None)
    v3_top_20_success_rate = first_row_value(latest_v3_backtest, "v3_top_20_success_rate", None)
    v3_top_50_success_rate = first_row_value(latest_v3_backtest, "v3_top_50_success_rate", None)
    v3_top_10_evaluated_cases = first_row_value(latest_v3_backtest, "v3_top_10_evaluated_cases", 0)
    v3_top_20_evaluated_cases = first_row_value(latest_v3_backtest, "v3_top_20_evaluated_cases", 0)
    v3_top_50_evaluated_cases = first_row_value(latest_v3_backtest, "v3_top_50_evaluated_cases", 0)
    v3_top_20_benchmark_success_rate = first_row_value(
        latest_v3_backtest,
        "v3_top_20_benchmark_adjusted_success_rate",
        None,
    )
    latest_v3_backtest_update_time = file_mtime(latest_v3_backtest_path)

    news_provider_status = {}
    for provider_name in ["deepsearch_news", "google_news_rss", "gdelt", "naver_search"]:
        news_provider_status[provider_name] = {
            "status_en": None,
            "status_ko": "데이터 부족",
            "item_count": 0,
        }

    news_provider_item_count = len(latest_news_items)
    news_feature_count = len(latest_news_features)
    last_news_provider_update = file_mtime(latest_news_features_path) or file_mtime(latest_news_items_path)

    if not latest_news_status.empty and "source_provider" in latest_news_status.columns:
        for provider_name in news_provider_status:
            provider_rows = latest_news_status[
                latest_news_status["source_provider"].astype(str) == provider_name
            ]
            if provider_rows.empty:
                continue
            if "updated_at" in provider_rows.columns:
                last_news_provider_update = str(provider_rows.iloc[-1].get("updated_at", last_news_provider_update))
            item_total = int(pd.to_numeric(provider_rows.get("item_count", 0), errors="coerce").fillna(0).sum())
            statuses = provider_rows.get("status", pd.Series(dtype=str)).astype(str)
            if item_total > 0:
                status_en, status_ko = "Available", "수집 가능"
            elif statuses.str.contains("missing_credentials|api_hub_not_configured", regex=True).any():
                status_en, status_ko = "Optional", "선택 수집"
            elif statuses.eq("failed").any():
                status_en, status_ko = "Provider failed", "수집 실패"
            else:
                status_en, status_ko = "No items", "수집 항목 없음"
            news_provider_status[provider_name] = {
                "status_en": status_en,
                "status_ko": status_ko,
                "item_count": item_total,
            }

    if len(latest_naver_news) > 0 and not news_provider_status["naver_search"]["status_en"]:
        news_provider_status["naver_search"] = {
            "status_en": "Available",
            "status_ko": "수집 가능",
            "item_count": len(latest_naver_news),
        }

    provider_available_count = sum(
        1 for status in news_provider_status.values() if status["item_count"] > 0
    )
    if provider_available_count >= 2:
        news_coverage_en, news_coverage_ko, news_coverage_class = "Available", "정상 수집", "badge-green"
    elif provider_available_count == 1:
        news_coverage_en, news_coverage_ko, news_coverage_class = "Partial", "일부 수집", "badge-orange"
    else:
        news_coverage_en, news_coverage_ko, news_coverage_class = "Needs Review", "점검 필요", "badge-orange"

    news_rumor_noise_keyword_count = 0
    news_risk_keyword_count = 0
    if not latest_news_features.empty:
        if "rumor_noise_keyword_count" in latest_news_features.columns:
            news_rumor_noise_keyword_count = int(
                pd.to_numeric(latest_news_features["rumor_noise_keyword_count"], errors="coerce").fillna(0).sum()
            )
        if "risk_keyword_count" in latest_news_features.columns:
            news_risk_keyword_count = int(
                pd.to_numeric(latest_news_features["risk_keyword_count"], errors="coerce").fillna(0).sum()
            )

    market_noise_total = news_rumor_noise_keyword_count + news_risk_keyword_count
    if latest_news_features.empty:
        market_noise_en, market_noise_ko, market_noise_class = "Needs Review", "점검 필요", "badge-orange"
    elif market_noise_total >= 20:
        market_noise_en, market_noise_ko, market_noise_class = "Needs Review", "점검 필요", "badge-orange"
    elif market_noise_total > 0:
        market_noise_en, market_noise_ko, market_noise_class = "Partial", "일부 신호", "badge-orange"
    else:
        market_noise_en, market_noise_ko, market_noise_class = "Available", "안정적", "badge-green"

    naver_status_en = news_provider_status["naver_search"]["status_en"]
    naver_status_ko = news_provider_status["naver_search"]["status_ko"]
    google_status_en = news_provider_status["google_news_rss"]["status_en"]
    google_status_ko = news_provider_status["google_news_rss"]["status_ko"]
    deepsearch_status_en = news_provider_status["deepsearch_news"]["status_en"]
    deepsearch_status_ko = news_provider_status["deepsearch_news"]["status_ko"]
    gdelt_status_en = news_provider_status["gdelt"]["status_en"]
    gdelt_status_ko = news_provider_status["gdelt"]["status_ko"]
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
        "buy_evaluated_count": buy_direction_summary["evaluated_count"],
        "buy_success_count": buy_direction_summary["success_count"],
        "buy_success_rate": buy_direction_summary["success_rate"],
        "buy_benchmark_evaluated_count": buy_direction_summary["benchmark_evaluated_count"],
        "buy_benchmark_success_rate": buy_direction_summary["benchmark_success_rate"],
        "avoid_evaluated_count": avoid_direction_summary["evaluated_count"],
        "avoid_success_count": avoid_direction_summary["success_count"],
        "avoid_success_rate": avoid_direction_summary["success_rate"],
        "avoid_benchmark_evaluated_count": avoid_direction_summary["benchmark_evaluated_count"],
        "avoid_benchmark_success_rate": avoid_direction_summary["benchmark_success_rate"],
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
        "integrity_total_rows": integrity_total_rows,
        "integrity_unique_keys": integrity_unique_keys,
        "integrity_duplicate_rows": integrity_duplicate_rows,
        "integrity_duplicate_rate": integrity_duplicate_rate,
        "integrity_v2_evaluated_count": integrity_v2_evaluated_count,
        "integrity_v2_success_rate": integrity_v2_success_rate,
        "integrity_benchmark_coverage": integrity_benchmark_coverage,
        "integrity_benchmark_success_rate": integrity_benchmark_success_rate,
        "integrity_benchmark_evaluated": integrity_benchmark_evaluated,
        "integrity_benchmark_rows": integrity_benchmark_rows,
        "benchmark_latest_date": benchmark_latest_date,
        "price_signal_latest_date": price_signal_latest_date,
        "integrity_duplicate_status": integrity_duplicate_status,
        "integrity_benchmark_status": integrity_benchmark_status,
        "integrity_ranking_status": integrity_ranking_status,
        "price_candidate_rule_count": price_candidate_rule_count,
        "price_candidate_boost_rule_count": price_candidate_boost_rule_count,
        "price_candidate_penalize_rule_count": price_candidate_penalize_rule_count,
        "price_candidate_watch_rule_count": price_candidate_watch_rule_count,
        "suspicious_price_rule_count": suspicious_price_rule_count,
        "top_suspicious_price_rule": top_suspicious_price_rule,
        "top_suspicious_price_rule_reason": top_suspicious_price_rule_reason,
        "top_positive_price_rule": top_positive_price_rule,
        "top_negative_price_rule": top_negative_price_rule,
        "latest_price_rule_update_time": latest_price_rule_update_time,
        "v2_monitor_evaluated": v2_monitor_evaluated,
        "v2_monitor_raw_success_rate": v2_monitor_raw_success_rate,
        "v2_monitor_benchmark_success_rate": v2_monitor_benchmark_success_rate,
        "v2_monitor_benchmark_coverage_rate": v2_monitor_benchmark_coverage_rate,
        "v2_monitor_selected_evaluated": v2_monitor_selected_evaluated,
        "v2_monitor_selected_success_rate": v2_monitor_selected_success_rate,
        "v2_monitor_non_selected_evaluated": v2_monitor_non_selected_evaluated,
        "v2_monitor_non_selected_success_rate": v2_monitor_non_selected_success_rate,
        "v2_monitor_top_10_success_rate": v2_monitor_top_10_success_rate,
        "v2_monitor_top_20_success_rate": v2_monitor_top_20_success_rate,
        "v2_monitor_top_10_evaluated": v2_monitor_top_10_evaluated,
        "v2_monitor_top_20_evaluated": v2_monitor_top_20_evaluated,
        "v2_monitor_diagnosis_en": v2_monitor_diagnosis_en,
        "v2_monitor_diagnosis_ko": v2_monitor_diagnosis_ko,
        "v2_monitor_benchmark_diagnosis_en": v2_monitor_benchmark_diagnosis_en,
        "v2_monitor_benchmark_diagnosis_ko": v2_monitor_benchmark_diagnosis_ko,
        "latest_v2_monitor_update_time": latest_v2_monitor_update_time,
        "v2_monitor_buy_evaluated": v2_monitor_buy_evaluated,
        "v2_monitor_buy_success_rate": v2_monitor_buy_success_rate,
        "v2_monitor_buy_avg_t1_return": v2_monitor_buy_avg_t1_return,
        "v2_monitor_buy_avg_t3_return": v2_monitor_buy_avg_t3_return,
        "v2_monitor_buy_avg_t5_return": v2_monitor_buy_avg_t5_return,
        "v2_monitor_buy_benchmark_success_rate": v2_monitor_buy_benchmark_success_rate,
        "v2_monitor_avoid_evaluated": v2_monitor_avoid_evaluated,
        "v2_monitor_avoid_success_rate": v2_monitor_avoid_success_rate,
        "v2_monitor_avoid_avg_t1_return": v2_monitor_avoid_avg_t1_return,
        "v2_monitor_avoid_avg_t3_return": v2_monitor_avoid_avg_t3_return,
        "v2_monitor_avoid_avg_t5_return": v2_monitor_avoid_avg_t5_return,
        "v2_monitor_avoid_benchmark_success_rate": v2_monitor_avoid_benchmark_success_rate,
        "v3_component_coverage_rate": v3_component_coverage_rate,
        "v3_has_enough_historical_data": v3_has_enough_historical_data,
        "v3_coverage_note": v3_coverage_note,
        "v3_overall_success_rate": v3_overall_success_rate,
        "v3_current_selected_success_rate": v3_current_selected_success_rate,
        "v3_top_10_success_rate": v3_top_10_success_rate,
        "v3_top_20_success_rate": v3_top_20_success_rate,
        "v3_top_50_success_rate": v3_top_50_success_rate,
        "v3_top_10_evaluated_cases": v3_top_10_evaluated_cases,
        "v3_top_20_evaluated_cases": v3_top_20_evaluated_cases,
        "v3_top_50_evaluated_cases": v3_top_50_evaluated_cases,
        "v3_top_20_benchmark_success_rate": v3_top_20_benchmark_success_rate,
        "latest_v3_backtest_update_time": latest_v3_backtest_update_time,
        "performance_audit_raw_success_rate": first_row_value(latest_performance_audit, "raw_success_rate", None),
        "performance_audit_selected_raw_success_rate": first_row_value(latest_performance_audit, "selected_raw_success_rate", None),
        "performance_audit_non_selected_raw_success_rate": first_row_value(latest_performance_audit, "non_selected_raw_success_rate", None),
        "performance_audit_benchmark_success_rate": first_row_value(latest_performance_audit, "benchmark_adjusted_success_rate", None),
        "performance_audit_selected_benchmark_success_rate": first_row_value(latest_performance_audit, "selected_benchmark_adjusted_success_rate", None),
        "performance_audit_non_selected_benchmark_success_rate": first_row_value(latest_performance_audit, "non_selected_benchmark_adjusted_success_rate", None),
        "performance_audit_diagnosis_label": first_row_value(latest_performance_audit, "diagnosis_label", "not_available"),
        "performance_audit_public_metric_recommendation": first_row_value(latest_performance_audit, "public_metric_recommendation", "not_available"),
        "performance_audit_candidate_count_findings": first_row_value(latest_performance_audit, "candidate_count_bucket_findings", "N/A"),
        "naver_status_en": naver_status_en,
        "naver_status_ko": naver_status_ko,
        "google_status_en": google_status_en,
        "google_status_ko": google_status_ko,
        "deepsearch_status_en": deepsearch_status_en,
        "deepsearch_status_ko": deepsearch_status_ko,
        "gdelt_status_en": gdelt_status_en,
        "gdelt_status_ko": gdelt_status_ko,
        "snacks_status_en": snacks_status_en,
        "snacks_status_ko": snacks_status_ko,
        "news_provider_available_count": provider_available_count,
        "news_coverage_en": news_coverage_en,
        "news_coverage_ko": news_coverage_ko,
        "news_coverage_class": news_coverage_class,
        "market_noise_en": market_noise_en,
        "market_noise_ko": market_noise_ko,
        "market_noise_class": market_noise_class,
        "news_rumor_noise_keyword_count": news_rumor_noise_keyword_count,
        "news_risk_keyword_count": news_risk_keyword_count,
        "deepsearch_item_count": news_provider_status["deepsearch_news"]["item_count"],
        "google_item_count": news_provider_status["google_news_rss"]["item_count"],
        "gdelt_item_count": news_provider_status["gdelt"]["item_count"],
        "naver_item_count": news_provider_status["naver_search"]["item_count"],
        "last_news_provider_update": last_news_provider_update,
        "news_provider_item_count": news_provider_item_count,
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


def build_diagnostics_html(metrics, stock_data):
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
    v2_monitor_class = ranking_status_class(metrics.get("v2_monitor_diagnosis_en"))
    v2_benchmark_class = integrity_status_class(metrics.get("v2_monitor_benchmark_diagnosis_en"))
    v3_data_class = (
        "badge-green"
        if str(metrics.get("v3_has_enough_historical_data")).lower() in ["true", "1", "yes"]
        else "badge-orange"
    )
    suspicious_rule_class = "badge-red" if safe_float(metrics.get("suspicious_price_rule_count", 0)) > 0 else "badge-green"
    duplicate_class = integrity_status_class(metrics.get("integrity_duplicate_status"))
    benchmark_integrity_class = integrity_status_class(metrics.get("integrity_benchmark_status"))
    ranking_integrity_class = integrity_status_class(metrics.get("integrity_ranking_status"))
    benchmark_helper = ""
    if metrics.get("benchmark_success_rate") is None:
        benchmark_helper = "\n".join([
            '<div class="muted-helper">',
            '            Benchmark evaluation will appear after benchmark-matched candidate results are available.<br>',
            '            시장 기준 평가 데이터가 쌓이면 표시됩니다.',
            '          </div>',
        ])
    benchmark_warning = ""
    if metrics.get("v2_monitor_benchmark_coverage_rate") is None or safe_float(metrics.get("v2_monitor_benchmark_coverage_rate")) < 30:
        benchmark_warning = (
            "Benchmark coverage is still below 30%, so market-relative v2 conclusions remain provisional.<br>"
            "시장 기준 커버리지가 아직 30% 미만이므로 v2 시장 대비 판단은 임시 진단입니다."
        )
    buy_avg_t1_return_display = format_return_pct(metrics.get("v2_monitor_buy_avg_t1_return"))
    buy_avg_t3_return_display = format_return_pct(metrics.get("v2_monitor_buy_avg_t3_return"))
    buy_avg_t5_return_display = format_return_pct(metrics.get("v2_monitor_buy_avg_t5_return"))
    avoid_avg_t1_return_display = format_return_pct(metrics.get("v2_monitor_avoid_avg_t1_return"))
    avoid_avg_t3_return_display = format_return_pct(metrics.get("v2_monitor_avoid_avg_t3_return"))
    avoid_avg_t5_return_display = format_return_pct(metrics.get("v2_monitor_avoid_avg_t5_return"))

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
          <h2>V3 Ranker Backtest <span class="heading-ko">v3 실험 랭커 백테스트</span></h2>
          <p class="section-subtitle">This simulates the experimental v3_stability_ranker on already-evaluated candidates. It does not alter selected picks or public claims. 이미 평가된 후보를 v3 기준으로 재정렬하는 내부 진단입니다.</p>
        </div>
      </div>
      <div class="kpi-grid">
        <div class="card kpi-card">
          <div class="label">Historical Component Coverage</div>
          <div class="ko-desc">과거 컴포넌트 커버리지</div>
          {render_kpi_value(metrics["v3_component_coverage_rate"], "%")}
          <div class="muted-helper">{metrics["v3_coverage_note"]}</div>
        </div>
        <div class="card kpi-card">
          <div class="label">V3 Top 10 Success Rate</div>
          <div class="ko-desc">v3 일별 Top 10 성공률</div>
          {render_kpi_value(metrics["v3_top_10_success_rate"], "%")}
          <div class="muted-helper">Evaluated cases: {format_metric_value(metrics["v3_top_10_evaluated_cases"])}<br>평가 완료: {format_metric_value(metrics["v3_top_10_evaluated_cases"])}</div>
        </div>
        <div class="card kpi-card">
          <div class="label">V3 Top 20 Success Rate</div>
          <div class="ko-desc">v3 일별 Top 20 성공률</div>
          {render_kpi_value(metrics["v3_top_20_success_rate"], "%")}
          <div class="muted-helper">Evaluated cases: {format_metric_value(metrics["v3_top_20_evaluated_cases"])}<br>평가 완료: {format_metric_value(metrics["v3_top_20_evaluated_cases"])}</div>
        </div>
        <div class="card kpi-card">
          <div class="label">V3 Top 50 Success Rate</div>
          <div class="ko-desc">v3 일별 Top 50 성공률</div>
          {render_kpi_value(metrics["v3_top_50_success_rate"], "%")}
          <div class="muted-helper">Evaluated cases: {format_metric_value(metrics["v3_top_50_evaluated_cases"])}<br>평가 완료: {format_metric_value(metrics["v3_top_50_evaluated_cases"])}</div>
        </div>
        <div class="card kpi-card">
          <div class="label">V3 Top 20 Benchmark-Adjusted Rate</div>
          <div class="ko-desc">v3 Top 20 시장 대비 성공률</div>
          {render_kpi_value(metrics["v3_top_20_benchmark_success_rate"], "%")}
        </div>
        <div class="card kpi-card">
          <div class="label">V3 Data Status</div>
          <div class="ko-desc">v3 데이터 상태</div>
          <div class="kpi-value-small">{render_status_pill(metrics["v3_coverage_note"], "과거 컴포넌트 상태", v3_data_class)}</div>
        </div>
        <div class="card kpi-card">
          <div class="label">Current Selected Group</div>
          <div class="ko-desc">현재 선별군 성공률</div>
          {render_kpi_value(metrics["v3_current_selected_success_rate"], "%")}
        </div>
        <div class="card kpi-card">
          <div class="label">Latest V3 Backtest Update</div>
          <div class="ko-desc">최근 v3 백테스트 갱신</div>
          <div class="kpi-value-small">{render_status_pill(metrics["latest_v3_backtest_update_time"], "최근 갱신", "badge-gray")}</div>
        </div>
      </div>
      <div class="note section">
        V3 is an internal experiment only. Public recommendation quality remains based on conservative cumulative price-candidate evaluation.<br>
        v3는 내부 실험 전용입니다. 공개 추천 품질 평가는 보수적인 누적 가격 후보 평가를 기준으로 합니다.
      </div>
    </section>

    <section class="section">
      <div class="section-heading">
        <div>
          <h2>V2 Performance Monitor <span class="heading-ko">v2 성과 추적</span></h2>
          <p class="section-subtitle">This layer monitors only v2_conservative_ranker after candidate-level deduplication. 후보 생성과 점수 산식은 변경하지 않고 v2 성과만 추적합니다.</p>
        </div>
      </div>
      <div class="kpi-grid">
        <div class="card kpi-card">
          <div class="label">V2 Diagnosis</div>
          <div class="ko-desc">v2 진단</div>
          <div class="kpi-value-small">{render_status_pill(metrics["v2_monitor_diagnosis_en"], metrics["v2_monitor_diagnosis_ko"], v2_monitor_class)}</div>
        </div>
        <div class="card kpi-card">
          <div class="label">V2 Evaluated Cases</div>
          <div class="ko-desc">v2 평가 완료</div>
          {render_kpi_value(metrics["v2_monitor_evaluated"])}
        </div>
        <div class="card kpi-card">
          <div class="label">V2 Raw Success Rate</div>
          <div class="ko-desc">v2 원시 성공률</div>
          {render_kpi_value(metrics["v2_monitor_raw_success_rate"], "%")}
        </div>
        <div class="card kpi-card">
          <div class="label">V2 Benchmark-Adjusted Success Rate</div>
          <div class="ko-desc">v2 시장 대비 성공률</div>
          {render_kpi_value(metrics["v2_monitor_benchmark_success_rate"], "%")}
          <div class="muted-helper">Coverage: {format_metric_value(metrics["v2_monitor_benchmark_coverage_rate"], "%")}<br>커버리지: {format_metric_value(metrics["v2_monitor_benchmark_coverage_rate"], "%")}</div>
        </div>
        <div class="card kpi-card">
          <div class="label">Selected Pick Success Rate</div>
          <div class="ko-desc">선별 후보 성공률</div>
          {render_kpi_value(metrics["v2_monitor_selected_success_rate"], "%")}
          <div class="muted-helper">Evaluated cases: {format_metric_value(metrics["v2_monitor_selected_evaluated"])}<br>평가 완료: {format_metric_value(metrics["v2_monitor_selected_evaluated"])}</div>
        </div>
        <div class="card kpi-card">
          <div class="label">Non-Selected Success Rate</div>
          <div class="ko-desc">비선별 후보 성공률</div>
          {render_kpi_value(metrics["v2_monitor_non_selected_success_rate"], "%")}
          <div class="muted-helper">Evaluated cases: {format_metric_value(metrics["v2_monitor_non_selected_evaluated"])}<br>평가 완료: {format_metric_value(metrics["v2_monitor_non_selected_evaluated"])}</div>
        </div>
        <div class="card kpi-card">
          <div class="label">V2 Top 10 Success Rate</div>
          <div class="ko-desc">v2 일별 Top 10 성공률</div>
          {render_kpi_value(metrics["v2_monitor_top_10_success_rate"], "%")}
          <div class="muted-helper">Evaluated cases: {format_metric_value(metrics["v2_monitor_top_10_evaluated"])}<br>평가 완료: {format_metric_value(metrics["v2_monitor_top_10_evaluated"])}</div>
        </div>
        <div class="card kpi-card">
          <div class="label">V2 Top 20 Success Rate</div>
          <div class="ko-desc">v2 일별 Top 20 성공률</div>
          {render_kpi_value(metrics["v2_monitor_top_20_success_rate"], "%")}
          <div class="muted-helper">Evaluated cases: {format_metric_value(metrics["v2_monitor_top_20_evaluated"])}<br>평가 완료: {format_metric_value(metrics["v2_monitor_top_20_evaluated"])}</div>
        </div>
        <div class="card kpi-card">
          <div class="label">Benchmark Coverage Warning</div>
          <div class="ko-desc">시장 기준 커버리지 경고</div>
          <div class="kpi-value-small">{render_status_pill(metrics["v2_monitor_benchmark_diagnosis_en"], metrics["v2_monitor_benchmark_diagnosis_ko"], v2_benchmark_class)}</div>
        </div>
        <div class="card kpi-card">
          <div class="label">Latest V2 Monitor Update</div>
          <div class="ko-desc">최근 v2 모니터 갱신</div>
          <div class="kpi-value-small">{render_status_pill(metrics["latest_v2_monitor_update_time"], "최근 갱신", "badge-gray")}</div>
        </div>
      </div>
      <div class="note section">
        {benchmark_warning or "V2 monitoring should be judged over several new trading days, not a single run.<br>v2 성과는 단일 실행이 아니라 며칠 이상의 신규 거래일 누적으로 판단해야 합니다."}
      </div>
    </section>

    <section class="section">
      <div class="section-heading">
        <div>
          <h2>Evaluation Integrity <span class="heading-ko">평가 무결성</span></h2>
          <p class="section-subtitle">This audit checks duplicate cumulative evaluation rows, v2-only performance, benchmark coverage, and learned-rule activation. 누적 평가 중복, v2 전용 성과, 시장 대비 평가 커버리지, 학습 규칙 활성화를 점검합니다.</p>
        </div>
      </div>
      <div class="kpi-grid">
        <div class="card kpi-card">
          <div class="label">Evaluation Status</div>
          <div class="ko-desc">평가 상태</div>
          <div class="kpi-value-small">{render_status_pill(metrics["integrity_duplicate_status"], "중복 가능성" if str(metrics["integrity_duplicate_status"]).lower().find("duplicate") >= 0 else "평가 정상", duplicate_class)}</div>
        </div>
        <div class="card kpi-card">
          <div class="label">Total Evaluation Rows</div>
          <div class="ko-desc">전체 평가 행 수</div>
          {render_kpi_value(metrics["integrity_total_rows"])}
        </div>
        <div class="card kpi-card">
          <div class="label">Unique Evaluation Keys</div>
          <div class="ko-desc">고유 평가 키</div>
          {render_kpi_value(metrics["integrity_unique_keys"])}
        </div>
        <div class="card kpi-card">
          <div class="label">Duplicate Rows</div>
          <div class="ko-desc">중복 행 수</div>
          {render_kpi_value(metrics["integrity_duplicate_rows"])}
          <div class="muted-helper">Duplicate rate: {format_metric_value(metrics["integrity_duplicate_rate"], "%")}<br>중복률: {format_metric_value(metrics["integrity_duplicate_rate"], "%")}</div>
        </div>
        <div class="card kpi-card">
          <div class="label">V2 Evaluated Cases</div>
          <div class="ko-desc">v2 평가 완료</div>
          {render_kpi_value(metrics["integrity_v2_evaluated_count"])}
          <div class="muted-helper">V2 success rate: {format_metric_value(metrics["integrity_v2_success_rate"], "%")}<br>v2 성공률: {format_metric_value(metrics["integrity_v2_success_rate"], "%")}</div>
        </div>
        <div class="card kpi-card">
          <div class="label">Benchmark Coverage</div>
          <div class="ko-desc">시장 대비 평가 커버리지</div>
          {render_kpi_value(metrics["integrity_benchmark_coverage"], "%")}
          <div class="kpi-value-small">{render_status_pill(metrics["integrity_benchmark_status"], "시장 대비 평가 누락" if str(metrics["integrity_benchmark_status"]).lower().find("missing") >= 0 else "시장 대비 평가 가능", benchmark_integrity_class)}</div>
        </div>
        <div class="card kpi-card">
          <div class="label">Ranking Integrity</div>
          <div class="ko-desc">랭킹 무결성</div>
          <div class="kpi-value-small">{render_status_pill(metrics["integrity_ranking_status"], "랭킹 역방향" if str(metrics["integrity_ranking_status"]).lower().find("inverted") >= 0 else "랭킹 점검", ranking_integrity_class)}</div>
        </div>
        <div class="card kpi-card">
          <div class="label">Active Learned Rules</div>
          <div class="ko-desc">활성 학습 규칙</div>
          {render_kpi_value(metrics["active_learned_rule_count"])}
        </div>
      </div>
    </section>

    <section class="section">
      <div class="section-heading">
        <div>
          <h2>Benchmark Coverage <span class="heading-ko">시장 기준 커버리지</span></h2>
          <p class="section-subtitle">Benchmark-adjusted evaluation compares price candidates against KOSPI/KOSDAQ, using KOSPI as a fallback when market classification is missing. 시장 기준 평가는 KOSPI/KOSDAQ 대비 초과수익을 계산하며, 분류가 없으면 KOSPI를 기본값으로 사용합니다.</p>
        </div>
      </div>
      <div class="kpi-grid">
        <div class="card kpi-card">
          <div class="label">Benchmark Status</div>
          <div class="ko-desc">시장 기준 상태</div>
          <div class="kpi-value-small">{render_status_pill(metrics["integrity_benchmark_status"], "시장 기준 상태", benchmark_integrity_class)}</div>
        </div>
        <div class="card kpi-card">
          <div class="label">Benchmark Latest Date</div>
          <div class="ko-desc">시장 지수 최신일</div>
          <div class="kpi-value-small">{render_status_pill(metrics["benchmark_latest_date"], "시장 지수 최신일", "badge-gray")}</div>
        </div>
        <div class="card kpi-card">
          <div class="label">Price Signal Latest Date</div>
          <div class="ko-desc">가격 신호 최신일</div>
          <div class="kpi-value-small">{render_status_pill(metrics["price_signal_latest_date"], "가격 신호 최신일", "badge-gray")}</div>
        </div>
        <div class="card kpi-card">
          <div class="label">Benchmark Rows Available</div>
          <div class="ko-desc">시장 지수 행 수</div>
          {render_kpi_value(metrics["integrity_benchmark_rows"])}
        </div>
        <div class="card kpi-card">
          <div class="label">Benchmark-Adjusted Evaluated Cases</div>
          <div class="ko-desc">시장 대비 평가 완료</div>
          {render_kpi_value(metrics["integrity_benchmark_evaluated"])}
        </div>
        <div class="card kpi-card">
          <div class="label">Benchmark Coverage Rate</div>
          <div class="ko-desc">시장 대비 커버리지</div>
          {render_kpi_value(metrics["integrity_benchmark_coverage"], "%")}
          <div class="muted-helper">Benchmark-adjusted success rate: {format_metric_value(metrics["integrity_benchmark_success_rate"], "%")}<br>시장 대비 성공률: {format_metric_value(metrics["integrity_benchmark_success_rate"], "%")}</div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="section-heading">
        <div>
          <h2>Price Candidate Learned Rules <span class="heading-ko">가격 후보 학습 룰</span></h2>
          <p class="section-subtitle">These rules summarize deduped KIS price-candidate outcomes by explainable score and penalty buckets. 점수 산식은 변경하지 않고, 설명 가능한 가격 후보 그룹별 성과만 진단합니다.</p>
        </div>
      </div>
      <div class="kpi-grid">
        <div class="card kpi-card">
          <div class="label">Rule Rows</div>
          <div class="ko-desc">학습 룰 행 수</div>
          {render_kpi_value(metrics["price_candidate_rule_count"])}
        </div>
        <div class="card kpi-card">
          <div class="label">Active Boost Rules</div>
          <div class="ko-desc">상향 후보 룰</div>
          {render_kpi_value(metrics["price_candidate_boost_rule_count"])}
        </div>
        <div class="card kpi-card">
          <div class="label">Active Penalize Rules</div>
          <div class="ko-desc">하향 후보 룰</div>
          {render_kpi_value(metrics["price_candidate_penalize_rule_count"])}
        </div>
        <div class="card kpi-card">
          <div class="label">Watch Rules</div>
          <div class="ko-desc">관찰 룰</div>
          {render_kpi_value(metrics["price_candidate_watch_rule_count"])}
        </div>
        <div class="card kpi-card">
          <div class="label">Top Positive Rule</div>
          <div class="ko-desc">상위 긍정 룰</div>
          <div class="muted-helper">{metrics["top_positive_price_rule"]}</div>
        </div>
        <div class="card kpi-card">
          <div class="label">Top Negative Rule</div>
          <div class="ko-desc">상위 부정 룰</div>
          <div class="muted-helper">{metrics["top_negative_price_rule"]}</div>
        </div>
        <div class="card kpi-card">
          <div class="label">Latest Rule Update</div>
          <div class="ko-desc">최근 룰 갱신</div>
          <div class="kpi-value-small">{render_status_pill(metrics["latest_price_rule_update_time"], "최근 룰 갱신", "badge-gray")}</div>
        </div>
      </div>
      <div class="note section">
        Suspicious rules are diagnostic only and are not applied to scoring.<br>
        의심 룰은 진단용이며 점수 산식에 자동 반영하지 않습니다.
      </div>
    </section>

    <section class="section">
      <div class="section-heading">
        <div>
          <h2>Suspicious Learned Rules <span class="heading-ko">의심 학습 룰</span></h2>
          <p class="section-subtitle">These flags catch risky-looking learned rules before anyone treats them as score logic. 위험해 보이는 학습 룰을 점수 산식으로 오해하지 않도록 따로 표시합니다.</p>
        </div>
      </div>
      <div class="signal-grid">
        <div class="card">
          <div class="label">Suspicious Rule Count</div>
          <div class="ko-desc">의심 룰 수</div>
          {render_kpi_value(metrics["suspicious_price_rule_count"])}
        </div>
        <div class="card">
          <div class="label">Top Suspicious Rule</div>
          <div class="ko-desc">대표 의심 룰</div>
          <div class="kpi-value-small">{render_status_pill(metrics["top_suspicious_price_rule"], "대표 의심 룰", suspicious_rule_class)}</div>
        </div>
        <div class="card">
          <div class="label">Suspicious Reason</div>
          <div class="ko-desc">의심 사유</div>
          <div class="muted-helper">{metrics["top_suspicious_price_rule_reason"]}</div>
        </div>
      </div>
      <div class="note section">
        Suspicious rules are diagnostic only and are not applied to scoring.<br>
        의심 룰은 진단용이며 점수 산식에 자동 반영하지 않습니다.
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
          <h2>Directional Breakdown <span class="heading-ko">방향별 성과 (매수형 vs 회피형)</span></h2>
          <p class="section-subtitle">v2_conservative_ranker only, split by expected direction (expected_positive()). Diagnostic only; does not change scoring. v2_conservative_ranker 기준으로 예상 방향(expected_positive())별 성과를 나눠 봅니다. 진단 전용이며 점수 산식에는 반영하지 않습니다.</p>
        </div>
      </div>
      <div class="kpi-grid">
        <div class="card kpi-card primary">
          <div class="label">Buy-Type Success Rate</div>
          <div class="ko-desc">매수형 성공률</div>
          {render_kpi_value(metrics["v2_monitor_buy_success_rate"], "%")}
          <div class="muted-helper">Evaluated cases: {format_metric_value(metrics["v2_monitor_buy_evaluated"])}<br>평가 완료: {format_metric_value(metrics["v2_monitor_buy_evaluated"])}</div>
        </div>
        <div class="card kpi-card">
          <div class="label">Buy-Type Avg T1/T3/T5 Return</div>
          <div class="ko-desc">매수형 평균 T1/T3/T5 수익률</div>
          <div class="muted-helper">T1: {buy_avg_t1_return_display} · T3: {buy_avg_t3_return_display} · T5: {buy_avg_t5_return_display}</div>
        </div>
        <div class="card kpi-card">
          <div class="label">Buy-Type Benchmark-Adjusted Success Rate</div>
          <div class="ko-desc">매수형 시장 대비 성공률</div>
          {render_kpi_value(metrics["v2_monitor_buy_benchmark_success_rate"], "%")}
        </div>
        <div class="card kpi-card primary">
          <div class="label">Avoid-Type Success Rate</div>
          <div class="ko-desc">회피형 성공률</div>
          {render_kpi_value(metrics["v2_monitor_avoid_success_rate"], "%")}
          <div class="muted-helper">Evaluated cases: {format_metric_value(metrics["v2_monitor_avoid_evaluated"])}<br>평가 완료: {format_metric_value(metrics["v2_monitor_avoid_evaluated"])}</div>
        </div>
        <div class="card kpi-card">
          <div class="label">Avoid-Type Avg T1/T3/T5 Return</div>
          <div class="ko-desc">회피형 평균 T1/T3/T5 수익률</div>
          <div class="muted-helper">T1: {avoid_avg_t1_return_display} · T3: {avoid_avg_t3_return_display} · T5: {avoid_avg_t5_return_display}</div>
        </div>
        <div class="card kpi-card">
          <div class="label">Avoid-Type Benchmark-Adjusted Success Rate</div>
          <div class="ko-desc">회피형 시장 대비 성공률</div>
          {render_kpi_value(metrics["v2_monitor_avoid_benchmark_success_rate"], "%")}
        </div>
      </div>
      <div class="note section">
        Buy-type sample sizes are typically much smaller than avoid-type, so buy-type conclusions should be treated as preliminary.<br>
        매수형 표본 수는 회피형보다 훨씬 적은 경우가 많으므로, 매수형 결론은 잠정적으로 해석해야 합니다.
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
          <div class="label">DeepSearch Status</div>
          <div class="ko-desc">DeepSearch 뉴스 상태</div>
          <div class="kpi-value-small">{render_status_pill(metrics["deepsearch_status_en"], metrics["deepsearch_status_ko"])}</div>
          <div class="muted-helper">Items: {metrics["deepsearch_item_count"]}</div>
        </div>
        <div class="card">
          <div class="label">Google News RSS Status</div>
          <div class="ko-desc">Google News RSS 상태</div>
          <div class="kpi-value-small">{render_status_pill(metrics["google_status_en"], metrics["google_status_ko"])}</div>
          <div class="muted-helper">Items: {metrics["google_item_count"]}</div>
        </div>
        <div class="card">
          <div class="label">GDELT Status</div>
          <div class="ko-desc">GDELT 뉴스 상태</div>
          <div class="kpi-value-small">{render_status_pill(metrics["gdelt_status_en"], metrics["gdelt_status_ko"])}</div>
          <div class="muted-helper">Items: {metrics["gdelt_item_count"]}</div>
        </div>
        <div class="card">
          <div class="label">Naver Status</div>
          <div class="ko-desc">네이버 뉴스 상태</div>
          <div class="kpi-value-small">{render_status_pill(metrics["naver_status_en"], metrics["naver_status_ko"])}</div>
          <div class="muted-helper">Items: {metrics["naver_item_count"]}</div>
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
        <div class="card">
          <div class="label">Rumor / Noise Keywords</div>
          <div class="ko-desc">루머/노이즈 키워드</div>
          <div class="value warning">{metrics["news_rumor_noise_keyword_count"]}</div>
        </div>
        <div class="card">
          <div class="label">Risk Keywords</div>
          <div class="ko-desc">리스크 키워드</div>
          <div class="value risk">{metrics["news_risk_keyword_count"]}</div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="section-heading">
        <div>
          <h2>Performance Decision Audit <span class="heading-ko">성과 판단 감사</span></h2>
          <p class="section-subtitle">Internal guardrail before any ranking formula change. 점수 산식 변경 전 내부 판단 근거입니다.</p>
        </div>
      </div>
      <div class="signal-grid">
        <div class="card">
          <div class="label">Raw Success Rate</div>
          <div class="ko-desc">단순 성공률</div>
          {render_kpi_value(metrics["performance_audit_raw_success_rate"], "%")}
        </div>
        <div class="card">
          <div class="label">Benchmark-Adjusted Success Rate</div>
          <div class="ko-desc">시장 대비 성공률</div>
          {render_kpi_value(metrics["performance_audit_benchmark_success_rate"], "%")}
        </div>
        <div class="card">
          <div class="label">Selected Raw Success Rate</div>
          <div class="ko-desc">선별 후보 단순 성공률</div>
          {render_kpi_value(metrics["performance_audit_selected_raw_success_rate"], "%")}
        </div>
        <div class="card">
          <div class="label">Non-Selected Raw Success Rate</div>
          <div class="ko-desc">비선별 후보 단순 성공률</div>
          {render_kpi_value(metrics["performance_audit_non_selected_raw_success_rate"], "%")}
        </div>
        <div class="card">
          <div class="label">Diagnosis Label</div>
          <div class="ko-desc">진단 라벨</div>
          <div class="kpi-value-small">{render_status_pill(metrics["performance_audit_diagnosis_label"], "내부 진단", "badge-gray")}</div>
        </div>
        <div class="card">
          <div class="label">Public Metric Recommendation</div>
          <div class="ko-desc">공개 지표 권장 방향</div>
          <div class="kpi-value-small">{render_status_pill(metrics["performance_audit_public_metric_recommendation"], "표시 권장", "badge-gray")}</div>
        </div>
      </div>
      <div class="note section">
        Candidate count bucket findings: {metrics["performance_audit_candidate_count_findings"]}<br>
        후보 수 구간별 내부 진단입니다. 후보 생성이나 점수 산식은 변경하지 않습니다.
      </div>
    </section>

    <section class="section">
      <div class="section-heading">
        <div>
          <h2>Supplementary Signals <span class="heading-ko">보조 신호</span></h2>
          <p class="section-subtitle">DART, news, Snacks, social attention, and DART learned rules provide context around the primary price loop. DART, 뉴스, Snacks, 관심도 분석과 DART 학습 룰은 가격 기반 학습을 보조합니다.</p>
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
          <div class="label">DART Learned Rule Types</div>
          <div class="ko-desc">DART 학습 대상 이벤트 유형</div>
          <div class="value">{metrics["learned_rule_count"]}</div>
        </div>
        <div class="card">
          <div class="label">Active DART Learned Rules</div>
          <div class="ko-desc">활성 DART 학습 룰</div>
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


def simple_status(value_en, value_ko, css_class="badge-gray"):
    return render_status_pill(value_en, value_ko, css_class)


def quality_label_from_rate(rate, strong_threshold=55, promising_threshold=50):
    if rate is None:
        return "Needs Improvement", "개선 필요", "badge-orange"
    rate = safe_float(rate)
    if rate >= strong_threshold:
        return "Strong", "강함", "badge-green"
    if rate >= promising_threshold:
        return "Promising", "가능성 있음", "badge-orange"
    if rate >= 45:
        return "Mixed", "혼재", "badge-orange"
    return "Needs Improvement", "개선 필요", "badge-red"


def data_status_label(metrics):
    duplicate_rate = safe_float(metrics.get("integrity_duplicate_rate"), 0)
    if duplicate_rate >= 20:
        return "Needs Review", "점검 필요", "badge-orange"
    if metrics.get("integrity_total_rows") is None:
        return "Needs Review", "점검 필요", "badge-orange"
    return "Good", "양호", "badge-green"


def benchmark_status_label(metrics):
    coverage = safe_float(metrics.get("integrity_benchmark_coverage"), 0)
    if coverage >= 70:
        return "Good", "양호", "badge-green"
    if coverage >= 30:
        return "Moderate", "보통", "badge-orange"
    return "Needs More Data", "데이터 더 필요", "badge-orange"


def source_status_label(has_data):
    if has_data:
        return "Available", "정상 수집", "badge-green"
    return "Needs Review", "점검 필요", "badge-orange"


def recommendation_quality_label(metrics):
    evaluated_cases = safe_float(metrics.get("price_evaluated_count"), 0)
    reliability_score = safe_float(metrics.get("reliability_score"), 0)
    price_success_rate = safe_float(metrics.get("price_success_rate"), 0)
    benchmark_success_rate = metrics.get("benchmark_success_rate")
    benchmark_coverage = safe_float(metrics.get("integrity_benchmark_coverage"), 0)
    selected_rate = metrics.get("v2_monitor_selected_success_rate") or metrics.get("top_20_success_rate")
    overall_rate = metrics.get("price_success_rate")

    if evaluated_cases < 300:
        return "Insufficient Data", "데이터 부족", "badge-gray"

    selected_beats_overall = (
        selected_rate is not None
        and overall_rate is not None
        and safe_float(selected_rate) > safe_float(overall_rate)
    )

    if (
        reliability_score >= 60
        and price_success_rate >= 55
        and benchmark_success_rate is not None
        and safe_float(benchmark_success_rate) >= 53
        and benchmark_coverage >= 30
    ):
        return "Strong", "강함", "badge-green"

    if (
        reliability_score >= 50
        and price_success_rate >= 50
        and benchmark_success_rate is not None
        and safe_float(benchmark_success_rate) >= 51
        and selected_beats_overall
    ):
        return "Promising", "가능성 있음", "badge-orange"

    if (
        benchmark_success_rate is not None
        and safe_float(benchmark_success_rate) >= 50
        and selected_beats_overall
    ):
        return "Mixed", "혼재", "badge-orange"

    return "Needs Improvement", "개선 필요", "badge-red"


def build_html(metrics, stock_data):
    success_width = min(max(safe_float(metrics.get("price_success_rate", 0)), 0), 100)
    reliability_width = min(max(safe_float(metrics.get("reliability_score", 0)), 0), 100)
    benchmark_width = min(max(safe_float(metrics.get("benchmark_success_rate", 0)), 0), 100)
    evaluated_width = 0
    price_total = metrics.get("price_evaluated_count", 0) + metrics.get("price_pending_count", 0)
    if price_total:
        evaluated_width = min(max(metrics.get("price_evaluated_count", 0) / price_total * 100, 0), 100)

    confidence_class = {
        "WATCHLIST": "badge-green",
        "MODERATE CONFIDENCE": "badge-green",
        "HIGH CONFIDENCE": "badge-green",
        "EARLY STAGE": "badge-orange",
        "NOT READY": "badge-orange",
        "LOW CONFIDENCE": "badge-red",
    }.get(str(metrics.get("confidence_status", "")).upper(), "badge-gray")
    data_en, data_ko, data_class = data_status_label(metrics)
    benchmark_en, benchmark_ko, benchmark_class = benchmark_status_label(metrics)
    news_en = metrics.get("news_coverage_en", "Needs Review")
    news_ko = metrics.get("news_coverage_ko", "점검 필요")
    news_class = metrics.get("news_coverage_class", "badge-orange")
    dart_en, dart_ko, dart_class = source_status_label(
        safe_float(metrics.get("pending_count"), 0) > 0 or safe_float(metrics.get("evaluated_count"), 0) > 0
    )
    overall_en, overall_ko, overall_class = quality_label_from_rate(metrics.get("price_success_rate"))
    recommendation_en, recommendation_ko, recommendation_class = recommendation_quality_label(metrics)
    buy_en, buy_ko, buy_class = quality_label_from_rate(metrics.get("buy_success_rate"))
    avoid_en, avoid_ko, avoid_class = quality_label_from_rate(metrics.get("avoid_success_rate"))
    top_group_rate = metrics.get("v2_monitor_selected_success_rate") or metrics.get("top_20_success_rate")
    last_updated = metrics.get("generated_at", "N/A")

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
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      background: var(--bg);
      color: var(--ink);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }}
    .container {{ max-width: 1120px; margin: 0 auto; padding: 28px 20px 44px; }}
    .hero {{
      display: grid;
      grid-template-columns: minmax(0, 1.4fr) minmax(280px, 0.8fr);
      gap: 28px;
      padding: 34px;
      border-radius: 24px;
      color: white;
      background:
        radial-gradient(circle at top left, rgba(79, 122, 255, 0.25), transparent 32%),
        linear-gradient(135deg, #111827 0%, #1d3557 54%, #235a67 100%);
      box-shadow: var(--shadow);
    }}
    .eyebrow {{ margin: 0 0 12px; color: rgba(255,255,255,0.72); font-size: 12px; font-weight: 800; letter-spacing: 0.08em; text-transform: uppercase; }}
    h1 {{ margin: 0; font-size: clamp(34px, 6vw, 56px); line-height: 1.02; }}
    h2 {{ margin: 0; font-size: 22px; }}
    .subtitle {{ margin-top: 14px; color: rgba(255,255,255,0.86); font-size: 20px; font-weight: 650; }}
    .hero-copy {{ max-width: 720px; margin: 18px 0 0; color: rgba(255,255,255,0.76); font-size: 15px; line-height: 1.7; }}
    .hero-panel {{
      min-height: 245px;
      padding: 24px;
      border: 1px solid rgba(255,255,255,0.18);
      border-radius: 18px;
      background: rgba(255,255,255,0.12);
      backdrop-filter: blur(10px);
    }}
    .badge, .status-pill {{
      display: inline-flex;
      align-items: center;
      width: fit-content;
      max-width: 100%;
      padding: 8px 12px;
      border-radius: 999px;
      font-size: 12px;
      font-weight: 800;
      line-height: 1.25;
      text-align: center;
    }}
    .badge {{ letter-spacing: 0.06em; text-transform: uppercase; }}
    .badge-green, .status-pill.badge-green {{ color: var(--green); background: var(--green-soft); }}
    .badge-orange, .status-pill.badge-orange {{ color: var(--orange); background: var(--orange-soft); }}
    .badge-red, .status-pill.badge-red {{ color: var(--red); background: var(--red-soft); }}
    .badge-gray, .status-pill.badge-gray {{ color: var(--gray); background: var(--gray-soft); }}
    .hero-rate-label {{ margin-top: 30px; color: rgba(255,255,255,0.68); font-size: 12px; font-weight: 800; letter-spacing: 0.08em; text-transform: uppercase; }}
    .hero-rate {{ margin-top: 8px; font-size: clamp(46px, 8vw, 72px); line-height: 0.95; font-weight: 850; }}
    .hero-rate-unit {{ font-size: clamp(22px, 4vw, 34px); color: rgba(255,255,255,0.68); }}
    .progress, .mini-bar {{ height: 9px; margin-top: 16px; border-radius: 999px; overflow: hidden; background: rgba(255,255,255,0.18); }}
    .mini-bar {{ background: #e7edf5; }}
    .progress > span, .mini-bar > span {{ display: block; height: 100%; border-radius: inherit; background: linear-gradient(90deg, #46d39a, #9ee6be); }}
    .mini-bar > span {{ background: var(--blue); }}
    .section {{ margin-top: 28px; }}
    .section-heading {{ margin-bottom: 14px; }}
    .heading-ko {{ display: inline-block; margin-left: 8px; color: var(--muted); font-size: 14px; font-weight: 650; }}
    .section-subtitle {{ margin: 6px 0 0; color: var(--muted); font-size: 14px; line-height: 1.5; }}
    .kpi-grid {{ display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 16px; }}
    .signal-grid {{ display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 14px; }}
    .card {{
      min-width: 0;
      min-height: 132px;
      padding: 18px;
      border: 1px solid rgba(226, 232, 240, 0.9);
      border-radius: 8px;
      background: var(--panel);
      box-shadow: 0 10px 26px rgba(23, 32, 51, 0.06);
    }}
    .card.primary {{ background: linear-gradient(180deg, #f1fff7 0%, #ffffff 100%); border-color: #bcebd4; }}
    .label {{ margin-bottom: 8px; color: var(--muted); font-size: 11px; font-weight: 800; letter-spacing: 0.08em; line-height: 1.35; text-transform: uppercase; }}
    .ko-desc {{ margin: 0 0 12px; color: #8190a3; font-size: 12px; }}
    .value {{ font-size: clamp(28px, 4vw, 40px); line-height: 1; font-weight: 850; }}
    .value.success {{ color: var(--green); }}
    .value.warning {{ color: var(--orange); }}
    .value.risk {{ color: var(--red); }}
    .muted-helper {{ margin-top: 10px; color: var(--muted); font-size: 12px; line-height: 1.45; }}
    .note {{ padding: 15px 18px; border: 1px solid #dbeafe; border-radius: 8px; background: var(--blue-soft); color: #28446d; font-size: 13px; line-height: 1.6; }}
    .links a {{ display: inline-block; margin: 10px 10px 0 0; padding: 10px 12px; border-radius: 999px; background: var(--gray-soft); color: #24435f; text-decoration: none; font-size: 13px; font-weight: 750; }}
    @media (max-width: 920px) {{
      .hero {{ grid-template-columns: 1fr; padding: 26px; }}
      .kpi-grid {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }}
      .signal-grid {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }}
    }}
    @media (max-width: 620px) {{
      .container {{ padding: 14px 12px 34px; }}
      .hero {{ border-radius: 20px; padding: 22px; }}
      .kpi-grid, .signal-grid {{ grid-template-columns: 1fr; }}
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
          A public research dashboard that tracks how well daily price-signal candidates are learning over time.
          매일 생성되는 가격 신호 후보의 성과와 데이터 상태를 쉽게 확인하는 공개 연구 대시보드입니다.
        </p>
      </div>
      <div class="hero-panel">
        <span class="badge {confidence_class}">{metrics["confidence_status"]} / {metrics["confidence_status_ko"]}</span>
        <div class="hero-rate-label">Reliability Score<br>신뢰도 점수</div>
        <div class="hero-rate">{metrics["reliability_score"]}<span class="hero-rate-unit"> / 100</span></div>
        <div class="progress" aria-label="Reliability score"><span style="width: {reliability_width:.0f}%"></span></div>
        <p class="hero-copy" style="margin-top:14px;">This is a conservative reliability estimate based on completed price-candidate evaluations.<br>완료된 가격 후보 평가를 바탕으로 계산한 보수적인 신뢰도입니다.</p>
      </div>
    </section>

    <section class="section">
      <div class="section-heading">
        <h2>Summary <span class="heading-ko">요약</span></h2>
        <p class="section-subtitle">The main health indicators for the learning system. 공개용 핵심 지표만 간단히 표시합니다.</p>
      </div>
      <div class="kpi-grid">
        <div class="card primary">
          <div class="label">Reliability Score</div>
          <div class="ko-desc">신뢰도 점수</div>
          <div class="value">{metrics["reliability_score"]} / 100</div>
          <div class="mini-bar"><span style="width: {reliability_width:.0f}%"></span></div>
        </div>
        <div class="card">
          <div class="label">Price Success Rate (All, Reference)</div>
          <div class="ko-desc">가격 후보 성공률 (전체, 참고용)</div>
          <div class="value success">{metrics["price_success_rate"]}%</div>
          <div class="mini-bar"><span style="width: {success_width:.0f}%"></span></div>
          <div class="muted-helper">Blends buy-type and avoid-type candidates. See directional breakdown below.<br>매수형과 회피형 후보를 합산한 값입니다. 아래 방향별 성과를 함께 확인하세요.</div>
        </div>
        <div class="card">
          <div class="label">Benchmark-Adjusted Success Rate</div>
          <div class="ko-desc">시장 대비 성공률</div>
          {render_kpi_value(metrics["benchmark_success_rate"], "%")}
          <div class="mini-bar"><span style="width: {benchmark_width:.0f}%"></span></div>
        </div>
        <div class="card">
          <div class="label">Evaluated Cases</div>
          <div class="ko-desc">평가 완료 수</div>
          <div class="value">{metrics["price_evaluated_count"]}</div>
          <div class="mini-bar"><span style="width: {evaluated_width:.0f}%"></span></div>
        </div>
        <div class="card">
          <div class="label">Last Updated</div>
          <div class="ko-desc">최근 업데이트</div>
          <div class="muted-helper">{last_updated}</div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="section-heading">
        <h2>Core Performance <span class="heading-ko">핵심 성과</span></h2>
        <p class="section-subtitle">Buy-type and avoid-type candidates are evaluated in opposite directions, so their success rates are shown separately as the primary metrics. 매수형과 회피형 후보는 성공 방향이 반대이므로 방향별 성과를 핵심 지표로 우선 표시합니다.</p>
      </div>
      <div class="signal-grid">
        <div class="card primary">
          <div class="label">Buy-Type Candidate Success Rate</div>
          <div class="ko-desc">매수형 후보 성과</div>
          {render_kpi_value(metrics["buy_success_rate"], "%")}
          <div class="muted-helper">Evaluated cases: {metrics["buy_evaluated_count"]}<br>평가 완료: {metrics["buy_evaluated_count"]}</div>
        </div>
        <div class="card primary">
          <div class="label">Avoid-Type Candidate Success Rate</div>
          <div class="ko-desc">회피형 후보 성과</div>
          {render_kpi_value(metrics["avoid_success_rate"], "%")}
          <div class="muted-helper">Evaluated cases: {metrics["avoid_evaluated_count"]}<br>평가 완료: {metrics["avoid_evaluated_count"]}</div>
        </div>
        <div class="card">
          <div class="label">Recent 7-Day Success Rate</div>
          <div class="ko-desc">최근 7일 성공률</div>
          {render_kpi_value(metrics["rolling_7d_success_rate"], "%")}
        </div>
        <div class="card">
          <div class="label">Recent 30-Day Success Rate</div>
          <div class="ko-desc">최근 30일 성공률</div>
          {render_kpi_value(metrics["rolling_30d_success_rate"], "%")}
        </div>
        <div class="card">
          <div class="label">Pending Candidates</div>
          <div class="ko-desc">평가 대기 수</div>
          <div class="value warning">{metrics["price_pending_count"]}</div>
        </div>
        <div class="card">
          <div class="label">Today Candidate Count</div>
          <div class="ko-desc">오늘 후보 수</div>
          <div class="value">{metrics["price_candidate_rows"]}</div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="section-heading">
        <h2>System & Data Status <span class="heading-ko">시스템 및 데이터 상태</span></h2>
      </div>
      <div class="signal-grid">
        <div class="card">
          <div class="label">Data Integrity Status</div>
          <div class="ko-desc">데이터 무결성 상태</div>
          <div>{simple_status(data_en, data_ko, data_class)}</div>
          <div class="muted-helper">Public metrics use deduplicated evaluation counts.<br>공개 지표는 중복을 줄인 평가 수를 사용합니다.</div>
        </div>
        <div class="card">
          <div class="label">Benchmark Coverage</div>
          <div class="ko-desc">시장 기준 데이터 커버리지</div>
          <div>{simple_status(benchmark_en, benchmark_ko, benchmark_class)}</div>
          <div class="muted-helper">{format_metric_value(metrics["integrity_benchmark_coverage"], "%")}</div>
        </div>
        <div class="card">
          <div class="label">News Source Status</div>
          <div class="ko-desc">뉴스 수집 상태</div>
          <div>{simple_status(news_en, news_ko, news_class)}</div>
        </div>
        <div class="card">
          <div class="label">News Provider Coverage</div>
          <div class="ko-desc">뉴스 소스 커버리지</div>
          <div>{simple_status(metrics["news_coverage_en"], metrics["news_coverage_ko"], metrics["news_coverage_class"])}</div>
          <div class="muted-helper">{metrics["news_provider_available_count"]} active provider(s)<br>활성 뉴스 소스 {metrics["news_provider_available_count"]}개</div>
        </div>
        <div class="card">
          <div class="label">Market Noise Status</div>
          <div class="ko-desc">시장 노이즈 상태</div>
          <div>{simple_status(metrics["market_noise_en"], metrics["market_noise_ko"], metrics["market_noise_class"])}</div>
          <div class="muted-helper">Rumor/noise: {metrics["news_rumor_noise_keyword_count"]} · Risk: {metrics["news_risk_keyword_count"]}<br>루머/노이즈: {metrics["news_rumor_noise_keyword_count"]} · 리스크: {metrics["news_risk_keyword_count"]}</div>
        </div>
        <div class="card">
          <div class="label">DART Source Status</div>
          <div class="ko-desc">공시 데이터 상태</div>
          <div>{simple_status(dart_en, dart_ko, dart_class)}</div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="section-heading">
        <h2>Recommendation Quality <span class="heading-ko">추천 품질</span></h2>
        <p class="section-subtitle">A simple view of whether the candidate ranking is becoming useful. 후보 선별 품질을 쉬운 등급으로 표시합니다.</p>
      </div>
      <div class="signal-grid">
        <div class="card">
          <div class="label">Buy-Type Recommendation Quality</div>
          <div class="ko-desc">매수형 추천 품질</div>
          <div>{simple_status(buy_en, buy_ko, buy_class)}</div>
          <div class="muted-helper">{format_metric_value(metrics["buy_success_rate"], "%")} · {metrics["buy_evaluated_count"]} evaluated<br>{format_metric_value(metrics["buy_success_rate"], "%")} · 평가 완료 {metrics["buy_evaluated_count"]}건</div>
        </div>
        <div class="card">
          <div class="label">Avoid-Type Recommendation Quality</div>
          <div class="ko-desc">회피형 추천 품질</div>
          <div>{simple_status(avoid_en, avoid_ko, avoid_class)}</div>
          <div class="muted-helper">{format_metric_value(metrics["avoid_success_rate"], "%")} · {metrics["avoid_evaluated_count"]} evaluated<br>{format_metric_value(metrics["avoid_success_rate"], "%")} · 평가 완료 {metrics["avoid_evaluated_count"]}건</div>
        </div>
        <div class="card">
          <div class="label">Overall Candidate Performance (All, Reference)</div>
          <div class="ko-desc">전체 후보 성과 (혼합, 참고용)</div>
          <div>{simple_status(overall_en, overall_ko, overall_class)}</div>
          <div class="muted-helper">{metrics["price_success_rate"]}%</div>
        </div>
        <div class="card">
          <div class="label">Top Selected Group Performance</div>
          <div class="ko-desc">상위 추천군 성과</div>
          {render_kpi_value(top_group_rate, "%")}
        </div>
        <div class="card">
          <div class="label">Recommendation Quality Diagnosis</div>
          <div class="ko-desc">추천 품질 진단</div>
          <div>{simple_status(recommendation_en, recommendation_ko, recommendation_class)}</div>
        </div>
        <div class="card">
          <div class="label">Research Scope</div>
          <div class="ko-desc">연구 범위</div>
          <div class="muted-helper">Monitoring only. This dashboard does not provide investment advice or trading automation.<br>모니터링 전용이며 투자 조언이나 자동매매 기능을 제공하지 않습니다.</div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="note">
        Current performance is mixed and still under validation.<br>
        현재 성과는 혼재되어 있으며 계속 검증 중입니다.<br><br>
        Primary learning is based on Korea Investment API price-candidate evaluation. DART, news, Snacks, and social attention are supplementary signals.<br>
        주요 학습은 Korea Investment API 가격 후보 평가를 기반으로 하며, 공시/뉴스/Snacks/관심도 신호는 보조 지표입니다.
      </div>
      <div class="links">
        <a href="https://github.com/JustinSJung/overnight_alpha_lab#readme" target="_blank">README</a>
        <a href="index.html">Development Log</a>
        <a href="https://github.com/JustinSJung/overnight_alpha_lab/tree/main/reports/daily_prediction" target="_blank">Key Reports</a>
      </div>
    </section>
  </div>
</body>
</html>
"""
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
    diagnostics_html = build_diagnostics_html(metrics, stock_data)
    html = "\n".join(line.rstrip() for line in html.splitlines()) + "\n"
    diagnostics_html = "\n".join(line.rstrip() for line in diagnostics_html.splitlines()) + "\n"

    with open(OUTPUT_PATH, "w", encoding="utf-8") as file:
        file.write(html)
    with open(DIAGNOSTICS_OUTPUT_PATH, "w", encoding="utf-8") as file:
        file.write(diagnostics_html)

    print(f"Dashboard saved to: {OUTPUT_PATH}")
    print(f"Internal diagnostics saved to: {DIAGNOSTICS_OUTPUT_PATH}")
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
    print(f"- performance audit diagnosis: {metrics['performance_audit_diagnosis_label']}")
    print(f"- performance audit benchmark-adjusted success rate: {format_metric_value(metrics['performance_audit_benchmark_success_rate'], '%')}")
    print(f"- news provider coverage: {metrics['news_coverage_en']} ({metrics['news_provider_available_count']} active)")
    print(f"- DeepSearch item count: {metrics['deepsearch_item_count']}")
    print(f"- Google News RSS item count: {metrics['google_item_count']}")
    print(f"- GDELT item count: {metrics['gdelt_item_count']}")
    print(f"- Naver item count: {metrics['naver_item_count']}")
    print(f"- news provider feature count: {metrics['news_provider_feature_count']}")
    print(f"- rumor/noise keyword count: {metrics['news_rumor_noise_keyword_count']}")


if __name__ == "__main__":
    main()
