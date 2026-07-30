"""
Learn diagnostic rules from price-candidate evaluation outcomes.

This is a research-only learning layer. It does not change candidate scoring,
place orders, or replace the DART learned-rule updater.
"""

from datetime import datetime
from pathlib import Path

import pandas as pd


PROCESSED_DIR = Path("data/processed")
PREDICTIONS_DIR = Path("data/predictions")
REPORT_DIR = Path("reports/daily_review")

RESULT_SUCCESS = "success"
RESULT_FAILURE = "failure"
MIN_EVALUATED_COUNT = 50
BOOST_LIFT_THRESHOLD = 3.0
PENALIZE_LIFT_THRESHOLD = -3.0


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
    if column not in df.columns:
        return pd.Series([""] * len(df), index=df.index, dtype=object)
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
        + date_key(df, "signal_date")
        + "|"
        + date_key(df, "prediction_date")
        + "|"
        + score_version_series(df)
    )
    return candidate_id.where(valid, fallback)


def normalize_result_series(df: pd.DataFrame) -> pd.Series:
    if df.empty:
        return pd.Series(dtype=str)
    result = pd.Series(["pending"] * len(df), index=df.index, dtype=object)
    for column in ["success_close_t1", "prediction_result", "price_candidate_result"]:
        if column in df.columns:
            series = df[column].astype(str).str.strip().str.lower()
            valid = ~series.isin(["", "nan", "none", "<na>"])
            result = result.where(~(result.eq("pending") & valid), series)
    return result


