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

from src.evaluation.metrics import (
    candidate_direction_label,
    expected_positive,
    safe_percentage,
    stable_prediction_id_series,
)
from src.storage.schema import (
    EVALUATION_STATE_DATA_UNAVAILABLE,
    EVALUATION_STATE_EVALUATED,
    EVALUATION_STATE_NOT_SCORED,
    EVALUATION_STATE_WAITING_FOR_OUTCOME,
    EVALUATION_WAIT_TIMEOUT_DAYS,
    REASON_INITIAL_ACTION_HOLD,
    REASON_INSUFFICIENT_PRICE_HISTORY,
    REASON_INVALID_CANDIDATE_IDENTITY,
    REASON_MALFORMED_PRICE_DATA,
    REASON_NEUTRAL_DIRECTION,
    REASON_PRICE_FILE_MISSING,
    REASON_PRICE_HISTORY_GAP_TIMEOUT,
    REASON_T1_NOT_AVAILABLE,
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
    df["stable_prediction_id"] = stable_prediction_id_series(df)

    # Dedup on stable_prediction_id, not legacy candidate_id: candidate_id
    # hashes in prediction_date/candidate_action/price_candidate_score, all
    # of which drift between re-scoring passes of the same real-world
    # signal (same-day workflow_dispatch reruns overwrite that day's
    # price_based_candidates_{date}.csv in place; weekend/holiday reruns
    # carry a stale signal_date into a new day's file). Deduping on
    # candidate_id let every such revision survive into the evaluation
    # pool as if it were a separate candidate. keep="last" (sorted by
    # source file, i.e. the most recently generated price_based_candidates
    # file) keeps the most recent revision's score/action, matching
    # dedupe_evaluations()'s same "latest snapshot wins" behavior.
    sort_columns = [column for column in ["candidate_source_file"] if column in df.columns]
    if sort_columns:
        df = df.sort_values(sort_columns)
    df = df.drop_duplicates(subset=["stable_prediction_id"], keep="last")
    return df


def load_prediction_history() -> tuple[dict[str, dict], dict[str, dict]]:
    """
    Reads all existing price_candidate_evaluation_*.csv files once and
    returns (prior_resolved, initial_snapshots), both keyed by
    stable_prediction_id, both derived from the SAME evaluated_at/
    source_file-sorted frame (ascending) so "latest" and "initial" are
    picked with exactly symmetric tie-breaking -- only which end of the
    same sorted sequence differs (keep="last" vs keep="first"):

    - prior_resolved: stable_prediction_id -> {"success_close_t1",
      "evaluation_date"} for the most recent prior snapshot (keep="last").
      Used so evaluate_row() can keep evaluation_date stable for
      predictions already resolved to the same success/failure outcome,
      instead of re-stamping it to today on every re-run.
    - initial_snapshots: stable_prediction_id -> {"candidate_action",
      "prediction_direction"} of the EARLIEST known snapshot (keep=
      "first"). This is what evaluate_row() uses to classify
      success/failure -- see its docstring for why: a prediction's
      outcome must be judged against the action it actually made at
      signal_date, not whatever a later re-scoring pass changed it to.
    """
    frames = []
    for path in sorted(PREDICTIONS_DIR.glob("price_candidate_evaluation_*.csv")):
        try:
            df = pd.read_csv(path)
            df["source_file"] = str(path)
            frames.append(df)
        except Exception:
            continue

    if not frames:
        return {}, {}

    combined = pd.concat(frames, ignore_index=True)
    combined["stable_prediction_id"] = stable_prediction_id_series(combined)
    sort_columns = [column for column in ["evaluated_at", "source_file"] if column in combined.columns]
    if sort_columns:
        combined = combined.sort_values(sort_columns)

    prior_resolved = {}
    for _, row in combined.drop_duplicates(subset=["stable_prediction_id"], keep="last").iterrows():
        stable_prediction_id = row.get("stable_prediction_id")
        if stable_prediction_id is None or pd.isna(stable_prediction_id):
            continue
        prior_resolved[str(stable_prediction_id)] = {
            "success_close_t1": row.get("success_close_t1"),
            "evaluation_date": row.get("evaluation_date"),
        }

    initial_snapshots = {}
    for _, row in combined.drop_duplicates(subset=["stable_prediction_id"], keep="first").iterrows():
        stable_prediction_id = row.get("stable_prediction_id")
        if stable_prediction_id is None or pd.isna(stable_prediction_id):
            continue
        initial_snapshots[str(stable_prediction_id)] = {
            "candidate_action": str(row.get("candidate_action", "")),
            "prediction_direction": str(row.get("prediction_direction", "")),
        }

    return prior_resolved, initial_snapshots


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
    return df.dropna(subset=["date", "close"]).sort_values(["index_name", "date"] if "index_name" in df.columns else ["date"])


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
    requested_group = str(market_group or "").strip().upper()
    if requested_group in {"", "UNKNOWN", "NAN", "NONE"}:
        requested_group = "KOSPI"

    result = {
        "benchmark_source": "",
        "benchmark_market_group": requested_group,
        "benchmark_return_t1": pd.NA,
        "benchmark_return_t3": pd.NA,
        "benchmark_return_t5": pd.NA,
    }

    if market_index_df.empty or pd.isna(candidate_date):
        return result

    benchmark_df = market_index_df.copy()

    if "index_name" in benchmark_df.columns:
        matched = benchmark_df[benchmark_df["index_name"].astype(str).str.upper() == requested_group]
        if not matched.empty:
            benchmark_df = matched
            result["benchmark_source"] = str(matched.iloc[-1].get("source_type", "market_index"))
        else:
            fallback = benchmark_df[benchmark_df["index_name"].astype(str).str.upper() == "KOSPI"]
            if not fallback.empty:
                benchmark_df = fallback
                result["benchmark_market_group"] = "KOSPI"
                result["benchmark_source"] = "kospi_fallback"
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
    prior_evaluations: dict[str, dict] | None = None,
    initial_snapshots: dict[str, dict] | None = None,
) -> dict:
    stock_code = normalize_stock_code(row.get("stock_code", ""))
    candidate_date = candidate_date_value(row)

    result = row.to_dict()
    signal_date = row.get("signal_date", row.get("candidate_date", ""))
    prediction_date = row.get("prediction_date", row.get("candidate_date", signal_date))

    stable_prediction_id = str(row.get("stable_prediction_id", ""))
    latest_candidate_action = str(row.get("candidate_action", ""))
    initial_snapshot = (initial_snapshots or {}).get(stable_prediction_id)
    if initial_snapshot is not None:
        # A prior revision (possibly from an earlier calendar day, possibly
        # a same-day rerun) already exists for this stable_prediction_id --
        # use ITS action/direction, not this row's, so a later re-scoring
        # pass (e.g. WATCHLIST -> HOLD) can never redefine what an already-
        # existing prediction's outcome is being judged against. See
        # load_prediction_history(): initial_snapshot is the earliest
        # snapshot (keep="first") on the same evaluated_at/source_file
        # ascending sort that keep="last" uses for "latest" -- symmetric
        # tie-breaking, just opposite ends of the same sequence.
        initial_candidate_action = initial_snapshot.get("candidate_action", "")
        initial_prediction_direction = initial_snapshot.get("prediction_direction", "")
    else:
        # No prior history -- this row IS the first-ever observation of
        # this stable_prediction_id, so its own action/direction is, by
        # definition, the initial one.
        initial_candidate_action = latest_candidate_action
        initial_prediction_direction = str(row.get("prediction_direction", ""))

    # Directional target is fixed to the INITIAL action/direction -- never
    # the latest/current row's -- so success/failure is always judged
    # against what the prediction actually said at signal_date, immune to
    # later revisions (including ones that arrive after the outcome was
    # already observable, which would otherwise be look-ahead/evaluation
    # drift).
    expects_positive = expected_positive(
        {
            "candidate_action": initial_candidate_action,
            "prediction_direction": initial_prediction_direction,
        }
    )
    action_changed = bool(initial_candidate_action != latest_candidate_action)

    result.update(
        {
            "candidate_id": candidate_id_for_row(row),
            "stable_prediction_id": stable_prediction_id,
            "initial_candidate_action": initial_candidate_action,
            "latest_candidate_action": latest_candidate_action,
            "action_changed": action_changed,
            "candidate_direction": candidate_direction_label(expects_positive),
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
            # New state model (additive, backward-compatible -- see
            # src/storage/schema.py). Every return path below sets these
            # explicitly; these are just defensive fallbacks.
            "evaluation_state": None,
            "evaluation_result": None,
            "reason_code": None,
        }
    )

    if not stock_code or pd.isna(candidate_date):
        result["evaluation_status"] = RESULT_SKIPPED
        result["price_candidate_result"] = RESULT_SKIPPED
        result["prediction_result"] = RESULT_SKIPPED
        result["evaluation_note"] = "Invalid candidate stock code or date."
        result["evaluation_state"] = EVALUATION_STATE_DATA_UNAVAILABLE
        result["reason_code"] = REASON_INVALID_CANDIDATE_IDENTITY
        return result

    price_path = latest_price_file(stock_code)
    if price_path is None:
        result["evaluation_note"] = "No price file found."
        result["evaluation_state"] = EVALUATION_STATE_DATA_UNAVAILABLE
        result["reason_code"] = REASON_PRICE_FILE_MISSING
        return result

    try:
        price_df = normalize_price_df(price_path)
    except Exception as error:
        result["evaluation_status"] = RESULT_SKIPPED
        result["price_candidate_result"] = RESULT_SKIPPED
        result["prediction_result"] = RESULT_SKIPPED
        result["evaluation_note"] = f"Price file error: {error}"
        result["evaluation_state"] = EVALUATION_STATE_DATA_UNAVAILABLE
        result["reason_code"] = REASON_MALFORMED_PRICE_DATA
        return result

    previous_rows = price_df[price_df["date"] <= candidate_date]
    future_rows = price_df[price_df["date"] > candidate_date]

    if previous_rows.empty:
        # No price history reaches back to signal_date at all -- this isn't
        # "waiting," there is nothing to wait for; a longer timeout won't
        # fix a gap in the price series itself. Immediate data_unavailable,
        # no EVALUATION_WAIT_TIMEOUT_DAYS grace period (that timeout is only
        # for the future_rows-empty case below).
        result["evaluation_note"] = "No next trading day price data available yet."
        result["evaluation_state"] = EVALUATION_STATE_DATA_UNAVAILABLE
        result["reason_code"] = REASON_INSUFFICIENT_PRICE_HISTORY
        return result

    if future_rows.empty:
        # History exists up to signal_date, but no trading day after it has
        # priced in yet. Genuinely time-bound: still within
        # EVALUATION_WAIT_TIMEOUT_DAYS of signal_date -> waiting_for_outcome;
        # past it -> the price feed for this stock has stopped advancing,
        # so treat it as data_unavailable instead of waiting forever.
        signal_date_parsed = pd.to_datetime(signal_date, errors="coerce")
        age_days = None
        if not pd.isna(signal_date_parsed):
            age_days = (pd.Timestamp(datetime.today().date()) - signal_date_parsed).days

        result["evaluation_note"] = "No next trading day price data available yet."
        if age_days is not None and age_days > EVALUATION_WAIT_TIMEOUT_DAYS:
            result["evaluation_state"] = EVALUATION_STATE_DATA_UNAVAILABLE
            result["reason_code"] = REASON_PRICE_HISTORY_GAP_TIMEOUT
        else:
            # age_days is None only when signal_date itself doesn't parse --
            # too rare/ambiguous to force a data_unavailable verdict, so it
            # stays waiting_for_outcome by default rather than guessing.
            result["evaluation_state"] = EVALUATION_STATE_WAITING_FOR_OUTCOME
            result["reason_code"] = REASON_T1_NOT_AVAILABLE
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

    if t1_result in {RESULT_SUCCESS, RESULT_FAILURE}:
        result["evaluation_state"] = EVALUATION_STATE_EVALUATED
        result["evaluation_result"] = t1_result
        result["reason_code"] = None
    elif expects_positive is None:
        # No directional target at signal_date (initial action was
        # HOLD/neutral) -- close_t1_return above may well be a real,
        # already-computed number, it's just never graded because there's
        # nothing to grade it against.
        result["evaluation_state"] = EVALUATION_STATE_NOT_SCORED
        result["evaluation_result"] = None
        result["reason_code"] = (
            REASON_INITIAL_ACTION_HOLD if initial_candidate_action == "HOLD" else REASON_NEUTRAL_DIRECTION
        )
    else:
        # expects_positive was defined but close_t1_return itself came back
        # NaN (e.g. a degenerate base_close) -- a data-quality problem, not
        # a missing-direction one.
        result["evaluation_state"] = EVALUATION_STATE_DATA_UNAVAILABLE
        result["evaluation_result"] = None
        result["reason_code"] = REASON_MALFORMED_PRICE_DATA

    if t1_result in {RESULT_SUCCESS, RESULT_FAILURE} and prior_evaluations:
        prior = prior_evaluations.get(stable_prediction_id)
        if (
            prior is not None
            and prior.get("success_close_t1") == t1_result
            and prior.get("evaluation_date")
            and not pd.isna(prior.get("evaluation_date"))
        ):
            result["evaluation_date"] = prior["evaluation_date"]

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
    benchmark_t1_available = int(pd.to_numeric(df.get("benchmark_return_t1", pd.Series(dtype=float)), errors="coerce").notna().sum())
    benchmark_latest_date = ""
    if "next_trade_date" in df.columns:
        parsed = pd.to_datetime(df["next_trade_date"], errors="coerce")
        if parsed.notna().any():
            benchmark_latest_date = parsed.max().strftime("%Y-%m-%d")

    print("Price candidate evaluation summary:")
    print(f"- candidates loaded: {len(df)}")
    print(f"- evaluated close_t1: {close_t1_evaluated}")
    print(f"- success_close_t1 count: {close_t1_counts[RESULT_SUCCESS]}")
    print(f"- failure_close_t1 count: {close_t1_counts[RESULT_FAILURE]}")
    print(f"- pending count: {close_t1_counts[RESULT_PENDING]}")
    print(f"- benchmark-adjusted evaluated count: {excess_t1_evaluated}")
    print(f"- benchmark-adjusted success count: {excess_t1_counts[RESULT_SUCCESS]}")
    print(f"- benchmark_return_t1 available rows: {benchmark_t1_available}")
    print(f"- benchmark coverage rate: {safe_percentage(excess_t1_evaluated, len(df)):.2f}%")
    print(f"- latest evaluated next trade date: {benchmark_latest_date or 'N/A'}")
    print(f"- skipped count: {close_t1_counts[RESULT_SKIPPED]}")


