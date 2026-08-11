"""
Cross-tabulate overextension_penalty / reversal_risk_penalty buckets against
base_momentum_score tertiles, split by candidate direction (buy vs avoid).

This is a research-only diagnostic layer. It reuses the dedup and bucket logic
from price_candidate_rule_learner.py, but does not change score weights,
penalty formulas, candidate selection, or place trades.
"""

import sys
from datetime import datetime
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.evaluation.metrics import dedupe_evaluations, direction_series, success_series
from src.models.price_candidate_rule_learner import PREDICTIONS_DIR, bucket_numeric, read_all_csv
from src.storage.schema import RESULT_FAILURE, RESULT_SUCCESS


REPORT_DIR = Path("reports/daily_review")
MIN_CELL_COUNT = 20

PENALTY_SPECS = {
    "overextension_penalty": [0, 0.01, 2, 5, float("inf")],
    "reversal_risk_penalty": [0, 0.01, 2, 5, float("inf")],
}
PENALTY_LABELS = ["none", "low", "medium", "high"]
MOMENTUM_TERTILE_LABELS = ["T1_low", "T2_mid", "T3_high"]


def momentum_tertile_series(values: pd.Series) -> pd.Series:
    numeric = pd.to_numeric(values, errors="coerce")
    if numeric.dropna().nunique() < 3:
        return pd.Series(["insufficient_range"] * len(values), index=values.index, dtype=object)
    try:
        tertiles = pd.qcut(numeric.rank(method="first"), 3, labels=MOMENTUM_TERTILE_LABELS)
    except Exception:
        return pd.Series(["insufficient_range"] * len(values), index=values.index, dtype=object)
    return tertiles.astype(str).replace("nan", "missing")


def direction_summary(df: pd.DataFrame) -> dict:
    if df.empty:
        return {"evaluated_count": 0, "success_count": 0, "success_rate": None}
    result = success_series(df)
    evaluated = result.isin([RESULT_SUCCESS, RESULT_FAILURE])
    evaluated_count = int(evaluated.sum())
    success_count = int((result == RESULT_SUCCESS).sum())
    success_rate = round(success_count / evaluated_count * 100, 2) if evaluated_count else None
    return {"evaluated_count": evaluated_count, "success_count": success_count, "success_rate": success_rate}


def cross_tab(df: pd.DataFrame, penalty_column: str) -> list[dict]:
    if df.empty or penalty_column not in df.columns or "base_momentum_score" not in df.columns:
        return []

    working = df.copy()
    working["penalty_bucket"] = bucket_numeric(working[penalty_column], PENALTY_SPECS[penalty_column], PENALTY_LABELS)
    working["momentum_tertile"] = momentum_tertile_series(working["base_momentum_score"])

    result = success_series(working)
    evaluated_mask = result.isin([RESULT_SUCCESS, RESULT_FAILURE])
    working = working[evaluated_mask].copy()
    result = result[evaluated_mask]
    if working.empty:
        return []
    working["normalized_result"] = result

    rows = []
    for (penalty_bucket, tertile), group in working.groupby(["penalty_bucket", "momentum_tertile"], dropna=False):
        evaluated_count = len(group)
        success_count = int((group["normalized_result"] == RESULT_SUCCESS).sum())
        failure_count = int((group["normalized_result"] == RESULT_FAILURE).sum())
        success_rate = round(success_count / evaluated_count * 100, 2) if evaluated_count else None
        rows.append(
            {
                "penalty_bucket": str(penalty_bucket),
                "momentum_tertile": str(tertile),
                "evaluated_count": evaluated_count,
                "success_count": success_count,
                "failure_count": failure_count,
                "success_rate": success_rate,
                "confidence_flag": "insufficient" if evaluated_count < MIN_CELL_COUNT else "ok",
            }
        )

    bucket_order = {label: index for index, label in enumerate(PENALTY_LABELS + ["missing"])}
    tertile_order = {label: index for index, label in enumerate(MOMENTUM_TERTILE_LABELS + ["insufficient_range", "missing"])}
    rows.sort(
        key=lambda row: (
            bucket_order.get(row["penalty_bucket"], 99),
            tertile_order.get(row["momentum_tertile"], 99),
        )
    )
    return rows


