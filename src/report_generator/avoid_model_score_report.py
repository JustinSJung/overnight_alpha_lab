"""
Diagnostic-only comparison of avoid_lr_model_v1's ranking quality against the
existing final_price_signal_score_v2, restricted to AVOID-direction
candidates whose outcome has already resolved.

This report does not affect scoring, candidate_action, final_price_signal_score,
or selected_pick. It is internal-diagnostics-only (docs/diagnostics.html);
the public dashboard is not touched by this script.
"""

import sys
from datetime import datetime
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.evaluation.metrics import (
    dedupe_evaluations,
    direction_series,
    reliability_score_from_wilson,
    safe_percentage,
    success_series,
)
from src.storage.schema import RESULT_FAILURE, RESULT_SUCCESS


PREDICTIONS_DIR = Path("data/predictions")
PROCESSED_DIR = Path("data/processed")
REPORT_DIR = Path("reports/daily_review")
MIN_CELL_COUNT = 20
TOP_PERCENTILES = [0.10, 0.20, 0.30]


def read_all_csv(directory: Path, pattern: str) -> pd.DataFrame:
    frames = []
    for path in sorted(directory.glob(pattern)):
        try:
            df = pd.read_csv(path, low_memory=False)
            df["source_file"] = str(path)
            frames.append(df)
        except Exception as error:
            print(f"Failed to read {path}: {error}")
    if not frames:
        return pd.DataFrame()
    return pd.concat(frames, ignore_index=True)


def top_pct_stats(df: pd.DataFrame, score_column: str, pct: float, ascending: bool) -> dict:
    valid = df.dropna(subset=[score_column])
    n_total = len(valid)
    if n_total == 0:
        return {"n": 0, "success_count": 0, "success_rate": None, "wilson": None, "insufficient": True}

    k = max(1, int(round(n_total * pct)))
    ordered = valid.sort_values(score_column, ascending=ascending)
    top = ordered.head(k)
    n = len(top)
    success_count = int((top["_result"] == RESULT_SUCCESS).sum())
    return {
        "n": n,
        "success_count": success_count,
        "success_rate": round(safe_percentage(success_count, n), 2),
        "wilson": round(reliability_score_from_wilson(success_count, n), 1),
        "insufficient": n < MIN_CELL_COUNT,
    }


def build_report() -> dict | None:
    all_eval = read_all_csv(PREDICTIONS_DIR, "price_candidate_evaluation_*.csv")
    if all_eval.empty:
        return None

    unique = dedupe_evaluations(all_eval, key_column="avoid_model_report_key")
    unique["direction"] = direction_series(unique)
    unique["_result"] = success_series(unique, "success_close_t1")
    evaluated = unique[unique["_result"].isin([RESULT_SUCCESS, RESULT_FAILURE])]
    avoid_evaluated = evaluated[evaluated["direction"] == "avoid"].copy()

    if "avoid_model_score" in avoid_evaluated.columns:
        avoid_evaluated["avoid_model_score"] = pd.to_numeric(
            avoid_evaluated["avoid_model_score"], errors="coerce"
        )
    else:
        avoid_evaluated["avoid_model_score"] = pd.NA

    avoid_evaluated["final_price_signal_score_v2"] = pd.to_numeric(
        avoid_evaluated.get("final_price_signal_score_v2"), errors="coerce"
    )

    overall_n = len(avoid_evaluated)
    overall_success = int((avoid_evaluated["_result"] == RESULT_SUCCESS).sum())
    overall_rate = round(safe_percentage(overall_success, overall_n), 2) if overall_n else None

    model_available_n = int(avoid_evaluated["avoid_model_score"].notna().sum())
    has_model_scores = model_available_n >= MIN_CELL_COUNT

    rows = []
    for pct in TOP_PERCENTILES:
        # avoid_model_score: higher = model more confident the AVOID call succeeds -> descending.
        model_stats = top_pct_stats(avoid_evaluated, "avoid_model_score", pct, ascending=False)
        # final_price_signal_score_v2 on AVOID candidates: lower score = stronger avoid
        # conviction (further from the HOLD/40 boundary) -> ascending.
        v2_stats = top_pct_stats(avoid_evaluated, "final_price_signal_score_v2", pct, ascending=True)
        rows.append(
            {
                "top_pct": f"{int(pct * 100)}%",
                "model_n": model_stats["n"],
                "model_success_rate": model_stats["success_rate"],
                "model_wilson": model_stats["wilson"],
                "model_insufficient": model_stats["insufficient"],
                "v2_n": v2_stats["n"],
                "v2_success_rate": v2_stats["success_rate"],
                "v2_wilson": v2_stats["wilson"],
                "v2_insufficient": v2_stats["insufficient"],
            }
        )

    return {
        "generated_at": datetime.today().strftime("%Y-%m-%d %H:%M:%S"),
        "overall_n": overall_n,
        "overall_success": overall_success,
        "overall_rate": overall_rate,
        "model_available_n": model_available_n,
        "has_model_scores": has_model_scores,
        "rows": rows,
    }


