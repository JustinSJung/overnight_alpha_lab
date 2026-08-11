"""
Monitor v2_conservative_ranker performance from price-candidate evaluations.

This report is diagnostic only. It does not change scoring, generate orders, or
reduce the broad candidate pool used for learning.
"""

import sys
from datetime import datetime
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.evaluation.metrics import safe_percentage
from src.evaluator.price_candidate_evaluator import direction_series
from src.storage.schema import RESULT_FAILURE, RESULT_PENDING, RESULT_SUCCESS


PREDICTIONS_DIR = Path("data/predictions")
PROCESSED_DIR = Path("data/processed")
REPORT_DIR = Path("reports/daily_review")
V2_SCORE_VERSION = "v2_conservative_ranker"

RANK_BUCKETS = [
    ("Top 10", 10),
    ("Top 20", 20),
    ("Top 50", 50),
    ("Top 100", 100),
]


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
    working["v2_monitor_key"] = dedupe_key_series(working)
    sort_columns = [column for column in ["evaluated_at", "source_file"] if column in working.columns]
    if sort_columns:
        working = working.sort_values(sort_columns)
    return working.drop_duplicates(subset=["v2_monitor_key"], keep="last")


def normalize_result_series(df: pd.DataFrame) -> pd.Series:
    if df.empty:
        return pd.Series(dtype=str)
    result = pd.Series([RESULT_PENDING] * len(df), index=df.index, dtype=object)
    for column in ["success_close_t1", "prediction_result", "price_candidate_result"]:
        if column in df.columns:
            series = df[column].astype(str).str.strip().str.lower()
            valid = ~series.isin(["", "nan", "none", "<na>"])
            result = result.where(~(result.eq(RESULT_PENDING) & valid), series)
    return result


def selected_pick_series(df: pd.DataFrame) -> pd.Series:
    if "selected_pick" not in df.columns:
        return pd.Series([False] * len(df), index=df.index)
    return df["selected_pick"].astype(str).str.lower().isin(["true", "1", "yes"])


def coalesced_score(df: pd.DataFrame) -> pd.Series:
    score = pd.Series(pd.NA, index=df.index, dtype="Float64")
    for column in ["final_price_signal_score_v2", "final_price_signal_score", "price_candidate_score", "prediction_score"]:
        if column in df.columns:
            score = score.fillna(pd.to_numeric(df[column], errors="coerce"))
    return score


def rank_date_series(df: pd.DataFrame) -> pd.Series:
    dates = pd.Series(pd.NaT, index=df.index, dtype="datetime64[ns]")
    for column in ["signal_date", "prediction_date", "candidate_date"]:
        if column in df.columns:
            dates = dates.fillna(pd.to_datetime(df[column], errors="coerce"))
    return dates.dt.strftime("%Y-%m-%d").fillna("unknown")