def build_diagnostics() -> dict:
    evaluations = read_all_csv(PREDICTIONS_DIR, "price_candidate_evaluation_*.csv")
    evaluations = dedupe_evaluations(evaluations)

    diagnostics = {"generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "directions": {}}
    if evaluations.empty:
        return diagnostics

    evaluations = evaluations.copy()
    evaluations["candidate_direction"] = direction_series(evaluations)

    for direction in ["buy", "avoid"]:
        subset = evaluations[evaluations["candidate_direction"] == direction]
        diagnostics["directions"][direction] = {
            "summary": direction_summary(subset),
            "cross_tabs": {
                penalty_column: cross_tab(subset, penalty_column) for penalty_column in PENALTY_SPECS
            },
        }
    return diagnostics


def table(rows: list[dict], columns: list[str]) -> list[str]:
    lines = ["| " + " | ".join(columns) + " |", "|" + "|".join(["---"] * len(columns)) + "|"]
    for row in rows:
        values = [str(row.get(column, "N/A")) for column in columns]
        lines.append("| " + " | ".join(values) + " |")
    return lines


def write_report(diagnostics: dict) -> Path:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    today_display = datetime.today().strftime("%Y-%m-%d")
    report_path = REPORT_DIR / f"{today_display}_directional_penalty_diagnostics.md"

    columns = ["penalty_bucket", "momentum_tertile", "evaluated_count", "success_count", "failure_count", "success_rate", "confidence_flag"]
    direction_labels = {"buy": "Buy-Type (매수형)", "avoid": "Avoid-Type (회피형)"}

    lines = [
        f"# Directional Penalty Diagnostics - {today_display}",
        "",
        "Cross-tabulates overextension_penalty and reversal_risk_penalty buckets against base_momentum_score "
        "tertiles, split by candidate direction. This report is diagnostic only: it does not change score "
        "weights, penalty formulas, or candidate selection.",
        "",
        f"Cells with fewer than {MIN_CELL_COUNT} evaluated cases are flagged `insufficient` and should be read "
        "conservatively rather than acted on.",
        "",
    ]

    directions = diagnostics.get("directions", {})
    if not directions:
        lines.append("No price-candidate evaluations available yet.")
        report_path.write_text("\n".join(lines), encoding="utf-8")
        return report_path

    for direction in ["buy", "avoid"]:
        direction_data = directions.get(direction, {"summary": {"evaluated_count": 0, "success_rate": None}, "cross_tabs": {}})
        summary = direction_data["summary"]
        lines.extend(
            [
                f"## {direction_labels[direction]}",
                "",
                f"- Evaluated cases (all penalty/momentum buckets): **{summary['evaluated_count']}**",
                f"- Overall success rate: **{summary['success_rate']}%**" if summary["success_rate"] is not None else "- Overall success rate: **N/A**",
                "",
            ]
        )
        for penalty_column in PENALTY_SPECS:
            rows = direction_data["cross_tabs"].get(penalty_column, [])
            lines.append(f"### {penalty_column} x base_momentum_score tertile")
            lines.append("")
            if not rows:
                lines.append("No evaluated cases available for this cross tab.")
            else:
                lines.extend(table(rows, columns))
            lines.append("")

    lines.extend(
        [
            "## Notes",
            "",
            "- `momentum_tertile` is computed within each direction's evaluated subset "
            "(T1_low/T2_mid/T3_high by base_momentum_score rank); `insufficient_range` means too few "
            "distinct momentum values were available to split into tertiles.",
            "- Buy-type sample sizes are typically much smaller than avoid-type; treat buy-type cells "
            "conservatively even when not flagged `insufficient`.",
            "- This report does not feed back into scoring, penalty weights, or candidate selection.",
        ]
    )

    report_path.write_text("\n".join(lines), encoding="utf-8")
    return report_path


def main():
    print("Generating directional penalty diagnostics...")
    diagnostics = build_diagnostics()
    report_path = write_report(diagnostics)
    print(f"Directional penalty diagnostics saved to: {report_path}")

    directions = diagnostics.get("directions", {})
    for direction in ["buy", "avoid"]:
        summary = directions.get(direction, {}).get("summary", {"evaluated_count": 0, "success_rate": None})
        print(f"{direction}-type evaluated cases: {summary['evaluated_count']}, success rate: {summary['success_rate']}%")
        cross_tabs = directions.get(direction, {}).get("cross_tabs", {})
        for penalty_column, rows in cross_tabs.items():
            insufficient_count = sum(1 for row in rows if row["confidence_flag"] == "insufficient")
            print(f"  {penalty_column}: {len(rows)} cells, {insufficient_count} flagged insufficient")


if __name__ == "__main__":
    main()