def write_report(report: dict) -> Path:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    today = datetime.today().strftime("%Y-%m-%d")
    path = REPORT_DIR / f"{today}_avoid_model_score_report.md"

    lines = [
        "# AVOID Model Score Report (diagnostic only)",
        "",
        f"Generated at: {report['generated_at']}",
        "",
        "Compares avoid_lr_model_v1 (logistic regression, trained on first-snapshot "
        "features, diagnostic only) against the existing final_price_signal_score_v2, "
        "on AVOID-direction candidates whose outcome has already resolved. Does not "
        "affect candidate_action, final_price_signal_score, or selected_pick.",
        "",
        f"Overall AVOID evaluated pool: N={report['overall_n']}, success rate="
        f"{report['overall_rate']}%",
        f"Candidates with avoid_model_score populated: N={report['model_available_n']}",
        "",
    ]

    if not report["has_model_scores"]:
        lines.append(
            f"**Fewer than {MIN_CELL_COUNT} evaluated candidates have avoid_model_score "
            "so far.** The model was only added to candidate generation recently; T+1 "
            "outcomes take at least one more trading day to resolve, so this comparison "
            "is not yet meaningful with live data. Check back after upcoming daily runs."
        )
    else:
        lines.append(
            "| Top % | Model N | Model success rate | Model Wilson | v2 raw N | "
            "v2 raw success rate | v2 raw Wilson |"
        )
        lines.append("|---|---|---|---|---|---|---|")
        for row in report["rows"]:
            model_cell = (
                "insufficient sample" if row["model_insufficient"] else f"{row['model_success_rate']}%"
            )
            v2_cell = "insufficient sample" if row["v2_insufficient"] else f"{row['v2_success_rate']}%"
            lines.append(
                f"| {row['top_pct']} | {row['model_n']} | {model_cell} | {row['model_wilson']} | "
                f"{row['v2_n']} | {v2_cell} | {row['v2_wilson']} |"
            )

    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def write_summary_csv(report: dict) -> Path:
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    today = datetime.today().strftime("%Y%m%d")
    path = PROCESSED_DIR / f"avoid_model_score_summary_{today}.csv"

    flat = {
        "generated_at": report["generated_at"],
        "overall_n": report["overall_n"],
        "overall_success": report["overall_success"],
        "overall_rate": report["overall_rate"],
        "model_available_n": report["model_available_n"],
        "has_model_scores": report["has_model_scores"],
    }
    for row in report["rows"]:
        prefix = row["top_pct"]
        flat[f"model_n_{prefix}"] = row["model_n"]
        flat[f"model_success_rate_{prefix}"] = row["model_success_rate"]
        flat[f"model_wilson_{prefix}"] = row["model_wilson"]
        flat[f"model_insufficient_{prefix}"] = row["model_insufficient"]
        flat[f"v2_n_{prefix}"] = row["v2_n"]
        flat[f"v2_success_rate_{prefix}"] = row["v2_success_rate"]
        flat[f"v2_wilson_{prefix}"] = row["v2_wilson"]
        flat[f"v2_insufficient_{prefix}"] = row["v2_insufficient"]

    pd.DataFrame([flat]).to_csv(path, index=False, encoding="utf-8-sig")
    return path


def main():
    print("Generating AVOID model score report...")
    report = build_report()
    if report is None:
        print("No evaluation data found. Skipping.")
        return

    report_path = write_report(report)
    summary_path = write_summary_csv(report)
    print(f"AVOID model score report saved to: {report_path}")
    print(f"AVOID model score summary saved to: {summary_path}")
    print(f"overall AVOID evaluated N: {report['overall_n']}, success rate: {report['overall_rate']}%")
    print(f"candidates with avoid_model_score populated: {report['model_available_n']}")
    for row in report["rows"]:
        print(
            f"  top {row['top_pct']}: model N={row['model_n']} rate={row['model_success_rate']}"
            f"  |  v2 raw N={row['v2_n']} rate={row['v2_success_rate']}"
        )


if __name__ == "__main__":
    main()
