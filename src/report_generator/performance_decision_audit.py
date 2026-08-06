"""
Audit price-candidate performance before changing ranking logic.

This report is diagnostic only. It does not tune scores, create a new ranker,
place orders, or reduce the broad candidate pool.
"""

import sys
from datetime import datetime
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.evaluation.metrics import safe_percentage
from src.storage.schema import RESULT_FAILURE, RESULT_PENDING, RESULT_SUCCESS


PREDICTIONS_DIR = Path("data/predictions")
PROCESSED_DIR = Path("data/processed")
REPORT_DIR = Path("reports/daily_review")


def read_all_csv(directory: Path, pattern: str) -> pd.DataFrame:
    frames = []
    for path in sorted(directory.glob(pattern)):
        try:
            df = pd.read_csv(path)
            df["source_file"] = str(path)
            frames.append(df)
        except Exception as error:
            print(f"Failed to read {path}: {error}")
    if not frames:
        return pd.DataFrame()
    return pd.concat(frames, ignore_index=True)


def normalize_stock_code(value) -> str:
    if value is None or pd.isna(value):
        return ""
    try:
        return str(int(float(value))).zfill(6)
    except Exception:
        return str(value).strip().zfill(6)


def date_key(df: pd.DataFrame, column: str) -> pd.Series:
    if df.empty:
        return pd.Series(dtype=str)
    if column not in df.columns:
        return pd.Series([""] * len(df), index=df.index, dtype=object)
    parsed = pd.to_datetime(df[column], errors="coerce")
    return parsed.dt.strftime("%Y-%m-%d").fillna(df[column].astype(str).replace("nan", ""))


def score_version_series(df: pd.DataFrame) -> pd.Series:
    if "score_version" not in df.columns:
        return pd.Series(["legacy_or_unknown"] * len(df), index=df.index, dtype=object)
    version = df["score_version"].astype(str).str.strip()
    return version.where(~version.isin(["", "nan", "None", "<NA>"]), "legacy_or_unknown")


def dedupe_key_series(df: pd.DataFrame) -> pd.Series:
    if df.empty:
        return pd.Series(dtype=str)
    return (
        df.get("stock_code", pd.Series([""] * len(df), index=df.index)).apply(normalize_stock_code)
        + "|"
        + date_key(df, "signal_date")
        + "|"
        + date_key(df, "prediction_date")
        + "|"
        + date_key(df, "evaluation_date")
        + "|"
        + score_version_series(df)
    )