def add_daily_rank(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df
    working = df.copy()
    working["v2_rank_date"] = rank_date_series(working)
    working["v2_rank_score"] = coalesced_score(working)
    if working["v2_rank_score"].notna().any():
        working["v2_daily_rank"] = working.groupby("v2_rank_date", dropna=False)["v2_rank_score"].rank(
            method="first",
            ascending=False,
        )
    elif "candidate_rank" in working.columns:
        working["v2_daily_rank"] = pd.to_numeric(working["candidate_rank"], errors="coerce")
    else:
        working["v2_daily_rank"] = pd.NA

    if "candidate_rank" in working.columns:
        fallback_rank = pd.to_numeric(working["candidate_rank"], errors="coerce")
        working["v2_daily_rank"] = working["v2_daily_rank"].fillna(fallback_rank)
    return working


def average_numeric(df: pd.DataFrame, column: str, mask: pd.Series):
    if column not in df.columns or not mask.any():
        return None
    value = pd.to_numeric(df.loc[mask, column], errors="coerce").mean()
    if pd.isna(value):
        return None
    return round(float(value), 4)


def summarize_subset(df: pd.DataFrame) -> dict:
    if df.empty:
        return {
            "evaluated_count": 0,
            "success_count": 0,
            "failure_count": 0,
            "success_rate": None,
        }
    results = normalize_result_series(df)
    evaluated = results.isin([RESULT_SUCCESS, RESULT_FAILURE])
    evaluated_count = int(evaluated.sum())
    success_count = int((results[evaluated] == RESULT_SUCCESS).sum())
    failure_count = int((results[evaluated] == RESULT_FAILURE).sum())
    return {
        "evaluated_count": evaluated_count,
        "success_count": success_count,
        "failure_count": failure_count,
        "success_rate": round(safe_percentage(success_count, evaluated_count), 2) if evaluated_count else None,
    }


def directional_summary(df: pd.DataFrame) -> dict:
    """
    Diagnostic-only breakdown of a v2 subset by candidate direction (buy/avoid).
    Does not feed scoring or candidate selection.
    """
    base = summarize_subset(df)
    evaluated = normalize_result_series(df).isin([RESULT_SUCCESS, RESULT_FAILURE]) if not df.empty else pd.Series(dtype=bool)
    benchmark_results = benchmark_success_series(df)
    benchmark_evaluated = benchmark_results.isin([RESULT_SUCCESS, RESULT_FAILURE])
    benchmark_evaluated_count = int(benchmark_evaluated.sum())
    benchmark_success_count = int((benchmark_results[benchmark_evaluated] == RESULT_SUCCESS).sum())
    return {
        **base,
        "avg_close_t1_return": average_numeric(df, "close_t1_return", evaluated),
        "avg_close_t3_return": average_numeric(df, "close_t3_return", evaluated),
        "avg_close_t5_return": average_numeric(df, "close_t5_return", evaluated),
        "benchmark_evaluated_cases": benchmark_evaluated_count,
        "benchmark_success_rate": round(safe_percentage(benchmark_success_count, benchmark_evaluated_count), 2)
        if benchmark_evaluated_count
        else None,
    }


def benchmark_success_series(df: pd.DataFrame) -> pd.Series:
    if "success_excess_t1" not in df.columns:
        return pd.Series([""] * len(df), index=df.index, dtype=object)
    series = df["success_excess_t1"].astype(str).str.strip().str.lower()
    return series.where(~series.isin(["", "nan", "none", "<na>"]), "")


def diagnose_v2(evaluated_count: int, selected_rate, non_selected_rate) -> tuple[str, str]:
    if evaluated_count < 300 or selected_rate is None or non_selected_rate is None:
        return "Insufficient data", "데이터 부족"
    delta = selected_rate - non_selected_rate
    if delta > 3:
        return "Improving", "개선 가능성"
    if delta < -3:
        return "Inverted", "역방향 가능성"
    return "Weak", "약함"


def diagnose_benchmark(coverage_rate, benchmark_success_rate) -> tuple[str, str]:
    if coverage_rate is None or coverage_rate < 30:
        return "Benchmark coverage still low", "시장 기준 커버리지 낮음"
    if benchmark_success_rate is None:
        return "Benchmark data unavailable", "시장 기준 데이터 부족"
    if benchmark_success_rate > 53:
        return "Positive market-relative signal", "시장 대비 긍정 신호"
    if benchmark_success_rate < 48:
        return "Weak market-relative signal", "시장 대비 약한 신호"
    return "Neutral", "중립"


def build_monitor() -> tuple[dict, list[dict]]:
    evaluations = read_all_csv(PREDICTIONS_DIR, "price_candidate_evaluation_*.csv")
    evaluations = dedupe_evaluations(evaluations)
    if evaluations.empty or "score_version" not in evaluations.columns:
        v2 = pd.DataFrame()
    else:
        v2 = evaluations[score_version_series(evaluations).eq(V2_SCORE_VERSION)].copy()

    v2 = add_daily_rank(v2)
    result_summary = summarize_subset(v2)
    results = normalize_result_series(v2)
    evaluated = results.isin([RESULT_SUCCESS, RESULT_FAILURE])

    benchmark_results = benchmark_success_series(v2)
    benchmark_evaluated = benchmark_results.isin([RESULT_SUCCESS, RESULT_FAILURE])
    benchmark_success_count = int((benchmark_results[benchmark_evaluated] == RESULT_SUCCESS).sum())
    benchmark_evaluated_count = int(benchmark_evaluated.sum())
    benchmark_success_rate = (
        round(safe_percentage(benchmark_success_count, benchmark_evaluated_count), 2)
        if benchmark_evaluated_count
        else None
    )
    benchmark_coverage_rate = (
        round(safe_percentage(benchmark_evaluated_count, result_summary["evaluated_count"]), 2)
        if result_summary["evaluated_count"]
        else None
    )

    selected_mask = selected_pick_series(v2)
    selected_summary = summarize_subset(v2[selected_mask])
    non_selected_summary = summarize_subset(v2[~selected_mask])

    v2["candidate_direction"] = direction_series(v2)
    buy_summary = directional_summary(v2[v2["candidate_direction"] == "buy"])
    avoid_summary = directional_summary(v2[v2["candidate_direction"] == "avoid"])

    rank_rows = []
    for label, end in RANK_BUCKETS:
        subset = v2[pd.to_numeric(v2.get("v2_daily_rank", pd.Series(dtype=float)), errors="coerce") <= end]
        bucket_summary = summarize_subset(subset)
        rank_rows.append({"bucket": label, **bucket_summary})

    rank_lookup = {row["bucket"]: row for row in rank_rows}
    diagnosis_en, diagnosis_ko = diagnose_v2(
        result_summary["evaluated_count"],
        selected_summary["success_rate"],
        non_selected_summary["success_rate"],
    )
    benchmark_diagnosis_en, benchmark_diagnosis_ko = diagnose_benchmark(
        benchmark_coverage_rate,
        benchmark_success_rate,
    )

    summary = {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "score_version": V2_SCORE_VERSION,
        "v2_evaluated_cases": result_summary["evaluated_count"],
        "v2_success_count": result_summary["success_count"],
        "v2_failure_count": result_summary["failure_count"],
        "v2_raw_success_rate": result_summary["success_rate"],
        "v2_benchmark_adjusted_evaluated_cases": benchmark_evaluated_count,
        "v2_benchmark_adjusted_success_count": benchmark_success_count,
        "v2_benchmark_adjusted_success_rate": benchmark_success_rate,
        "v2_benchmark_coverage_rate": benchmark_coverage_rate,
        "v2_average_close_t1_return": average_numeric(v2, "close_t1_return", evaluated),
        "v2_average_excess_t1_return": average_numeric(v2, "excess_return_t1", evaluated),
        "v2_selected_pick_evaluated_cases": selected_summary["evaluated_count"],
        "v2_selected_pick_success_rate": selected_summary["success_rate"],
        "v2_non_selected_evaluated_cases": non_selected_summary["evaluated_count"],
        "v2_non_selected_success_rate": non_selected_summary["success_rate"],
        "v2_top_10_success_rate": rank_lookup["Top 10"]["success_rate"],
        "v2_top_20_success_rate": rank_lookup["Top 20"]["success_rate"],
        "v2_top_50_success_rate": rank_lookup["Top 50"]["success_rate"],
        "v2_top_100_success_rate": rank_lookup["Top 100"]["success_rate"],
        "v2_top_10_evaluated_cases": rank_lookup["Top 10"]["evaluated_count"],
        "v2_top_20_evaluated_cases": rank_lookup["Top 20"]["evaluated_count"],
        "v2_top_50_evaluated_cases": rank_lookup["Top 50"]["evaluated_count"],
        "v2_top_100_evaluated_cases": rank_lookup["Top 100"]["evaluated_count"],
        "v2_diagnosis_en": diagnosis_en,
        "v2_diagnosis_ko": diagnosis_ko,
        "v2_benchmark_diagnosis_en": benchmark_diagnosis_en,
        "v2_benchmark_diagnosis_ko": benchmark_diagnosis_ko,
        "v2_buy_evaluated_cases": buy_summary["evaluated_count"],
        "v2_buy_success_count": buy_summary["success_count"],
        "v2_buy_failure_count": buy_summary["failure_count"],
        "v2_buy_success_rate": buy_summary["success_rate"],
        "v2_buy_avg_close_t1_return": buy_summary["avg_close_t1_return"],
        "v2_buy_avg_close_t3_return": buy_summary["avg_close_t3_return"],
        "v2_buy_avg_close_t5_return": buy_summary["avg_close_t5_return"],
        "v2_buy_benchmark_evaluated_cases": buy_summary["benchmark_evaluated_cases"],
        "v2_buy_benchmark_success_rate": buy_summary["benchmark_success_rate"],
        "v2_avoid_evaluated_cases": avoid_summary["evaluated_count"],
        "v2_avoid_success_count": avoid_summary["success_count"],
        "v2_avoid_failure_count": avoid_summary["failure_count"],
        "v2_avoid_success_rate": avoid_summary["success_rate"],
        "v2_avoid_avg_close_t1_return": avoid_summary["avg_close_t1_return"],
        "v2_avoid_avg_close_t3_return": avoid_summary["avg_close_t3_return"],
        "v2_avoid_avg_close_t5_return": avoid_summary["avg_close_t5_return"],
        "v2_avoid_benchmark_evaluated_cases": avoid_summary["benchmark_evaluated_cases"],
        "v2_avoid_benchmark_success_rate": avoid_summary["benchmark_success_rate"],
    }
    return summary, rank_rows


def format_percent(value):
    if value is None or pd.isna(value):
        return "N/A"
    return f"{float(value):.2f}%"


def format_return(value):
    if value is None or pd.isna(value):
        return "N/A"
    return f"{float(value) * 100:.2f}%"


def write_outputs(summary: dict, rank_rows: list[dict]) -> tuple[Path, Path]:
    today_csv = datetime.today().strftime("%Y%m%d")
    today_display = datetime.today().strftime("%Y-%m-%d")
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    summary_path = PROCESSED_DIR / f"v2_performance_summary_{today_csv}.csv"
    pd.DataFrame([summary]).to_csv(summary_path, index=False, encoding="utf-8-sig")

    report_path = REPORT_DIR / f"{today_display}_v2_performance_monitor.md"
    lines = [
        f"# V2 Performance Monitor - {today_display}",
        "",
        "This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.",
        "",
        "## Summary",
        "",
        f"- V2 evaluated cases: **{summary['v2_evaluated_cases']}**",
        f"- V2 success count: **{summary['v2_success_count']}**",
        f"- V2 failure count: **{summary['v2_failure_count']}**",
        f"- V2 raw success rate: **{format_percent(summary['v2_raw_success_rate'])}**",
        f"- V2 benchmark-adjusted evaluated cases: **{summary['v2_benchmark_adjusted_evaluated_cases']}**",
        f"- V2 benchmark-adjusted success rate: **{format_percent(summary['v2_benchmark_adjusted_success_rate'])}**",
        f"- V2 benchmark coverage rate: **{format_percent(summary['v2_benchmark_coverage_rate'])}**",
        f"- V2 average close_t1_return: **{format_return(summary['v2_average_close_t1_return'])}**",
        f"- V2 average excess_t1_return: **{format_return(summary['v2_average_excess_t1_return'])}**",
        f"- Selected-pick evaluated cases: **{summary['v2_selected_pick_evaluated_cases']}**",
        f"- Selected-pick success rate: **{format_percent(summary['v2_selected_pick_success_rate'])}**",
        f"- Non-selected evaluated cases: **{summary['v2_non_selected_evaluated_cases']}**",
        f"- Non-selected success rate: **{format_percent(summary['v2_non_selected_success_rate'])}**",
        f"- V2 diagnosis: **{summary['v2_diagnosis_en']} / {summary['v2_diagnosis_ko']}**",
        f"- Benchmark diagnosis: **{summary['v2_benchmark_diagnosis_en']} / {summary['v2_benchmark_diagnosis_ko']}**",
        "",
        "## Rank Buckets",
        "",
        "| bucket | evaluated_count | success_count | failure_count | success_rate |",
        "|---|---|---|---|---|",
    ]
    for row in rank_rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row.get("bucket", "")),
                    str(row.get("evaluated_count", 0)),
                    str(row.get("success_count", 0)),
                    str(row.get("failure_count", 0)),
                    format_percent(row.get("success_rate")),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- Improving means selected picks beat non-selected candidates by more than 3 percentage points.",
            "- Weak means selected and non-selected performance are within +/-3 percentage points.",
            "- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.",
            "- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.",
            "",
            "## Directional Breakdown (Buy vs Avoid)",
            "",
            "Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.",
            "",
            "| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |",
            "|---|---|---|---|---|---|---|---|---|---|",
            (
                "| buy | "
                f"{summary['v2_buy_evaluated_cases']} | {summary['v2_buy_success_count']} | {summary['v2_buy_failure_count']} | "
                f"{format_percent(summary['v2_buy_success_rate'])} | {format_return(summary['v2_buy_avg_close_t1_return'])} | "
                f"{format_return(summary['v2_buy_avg_close_t3_return'])} | {format_return(summary['v2_buy_avg_close_t5_return'])} | "
                f"{summary['v2_buy_benchmark_evaluated_cases']} | {format_percent(summary['v2_buy_benchmark_success_rate'])} |"
            ),
            (
                "| avoid | "
                f"{summary['v2_avoid_evaluated_cases']} | {summary['v2_avoid_success_count']} | {summary['v2_avoid_failure_count']} | "
                f"{format_percent(summary['v2_avoid_success_rate'])} | {format_return(summary['v2_avoid_avg_close_t1_return'])} | "
                f"{format_return(summary['v2_avoid_avg_close_t3_return'])} | {format_return(summary['v2_avoid_avg_close_t5_return'])} | "
                f"{summary['v2_avoid_benchmark_evaluated_cases']} | {format_percent(summary['v2_avoid_benchmark_success_rate'])} |"
            ),
            "",
            "Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). "
            "Small buy-type sample sizes should be read conservatively.",
        ]
    )
    report_path.write_text("\n".join(lines), encoding="utf-8")
    return summary_path, report_path


