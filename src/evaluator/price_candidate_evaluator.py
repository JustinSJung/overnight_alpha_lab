"""
Evaluate price-based candidates using multi-horizon and benchmark-adjusted returns.
"""

import hashlib
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.evaluation.metrics import safe_percentage
from src.storage.schema import (
    RESULT_FAILURE,
    RESULT_PENDING,
    RESULT_SKIPPED,
    RESULT_SUCCESS,
)


RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")
PREDICTIONS_DIR = Path("data/predictions")
REPORT_DIR = Path("reports/daily_review")
HORIZONS = {"t1": 1, "t3": 3, "t5": 5}


def normalize_stock_code(value) -> str:
    if value is None or pd.isna(value):
        return ""

    try:
        return str(int(float(value))).zfill(6)
    except Exception:
        return str(value).strip().zfill(6)


def safe_float(value, default=None):
    try:
        if pd.isna(value):
            return default
        return float(value)
    except Exception:
        return default


def latest_file(directory: Path, pattern: str):
    files = sorted(directory.glob(pattern))
    if not files:
        return None
    return files[-1]


def latest_price_file(stock_code: str):
    return latest_file(RAW_DIR, f"price_{stock_code}_*.csv")


def candidate_date_value(row) -> pd.Timestamp:
    for column in ["prediction_date", "signal_date", "candidate_date"]:
        value = pd.to_datetime(row.get(column), errors="coerce")
        if not pd.isna(value):
            return value
    return pd.NaT


def candidate_id_for_row(row) -> str:
    existing = row.get("candidate_id", "")
    if existing and not pd.isna(existing):
        return str(existing)

    stock_code = normalize_stock_code(row.get("stock_code", ""))
    candidate_date = candidate_date_value(row)
    action = str(row.get("candidate_action", ""))
    score = str(row.get("price_candidate_score", ""))
    raw = f"{stock_code}|{candidate_date}|{action}|{score}"
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()[:16]


def read_candidates() -> pd.DataFrame:
    frames = []

    for path in sorted(PROCESSED_DIR.glob("price_based_candidates_*.csv")):
        try:
            df = pd.read_csv(path)
            df["candidate_source_file"] = str(path)
            frames.append(df)
        except Exception:
            continue

    if not frames:
        return pd.DataFrame()

    df = pd.concat(frames, ignore_index=True)
    if "stock_code" in df.columns:
        df["stock_code"] = df["stock_code"].apply(normalize_stock_code)

    df["candidate_id"] = df.apply(candidate_id_for_row, axis=1)
    df = df.drop_duplicates(subset=["candidate_id"], keep="last")
    return df


