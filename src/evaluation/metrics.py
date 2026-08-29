"""
Statistical evaluation helpers for Overnight Alpha Lab.

Also the single source of truth for candidate-level identity, dedup,
result normalization, buy/avoid direction, and Top-N rank-bucket
assignment across price-candidate evaluation reports. These were
previously re-implemented with small, drifting differences in
price_candidate_rule_learner.py, dashboard_generator.py,
evaluation_integrity_audit.py, v2_performance_monitor.py, and
directional_penalty_diagnostics.py -- import from here instead of
adding another local copy.
"""

import hashlib
import math
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.storage.schema import (
    EVALUATION_STATE_DATA_UNAVAILABLE,
    EVALUATION_STATE_EVALUATED,
    EVALUATION_STATE_NOT_SCORED,
    EVALUATION_STATE_WAITING_FOR_OUTCOME,
    EVALUATION_WAIT_TIMEOUT_DAYS,
    REASON_INITIAL_ACTION_HOLD,
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


def wilson_lower_bound(success: int, total: int, z: float = 1.96) -> float:
    """
    Return the Wilson score lower bound for a binomial success proportion.
    """

    if total <= 0:
        return 0.0

    phat = success / total
    z2 = z * z
    denominator = 1 + z2 / total
    center = phat + z2 / (2 * total)
    margin = z * math.sqrt((phat * (1 - phat) + z2 / (4 * total)) / total)

    return max(0.0, (center - margin) / denominator)


def reliability_score_from_wilson(success: int, total: int) -> float:
    """
    Convert Wilson lower bound to a 0-100 reliability score.
    """

    return wilson_lower_bound(success, total) * 100


def safe_percentage(numerator, denominator) -> float:
    """
    Return numerator / denominator * 100, or 0.0 when unavailable.
    """

    try:
        denominator = float(denominator)
        if denominator == 0:
            return 0.0
        return float(numerator) / denominator * 100
    except Exception:
        return 0.0


def classify_confidence_status(reliability_score: float) -> tuple[str, str]:
    """
    Classify reliability score into dashboard status labels.
    """

    if reliability_score < 30:
        return "NOT READY", "준비 부족"
    if reliability_score < 50:
        return "EARLY STAGE", "초기 검증 단계"
    if reliability_score < 65:
        return "WATCHLIST", "관찰 가능 단계"
    if reliability_score < 80:
        return "MODERATE CONFIDENCE", "중간 신뢰도"
    return "HIGH CONFIDENCE", "높은 신뢰도"


# ---------------------------------------------------------------------------
# Candidate identity, dedup, and result normalization
# ---------------------------------------------------------------------------

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


def stable_prediction_id_series(df: pd.DataFrame) -> pd.Series:
    """
    stable_prediction_id = sha1(stock_code | signal_date | score_version)[:16].

    Deliberately excludes candidate_action, prediction_date, and
    price_candidate_score. All three legitimately change between re-scoring
    passes of the SAME real-world prediction: candidate_action flips near
    its scoring thresholds (~1.3% of (stock_code, signal_date) pairs
    measured across the full history), and prediction_date/score are
    re-stamped on every re-run (same-day workflow_dispatch reruns,
    weekend/holiday reruns that carry a stale signal_date forward, or a
    long-unresolved candidate re-scored on an ordinary later day). The
    legacy candidate_id (stock_code|candidate_date|action|score, computed in
    price_candidate_evaluator.py::candidate_id_for_row()) incorporated
    exactly those unstable fields, which fragmented ~10% of the historical
    candidate pool into duplicate identities for what was really one
    prediction re-scored multiple times (see fix/stable-prediction-identity
    investigation notes).

    Always computed fresh from stock_code/signal_date/score_version --
    never read from a stored column -- so the result is identical whether
    the row already carries a stable_prediction_id column (new rows) or
    not (legacy rows read from older CSVs): no separate fallback path is
    needed.
    """
    if df.empty:
        return pd.Series(dtype=str)

    stock_code = df.get("stock_code", pd.Series([""] * len(df), index=df.index)).apply(normalize_stock_code)
    raw = stock_code + "|" + date_key(df, "signal_date") + "|" + score_version_series(df)
    return raw.apply(lambda value: hashlib.sha1(value.encode("utf-8")).hexdigest()[:16])


def candidate_key_series(df: pd.DataFrame) -> pd.Series:
    """
    Candidate-level identity key, now always stable_prediction_id_series()
    (stock_code|signal_date|score_version).

    This replaces the previous candidate_id-based key. candidate_id
    incorporated prediction_date and price_candidate_score, both of which
    legitimately change between re-scoring passes of the same real-world
    prediction -- see stable_prediction_id_series() docstring. The legacy
    candidate_id column is left untouched in stored CSVs and is still
    written by price_candidate_evaluator.py for backward compatibility, but
    is no longer used to compute this identity key.
    """
    return stable_prediction_id_series(df)


def dedupe_evaluations(df: pd.DataFrame, key_column: str = "candidate_evaluation_key") -> pd.DataFrame:
    """
    Collapse repeat evaluation rows for the same candidate down to one row:
    sorts by evaluation_date/evaluated_at/source_file (oldest first) and
    keeps the last row per candidate_key_series() key, so the most complete
    snapshot (e.g. with t3/t5 returns filled in) wins.
    """
    if df.empty:
        return df
    working = df.copy()
    working[key_column] = candidate_key_series(working)
    # evaluated_at/source_file first: they are stamped fresh on every run
    # regardless of outcome, so they stay monotonic with real run recency.
    # evaluation_date can now be preserved (not re-stamped) once a candidate
    # is resolved to success/failure, so it can no longer be trusted as the
    # primary "most recent snapshot" sort key -- a resolved row's pinned,
    # older evaluation_date would otherwise sort before a later transient
    # pending blip and get dropped by keep="last".
    sort_columns = [column for column in ["evaluated_at", "source_file", "evaluation_date"] if column in working.columns]
    if sort_columns:
        working = working.sort_values(sort_columns)
    return working.drop_duplicates(subset=[key_column], keep="last")


def success_series(df: pd.DataFrame, success_column: str = "success_close_t1") -> pd.Series:
    """
    Normalize a price-candidate evaluation outcome column into
    RESULT_SUCCESS / RESULT_FAILURE / RESULT_PENDING. Tries success_column
    first, then falls back through prediction_result and
    price_candidate_result (in that order) for older schema rows.
    Case-insensitive and whitespace-stripped; anything still unresolved
    defaults to RESULT_PENDING.
    """
    if df.empty:
        return pd.Series(dtype=object)

    result = pd.Series([RESULT_PENDING] * len(df), index=df.index, dtype=object)
    seen = set()
    priority_columns = []
    for column in [success_column, "prediction_result", "price_candidate_result"]:
        if column not in seen:
            seen.add(column)
            priority_columns.append(column)

    for column in priority_columns:
        if column in df.columns:
            series = df[column].astype(str).str.strip().str.lower()
            valid = ~series.isin(["", "nan", "none", "<na>"])
            result = result.where(~(result.eq(RESULT_PENDING) & valid), series)
    return result


def _blank(value) -> bool:
    return value is None or (isinstance(value, float) and pd.isna(value)) or str(value).strip() == ""


def _derive_state_for_row(row, as_of: pd.Timestamp) -> tuple[str, Optional[str], Optional[str]]:
    """
    Row-level fallback for legacy rows that predate the persisted
    evaluation_state/evaluation_result/reason_code columns. Reconstructs the
    same classification evaluate_row() would have assigned, from whatever
    older columns/notes that row actually has. Not exact for every historical
    edge case (evaluation_note free text is the only signal for some
    branches), but matches the current code's own branches wherever the
    needed signal survived onto the row.
    """
    outcome = str(row.get("success_close_t1", "")).strip().lower()
    if outcome in (RESULT_SUCCESS, RESULT_FAILURE):
        return EVALUATION_STATE_EVALUATED, outcome, None

    prediction_result = str(row.get("prediction_result", "")).strip().lower()
    note = str(row.get("evaluation_note", "")).strip() if not _blank(row.get("evaluation_note")) else ""

    if prediction_result == RESULT_SKIPPED:
        # Both "Invalid candidate stock code or date." and "Price file
        # error: ..." set prediction_result=skipped; the note text is the
        # only way left to tell them apart on a legacy row.
        if note.startswith("Price file error"):
            return EVALUATION_STATE_DATA_UNAVAILABLE, None, REASON_MALFORMED_PRICE_DATA
        return EVALUATION_STATE_DATA_UNAVAILABLE, None, REASON_INVALID_CANDIDATE_IDENTITY

    if note == "No price file found.":
        return EVALUATION_STATE_DATA_UNAVAILABLE, None, REASON_PRICE_FILE_MISSING

    if note == "No next trading day price data available yet.":
        # Legacy rows don't record whether previous_rows or future_rows was
        # the empty one, so age-vs-timeout is the best available signal
        # (matches the fix/evaluation-state-model investigation's
        # age-based reclassification of the pre-migration "waiting_or_data_gap"
        # bucket).
        signal_date_parsed = pd.to_datetime(row.get("signal_date"), errors="coerce")
        if pd.isna(signal_date_parsed):
            return EVALUATION_STATE_WAITING_FOR_OUTCOME, None, REASON_T1_NOT_AVAILABLE
        age_days = (as_of - signal_date_parsed).days
        if age_days > EVALUATION_WAIT_TIMEOUT_DAYS:
            return EVALUATION_STATE_DATA_UNAVAILABLE, None, REASON_PRICE_HISTORY_GAP_TIMEOUT
        return EVALUATION_STATE_WAITING_FOR_OUTCOME, None, REASON_T1_NOT_AVAILABLE

    # note is blank: either not_scored (no directional target) or a
    # degenerate close_t1_return despite having a direction.
    initial_action = row.get("initial_candidate_action")
    if _blank(initial_action):
        initial_action = row.get("candidate_action", "")
    expects_positive = expected_positive({"candidate_action": initial_action, "prediction_direction": ""})
    if expects_positive is None:
        reason = REASON_INITIAL_ACTION_HOLD if str(initial_action).strip() == "HOLD" else REASON_NEUTRAL_DIRECTION
        return EVALUATION_STATE_NOT_SCORED, None, reason
    return EVALUATION_STATE_DATA_UNAVAILABLE, None, REASON_MALFORMED_PRICE_DATA


def derive_evaluation_state(df: pd.DataFrame, as_of: Optional[pd.Timestamp] = None) -> pd.DataFrame:
    """
    Returns a DataFrame (same index as df) with columns evaluation_state,
    evaluation_result, reason_code for every row.

    Additive/backward-compatible: if a row already carries a persisted,
    non-blank evaluation_state (written by evaluate_row() going forward),
    that value is trusted as-is. Only rows from before this columns existed
    (or where it's blank) get derived from older proxies (evaluation_note,
    success_close_t1, initial_candidate_action, signal_date) via
    _derive_state_for_row() -- no historical CSV is rewritten; this is a
    pure read-time view.
    """
    if df.empty:
        return pd.DataFrame(columns=["evaluation_state", "evaluation_result", "reason_code"])

    if as_of is None:
        as_of = pd.Timestamp(datetime.today().date())

    has_persisted_column = "evaluation_state" in df.columns
    states, evaluation_results, reasons = [], [], []
    for _, row in df.iterrows():
        persisted = row.get("evaluation_state") if has_persisted_column else None
        if not _blank(persisted):
            states.append(persisted)
            evaluation_results.append(row.get("evaluation_result") if not _blank(row.get("evaluation_result")) else None)
            reasons.append(row.get("reason_code") if not _blank(row.get("reason_code")) else None)
            continue
        state, evaluation_result, reason = _derive_state_for_row(row, as_of)
        states.append(state)
        evaluation_results.append(evaluation_result)
        reasons.append(reason)

    return pd.DataFrame(
        {"evaluation_state": states, "evaluation_result": evaluation_results, "reason_code": reasons},
        index=df.index,
    )


# ---------------------------------------------------------------------------
# Buy / avoid candidate direction
# ---------------------------------------------------------------------------

def expected_positive(row) -> Optional[bool]:
    action = str(row.get("candidate_action", ""))
    direction = str(row.get("prediction_direction", ""))

    if direction in {"positive", "neutral_positive"} or action in {"BUY_CANDIDATE", "WATCHLIST"}:
        return True
    if direction == "negative" or action == "AVOID":
        return False
    return None


def candidate_direction_label(expects_positive: Optional[bool]) -> Optional[str]:
    if expects_positive is True:
        return "buy"
    if expects_positive is False:
        return "avoid"
    return None


def direction_series(df: pd.DataFrame) -> pd.Series:
    """
    Return "buy" / "avoid" / None per row, reusing expected_positive() so
    every caller derives direction the same way. Uses the candidate_direction
    column when present and fully valid; otherwise (e.g. evaluation CSVs
    saved before that column existed) recomputes it row-wise.
    """
    if df.empty:
        return pd.Series(dtype=object)

    if "candidate_direction" in df.columns:
        column = df["candidate_direction"].astype(str).str.strip().str.lower()
        valid = column.isin(["buy", "avoid"])
        if valid.all():
            return column
    else:
        column = pd.Series([None] * len(df), index=df.index, dtype=object)
        valid = pd.Series([False] * len(df), index=df.index)

    computed = df.apply(lambda row: candidate_direction_label(expected_positive(row)), axis=1)
    return column.where(valid, computed)


def direction_success_summary(df: pd.DataFrame, success_column: str = "success_close_t1") -> dict:
    """
    Diagnostic-only evaluated/success/failure/success_rate breakdown for
    "buy" and "avoid" candidate_direction slices of df. Callers that need
    additional stats (avg returns, benchmark rates, ...) should filter df by
    direction_series() themselves and compute those separately.
    """
    directions = direction_series(df) if not df.empty else pd.Series(dtype=object)
    summary = {}
    for label in ["buy", "avoid"]:
        subset = df[directions == label] if not df.empty else df
        results = success_series(subset, success_column)
        evaluated_count = int(results.isin([RESULT_SUCCESS, RESULT_FAILURE]).sum())
        success_count = int((results == RESULT_SUCCESS).sum())
        failure_count = int((results == RESULT_FAILURE).sum())
        summary[label] = {
            "evaluated_count": evaluated_count,
            "success_count": success_count,
            "failure_count": failure_count,
            "success_rate": round(safe_percentage(success_count, evaluated_count), 2) if evaluated_count else None,
        }
    return summary


# ---------------------------------------------------------------------------
# Daily score rank and Top-N rank buckets
# ---------------------------------------------------------------------------

RANK_BUCKETS = [("Top 10", 10), ("Top 20", 20), ("Top 50", 50), ("Top 100", 100)]


def coalesced_score(df: pd.DataFrame) -> pd.Series:
    """
    Prefers final_price_signal_score_v2, then final_price_signal_score,
    then price_candidate_score, then prediction_score -- whichever is
    populated first, per row.
    """
    score = pd.Series(pd.NA, index=df.index, dtype="Float64")
    for column in ["final_price_signal_score_v2", "final_price_signal_score", "price_candidate_score", "prediction_score"]:
        if column in df.columns:
            score = score.fillna(pd.to_numeric(df[column], errors="coerce"))
    return score


def rank_group_date_series(df: pd.DataFrame) -> pd.Series:
    dates = pd.Series(pd.NaT, index=df.index, dtype="datetime64[ns]")
    for column in ["signal_date", "prediction_date", "candidate_date"]:
        if column in df.columns:
            dates = dates.fillna(pd.to_datetime(df[column], errors="coerce"))
    return dates.dt.strftime("%Y-%m-%d").fillna("unknown")


def assign_daily_rank(df: pd.DataFrame, rank_column: str = "daily_rank") -> pd.DataFrame:
    """
    Assigns a 1-based daily rank by descending coalesced_score(), grouped by
    rank_group_date_series() (ties broken by row order). Falls back to an
    existing candidate_rank column for rows with no usable score.

    Rank is assigned over whatever population df contains -- callers must
    pass the FULL candidate pool for that score_version/day (pending +
    evaluated + skipped), not an evaluated-only subset, then filter to
    rank <= N and only afterward drop to evaluated rows for a success rate.

    This is a real behavior decision, not just deduplicated code: ranking
    only within already-evaluated rows (evaluation_integrity_audit.py's
    prior behavior) introduces a survivorship bias, because which
    candidates have resolved fastest is not independent of the outcome --
    it silently drops still-pending top scorers from competing for a Top-N
    slot, which shifts materially more evaluated (and often higher-scoring)
    candidates into the bucket than would have actually been "Top N" on the
    day the pick was made. Ranking the full pool first (then reporting the
    success rate only among whichever Top-N members have since resolved)
    reflects what you would have actually picked at signal time. Measured
    on 2026-08-11 data this alone moved the Top 50 success rate from 46.29%
    (evaluated-only pool) to 58.21% (full pool) for the same underlying
    dataset -- see the fix/shared-evaluation-utils PR description.
    """
    if df.empty:
        return df

    working = df.copy()
    working[f"{rank_column}_date"] = rank_group_date_series(working)
    working[f"{rank_column}_score"] = coalesced_score(working)

    if working[f"{rank_column}_score"].notna().any():
        working[rank_column] = working.groupby(f"{rank_column}_date", dropna=False)[f"{rank_column}_score"].rank(
            method="first",
            ascending=False,
        )
    elif "candidate_rank" in working.columns:
        working[rank_column] = pd.to_numeric(working["candidate_rank"], errors="coerce")
    else:
        working[rank_column] = pd.NA

    if "candidate_rank" in working.columns:
        fallback_rank = pd.to_numeric(working["candidate_rank"], errors="coerce")
        working[rank_column] = working[rank_column].fillna(fallback_rank)

    return working


def rank_bucket_rows(ranked_df: pd.DataFrame, summarize_fn, rank_column: str = "daily_rank") -> list[dict]:
    """
    Applies summarize_fn (e.g. a script-local performance_summary()) to the
    rank <= N subset for each of RANK_BUCKETS, on a df already produced by
    assign_daily_rank(). Returns [{"bucket": "Top 10", **summarize_fn(...)}, ...].
    """
    if ranked_df.empty or rank_column not in ranked_df.columns:
        return [{"bucket": label, **summarize_fn(ranked_df.iloc[0:0])} for label, _ in RANK_BUCKETS]

    rows = []
    rank_values = pd.to_numeric(ranked_df[rank_column], errors="coerce")
    for label, end in RANK_BUCKETS:
        subset = ranked_df[rank_values <= end]
        rows.append({"bucket": label, **summarize_fn(subset)})
    return rows