def main():
    print("Evaluating price-based candidates...")

    candidates = read_candidates()
    if candidates.empty:
        print("No price-based candidates found. Evaluation skipped.")
        return

    market_lookup = load_market_lookup()
    market_index_df = load_market_index()
    # prior_evaluations/initial_snapshots are both keyed by stable_prediction_id
    # (stock_code|signal_date|score_version), not legacy candidate_id.
    # Note on which action success/failure judging uses: classify_success()
    # in evaluate_row() is judged against initial_snapshot's action/direction
    # (the EARLIEST known revision for this stable_prediction_id), never the
    # current row's -- see evaluate_row()'s docstring comments. This is a
    # deliberate fix: judging against the latest revision let a later
    # re-score (e.g. WATCHLIST -> HOLD, arriving after the outcome was
    # already observable) silently redefine what an existing prediction's
    # outcome was being judged against -- a look-ahead/evaluation-drift
    # risk. latest_candidate_action/action_changed are still recorded on
    # every row as diagnostic revision info, just no longer used to decide
    # success/failure.
    prior_evaluations, initial_snapshots = load_prediction_history()

    rows = []
    for _, row in candidates.iterrows():
        try:
            rows.append(evaluate_row(row, market_lookup, market_index_df, prior_evaluations, initial_snapshots))
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
