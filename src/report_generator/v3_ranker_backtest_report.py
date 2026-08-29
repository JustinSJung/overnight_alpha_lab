"""
Simulate an experimental v3 stability ranker on historical price candidates.

This report is diagnostic only. It does not alter historical decisions, change
selected_pick, place orders, or reduce the broad candidate pool.
"""

import sys
from datetime import datetime
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.evaluation.metrics import dedupe_evaluations, safe_percentage
from src.models.price_based_daily_recommender import EXPERIMENTAL_SCORE_VERSION, calculate_v3_components
from src.storage.schema import RESULT_FAILURE, RESULT_PENDING, RESULT_SUCCESS


PREDICTIONS_DIR = Path("data/predictions")
PROCESSED_DIR = Path("data/processed")
REPORT_DIR = Path("reports/daily_review")

REQUIRED_V3_COLUMNS = [
    "return_1d",
    "return_5d",
    "return_20d",
    "volume_ratio_20d",
    "volatility_20d",
    "close",
    "ma20",
]

RANK_BUCKETS = [
    ("Top 10", 10),
    ("Top 20", 20),
    ("Top 50", 50),
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


def rank_date_series(df: pd.DataFrame) -> pd.Series:
    dates = pd.Series(pd.NaT, index=df.index, dtype="datetime64[ns]")
    for column in ["signal_date", "prediction_date", "candidate_date"]:
        if column in df.columns:
            dates = dates.fillna(pd.to_datetime(df[column], errors="coerce"))
    return dates.dt.strftime("%Y-%m-%d").fillna("unknown")


def benchmark_success_series(df: pd.DataFrame) -> pd.Series:
    if "success_excess_t1" not in df.columns:
        return pd.Series([""] * len(df), index=df.index, dtype=object)
    series = df["success_excess_t1"].astype(str).str.strip().str.lower()
    return series.where(~series.isin(["", "nan", "none", "<na>"]), "")


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
            "avg_close_t1_return": None,
            "avg_excess_t1_return": None,
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
        "avg_close_t1_return": average_numeric(df, "close_t1_return", evaluated),
        "avg_excess_t1_return": average_numeric(df, "excess_return_t1", evaluated),
    }


def summarize_benchmark(df: pd.DataFrame) -> dict:
    if df.empty:
        return {
            "benchmark_evaluated_count": 0,
            "benchmark_success_count": 0,
            "benchmark_adjusted_success_rate": None,
        }
    benchmark_results = benchmark_success_series(df)
    evaluated = benchmark_results.isin([RESULT_SUCCESS, RESULT_FAILURE])
    evaluated_count = int(evaluated.sum())
    success_count = int((benchmark_results[evaluated] == RESULT_SUCCESS).sum())
    return {
        "benchmark_evaluated_count": evaluated_count,
        "benchmark_success_count": success_count,
        "benchmark_adjusted_success_rate": (
            round(safe_percentage(success_count, evaluated_count), 2) if evaluated_count else None
        ),
    }


def row_context(row: pd.Series) -> tuple[dict, dict, dict]:
    social = {
        "risk_label": row.get("social_risk_label", ""),
        "risk_noise_score": row.get("risk_noise_score", 0),
        "hype_keyword_count": row.get("hype_keyword_count", 0),
    }
    news = {
        "news_risk_score": row.get("news_risk_score", 0),
        "negative_keyword_count": row.get("news_negative_keyword_count", 0),
        "risk_keyword_count": row.get("news_risk_keyword_count", 0),
    }
    ml_context = {
        "prediction_direction": row.get("prediction_direction", ""),
        "market_regime_bucket": row.get("market_regime_bucket", ""),
    }
    return social, ml_context, news


