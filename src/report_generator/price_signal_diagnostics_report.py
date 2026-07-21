"""
Generate price-signal diagnostics for the broad candidate pool and ranked picks.

This report is diagnostic only. It does not place orders or reduce the candidate
pool used for learning and evaluation.
"""

import sys
from datetime import datetime
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.evaluation.metrics import reliability_score_from_wilson, safe_percentage
from src.storage.schema import RESULT_FAILURE, RESULT_PENDING, RESULT_SUCCESS


PROCESSED_DIR = Path("data/processed")
PREDICTIONS_DIR = Path("data/predictions")
REPORT_DIR = Path("reports/daily_review")

RANK_BUCKETS = [
    ("Top 10", 10),
    ("Top 20", 20),
    ("Top 50", 50),
    ("Top 100", 100),
    ("Rest", None),
]


def latest_file(directory: Path, pattern: str):
    files = sorted(directory.glob(pattern))
    return files[-1] if files else None


def read_csv(path):
    if path is None or not path.exists():
        return pd.DataFrame()

    try:
        return pd.read_csv(path)
    except Exception as error:
        print(f"Failed to read {path}: {error}")
        return pd.DataFrame()


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
            series = df[column].astype(str).str.lower()
            valid = ~series.isin(["", "nan", "none", "<na>"])
            missing = result.isin([RESULT_PENDING]) & valid
            result.loc[missing] = series.loc[missing]

    return result


def score_columns(df: pd.DataFrame) -> list[str]:
    return [
        column
        for column in ["final_price_signal_score", "prediction_score", "price_candidate_score"]
        if column in df.columns
    ]


def coalesced_score(df: pd.DataFrame) -> pd.Series:
    score = pd.Series(pd.NA, index=df.index, dtype="Float64")

    for column in score_columns(df):
        values = pd.to_numeric(df[column], errors="coerce")
        score = score.fillna(values)

    return score


def coalesced_rank_date(df: pd.DataFrame) -> pd.Series:
    dates = pd.Series(pd.NaT, index=df.index, dtype="datetime64[ns]")

    for column in ["signal_date", "prediction_date", "candidate_date"]:
        if column in df.columns:
            parsed = pd.to_datetime(df[column], errors="coerce")
            dates = dates.fillna(parsed)

    return dates.dt.strftime("%Y-%m-%d").fillna("unknown")