def main():
    print("Generating v2 performance monitor...")
    summary, rank_rows = build_monitor()
    summary_path, report_path = write_outputs(summary, rank_rows)
    print(f"V2 performance summary saved to: {summary_path}")
    print(f"V2 performance report saved to: {report_path}")
    print(f"v2 evaluated cases: {summary['v2_evaluated_cases']}")
    print(f"v2 raw success rate: {format_percent(summary['v2_raw_success_rate'])}")
    print(f"v2 benchmark-adjusted success rate: {format_percent(summary['v2_benchmark_adjusted_success_rate'])}")
    print(f"selected_pick success rate: {format_percent(summary['v2_selected_pick_success_rate'])}")
    print(f"non-selected success rate: {format_percent(summary['v2_non_selected_success_rate'])}")
    print(f"v2 Top 10 success rate: {format_percent(summary['v2_top_10_success_rate'])}")
    print(f"v2 Top 20 success rate: {format_percent(summary['v2_top_20_success_rate'])}")
    print(f"v2 diagnosis: {summary['v2_diagnosis_en']} / {summary['v2_diagnosis_ko']}")
    print(f"benchmark coverage status: {summary['v2_benchmark_diagnosis_en']} / {summary['v2_benchmark_diagnosis_ko']}")
    print(
        f"v2 buy-type: {summary['v2_buy_evaluated_cases']} evaluated, "
        f"{format_percent(summary['v2_buy_success_rate'])} success rate"
    )
    print(
        f"v2 avoid-type: {summary['v2_avoid_evaluated_cases']} evaluated, "
        f"{format_percent(summary['v2_avoid_success_rate'])} success rate"
    )


if __name__ == "__main__":
    main()