def add_v3_scores(df: pd.DataFrame) -> pd.DataFrame:
    working = df.copy()
    existing_v3_columns = [column for column in working.columns if column.startswith("v3_")]
    existing_v3_columns += [
        column
        for column in ["final_price_signal_score_v3", "experimental_score_version"]
        if column in working.columns
    ]
    if existing_v3_columns:
        working = working.drop(columns=list(dict.fromkeys(existing_v3_columns)))

    component_rows = []
    for _, row in working.iterrows():
        social, ml_context, news = row_context(row)
        component_rows.append(calculate_v3_components(row, social, ml_context, news))
    components = pd.DataFrame(component_rows, index=working.index)
    working = pd.concat([working, components], axis=1)
    working["v3_rank_date"] = rank_date_series(working)
    working["v3_daily_rank"] = working.groupby("v3_rank_date", dropna=False)["v3_final_score"].rank(
        method="first",
        ascending=False,
    )
    return working


def build_backtest() -> tuple[dict, list[dict]]:
    evaluations = read_all_csv(PREDICTIONS_DIR, "price_candidate_evaluation_*.csv")
    evaluations = dedupe_evaluations(evaluations)

    missing_columns = [column for column in REQUIRED_V3_COLUMNS if column not in evaluations.columns]
    component_coverage = 0.0
    if not evaluations.empty and not missing_columns:
        complete_rows = evaluations[REQUIRED_V3_COLUMNS].notna().all(axis=1)
        component_coverage = round(safe_percentage(int(complete_rows.sum()), len(evaluations)), 2)
        evaluations = evaluations[complete_rows].copy()

    if evaluations.empty or missing_columns:
        summary = {
            "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "experimental_score_version": EXPERIMENTAL_SCORE_VERSION,
            "historical_component_coverage_rate": component_coverage,
            "has_enough_historical_data": False,
            "coverage_note": "insufficient historical component coverage",
            "missing_component_columns": ",".join(missing_columns),
            "overall_evaluated_cases": 0,
            "overall_success_rate": None,
            "current_selected_group_success_rate": None,
            "v3_top_10_success_rate": None,
            "v3_top_20_success_rate": None,
            "v3_top_50_success_rate": None,
            "v3_top_20_benchmark_adjusted_success_rate": None,
        }
        return summary, []

    scored = add_v3_scores(evaluations)
    overall = summarize_subset(scored)
    selected = summarize_subset(scored[selected_pick_series(scored)])

    rank_rows = []
    for label, end in RANK_BUCKETS:
        subset = scored[pd.to_numeric(scored["v3_daily_rank"], errors="coerce") <= end]
        bucket_summary = summarize_subset(subset)
        benchmark_summary = summarize_benchmark(subset)
        rank_rows.append(
            {
                "bucket": label,
                **bucket_summary,
                **benchmark_summary,
            }
        )

    rank_lookup = {row["bucket"]: row for row in rank_rows}
    top_20_benchmark = rank_lookup["Top 20"]["benchmark_adjusted_success_rate"]
    summary = {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "experimental_score_version": EXPERIMENTAL_SCORE_VERSION,
        "historical_component_coverage_rate": component_coverage,
        "has_enough_historical_data": True,
        "coverage_note": (
            "partial historical component coverage"
            if component_coverage < 70
            else "sufficient historical component coverage"
        ),
        "missing_component_columns": "",
        "overall_evaluated_cases": overall["evaluated_count"],
        "overall_success_rate": overall["success_rate"],
        "current_selected_group_success_rate": selected["success_rate"],
        "v3_top_10_success_rate": rank_lookup["Top 10"]["success_rate"],
        "v3_top_20_success_rate": rank_lookup["Top 20"]["success_rate"],
        "v3_top_50_success_rate": rank_lookup["Top 50"]["success_rate"],
        "v3_top_10_evaluated_cases": rank_lookup["Top 10"]["evaluated_count"],
        "v3_top_20_evaluated_cases": rank_lookup["Top 20"]["evaluated_count"],
        "v3_top_50_evaluated_cases": rank_lookup["Top 50"]["evaluated_count"],
        "v3_top_20_benchmark_adjusted_success_rate": top_20_benchmark,
        "v3_top_20_benchmark_adjusted_evaluated_cases": rank_lookup["Top 20"]["benchmark_evaluated_count"],
        "v3_top_20_average_close_t1_return": rank_lookup["Top 20"]["avg_close_t1_return"],
        "v3_top_20_average_excess_t1_return": rank_lookup["Top 20"]["avg_excess_t1_return"],
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

    summary_path = PROCESSED_DIR / f"v3_ranker_backtest_summary_{today_csv}.csv"
    pd.DataFrame([summary]).to_csv(summary_path, index=False, encoding="utf-8-sig")

    report_path = REPORT_DIR / f"{today_display}_v3_ranker_backtest_report.md"
    lines = [
        f"# V3 Ranker Backtest Report - {today_display}",
        "",
        "This report simulates `v3_stability_ranker` on already-evaluated historical candidates.",
        "It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.",
        "",
        "## Summary",
        "",
        f"- Experimental score version: **{summary['experimental_score_version']}**",
        f"- Historical component coverage: **{format_percent(summary['historical_component_coverage_rate'])}**",
        f"- Data status: **{summary['coverage_note']}**",
    ]

    if not summary.get("has_enough_historical_data"):
        lines.extend(
            [
                f"- Missing component columns: **{summary.get('missing_component_columns') or 'N/A'}**",
                "",
                "V3 results were not calculated because historical component coverage is insufficient.",
            ]
        )
    else:
        lines.extend(
            [
                f"- Overall evaluated cases: **{summary['overall_evaluated_cases']}**",
                f"- Overall success rate: **{format_percent(summary['overall_success_rate'])}**",
                f"- Current selected group success rate: **{format_percent(summary['current_selected_group_success_rate'])}**",
                f"- Simulated v3 Top 10 success rate: **{format_percent(summary['v3_top_10_success_rate'])}**",
                f"- Simulated v3 Top 20 success rate: **{format_percent(summary['v3_top_20_success_rate'])}**",
                f"- Simulated v3 Top 50 success rate: **{format_percent(summary['v3_top_50_success_rate'])}**",
                f"- Simulated v3 Top 20 benchmark-adjusted success rate: **{format_percent(summary['v3_top_20_benchmark_adjusted_success_rate'])}**",
                "",
                "## Rank Buckets",
                "",
                "| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |",
                "|---|---:|---:|---:|---:|---:|---:|---:|",
            ]
        )
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
                        format_return(row.get("avg_close_t1_return")),
                        format_return(row.get("avg_excess_t1_return")),
                        format_percent(row.get("benchmark_adjusted_success_rate")),
                    ]
                )
                + " |"
            )

    lines.extend(
        [
            "",
            "## Notes",
            "",
            "- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.",
            "- V3 is not public production scoring yet.",
            "- No order placement or trading action is performed by this project.",
        ]
    )
    report_path.write_text("\n".join(lines), encoding="utf-8")
    return summary_path, report_path


def main():
    print("Generating v3 ranker backtest report...")
    summary, rank_rows = build_backtest()
    summary_path, report_path = write_outputs(summary, rank_rows)
    print(f"V3 backtest summary saved to: {summary_path}")
    print(f"V3 backtest report saved to: {report_path}")
    print(f"historical component coverage: {format_percent(summary['historical_component_coverage_rate'])}")
    print(f"v3 enough historical data: {summary['has_enough_historical_data']}")
    print(f"overall success rate: {format_percent(summary['overall_success_rate'])}")
    print(f"current selected group success rate: {format_percent(summary['current_selected_group_success_rate'])}")
    print(f"v3 Top 10 success rate: {format_percent(summary['v3_top_10_success_rate'])}")
    print(f"v3 Top 20 success rate: {format_percent(summary['v3_top_20_success_rate'])}")
    print(f"v3 Top 50 success rate: {format_percent(summary.get('v3_top_50_success_rate'))}")
    print(
        "v3 Top 20 benchmark-adjusted success rate: "
        f"{format_percent(summary['v3_top_20_benchmark_adjusted_success_rate'])}"
    )


if __name__ == "__main__":
    main()