def normalize_price_df(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["close"] = pd.to_numeric(df["close"], errors="coerce")
    df["open"] = pd.to_numeric(df.get("open", pd.NA), errors="coerce")
    return df.dropna(subset=["date", "close"]).sort_values("date")


def load_market_lookup() -> dict[str, str]:
    path = latest_file(RAW_DIR, "stock_market_lookup_*.csv")
    if path is None:
        return {}

    try:
        df = pd.read_csv(path)
    except Exception:
        return {}

    if "stock_code" not in df.columns or "market_group" not in df.columns:
        return {}

    df["stock_code"] = df["stock_code"].apply(normalize_stock_code)
    return dict(zip(df["stock_code"], df["market_group"].astype(str)))


def load_market_index() -> pd.DataFrame:
    path = latest_file(RAW_DIR, "market_index_*.csv")
    if path is None:
        return pd.DataFrame()

    try:
        df = pd.read_csv(path)
    except Exception:
        return pd.DataFrame()

    if "date" not in df.columns or "close" not in df.columns:
        return pd.DataFrame()

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["close"] = pd.to_numeric(df["close"], errors="coerce")
    return df.dropna(subset=["date", "close"]).sort_values("date")


def horizon_row(future_rows: pd.DataFrame, horizon: int):
    if len(future_rows) < horizon:
        return None
    return future_rows.iloc[horizon - 1]


def return_from_base(base_close, target_close):
    base_close = safe_float(base_close)
    target_close = safe_float(target_close)
    if base_close in (None, 0) or target_close is None:
        return pd.NA
    return round((target_close - base_close) / base_close, 4)


def expected_positive(row) -> Optional[bool]:
    action = str(row.get("candidate_action", ""))
    direction = str(row.get("prediction_direction", ""))

    if direction in {"positive", "neutral_positive"} or action in {"BUY_CANDIDATE", "WATCHLIST"}:
        return True
    if direction == "negative" or action == "AVOID":
        return False
    return None


def classify_success(value, expects_positive: Optional[bool]):
    if pd.isna(value) or expects_positive is None:
        return RESULT_PENDING

    value = safe_float(value)
    if value is None:
        return RESULT_PENDING

    if expects_positive:
        return RESULT_SUCCESS if value > 0 else RESULT_FAILURE
    return RESULT_SUCCESS if value < 0 else RESULT_FAILURE


def evaluate_benchmark(
    market_index_df: pd.DataFrame,
    market_group: str,
    candidate_date: pd.Timestamp,
):
    result = {
        "benchmark_source": "",
        "benchmark_market_group": market_group or "",
        "benchmark_return_t1": pd.NA,
        "benchmark_return_t3": pd.NA,
        "benchmark_return_t5": pd.NA,
    }

    if market_index_df.empty or pd.isna(candidate_date):
        return result

    benchmark_df = market_index_df.copy()

    if market_group and "index_name" in benchmark_df.columns:
        matched = benchmark_df[benchmark_df["index_name"].astype(str) == str(market_group)]
        if not matched.empty:
            benchmark_df = matched
            result["benchmark_source"] = str(matched.iloc[-1].get("source_type", "market_index"))
        else:
            result["benchmark_source"] = "generic_market_index"
    else:
        result["benchmark_source"] = "generic_market_index"

    previous_rows = benchmark_df[benchmark_df["date"] <= candidate_date]
    future_rows = benchmark_df[benchmark_df["date"] > candidate_date]

    if previous_rows.empty or future_rows.empty:
        return result

    base_close = previous_rows.iloc[-1]["close"]
    for label, horizon in HORIZONS.items():
        row = horizon_row(future_rows, horizon)
        if row is not None:
            result[f"benchmark_return_{label}"] = return_from_base(base_close, row["close"])

    return result


def evaluate_row(
    row,
    market_lookup: dict[str, str],
    market_index_df: pd.DataFrame,
) -> dict:
    stock_code = normalize_stock_code(row.get("stock_code", ""))
    candidate_date = candidate_date_value(row)
    expects_positive = expected_positive(row)

    result = row.to_dict()
    signal_date = row.get("signal_date", row.get("candidate_date", ""))
    prediction_date = row.get("prediction_date", row.get("candidate_date", signal_date))

    result.update(
        {
            "candidate_id": candidate_id_for_row(row),
            "signal_date": signal_date,
            "prediction_date": prediction_date,
            "evaluation_date": datetime.today().strftime("%Y-%m-%d"),
            "evaluated_at": datetime.today().strftime("%Y-%m-%d"),
            "next_trade_date": pd.NA,
            "next_open_return": pd.NA,
            "next_close_return": pd.NA,
            "close_t1_return": pd.NA,
            "close_t3_return": pd.NA,
            "close_t5_return": pd.NA,
            "benchmark_market_group": market_lookup.get(stock_code, ""),
            "benchmark_source": "",
            "benchmark_return_t1": pd.NA,
            "benchmark_return_t3": pd.NA,
            "benchmark_return_t5": pd.NA,
            "excess_return_t1": pd.NA,
            "excess_return_t3": pd.NA,
            "excess_return_t5": pd.NA,
            "success_close_t1": RESULT_PENDING,
            "success_close_t3": RESULT_PENDING,
            "success_close_t5": RESULT_PENDING,
            "success_excess_t1": RESULT_PENDING,
            "success_excess_t3": RESULT_PENDING,
            "success_excess_t5": RESULT_PENDING,
            "prediction_result": RESULT_PENDING,
            "price_candidate_result": RESULT_PENDING,
            "evaluation_status": RESULT_PENDING,
            "evaluation_note": "",
        }
    )

    if not stock_code or pd.isna(candidate_date):
        result["evaluation_status"] = RESULT_SKIPPED
        result["price_candidate_result"] = RESULT_SKIPPED
        result["prediction_result"] = RESULT_SKIPPED
        result["evaluation_note"] = "Invalid candidate stock code or date."
        return result

    price_path = latest_price_file(stock_code)
    if price_path is None:
        result["evaluation_note"] = "No price file found."
        return result

    try:
        price_df = normalize_price_df(price_path)
    except Exception as error:
        result["evaluation_status"] = RESULT_SKIPPED
        result["price_candidate_result"] = RESULT_SKIPPED
        result["prediction_result"] = RESULT_SKIPPED
        result["evaluation_note"] = f"Price file error: {error}"
        return result

    previous_rows = price_df[price_df["date"] <= candidate_date]
    future_rows = price_df[price_df["date"] > candidate_date]

    if previous_rows.empty or future_rows.empty:
        result["evaluation_note"] = "No next trading day price data available yet."
        return result

    base_close = previous_rows.iloc[-1]["close"]
    next_row = future_rows.iloc[0]
    result["next_trade_date"] = next_row["date"].strftime("%Y-%m-%d")
    result["next_open_return"] = return_from_base(base_close, next_row.get("open"))

    for label, horizon in HORIZONS.items():
        row_at_horizon = horizon_row(future_rows, horizon)
        if row_at_horizon is None:
            continue
        close_return = return_from_base(base_close, row_at_horizon["close"])
        result[f"close_{label}_return"] = close_return
        result[f"success_close_{label}"] = classify_success(close_return, expects_positive)

    result["next_close_return"] = result["close_t1_return"]

    benchmark_result = evaluate_benchmark(
        market_index_df,
        result["benchmark_market_group"],
        candidate_date,
    )
    result.update(benchmark_result)

    for label in HORIZONS:
        close_return = result.get(f"close_{label}_return")
        benchmark_return = result.get(f"benchmark_return_{label}")
        if not pd.isna(close_return) and not pd.isna(benchmark_return):
            excess_return = round(safe_float(close_return) - safe_float(benchmark_return), 4)
            result[f"excess_return_{label}"] = excess_return
            result[f"success_excess_{label}"] = classify_success(excess_return, expects_positive)

    t1_result = result["success_close_t1"]
    result["prediction_result"] = t1_result
    result["price_candidate_result"] = t1_result
    result["evaluation_status"] = "evaluated" if t1_result in {RESULT_SUCCESS, RESULT_FAILURE} else RESULT_PENDING

    return result


def result_counts(series: pd.Series) -> dict[str, int]:
    return {
        RESULT_SUCCESS: int((series == RESULT_SUCCESS).sum()),
        RESULT_FAILURE: int((series == RESULT_FAILURE).sum()),
        RESULT_PENDING: int((series == RESULT_PENDING).sum()),
        RESULT_SKIPPED: int((series == RESULT_SKIPPED).sum()),
    }


def save_report(df: pd.DataFrame, output_csv: Path) -> str:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    today_display = datetime.today().strftime("%Y-%m-%d")
    output_path = REPORT_DIR / f"{today_display}_price_candidate_evaluation_report.md"

    close_t1_counts = result_counts(df["success_close_t1"].astype(str))
    excess_t1_evaluated = df[df["success_excess_t1"].isin([RESULT_SUCCESS, RESULT_FAILURE])]
    excess_t1_counts = result_counts(df["success_excess_t1"].astype(str))
    t3_available = int(df["close_t3_return"].notna().sum())
    t5_available = int(df["close_t5_return"].notna().sum())

    success_examples = df[df["success_close_t1"] == RESULT_SUCCESS].copy()
    failure_examples = df[df["success_close_t1"] == RESULT_FAILURE].copy()

    if "close_t1_return" in success_examples.columns:
        success_examples = success_examples.sort_values("close_t1_return", ascending=False)
    if "close_t1_return" in failure_examples.columns:
        failure_examples = failure_examples.sort_values("close_t1_return", ascending=True)

    lines = [
        f"# {today_display} Price Candidate Evaluation",
        "",
        f"Source CSV: `{output_csv}`",
        "",
        "## Summary",
        "",
        f"- Absolute close T1 evaluated cases: {close_t1_counts[RESULT_SUCCESS] + close_t1_counts[RESULT_FAILURE]}",
        f"- Absolute close T1 success rate: {safe_percentage(close_t1_counts[RESULT_SUCCESS], close_t1_counts[RESULT_SUCCESS] + close_t1_counts[RESULT_FAILURE]):.2f}%",
        f"- Benchmark-adjusted T1 evaluated cases: {len(excess_t1_evaluated)}",
        f"- Benchmark-adjusted T1 success rate: {safe_percentage(excess_t1_counts[RESULT_SUCCESS], len(excess_t1_evaluated)):.2f}%",
        f"- Pending cases: {close_t1_counts[RESULT_PENDING]}",
        f"- Skipped cases: {close_t1_counts[RESULT_SKIPPED]}",
        f"- T3 return available: {t3_available}",
        f"- T5 return available: {t5_available}",
        "",
        "Small samples should be interpreted conservatively; dashboard reliability uses Wilson lower bound.",
        "",
        "## Top Success Examples",
        "",
        "| Stock | Candidate Date | T1 Return | Excess T1 |",
        "|---|---|---:|---:|",
    ]

    for _, row in success_examples.head(5).iterrows():
        lines.append(
            f"| {row.get('stock_code', '')} | {row.get('candidate_date', row.get('signal_date', ''))} | "
            f"{safe_float(row.get('close_t1_return'), 0) * 100:.2f}% | "
            f"{safe_float(row.get('excess_return_t1'), 0) * 100:.2f}% |"
        )

    lines.extend(["", "## Top Failure Examples", "", "| Stock | Candidate Date | T1 Return | Excess T1 |", "|---|---|---:|---:|"])

    for _, row in failure_examples.head(5).iterrows():
        lines.append(
            f"| {row.get('stock_code', '')} | {row.get('candidate_date', row.get('signal_date', ''))} | "
            f"{safe_float(row.get('close_t1_return'), 0) * 100:.2f}% | "
            f"{safe_float(row.get('excess_return_t1'), 0) * 100:.2f}% |"
        )

    output_path.write_text("\n".join(lines), encoding="utf-8")
    return str(output_path)


def print_summary(df: pd.DataFrame) -> None:
    close_t1_counts = result_counts(df["success_close_t1"].astype(str))
    excess_t1_counts = result_counts(df["success_excess_t1"].astype(str))
    close_t1_evaluated = close_t1_counts[RESULT_SUCCESS] + close_t1_counts[RESULT_FAILURE]
    excess_t1_evaluated = excess_t1_counts[RESULT_SUCCESS] + excess_t1_counts[RESULT_FAILURE]

    print("Price candidate evaluation summary:")
    print(f"- candidates loaded: {len(df)}")
    print(f"- evaluated close_t1: {close_t1_evaluated}")
    print(f"- success_close_t1 count: {close_t1_counts[RESULT_SUCCESS]}")
    print(f"- failure_close_t1 count: {close_t1_counts[RESULT_FAILURE]}")
    print(f"- pending count: {close_t1_counts[RESULT_PENDING]}")
    print(f"- benchmark-adjusted evaluated count: {excess_t1_evaluated}")
    print(f"- benchmark-adjusted success count: {excess_t1_counts[RESULT_SUCCESS]}")
    print(f"- skipped count: {close_t1_counts[RESULT_SKIPPED]}")


def main():
    print("Evaluating price-based candidates...")

    candidates = read_candidates()
    if candidates.empty:
        print("No price-based candidates found. Evaluation skipped.")
        return

    market_lookup = load_market_lookup()
    market_index_df = load_market_index()

    rows = []
    for _, row in candidates.iterrows():
        try:
            rows.append(evaluate_row(row, market_lookup, market_index_df))
        except Exception as error:
            stock_code = normalize_stock_code(row.get("stock_code", ""))
            print(f"Price candidate evaluation skipped for {stock_code}: {error}")
            continue

    if not rows:
        print("No price candidate evaluations generated.")
        return

    PREDICTIONS_DIR.mkdir(parents=True, exist_ok=True)
    today = datetime.today().strftime("%Y%m%d")
    output_csv = PREDICTIONS_DIR / f"price_candidate_evaluation_{today}.csv"
    result_df = pd.DataFrame(rows)
    result_df.to_csv(output_csv, index=False, encoding="utf-8-sig")
    report_path = save_report(result_df, output_csv)

    print_summary(result_df)
    print(f"Saved {len(result_df)} price candidate evaluations: {output_csv}")
    print(f"Saved report: {report_path}")


if __name__ == "__main__":
    main()
