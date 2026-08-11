"""
Audit price-candidate evaluation integrity and ranking drift.

This report is diagnostic only. It does not change score weights, place orders,
or delete historical data.
"""

import sys
from datetime import datetime
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.evaluator.price_candidate_evaluator import direction_series


PROCESSED_DIR = Path("data/processed")
PREDICTIONS_DIR = Path("data/predictions")
RAW_DIR = Path("data/raw")
REPORT_DIR = Path("reports/daily_review")

RESULT_SUCCESS = "success"
RESULT_FAILURE = "failure"
RESULT_PENDING = "pending"
V2_VERSION = "v2_conservative_ranker"
RANK_BUCKETS = [("Top 10", 10), ("Top 20", 20), ("Top 50", 50), ("Top 100", 100)]
COMPONENT_COLUMNS = [
    "base_momentum_score",
    "volume_confirmation_score",
    "liquidity_score",
    "overextension_penalty",
    "reversal_risk_penalty",
    "news_risk_penalty",
    "attention_noise_penalty",
    "market_regime_penalty",
]


def latest_file(directory: Path, pattern: str):
    files = sorted(directory.glob(pattern))
    return files[-1] if files else None


def read_csv(path: Path | None) -> pd.DataFrame:
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


def normalize_stock_code(value) -> str:
    if value is None or pd.isna(value):
        return ""
    try:
        return str(int(float(value))).zfill(6)
    except Exception:
        return str(value).strip().zfill(6)


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


def date_value(df: pd.DataFrame, column: str) -> pd.Series:
    if column not in df.columns:
        return pd.Series([""], index=df.index, dtype=object)
    parsed = pd.to_datetime(df[column], errors="coerce")
    return parsed.dt.strftime("%Y-%m-%d").fillna(df[column].astype(str).replace("nan", ""))


def score_version_series(df: pd.DataFrame) -> pd.Series:
    if "score_version" not in df.columns:
        return pd.Series(["legacy_or_unknown"] * len(df), index=df.index, dtype=object)
    version = df["score_version"].astype(str).str.strip()
    return version.where(~version.isin(["", "nan", "None", "<NA>"]), "legacy_or_unknown")


def candidate_key_series(df: pd.DataFrame) -> pd.Series:
    if df.empty:
        return pd.Series(dtype=str)
    if "candidate_id" in df.columns:
        candidate_id = df["candidate_id"].astype(str).str.strip()
        valid = ~candidate_id.isin(["", "nan", "None", "<NA>"])
    else:
        candidate_id = pd.Series([""] * len(df), index=df.index, dtype=object)
        valid = pd.Series([False] * len(df), index=df.index)

    fallback = (
        df.get("stock_code", pd.Series([""] * len(df), index=df.index)).apply(normalize_stock_code)
        + "|"
        + date_value(df, "signal_date")
        + "|"
        + date_value(df, "prediction_date")
        + "|"
        + score_version_series(df)
    )
    return candidate_id.where(valid, fallback)


def exact_evaluation_key_series(df: pd.DataFrame) -> pd.Series:
    if df.empty:
        return pd.Series(dtype=str)
    return (
        df.get("stock_code", pd.Series([""] * len(df), index=df.index)).apply(normalize_stock_code)
        + "|"
        + date_value(df, "signal_date")
        + "|"
        + date_value(df, "prediction_date")
        + "|"
        + date_value(df, "evaluation_date")
        + "|"
        + score_version_series(df)
    )


def safe_percentage(numerator: int, denominator: int):
    if not denominator:
        return None
    return round(numerator / denominator * 100, 2)


def evaluated_mask(df: pd.DataFrame) -> pd.Series:
    return normalize_result_series(df).isin([RESULT_SUCCESS, RESULT_FAILURE])


def performance_summary(df: pd.DataFrame) -> dict:
    if df.empty:
        return {
            "evaluated_count": 0,
            "success_count": 0,
            "failure_count": 0,
            "success_rate": None,
            "avg_close_t1_return": None,
            "avg_close_t3_return": None,
            "avg_close_t5_return": None,
        }
    result = normalize_result_series(df)
    mask = result.isin([RESULT_SUCCESS, RESULT_FAILURE])
    success_count = int((result == RESULT_SUCCESS).sum())
    failure_count = int((result == RESULT_FAILURE).sum())
    evaluated_count = success_count + failure_count
    summary = {
        "evaluated_count": evaluated_count,
        "success_count": success_count,
        "failure_count": failure_count,
        "success_rate": safe_percentage(success_count, evaluated_count),
    }
    for column in ["close_t1_return", "close_t3_return", "close_t5_return"]:
        if column in df.columns and mask.any():
            value = pd.to_numeric(df.loc[mask, column], errors="coerce").mean()
            summary[f"avg_{column}"] = round(value, 4) if pd.notna(value) else None
        else:
            summary[f"avg_{column}"] = None
    return summary