def dedupe_evaluations(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df
    working = df.copy()
    working["performance_audit_key"] = dedupe_key_series(working)
    sort_columns = [column for column in ["evaluated_at", "evaluation_date", "source_file"] if column in working.columns]
    if sort_columns:
        working = working.sort_values(sort_columns)
    return working.drop_duplicates(subset=["performance_audit_key"], keep="last")


def result_series(df: pd.DataFrame, preferred_column: str = "success_close_t1") -> pd.Series:
    if df.empty:
        return pd.Series(dtype=str)
    result = pd.Series([RESULT_PENDING] * len(df), index=df.index, dtype=object)
    for column in [preferred_column, "prediction_result", "price_candidate_result"]:
        if column in df.columns:
            series = df[column].astype(str).str.strip().str.lower()
            valid = ~series.isin(["", "nan", "none", "<na>"])
            result = result.where(~(result.eq(RESULT_PENDING) & valid), series)
    return result


def explicit_result_series(df: pd.DataFrame, column: str) -> pd.Series:
    if df.empty or column not in df.columns:
        return pd.Series([""] * len(df), index=df.index, dtype=object)
    series = df[column].astype(str).str.strip().str.lower()
    return series.where(~series.isin(["", "nan", "none", "<na>"]), "")


def selected_pick_series(df: pd.DataFrame) -> pd.Series:
    if "selected_pick" not in df.columns:
        return pd.Series([False] * len(df), index=df.index)
    return df["selected_pick"].astype(str).str.lower().isin(["true", "1", "yes"])


def summarize_result(series: pd.Series) -> dict:
    evaluated = series.isin([RESULT_SUCCESS, RESULT_FAILURE])
    evaluated_count = int(evaluated.sum())
    success_count = int((series[evaluated] == RESULT_SUCCESS).sum())
    failure_count = int((series[evaluated] == RESULT_FAILURE).sum())
    return {
        "evaluated_count": evaluated_count,
        "success_count": success_count,
        "failure_count": failure_count,
        "success_rate": round(safe_percentage(success_count, evaluated_count), 2) if evaluated_count else None,
    }


def summarize_subset(df: pd.DataFrame, preferred_column: str = "success_close_t1") -> dict:
    return summarize_result(result_series(df, preferred_column))


def summarize_benchmark(df: pd.DataFrame, column: str = "success_excess_t1") -> dict:
    return summarize_result(explicit_result_series(df, column))


def numeric_success_rate(df: pd.DataFrame, column: str) -> float | None:
    if df.empty or column not in df.columns:
        return None
    values = pd.to_numeric(df[column], errors="coerce")
    valid = values.notna()
    if not valid.any():
        return None
    return round(float((values[valid] > 0).sum() / valid.sum() * 100), 2)


def average_numeric(df: pd.DataFrame, column: str):
    if df.empty or column not in df.columns:
        return None
    value = pd.to_numeric(df[column], errors="coerce").mean()
    if pd.isna(value):
        return None
    return round(float(value), 4)


def candidate_day_series(df: pd.DataFrame) -> pd.Series:
    dates = pd.Series(pd.NaT, index=df.index, dtype="datetime64[ns]")
    for column in ["signal_date", "prediction_date", "candidate_date"]:
        if column in df.columns:
            dates = dates.fillna(pd.to_datetime(df[column], errors="coerce"))
    return dates.dt.strftime("%Y-%m-%d").fillna("unknown")


def candidate_count_bucket(count: int) -> str:
    if count < 50:
        return "0-49"
    if count < 100:
        return "50-99"
    if count < 200:
        return "100-199"
    return "200+"


def candidate_count_findings(df: pd.DataFrame) -> str:
    if df.empty:
        return "No evaluated candidate days available."
    working = df.copy()
    working["candidate_day"] = candidate_day_series(working)
    working["day_candidate_count"] = working.groupby("candidate_day")["candidate_day"].transform("size")
    working["candidate_count_bucket"] = working["day_candidate_count"].apply(candidate_count_bucket)
    rows = []
    for bucket in ["0-49", "50-99", "100-199", "200+"]:
        subset = working[working["candidate_count_bucket"] == bucket]
        summary = summarize_subset(subset)
        if summary["evaluated_count"]:
            rows.append(f"{bucket}: {summary['success_rate']}% ({summary['evaluated_count']} eval)")
    return "; ".join(rows) if rows else "No evaluated candidate count buckets available."


def classify_selected_edge(selected_rate, non_selected_rate) -> str:
    if selected_rate is None or non_selected_rate is None:
        return "insufficient_selected_group_data"
    delta = selected_rate - non_selected_rate
    if delta >= 3:
        return "selected_group_leads"
    if delta <= -3:
        return "selected_group_trails"
    return "selected_group_near_pool"


def decide_diagnosis(overall: dict, benchmark: dict, selected: dict, non_selected: dict, benchmark_coverage_rate) -> str:
    raw_rate = overall["success_rate"]
    benchmark_rate = benchmark["success_rate"]
    selected_edge = classify_selected_edge(selected["success_rate"], non_selected["success_rate"])
    if overall["evaluated_count"] < 50:
        return "insufficient_sample_size"
    if benchmark_coverage_rate is None or benchmark_coverage_rate < 30:
        return "insufficient_benchmark_coverage"
    if raw_rate is not None and raw_rate < 50 and benchmark_rate is not None and benchmark_rate >= 50:
        return "market_relative_signal_only"
    if selected_edge == "selected_group_leads":
        return "overall_pool_noisy_selected_group_promising"
    if raw_rate is not None and raw_rate >= 55:
        return "absolute_return_signal_positive"
    return "weak_or_mixed_signal"


def public_metric_recommendation(selected_benchmark: dict, benchmark: dict, selected: dict, overall: dict) -> str:
    if (
        selected_benchmark["evaluated_count"] >= 30
        and benchmark["success_rate"] is not None
        and selected_benchmark["success_rate"] is not None
        and selected_benchmark["success_rate"] > benchmark["success_rate"]
    ):
        return "selected_group_benchmark_adjusted_success_rate"
    if (
        selected["evaluated_count"] >= 30
        and selected["success_rate"] is not None
        and overall["success_rate"] is not None
        and selected["success_rate"] >= overall["success_rate"] + 3
    ):
        return "selected_group_success_rate"
    return "overall_candidate_pool_with_market_relative_context"


def build_audit() -> tuple[dict, pd.DataFrame]:
    evaluations = read_all_csv(PREDICTIONS_DIR, "price_candidate_evaluation_*.csv")
    evaluations = dedupe_evaluations(evaluations)
    selected_mask = selected_pick_series(evaluations)

    overall = summarize_subset(evaluations)
    selected = summarize_subset(evaluations[selected_mask])
    non_selected = summarize_subset(evaluations[~selected_mask])
    benchmark = summarize_benchmark(evaluations)
    selected_benchmark = summarize_benchmark(evaluations[selected_mask])
    non_selected_benchmark = summarize_benchmark(evaluations[~selected_mask])
    benchmark_coverage_rate = (
        round(safe_percentage(benchmark["evaluated_count"], overall["evaluated_count"]), 2)
        if overall["evaluated_count"]
        else None
    )

    summary = {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "evaluation_rows_after_deduplication": len(evaluations),
        "raw_evaluated_count": overall["evaluated_count"],
        "raw_success_count": overall["success_count"],
        "raw_failure_count": overall["failure_count"],
        "raw_success_rate": overall["success_rate"],
        "selected_raw_evaluated_count": selected["evaluated_count"],
        "selected_raw_success_rate": selected["success_rate"],
        "non_selected_raw_evaluated_count": non_selected["evaluated_count"],
        "non_selected_raw_success_rate": non_selected["success_rate"],
        "benchmark_adjusted_evaluated_count": benchmark["evaluated_count"],
        "benchmark_adjusted_success_count": benchmark["success_count"],
        "benchmark_adjusted_failure_count": benchmark["failure_count"],
        "benchmark_adjusted_success_rate": benchmark["success_rate"],
        "benchmark_adjusted_coverage_rate": benchmark_coverage_rate,
        "selected_benchmark_adjusted_evaluated_count": selected_benchmark["evaluated_count"],
        "selected_benchmark_adjusted_success_rate": selected_benchmark["success_rate"],
        "non_selected_benchmark_adjusted_evaluated_count": non_selected_benchmark["evaluated_count"],
        "non_selected_benchmark_adjusted_success_rate": non_selected_benchmark["success_rate"],
        "close_t1_success_rate": numeric_success_rate(evaluations, "close_t1_return"),
        "close_t3_success_rate": numeric_success_rate(evaluations, "close_t3_return"),
        "close_t5_success_rate": numeric_success_rate(evaluations, "close_t5_return"),
        "excess_t1_success_rate": numeric_success_rate(evaluations, "excess_return_t1"),
        "excess_t3_success_rate": numeric_success_rate(evaluations, "excess_return_t3"),
        "excess_t5_success_rate": numeric_success_rate(evaluations, "excess_return_t5"),
        "avg_close_t1_return": average_numeric(evaluations, "close_t1_return"),
        "avg_excess_t1_return": average_numeric(evaluations, "excess_return_t1"),
        "candidate_count_bucket_findings": candidate_count_findings(evaluations),
        "selected_edge_status": classify_selected_edge(selected["success_rate"], non_selected["success_rate"]),
    }
    summary["diagnosis_label"] = decide_diagnosis(
        overall,
        benchmark,
        selected,
        non_selected,
        benchmark_coverage_rate,
    )
    summary["public_metric_recommendation"] = public_metric_recommendation(
        selected_benchmark,
        benchmark,
        selected,
        overall,
    )
    return summary, evaluations


def write_outputs(summary: dict) -> tuple[Path, Path]:
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    today_csv = datetime.today().strftime("%Y%m%d")
    today_display = datetime.today().strftime("%Y-%m-%d")
    csv_path = PROCESSED_DIR / f"performance_decision_audit_{today_csv}.csv"
    report_path = REPORT_DIR / f"{today_display}_performance_decision_audit.md"

    pd.DataFrame([summary]).to_csv(csv_path, index=False, encoding="utf-8-sig")

    lines = [
        f"# Performance Decision Audit - {today_display}",
        "",
        "This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.",
        "",
        "## Summary",
        "",
        f"- Raw success rate: **{summary['raw_success_rate']}%** ({summary['raw_evaluated_count']} evaluated)",
        f"- Benchmark-adjusted success rate: **{summary['benchmark_adjusted_success_rate']}%** ({summary['benchmark_adjusted_evaluated_count']} evaluated)",
        f"- Selected raw success rate: **{summary['selected_raw_success_rate']}%**",
        f"- Non-selected raw success rate: **{summary['non_selected_raw_success_rate']}%**",
        f"- Selected benchmark-adjusted success rate: **{summary['selected_benchmark_adjusted_success_rate']}%**",
        f"- Non-selected benchmark-adjusted success rate: **{summary['non_selected_benchmark_adjusted_success_rate']}%**",
        f"- Benchmark coverage: **{summary['benchmark_adjusted_coverage_rate']}%**",
        f"- Diagnosis: **{summary['diagnosis_label']}**",
        f"- Public metric recommendation: **{summary['public_metric_recommendation']}**",
        "",
        "## Interpretation",
        "",
        "Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.",
        "",
        "## Candidate Count Buckets",
        "",
        summary["candidate_count_bucket_findings"],
        "",
        "## Return Horizons",
        "",
        f"- Close T+1 success rate: **{summary['close_t1_success_rate']}%**",
        f"- Close T+3 success rate: **{summary['close_t3_success_rate']}%**",
        f"- Close T+5 success rate: **{summary['close_t5_success_rate']}%**",
        f"- Excess T+1 success rate: **{summary['excess_t1_success_rate']}%**",
        f"- Excess T+3 success rate: **{summary['excess_t3_success_rate']}%**",
        f"- Excess T+5 success rate: **{summary['excess_t5_success_rate']}%**",
        "",
        "## Decision Guardrail",
        "",
        "Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.",
    ]
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return csv_path, report_path


def main():
    summary, _ = build_audit()
    csv_path, report_path = write_outputs(summary)
    print(f"Performance decision audit saved to: {csv_path}")
    print(f"Performance decision audit report saved to: {report_path}")
    print(f"raw success rate: {summary['raw_success_rate']}")
    print(f"benchmark-adjusted success rate: {summary['benchmark_adjusted_success_rate']}")
    print(f"selected raw success rate: {summary['selected_raw_success_rate']}")
    print(f"non-selected raw success rate: {summary['non_selected_raw_success_rate']}")
    print(f"selected benchmark-adjusted success rate: {summary['selected_benchmark_adjusted_success_rate']}")
    print(f"non-selected benchmark-adjusted success rate: {summary['non_selected_benchmark_adjusted_success_rate']}")
    print(f"diagnosis: {summary['diagnosis_label']}")


if __name__ == "__main__":
    main()