def dedupe_evaluations(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df
    working = df.copy()
    working["candidate_learning_key"] = candidate_key_series(working)
    sort_columns = [column for column in ["evaluation_date", "evaluated_at", "source_file"] if column in working.columns]
    if sort_columns:
        working = working.sort_values(sort_columns)
    return working.drop_duplicates(subset=["candidate_learning_key"], keep="last")


def bucket_numeric(series: pd.Series, edges: list[float], labels: list[str]) -> pd.Series:
    values = pd.to_numeric(series, errors="coerce")
    return pd.cut(values, bins=edges, labels=labels, include_lowest=True).astype(str).replace("nan", "missing")


def candidate_rank_bucket(series: pd.Series) -> pd.Series:
    rank = pd.to_numeric(series, errors="coerce")
    bucket = pd.Series(["missing"] * len(rank), index=rank.index, dtype=object)
    bucket.loc[rank <= 10] = "top_10"
    bucket.loc[(rank > 10) & (rank <= 20)] = "rank_11_20"
    bucket.loc[(rank > 20) & (rank <= 50)] = "rank_21_50"
    bucket.loc[(rank > 50) & (rank <= 100)] = "rank_51_100"
    bucket.loc[rank > 100] = "rank_101_plus"
    return bucket


def selected_pick_bucket(series: pd.Series) -> pd.Series:
    return series.astype(str).str.lower().isin(["true", "1", "yes"]).map({True: "selected", False: "broad_pool"})


def build_group_columns(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    result["score_version_bucket"] = score_version_series(result)

    if "selected_pick" in result.columns:
        result["selected_pick_bucket"] = selected_pick_bucket(result["selected_pick"])
    if "candidate_rank" in result.columns:
        result["candidate_rank_bucket"] = candidate_rank_bucket(result["candidate_rank"])
    if "final_price_signal_score_v2" in result.columns:
        result["final_price_signal_score_v2_bucket"] = bucket_numeric(
            result["final_price_signal_score_v2"],
            [-float("inf"), 20, 30, 40, 50, float("inf")],
            ["score_lt_20", "score_20_30", "score_30_40", "score_40_50", "score_50_plus"],
        )

    penalty_specs = {
        "overextension_penalty": [0, 0.01, 2, 5, float("inf")],
        "reversal_risk_penalty": [0, 0.01, 2, 5, float("inf")],
        "news_risk_penalty": [0, 0.01, 1, 3, float("inf")],
        "attention_noise_penalty": [0, 0.01, 1, 3, float("inf")],
    }
    penalty_labels = ["none", "low", "medium", "high"]
    for column, edges in penalty_specs.items():
        if column in result.columns:
            result[f"{column}_bucket"] = bucket_numeric(result[column], edges, penalty_labels)

    if "volume_confirmation_score" in result.columns:
        result["volume_confirmation_score_bucket"] = bucket_numeric(
            result["volume_confirmation_score"],
            [-float("inf"), -0.01, 0.01, 3, float("inf")],
            ["negative", "none", "moderate", "high"],
        )
    if "liquidity_score" in result.columns:
        result["liquidity_score_bucket"] = bucket_numeric(
            result["liquidity_score"],
            [-float("inf"), 0.01, 2.01, float("inf")],
            ["none", "basic", "confirmed"],
        )

    return result


def confidence_level(evaluated_count: int) -> str:
    if evaluated_count >= 300:
        return "high"
    if evaluated_count >= 100:
        return "medium"
    if evaluated_count >= MIN_EVALUATED_COUNT:
        return "low"
    return "insufficient"


def recommended_action(evaluated_count: int, lift: float | None) -> str:
    if lift is None:
        return "watch"
    if evaluated_count < MIN_EVALUATED_COUNT:
        return "watch"
    if lift >= BOOST_LIFT_THRESHOLD:
        return "boost"
    if lift <= PENALIZE_LIFT_THRESHOLD:
        return "penalize"
    return "neutral"


def summarize_rules(evaluations: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    if evaluations.empty:
        return pd.DataFrame(), {"baseline_success_rate": None, "baseline_evaluated_count": 0}

    working = build_group_columns(evaluations)
    result = normalize_result_series(working)
    evaluated = result.isin([RESULT_SUCCESS, RESULT_FAILURE])
    working = working[evaluated].copy()
    result = result[evaluated]
    if working.empty:
        return pd.DataFrame(), {"baseline_success_rate": None, "baseline_evaluated_count": 0}

    success_total = int((result == RESULT_SUCCESS).sum())
    baseline_evaluated = len(working)
    baseline_success_rate = round(success_total / baseline_evaluated * 100, 2)
    working["normalized_result"] = result

    group_columns = [
        "score_version_bucket",
        "selected_pick_bucket",
        "candidate_rank_bucket",
        "final_price_signal_score_v2_bucket",
        "overextension_penalty_bucket",
        "reversal_risk_penalty_bucket",
        "news_risk_penalty_bucket",
        "attention_noise_penalty_bucket",
        "volume_confirmation_score_bucket",
        "liquidity_score_bucket",
    ]
    rows = []
    for column in group_columns:
        if column not in working.columns:
            continue
        for value, group in working.groupby(column, dropna=False):
            group_result = group["normalized_result"]
            evaluated_count = len(group)
            success_count = int((group_result == RESULT_SUCCESS).sum())
            failure_count = int((group_result == RESULT_FAILURE).sum())
            success_rate = round(success_count / evaluated_count * 100, 2) if evaluated_count else None
            lift = round(success_rate - baseline_success_rate, 2) if success_rate is not None else None
            action = recommended_action(evaluated_count, lift)
            rows.append(
                {
                    "rule_group": column.replace("_bucket", ""),
                    "rule_value": str(value),
                    "evaluated_count": evaluated_count,
                    "success_count": success_count,
                    "failure_count": failure_count,
                    "success_rate": success_rate,
                    "baseline_success_rate": baseline_success_rate,
                    "lift_vs_baseline": lift,
                    "confidence_level": confidence_level(evaluated_count),
                    "recommended_action": action,
                }
            )

    rules = pd.DataFrame(rows)
    if rules.empty:
        return rules, {
            "baseline_success_rate": baseline_success_rate,
            "baseline_evaluated_count": baseline_evaluated,
        }
    action_order = {"boost": 0, "penalize": 1, "neutral": 2, "watch": 3}
    rules["action_order"] = rules["recommended_action"].map(action_order).fillna(9)
    rules = rules.sort_values(
        ["action_order", "confidence_level", "lift_vs_baseline", "evaluated_count"],
        ascending=[True, True, False, False],
    ).drop(columns=["action_order"])
    return rules, {
        "baseline_success_rate": baseline_success_rate,
        "baseline_evaluated_count": baseline_evaluated,
    }


def write_report(rules: pd.DataFrame, summary: dict, output_csv: Path) -> Path:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    today_display = datetime.today().strftime("%Y-%m-%d")
    report_path = REPORT_DIR / f"{today_display}_price_candidate_learned_rules_report.md"
    boost_count = int((rules.get("recommended_action", pd.Series(dtype=str)) == "boost").sum()) if not rules.empty else 0
    penalize_count = int((rules.get("recommended_action", pd.Series(dtype=str)) == "penalize").sum()) if not rules.empty else 0
    watch_count = int((rules.get("recommended_action", pd.Series(dtype=str)) == "watch").sum()) if not rules.empty else 0

    lines = [
        f"# Price Candidate Learned Rules Report - {today_display}",
        "",
        "This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.",
        "",
        "## Summary",
        "",
        f"- Source CSV: `{output_csv}`",
        f"- Baseline evaluated count: **{summary.get('baseline_evaluated_count', 0)}**",
        f"- Baseline success rate: **{summary.get('baseline_success_rate', 'N/A')}%**",
        f"- Total rule rows: **{len(rules)}**",
        f"- Boost rules: **{boost_count}**",
        f"- Penalize rules: **{penalize_count}**",
        f"- Watch rules: **{watch_count}**",
        "",
        "Conservative activation uses at least 50 evaluated rows and +/-3 percentage points lift versus baseline.",
        "",
        "## Learned Rule Table",
        "",
    ]

    if rules.empty:
        lines.append("No price-candidate learned rules available.")
    else:
        columns = [
            "rule_group",
            "rule_value",
            "evaluated_count",
            "success_count",
            "failure_count",
            "success_rate",
            "baseline_success_rate",
            "lift_vs_baseline",
            "confidence_level",
            "recommended_action",
        ]
        lines.append("| " + " | ".join(columns) + " |")
        lines.append("|" + "|".join(["---"] * len(columns)) + "|")
        for _, row in rules.iterrows():
            values = [str(row.get(column, "")).replace("|", "/") for column in columns]
            lines.append("| " + " | ".join(values) + " |")

    report_path.write_text("\n".join(lines), encoding="utf-8")
    return report_path


def main():
    print("Generating price candidate learned rules...")
    evaluations = read_all_csv(PREDICTIONS_DIR, "price_candidate_evaluation_*.csv")
    evaluations = dedupe_evaluations(evaluations)
    rules, summary = summarize_rules(evaluations)

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    today = datetime.today().strftime("%Y%m%d")
    output_csv = PROCESSED_DIR / f"price_candidate_learned_rules_{today}.csv"
    rules.to_csv(output_csv, index=False, encoding="utf-8-sig")
    report_path = write_report(rules, summary, output_csv)

    boost_count = int((rules.get("recommended_action", pd.Series(dtype=str)) == "boost").sum()) if not rules.empty else 0
    penalize_count = int((rules.get("recommended_action", pd.Series(dtype=str)) == "penalize").sum()) if not rules.empty else 0
    watch_count = int((rules.get("recommended_action", pd.Series(dtype=str)) == "watch").sum()) if not rules.empty else 0
    print(f"Price candidate learned rules saved to: {output_csv}")
    print(f"Price candidate learned rules report saved to: {report_path}")
    print(f"rules count: {len(rules)}")
    print(f"boost rules count: {boost_count}")
    print(f"penalize rules count: {penalize_count}")
    print(f"watch rules count: {watch_count}")
    if not rules.empty:
        positive = rules.sort_values("lift_vs_baseline", ascending=False).iloc[0]
        negative = rules.sort_values("lift_vs_baseline", ascending=True).iloc[0]
        print(f"top positive rule: {positive['rule_group']}={positive['rule_value']} ({positive['lift_vs_baseline']}pp)")
        print(f"top negative rule: {negative['rule_group']}={negative['rule_value']} ({negative['lift_vs_baseline']}pp)")


if __name__ == "__main__":
    main()