def add_v2_daily_rank(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    result["diagnostic_rank_date"] = date_value(result, "signal_date")
    missing_date = result["diagnostic_rank_date"].isin(["", "NaT", "nan"])
    if missing_date.any():
        result.loc[missing_date, "diagnostic_rank_date"] = date_value(result.loc[missing_date], "prediction_date")

    score = pd.to_numeric(result.get("final_price_signal_score_v2"), errors="coerce")
    result["diagnostic_score_v2"] = score
    result["diagnostic_rank_v2"] = result.groupby("diagnostic_rank_date", dropna=False)[
        "diagnostic_score_v2"
    ].rank(method="first", ascending=False)
    return result


def rank_bucket_summary(v2_df: pd.DataFrame) -> list[dict]:
    if v2_df.empty:
        return []
    ranked = add_v2_daily_rank(v2_df)
    rows = []
    for label, end in RANK_BUCKETS:
        subset = ranked[ranked["diagnostic_rank_v2"] <= end]
        rows.append({"bucket": label, **performance_summary(subset)})
    return rows


def decile_summary(v2_df: pd.DataFrame) -> tuple[list[dict], str]:
    if v2_df.empty or "final_price_signal_score_v2" not in v2_df.columns:
        return [], "Insufficient v2 data"
    working = v2_df.copy()
    working["score_numeric"] = pd.to_numeric(working["final_price_signal_score_v2"], errors="coerce")
    working = working[working["score_numeric"].notna()].copy()
    working = working[evaluated_mask(working)].copy()
    if len(working) < 20:
        return [], "Insufficient v2 data"
    try:
        working["score_decile"] = pd.qcut(
            working["score_numeric"].rank(method="first"),
            10,
            labels=[f"D{i}" for i in range(1, 11)],
        )
    except Exception:
        return [], "Insufficient v2 data"

    rows = []
    for decile, group in working.groupby("score_decile", observed=False):
        row = {"decile": str(decile), **performance_summary(group)}
        row["avg_final_price_signal_score_v2"] = round(group["score_numeric"].mean(), 2)
        rows.append(row)

    low = pd.DataFrame(rows[:3])
    high = pd.DataFrame(rows[-3:])
    low_rate = low["success_rate"].dropna().mean() if not low.empty else None
    high_rate = high["success_rate"].dropna().mean() if not high.empty else None
    if pd.isna(low_rate) or pd.isna(high_rate):
        diagnosis = "Insufficient v2 data"
    elif high_rate > low_rate + 3:
        diagnosis = "Ranking improving"
    elif low_rate > high_rate + 3:
        diagnosis = "Ranking inverted"
    else:
        diagnosis = "Ranking flat/random"
    return rows, diagnosis


def component_failure_audit(v2_df: pd.DataFrame) -> list[dict]:
    if v2_df.empty:
        return []
    result = normalize_result_series(v2_df)
    rows = []
    for column in COMPONENT_COLUMNS:
        if column not in v2_df.columns:
            continue
        values = pd.to_numeric(v2_df[column], errors="coerce")
        success_avg = values[result == RESULT_SUCCESS].mean()
        failure_avg = values[result == RESULT_FAILURE].mean()
        rows.append(
            {
                "component": column,
                "success_avg": round(success_avg, 4) if pd.notna(success_avg) else None,
                "failure_avg": round(failure_avg, 4) if pd.notna(failure_avg) else None,
                "failure_minus_success": round(failure_avg - success_avg, 4)
                if pd.notna(success_avg) and pd.notna(failure_avg)
                else None,
            }
        )
    return rows


def benchmark_audit(evaluations: pd.DataFrame, signals: pd.DataFrame) -> dict:
    benchmark_columns = ["benchmark_return_t1", "excess_return_t1", "success_excess_t1"]
    present = {column: column in evaluations.columns for column in benchmark_columns}
    total = len(evaluations)
    benchmark_available = 0
    excess_evaluated = 0
    excess_success_count = 0
    if present.get("benchmark_return_t1"):
        benchmark_available = int(pd.to_numeric(evaluations["benchmark_return_t1"], errors="coerce").notna().sum())
    if present.get("success_excess_t1"):
        excess = evaluations["success_excess_t1"].astype(str).str.lower()
        excess_evaluated = int(excess.isin([RESULT_SUCCESS, RESULT_FAILURE]).sum())
        excess_success_count = int((excess == RESULT_SUCCESS).sum())

    latest_market = latest_file(RAW_DIR, "market_index_*.csv")
    market_df = read_csv(latest_market)
    market_max_date = ""
    benchmark_rows = len(market_df)
    if not market_df.empty and "date" in market_df.columns:
        parsed = pd.to_datetime(market_df["date"], errors="coerce")
        if parsed.notna().any():
            market_max_date = parsed.max().strftime("%Y-%m-%d")

    signal_dates = pd.to_datetime(signals.get("signal_date"), errors="coerce") if not signals.empty else pd.Series(dtype="datetime64[ns]")
    latest_signal_date = signal_dates.max().strftime("%Y-%m-%d") if signal_dates.notna().any() else ""
    candidate_dates = pd.to_datetime(evaluations.get("signal_date"), errors="coerce") if not evaluations.empty else pd.Series(dtype="datetime64[ns]")
    latest_candidate_date = candidate_dates.max().strftime("%Y-%m-%d") if candidate_dates.notna().any() else latest_signal_date

    coverage_rate = safe_percentage(excess_evaluated, total)
    success_rate = safe_percentage(excess_success_count, excess_evaluated)
    if benchmark_rows == 0:
        status = "Missing"
    elif market_max_date and latest_signal_date and market_max_date < latest_signal_date:
        status = "Stale"
    elif excess_evaluated == 0:
        status = "Missing"
    elif coverage_rate is not None and coverage_rate < 90:
        status = "Partial"
    else:
        status = "Available"

    if excess_evaluated == 0 and market_max_date and latest_candidate_date and market_max_date < latest_candidate_date:
        finding = (
            f"Benchmark coverage is missing because latest market index data ends at {market_max_date}, "
            f"before latest price signal date {latest_candidate_date}."
        )
    elif excess_evaluated == 0:
        finding = "Benchmark columns exist but no benchmark-adjusted rows are evaluated."
    else:
        finding = "Benchmark-adjusted evaluation is partially available."

    return {
        "benchmark_columns_present": all(present.values()),
        "benchmark_rows_available": benchmark_rows,
        "benchmark_return_t1_available": benchmark_available,
        "benchmark_adjusted_evaluated": excess_evaluated,
        "benchmark_adjusted_success_count": excess_success_count,
        "benchmark_adjusted_success_rate": success_rate,
        "benchmark_adjusted_coverage_rate": coverage_rate,
        "benchmark_status": status,
        "latest_market_index_file": str(latest_market) if latest_market else "",
        "latest_market_index_date": market_max_date,
        "latest_price_signal_date": latest_signal_date,
        "latest_candidate_signal_date": latest_candidate_date,
        "finding": finding,
    }


def learned_rule_audit() -> dict:
    latest_rules_path = latest_file(PROCESSED_DIR, "learned_event_rules_*.csv")
    rules = read_csv(latest_rules_path)
    if rules.empty:
        return {
            "latest_rules_file": str(latest_rules_path) if latest_rules_path else "",
            "active_learned_rules": 0,
            "eligible_groups": 0,
            "close_to_activation_groups": 0,
            "finding": "No learned rule rows are available.",
            "criteria": "DART/error-note event_type groups, minimum 5 evaluated rows, neutral 45%-55% success gives zero adjustment.",
        }
    active = 0
    if "learned_event_score_adjustment" in rules.columns:
        active = int((pd.to_numeric(rules["learned_event_score_adjustment"], errors="coerce").fillna(0) != 0).sum())
    evaluated = pd.to_numeric(rules.get("evaluated_count", 0), errors="coerce").fillna(0)
    success_rate = pd.to_numeric(rules.get("success_rate", 0), errors="coerce").fillna(0)
    eligible = int((evaluated >= 5).sum())
    close_to_activation = int(((success_rate.between(0.40, 0.45, inclusive="left")) | (success_rate.between(0.55, 0.60))).sum())
    if active == 0:
        finding = (
            "Learned rules are inactive because the updater learns from DART error_notes event_type groups, "
            "not price-candidate v2 outcomes, and current eligible groups are in the neutral adjustment band."
        )
    else:
        finding = "Some learned event rules are active."
    return {
        "latest_rules_file": str(latest_rules_path),
        "active_learned_rules": active,
        "eligible_groups": eligible,
        "close_to_activation_groups": close_to_activation,
        "finding": finding,
        "criteria": "DART/error-note event_type groups, minimum 5 evaluated rows, neutral 45%-55% success gives zero adjustment.",
    }


def duplicate_examples(df: pd.DataFrame, key_column: str, limit=5) -> pd.DataFrame:
    if df.empty or key_column not in df.columns:
        return pd.DataFrame()
    counts = df[key_column].value_counts()
    duplicate_keys = counts[counts > 1].head(limit).index
    columns = [
        "stock_code",
        "signal_date",
        "prediction_date",
        "evaluation_date",
        "score_version",
        "candidate_id",
        "source_file",
        "prediction_result",
    ]
    columns = [column for column in columns if column in df.columns]
    return df[df[key_column].isin(duplicate_keys)][columns].head(limit * 3)


def table(rows: list[dict], columns: list[str]) -> list[str]:
    lines = ["| " + " | ".join(columns) + " |", "|" + "|".join(["---"] * len(columns)) + "|"]
    for row in rows:
        values = []
        for column in columns:
            value = row.get(column, "")
            if value is None or pd.isna(value):
                value = "N/A"
            values.append(str(value).replace("|", "/"))
        lines.append("| " + " | ".join(values) + " |")
    return lines


def dataframe_markdown(df: pd.DataFrame) -> str:
    if df.empty:
        return "No examples available."
    columns = list(df.columns)
    lines = ["| " + " | ".join(columns) + " |", "|" + "|".join(["---"] * len(columns)) + "|"]
    for _, row in df.iterrows():
        values = []
        for column in columns:
            value = row.get(column, "")
            if pd.isna(value):
                value = ""
            values.append(str(value).replace("|", "/"))
        lines.append("| " + " | ".join(values) + " |")
    return "\n".join(lines)


def build_audit() -> dict:
    evaluations = read_all_csv(PREDICTIONS_DIR, "price_candidate_evaluation_*.csv")
    candidates = read_all_csv(PROCESSED_DIR, "price_based_candidates_*.csv")
    signals = read_all_csv(PROCESSED_DIR, "daily_price_signals_*.csv")

    if not evaluations.empty and "stock_code" in evaluations.columns:
        evaluations["stock_code"] = evaluations["stock_code"].apply(normalize_stock_code)

    evaluations["integrity_candidate_key"] = candidate_key_series(evaluations)
    evaluations["integrity_exact_eval_key"] = exact_evaluation_key_series(evaluations)

    total_rows = len(evaluations)
    unique_candidate_keys = int(evaluations["integrity_candidate_key"].nunique()) if total_rows else 0
    duplicate_rows = max(total_rows - unique_candidate_keys, 0)
    exact_unique_keys = int(evaluations["integrity_exact_eval_key"].nunique()) if total_rows else 0
    exact_duplicate_rows = max(total_rows - exact_unique_keys, 0)
    duplicate_rate = safe_percentage(duplicate_rows, total_rows)

    stock_signal_counts = 0
    if not evaluations.empty and {"stock_code", "signal_date"}.issubset(evaluations.columns):
        stock_signal_counts = int(
            evaluations.groupby(["stock_code", "signal_date"], dropna=False).size().gt(1).sum()
        )

    source_repeats = 0
    if not evaluations.empty:
        source_repeats = int(
            evaluations.groupby("integrity_candidate_key")["source_file"].nunique().gt(1).sum()
        )

    result = normalize_result_series(evaluations)
    v2_mask = score_version_series(evaluations).eq(V2_VERSION)
    evaluated = result.isin([RESULT_SUCCESS, RESULT_FAILURE])
    v2_eval = evaluations[v2_mask & evaluated].copy()
    legacy_eval = evaluations[~v2_mask & evaluated].copy()

    v2_rank_rows = rank_bucket_summary(v2_eval)
    decile_rows, decile_diagnosis = decile_summary(v2_eval)
    component_rows = component_failure_audit(v2_eval)
    benchmark = benchmark_audit(evaluations, signals)
    learned = learned_rule_audit()

    v2_eval = v2_eval.copy()
    v2_eval["candidate_direction"] = direction_series(v2_eval)
    v2_buy_eval = v2_eval[v2_eval["candidate_direction"] == "buy"]
    v2_avoid_eval = v2_eval[v2_eval["candidate_direction"] == "avoid"]
    v2_buy_performance = performance_summary(v2_buy_eval)
    v2_avoid_performance = performance_summary(v2_avoid_eval)

    top20_rate = next((row["success_rate"] for row in v2_rank_rows if row["bucket"] == "Top 20"), None)
    v2_success_rate = performance_summary(v2_eval)["success_rate"]
    if top20_rate is None or len(v2_eval) < 30:
        ranking_status = "Insufficient v2 data"
    elif v2_success_rate is not None and top20_rate < v2_success_rate - 3:
        ranking_status = "Ranking inverted"
    elif v2_success_rate is not None and top20_rate > v2_success_rate + 3:
        ranking_status = "Ranking improving"
    else:
        ranking_status = "Ranking weak"

    benchmark_status = benchmark["benchmark_status"]
    duplicate_status = "Possible duplicates" if duplicate_rows > 0 else "Evaluation clean"

    return {
        "evaluations": evaluations,
        "candidates": candidates,
        "signals": signals,
        "summary": {
            "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_evaluation_rows": total_rows,
            "unique_evaluation_keys": unique_candidate_keys,
            "duplicate_rows": duplicate_rows,
            "duplicate_rate": duplicate_rate,
            "exact_duplicate_rows": exact_duplicate_rows,
            "same_stock_signal_repeated_keys": stock_signal_counts,
            "candidate_reevaluated_across_files": source_repeats,
            "cumulative_evaluated_cases_may_be_inflated": duplicate_rows > 0,
            "candidate_file_rows": len(candidates),
            "signal_file_rows": len(signals),
            "v1_unknown_evaluated_count": performance_summary(legacy_eval)["evaluated_count"],
            "v1_unknown_success_rate": performance_summary(legacy_eval)["success_rate"],
            "v2_evaluated_count": performance_summary(v2_eval)["evaluated_count"],
            "v2_success_rate": v2_success_rate,
            "v2_avg_close_t1_return": performance_summary(v2_eval)["avg_close_t1_return"],
            "v2_avg_close_t3_return": performance_summary(v2_eval)["avg_close_t3_return"],
            "v2_avg_close_t5_return": performance_summary(v2_eval)["avg_close_t5_return"],
            "v2_top_10_success_rate": next((row["success_rate"] for row in v2_rank_rows if row["bucket"] == "Top 10"), None),
            "v2_top_20_success_rate": top20_rate,
            "v2_top_50_success_rate": next((row["success_rate"] for row in v2_rank_rows if row["bucket"] == "Top 50"), None),
            "v2_top_100_success_rate": next((row["success_rate"] for row in v2_rank_rows if row["bucket"] == "Top 100"), None),
            "ranking_status": ranking_status,
            "score_decile_diagnosis": decile_diagnosis,
            "benchmark_adjusted_evaluated": benchmark["benchmark_adjusted_evaluated"],
            "benchmark_adjusted_coverage_rate": benchmark["benchmark_adjusted_coverage_rate"],
            "benchmark_adjusted_success_rate": benchmark["benchmark_adjusted_success_rate"],
            "benchmark_rows_available": benchmark["benchmark_rows_available"],
            "benchmark_latest_date": benchmark["latest_market_index_date"],
            "price_signal_latest_date": benchmark["latest_price_signal_date"],
            "benchmark_status": benchmark_status,
            "duplicate_status": duplicate_status,
            "active_learned_rules": learned["active_learned_rules"],
            "learned_rule_finding": learned["finding"],
            "benchmark_finding": benchmark["finding"],
            "v2_buy_evaluated_count": v2_buy_performance["evaluated_count"],
            "v2_buy_success_rate": v2_buy_performance["success_rate"],
            "v2_buy_avg_close_t1_return": v2_buy_performance["avg_close_t1_return"],
            "v2_buy_avg_close_t3_return": v2_buy_performance["avg_close_t3_return"],
            "v2_buy_avg_close_t5_return": v2_buy_performance["avg_close_t5_return"],
            "v2_avoid_evaluated_count": v2_avoid_performance["evaluated_count"],
            "v2_avoid_success_rate": v2_avoid_performance["success_rate"],
            "v2_avoid_avg_close_t1_return": v2_avoid_performance["avg_close_t1_return"],
            "v2_avoid_avg_close_t3_return": v2_avoid_performance["avg_close_t3_return"],
            "v2_avoid_avg_close_t5_return": v2_avoid_performance["avg_close_t5_return"],
        },
        "legacy_performance": performance_summary(legacy_eval),
        "v2_performance": performance_summary(v2_eval),
        "v2_buy_performance": v2_buy_performance,
        "v2_avoid_performance": v2_avoid_performance,
        "v2_rank_rows": v2_rank_rows,
        "decile_rows": decile_rows,
        "component_rows": component_rows,
        "benchmark": benchmark,
        "learned": learned,
        "duplicate_examples": duplicate_examples(evaluations, "integrity_candidate_key"),
        "exact_duplicate_examples": duplicate_examples(evaluations, "integrity_exact_eval_key"),
    }


def write_report(audit: dict) -> tuple[Path, Path]:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    today_display = datetime.today().strftime("%Y-%m-%d")
    today_file = datetime.today().strftime("%Y%m%d")
    report_path = REPORT_DIR / f"{today_display}_evaluation_integrity_audit.md"
    summary_path = PROCESSED_DIR / f"evaluation_integrity_audit_summary_{today_file}.csv"
    summary = audit["summary"]

    lines = [
        f"# Evaluation Integrity Audit - {today_display}",
        "",
        "This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.",
        "",
        "## Duplicate and Leakage Audit",
        "",
        f"- Total evaluation rows: **{summary['total_evaluation_rows']}**",
        f"- Unique evaluation keys: **{summary['unique_evaluation_keys']}**",
        f"- Duplicate rows by candidate key: **{summary['duplicate_rows']}**",
        f"- Duplicate rate: **{summary['duplicate_rate']}%**",
        f"- Exact same-day duplicate rows: **{summary['exact_duplicate_rows']}**",
        f"- Same stock_code + signal_date repeated keys: **{summary['same_stock_signal_repeated_keys']}**",
        f"- Same candidate re-evaluated across multiple files: **{summary['candidate_reevaluated_across_files']}**",
        f"- Cumulative evaluated cases may be inflated: **{summary['cumulative_evaluated_cases_may_be_inflated']}**",
        "",
        "Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.",
        "",
        "### Duplicate Examples",
        "",
        dataframe_markdown(audit["duplicate_examples"]),
        "",
        "## v1 vs v2 Performance",
        "",
        *table(
            [
                {"score_version": "v1/unknown", **audit["legacy_performance"]},
                {"score_version": V2_VERSION, **audit["v2_performance"]},
            ],
            [
                "score_version",
                "evaluated_count",
                "success_count",
                "failure_count",
                "success_rate",
                "avg_close_t1_return",
                "avg_close_t3_return",
                "avg_close_t5_return",
            ],
        ),
        "",
        "## v2 Directional Breakdown (Buy vs Avoid)",
        "",
        "Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.",
        "",
        *table(
            [
                {"direction": "buy", **audit["v2_buy_performance"]},
                {"direction": "avoid", **audit["v2_avoid_performance"]},
            ],
            [
                "direction",
                "evaluated_count",
                "success_count",
                "failure_count",
                "success_rate",
                "avg_close_t1_return",
                "avg_close_t3_return",
                "avg_close_t5_return",
            ],
        ),
        "",
        "## v2 Rank Bucket Performance",
        "",
        *table(
            audit["v2_rank_rows"],
            [
                "bucket",
                "evaluated_count",
                "success_count",
                "failure_count",
                "success_rate",
                "avg_close_t1_return",
                "avg_close_t3_return",
                "avg_close_t5_return",
            ],
        ),
        "",
        f"Ranking status: **{summary['ranking_status']}**",
        f"Score decile diagnosis: **{summary['score_decile_diagnosis']}**",
        "",
        "## v2 Score Deciles",
        "",
        *table(
            audit["decile_rows"],
            [
                "decile",
                "evaluated_count",
                "success_count",
                "failure_count",
                "success_rate",
                "avg_final_price_signal_score_v2",
                "avg_close_t1_return",
                "avg_close_t3_return",
                "avg_close_t5_return",
            ],
        ),
        "",
        "## v2 Component Failure Associations",
        "",
        *table(audit["component_rows"], ["component", "success_avg", "failure_avg", "failure_minus_success"]),
        "",
        "## Benchmark-Adjusted Evaluation Audit",
        "",
        f"- Benchmark-adjusted evaluated cases: **{summary['benchmark_adjusted_evaluated']}**",
        f"- Benchmark-adjusted coverage: **{summary['benchmark_adjusted_coverage_rate']}%**",
        f"- Benchmark-adjusted success rate: **{summary['benchmark_adjusted_success_rate']}%**",
        f"- Benchmark rows available: **{summary['benchmark_rows_available']}**",
        f"- Benchmark status: **{summary['benchmark_status']}**",
        f"- Latest market index file: `{audit['benchmark']['latest_market_index_file']}`",
        f"- Latest market index date: **{audit['benchmark']['latest_market_index_date']}**",
        f"- Latest price signal date: **{audit['benchmark']['latest_price_signal_date']}**",
        f"- Latest candidate signal date: **{audit['benchmark']['latest_candidate_signal_date']}**",
        f"- Finding: {summary['benchmark_finding']}",
        "",
        "## Learning Loop Audit",
        "",
        f"- Active learned rules: **{summary['active_learned_rules']}**",
        f"- Eligible groups: **{audit['learned']['eligible_groups']}**",
        f"- Groups close to activation: **{audit['learned']['close_to_activation_groups']}**",
        f"- Criteria: {audit['learned']['criteria']}",
        f"- Finding: {summary['learned_rule_finding']}",
        "",
        "## Dashboard Status Flags",
        "",
        f"- Duplicate status: **{summary['duplicate_status']}**",
        f"- Benchmark status: **{summary['benchmark_status']}**",
        f"- Ranking status: **{summary['ranking_status']}**",
        "",
        "## Next Diagnostic Recommendations",
        "",
        "- Deduplicate cumulative dashboard learning metrics by the recommended candidate-level key before interpreting reliability.",
        "- Refresh or extend market index data past the latest candidate dates before expecting benchmark-adjusted coverage.",
        "- Add price-signal component groups as a separate learning loop rather than relying on DART event_type learned rules.",
        "- Do not change v2 score weights until duplicate inflation and benchmark coverage are handled.",
    ]

    report_path.write_text("\n".join(lines), encoding="utf-8")
    pd.DataFrame([summary]).to_csv(summary_path, index=False, encoding="utf-8-sig")
    return report_path, summary_path


def main():
    print("Generating evaluation integrity audit...")
    audit = build_audit()
    report_path, summary_path = write_report(audit)
    summary = audit["summary"]
    print(f"Evaluation integrity audit saved to: {report_path}")
    print(f"Evaluation integrity summary saved to: {summary_path}")
    print(f"total evaluation rows: {summary['total_evaluation_rows']}")
    print(f"unique evaluation keys: {summary['unique_evaluation_keys']}")
    print(f"duplicate count: {summary['duplicate_rows']}")
    print(f"duplicate rate: {summary['duplicate_rate']}%")
    print(f"v1/unknown success rate: {summary['v1_unknown_success_rate']}%")
    print(f"v2 success rate: {summary['v2_success_rate']}%")
    print(f"v2 Top 10 success rate: {summary['v2_top_10_success_rate']}%")
    print(f"v2 Top 20 success rate: {summary['v2_top_20_success_rate']}%")
    print(f"v2 Top 50 success rate: {summary['v2_top_50_success_rate']}%")
    print(f"v2 Top 100 success rate: {summary['v2_top_100_success_rate']}%")
    print(f"ranking appears: {summary['ranking_status']}")
    print(f"benchmark-adjusted coverage: {summary['benchmark_adjusted_coverage_rate']}%")
    print(f"benchmark-adjusted evaluated cases: {summary['benchmark_adjusted_evaluated']}")
    print(f"benchmark-adjusted success rate: {summary['benchmark_adjusted_success_rate']}%")
    print(f"benchmark latest date: {summary['benchmark_latest_date']}")
    print(f"price signal latest date: {summary['price_signal_latest_date']}")
    print(f"learned rules finding: {summary['learned_rule_finding']}")
    print(f"v2 buy-type: {summary['v2_buy_evaluated_count']} evaluated, {summary['v2_buy_success_rate']}% success rate")
    print(f"v2 avoid-type: {summary['v2_avoid_evaluated_count']} evaluated, {summary['v2_avoid_success_rate']}% success rate")


if __name__ == "__main__":
    main()