def ensure_candidate_rank(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    result["diagnostic_rank_date"] = coalesced_rank_date(result)
    result["diagnostic_score"] = coalesced_score(result)

    if "candidate_rank" in result.columns:
        result["source_candidate_rank"] = pd.to_numeric(result["candidate_rank"], errors="coerce")
    else:
        result["source_candidate_rank"] = pd.NA

    if result["diagnostic_score"].notna().any():
        result["candidate_rank"] = result.groupby(
            "diagnostic_rank_date",
            dropna=False,
        )["diagnostic_score"].rank(
            method="first",
            ascending=False,
        )
    else:
        result["candidate_rank"] = result["source_candidate_rank"]

    missing_rank = result["candidate_rank"].isna()
    if missing_rank.any():
        result.loc[missing_rank, "candidate_rank"] = result.loc[missing_rank, "source_candidate_rank"]

    result["candidate_rank"] = pd.to_numeric(result["candidate_rank"], errors="coerce")
    return result


def add_rank_bucket(df: pd.DataFrame) -> pd.DataFrame:
    result = ensure_candidate_rank(df)
    result["rank_bucket"] = "Unknown"

    result.loc[result["candidate_rank"] <= 10, "rank_bucket"] = "Top 10"
    result.loc[(result["candidate_rank"] > 10) & (result["candidate_rank"] <= 20), "rank_bucket"] = "Rank 11-20"
    result.loc[(result["candidate_rank"] > 20) & (result["candidate_rank"] <= 50), "rank_bucket"] = "Rank 21-50"
    result.loc[(result["candidate_rank"] > 50) & (result["candidate_rank"] <= 100), "rank_bucket"] = "Rank 51-100"
    result.loc[result["candidate_rank"] > 100, "rank_bucket"] = "Rest"

    return result


def rank_bucket_mask(df: pd.DataFrame, end):
    if "candidate_rank" not in df.columns:
        return pd.Series(False, index=df.index)
    if end is None:
        return df["candidate_rank"] > 100
    return df["candidate_rank"] <= end


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

    result_series = normalize_result_series(df)
    evaluated = result_series.isin([RESULT_SUCCESS, RESULT_FAILURE])
    success_count = int((result_series == RESULT_SUCCESS).sum())
    failure_count = int((result_series == RESULT_FAILURE).sum())
    evaluated_count = success_count + failure_count

    avg_close = None
    avg_excess = None

    if "close_t1_return" in df.columns and evaluated.any():
        close_values = pd.to_numeric(df.loc[evaluated, "close_t1_return"], errors="coerce")
        if close_values.notna().sum() == 0 and "next_close_return" in df.columns:
            close_values = pd.to_numeric(df.loc[evaluated, "next_close_return"], errors="coerce")
        avg_close = close_values.mean()
    elif "next_close_return" in df.columns and evaluated.any():
        avg_close = pd.to_numeric(df.loc[evaluated, "next_close_return"], errors="coerce").mean()

    if "excess_return_t1" in df.columns and evaluated.any():
        avg_excess = pd.to_numeric(df.loc[evaluated, "excess_return_t1"], errors="coerce").mean()

    return {
        "evaluated_count": evaluated_count,
        "success_count": success_count,
        "failure_count": failure_count,
        "success_rate": round(safe_percentage(success_count, evaluated_count), 2)
        if evaluated_count
        else None,
        "avg_close_t1_return": round(avg_close, 4) if pd.notna(avg_close) else None,
        "avg_excess_t1_return": round(avg_excess, 4) if pd.notna(avg_excess) else None,
    }


def rolling_success_rate(df: pd.DataFrame, days: int):
    if df.empty:
        return None

    dates = pd.Series(pd.NaT, index=df.index, dtype="datetime64[ns]")
    for column in ["evaluation_date", "evaluated_at", "signal_date", "candidate_date"]:
        if column in df.columns:
            dates = dates.fillna(pd.to_datetime(df[column], errors="coerce"))

    results = normalize_result_series(df)
    evaluated = results.isin([RESULT_SUCCESS, RESULT_FAILURE]) & dates.notna()
    if not evaluated.any():
        return None

    latest_date = dates[evaluated].max()
    cutoff = latest_date - pd.Timedelta(days=days - 1)
    mask = evaluated & (dates >= cutoff) & (dates <= latest_date)

    if not mask.any():
        return None

    return round(safe_percentage(int((results[mask] == RESULT_SUCCESS).sum()), int(mask.sum())), 2)


def bucket_score(value):
    numeric = pd.to_numeric(value, errors="coerce")
    if pd.isna(numeric):
        return "unknown"
    if numeric >= 80:
        return "very_high"
    if numeric >= 65:
        return "high"
    if numeric >= 50:
        return "medium"
    return "low"


def summarize_score_buckets(df: pd.DataFrame, column: str) -> list[dict]:
    if df.empty or column not in df.columns:
        return []

    working = df.copy()
    working[f"{column}_bucket"] = working[column].apply(bucket_score)
    rows = []

    for bucket in ["very_high", "high", "medium", "low", "unknown"]:
        summary = summarize_subset(working[working[f"{column}_bucket"] == bucket])
        rows.append({"bucket": bucket, **summary})

    return rows


def summarize_optional_bucket(df: pd.DataFrame, source_column: str, label: str) -> list[dict]:
    if df.empty or source_column not in df.columns:
        return []

    working = df.copy()
    working[source_column] = working[source_column].astype(str).fillna("unknown")
    rows = []

    for bucket, group in working.groupby(source_column, dropna=False):
        rows.append({"diagnostic": label, "bucket": str(bucket), **summarize_subset(group)})

    return rows


def examples(df: pd.DataFrame, condition, limit=5) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame()

    try:
        subset = df[condition(df)].copy()
    except Exception:
        return pd.DataFrame()

    cols = [
        "stock_code",
        "stock_name",
        "corp_name",
        "signal_date",
        "prediction_date",
        "candidate_rank",
        "final_price_signal_score",
        "prediction_score",
        "price_candidate_score",
        "volume_ratio_20d",
        "close_t1_return",
        "excess_return_t1",
        "prediction_result",
    ]
    cols = [col for col in cols if col in subset.columns]
    return subset[cols].head(limit)


def build_diagnostics():
    evaluations = add_rank_bucket(read_all_csv(PREDICTIONS_DIR, "price_candidate_evaluation_*.csv"))
    candidates = add_rank_bucket(read_all_csv(PROCESSED_DIR, "price_based_candidates_*.csv"))
    signals = read_all_csv(PROCESSED_DIR, "daily_price_signals_*.csv")
    latest_candidates = read_csv(latest_file(PROCESSED_DIR, "price_based_candidates_*.csv"))

    results = normalize_result_series(evaluations)
    success_count = int((results == RESULT_SUCCESS).sum())
    failure_count = int((results == RESULT_FAILURE).sum())
    pending_count = int((results == RESULT_PENDING).sum())
    evaluated_count = success_count + failure_count
    raw_success_rate = round(safe_percentage(success_count, evaluated_count), 2) if evaluated_count else None
    reliability_score = round(reliability_score_from_wilson(success_count, evaluated_count), 1)

    rank_rows = []
    for label, end in RANK_BUCKETS:
        rank_rows.append({"rank_bucket": label, **summarize_subset(evaluations[rank_bucket_mask(evaluations, end)])})

    score_rows = {}
    for column in ["prediction_score", "final_price_signal_score", "price_candidate_score"]:
        score_rows[column] = summarize_score_buckets(evaluations, column)

    optional_rows = []
    optional_specs = [
        ("volume_ratio_20d", "volume_ratio_bucket"),
        ("abnormal_volume_bucket", "abnormal_volume_bucket"),
        ("social_risk_label", "risk_noise_bucket"),
        ("social_attention_label", "social_attention_bucket"),
        ("market_regime_bucket", "market_regime_bucket"),
    ]
    for column, label in optional_specs:
        if column == "volume_ratio_20d" and column in evaluations.columns:
            working = evaluations.copy()
            volume = pd.to_numeric(working[column], errors="coerce")
            working["volume_ratio_bucket"] = "unknown"
            working.loc[volume >= 3, "volume_ratio_bucket"] = "very_high"
            working.loc[(volume >= 1.5) & (volume < 3), "volume_ratio_bucket"] = "high"
            working.loc[(volume > 0) & (volume < 1.5), "volume_ratio_bucket"] = "normal"
            optional_rows.extend(summarize_optional_bucket(working, "volume_ratio_bucket", label))
        else:
            optional_rows.extend(summarize_optional_bucket(evaluations, column, label))

    score_series = coalesced_score(evaluations).fillna(0)
    volume_series = pd.to_numeric(evaluations.get("volume_ratio_20d", 0), errors="coerce")
    result_series = normalize_result_series(evaluations)

    example_groups = {
        "High score but failed": examples(evaluations, lambda df: (score_series >= 65) & (result_series == RESULT_FAILURE)),
        "High volume but failed": examples(evaluations, lambda df: (volume_series >= 2) & (result_series == RESULT_FAILURE)),
        "High risk noise and failed": examples(
            evaluations,
            lambda df: df.get("social_risk_label", pd.Series("", index=df.index)).astype(str).ne("")
            & df.get("social_risk_label", pd.Series("", index=df.index)).astype(str).ne("no_risk_noise")
            & (result_series == RESULT_FAILURE),
        ),
        "Low score but succeeded": examples(evaluations, lambda df: (score_series < 50) & (result_series == RESULT_SUCCESS)),
    }

    top_lookup = {row["rank_bucket"]: row for row in rank_rows}
    top10_rate = top_lookup.get("Top 10", {}).get("success_rate")
    top20_rate = top_lookup.get("Top 20", {}).get("success_rate")
    overall = raw_success_rate

    if overall is None:
        judgment_en = "Insufficient evaluated price-candidate data to judge ranking quality."
        judgment_ko = "평가 완료된 가격 후보 데이터가 부족하여 랭킹 품질을 판단하기 어렵습니다."
    elif (top10_rate is not None and top10_rate > overall) or (top20_rate is not None and top20_rate > overall):
        judgment_en = "Top-ranked candidates show some outperformance versus the broad pool, but continued data accumulation is needed."
        judgment_ko = "상위 후보가 전체 후보 풀 대비 일부 초과 성과를 보이나, 추가 데이터 누적이 필요합니다."
    elif 45 <= overall <= 55:
        judgment_en = "Overall performance remains close to random; ranking quality is not yet clearly proven."
        judgment_ko = "전체 성과가 아직 무작위에 가까우며, 랭킹 품질은 명확히 입증되지 않았습니다."
    else:
        judgment_en = "Ranking quality is still mixed; monitor Top 10 and Top 20 against the full pool over more evaluations."
        judgment_ko = "랭킹 품질은 아직 혼재되어 있으므로 Top 10/Top 20과 전체 후보 풀을 더 비교해야 합니다."

    latest_selected_count = 0
    if not latest_candidates.empty and "selected_pick" in latest_candidates.columns:
        latest_selected_count = int(latest_candidates["selected_pick"].astype(str).str.lower().isin(["true", "1", "yes"]).sum())

    summary = {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "evaluated_count": evaluated_count,
        "success_count": success_count,
        "failure_count": failure_count,
        "pending_count": pending_count,
        "raw_success_rate": raw_success_rate,
        "wilson_reliability_score": reliability_score,
        "rolling_7d_success_rate": rolling_success_rate(evaluations, 7),
        "rolling_30d_success_rate": rolling_success_rate(evaluations, 30),
        "top_10_success_rate": top_lookup.get("Top 10", {}).get("success_rate"),
        "top_20_success_rate": top_lookup.get("Top 20", {}).get("success_rate"),
        "top_50_success_rate": top_lookup.get("Top 50", {}).get("success_rate"),
        "top_100_success_rate": top_lookup.get("Top 100", {}).get("success_rate"),
        "top_10_evaluated_count": top_lookup.get("Top 10", {}).get("evaluated_count", 0),
        "top_20_evaluated_count": top_lookup.get("Top 20", {}).get("evaluated_count", 0),
        "top_50_evaluated_count": top_lookup.get("Top 50", {}).get("evaluated_count", 0),
        "top_100_evaluated_count": top_lookup.get("Top 100", {}).get("evaluated_count", 0),
        "candidate_pool_today": len(latest_candidates),
        "selected_picks_today": latest_selected_count,
        "daily_signal_rows": len(signals),
        "judgment_en": judgment_en,
        "judgment_ko": judgment_ko,
    }

    return {
        "summary": summary,
        "rank_rows": rank_rows,
        "score_rows": score_rows,
        "optional_rows": optional_rows,
        "example_groups": example_groups,
    }


def format_percent(value):
    if value is None or pd.isna(value):
        return "Insufficient data / 데이터 부족"
    return f"{float(value):.2f}%"


def format_return(value):
    if value is None or pd.isna(value):
        return "N/A"
    return f"{float(value) * 100:.2f}%"


def table_rows(rows, name_column):
    lines = [
        f"| {'bucket' if name_column == 'rank_bucket' else name_column} | Evaluated | Success | Failure | Success Rate | Avg Close T1 | Avg Excess T1 |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| {name} | {evaluated} | {success} | {failure} | {rate} | {close} | {excess} |".format(
                name=row.get(name_column, row.get("bucket", row.get("rank_bucket", ""))),
                evaluated=row.get("evaluated_count", 0),
                success=row.get("success_count", 0),
                failure=row.get("failure_count", 0),
                rate=format_percent(row.get("success_rate")),
                close=format_return(row.get("avg_close_t1_return")),
                excess=format_return(row.get("avg_excess_t1_return")),
            )
        )
    return lines


def dataframe_to_markdown(df: pd.DataFrame) -> str:
    if df.empty:
        return "No examples available."

    columns = list(df.columns)
    lines = [
        "| " + " | ".join(columns) + " |",
        "|" + "|".join(["---"] * len(columns)) + "|",
    ]

    for _, row in df.iterrows():
        values = []
        for column in columns:
            value = row.get(column, "")
            if pd.isna(value):
                value = ""
            values.append(str(value).replace("|", "/"))
        lines.append("| " + " | ".join(values) + " |")

    return "\n".join(lines)


def write_report(data):
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    today_display = datetime.today().strftime("%Y-%m-%d")
    today_file = datetime.today().strftime("%Y%m%d")
    report_path = REPORT_DIR / f"{today_display}_price_signal_diagnostics_report.md"
    summary_path = PROCESSED_DIR / f"price_signal_diagnostics_summary_{today_file}.csv"
    summary = data["summary"]

    lines = [
        f"# Price Signal Diagnostics Report - {today_display}",
        "",
        "This diagnostic report evaluates ranking quality for the broad KIS price-candidate pool. It is not investment advice.",
        "이 진단 리포트는 KIS 가격 후보 풀의 랭킹 품질을 점검하기 위한 것이며 투자 조언이 아닙니다.",
        "",
        "## Overall Performance",
        "",
        f"- Cumulative evaluated cases: **{summary['evaluated_count']}**",
        f"- Success count: **{summary['success_count']}**",
        f"- Failure count: **{summary['failure_count']}**",
        f"- Pending count: **{summary['pending_count']}**",
        f"- Raw success rate: **{format_percent(summary['raw_success_rate'])}**",
        f"- Wilson reliability score: **{summary['wilson_reliability_score']} / 100**",
        f"- Rolling 7-day success rate: **{format_percent(summary['rolling_7d_success_rate'])}**",
        f"- Rolling 30-day success rate: **{format_percent(summary['rolling_30d_success_rate'])}**",
        "",
        "## Rank Bucket Performance",
        "",
        "Ranks are recalculated within each signal/prediction day using final_price_signal_score, prediction_score, then price_candidate_score as fallback. Each Top N row below is cumulative per day before being aggregated across all evaluated days.",
        "랭킹은 각 signal/prediction 일자 안에서 점수 기준으로 다시 계산하며, 각 Top N은 일별 누적 구간을 전체 평가일에 걸쳐 집계한 값입니다.",
        "",
        *table_rows(data["rank_rows"], "rank_bucket"),
        "",
        "## Score Bucket Performance",
        "",
    ]

    for column, rows in data["score_rows"].items():
        lines.extend([f"### {column}", ""])
        if rows:
            lines.extend(table_rows(rows, "bucket"))
        else:
            lines.append("Insufficient data / 데이터 부족")
        lines.append("")

    lines.extend(["## Volume and Supplementary Signal Diagnostics", ""])
    if data["optional_rows"]:
        for diagnostic, group in pd.DataFrame(data["optional_rows"]).groupby("diagnostic"):
            lines.extend([f"### {diagnostic}", ""])
            lines.extend(table_rows(group.to_dict("records"), "bucket"))
            lines.append("")
    else:
        lines.append("Insufficient data / 데이터 부족")
        lines.append("")

    lines.extend(["## Failure Clusters", ""])
    for title, frame in data["example_groups"].items():
        lines.extend([f"### {title}", ""])
        if frame.empty:
            lines.append("No examples available.")
        else:
            lines.append(dataframe_to_markdown(frame))
        lines.append("")

    lines.extend(
        [
            "## Summary Judgment",
            "",
            f"- {summary['judgment_en']}",
            f"- {summary['judgment_ko']}",
            "",
            "Large candidate pools improve statistical reliability. Selected picks are a smaller top-ranked subset for focused monitoring.",
            "큰 후보 풀은 통계적 신뢰도 측정에 도움이 되며, 선별 후보는 집중 모니터링용 상위 후보입니다.",
        ]
    )

    report_path.write_text("\n".join(lines), encoding="utf-8")
    pd.DataFrame([summary]).to_csv(summary_path, index=False, encoding="utf-8-sig")
    return report_path, summary_path


def main():
    print("Generating price signal diagnostics report...")
    data = build_diagnostics()
    report_path, summary_path = write_report(data)
    summary = data["summary"]

    print(f"Diagnostics report saved to: {report_path}")
    print(f"Diagnostics summary saved to: {summary_path}")
    print(f"overall price success rate: {format_percent(summary['raw_success_rate'])}")
    print(f"Wilson reliability score: {summary['wilson_reliability_score']}")
    print(f"Top 10 success rate: {format_percent(summary['top_10_success_rate'])}")
    print(f"Top 20 success rate: {format_percent(summary['top_20_success_rate'])}")
    print(f"Top 50 success rate: {format_percent(summary['top_50_success_rate'])}")
    print(f"Top 100 success rate: {format_percent(summary['top_100_success_rate'])}")
    print(f"candidate pool today: {summary['candidate_pool_today']}")
    print(f"selected picks today: {summary['selected_picks_today']}")


if __name__ == "__main__":
    main()
