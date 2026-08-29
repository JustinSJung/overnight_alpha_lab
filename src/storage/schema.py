"""
Shared schema constants for price candidate and evaluation artifacts.
"""

RESULT_SUCCESS = "success"
RESULT_FAILURE = "failure"
RESULT_PENDING = "pending"
RESULT_SKIPPED = "skipped"

RESULT_LABELS = [
    RESULT_SUCCESS,
    RESULT_FAILURE,
    RESULT_PENDING,
    RESULT_SKIPPED,
]

# ---------------------------------------------------------------------------
# Evaluation state model
#
# success_close_t1/prediction_result/price_candidate_result/evaluation_status
# above are left untouched (backward compatibility). These three additional
# columns give the "pending" bucket a real taxonomy: a prediction can be
# pending because it's genuinely waiting on a future price, because it was
# never a directional call to begin with (HOLD/neutral), or because the
# price data needed to ever resolve it isn't there -- three very different
# situations previously indistinguishable downstream.
# ---------------------------------------------------------------------------

EVALUATION_STATE_EVALUATED = "evaluated"
EVALUATION_STATE_WAITING_FOR_OUTCOME = "waiting_for_outcome"
EVALUATION_STATE_NOT_SCORED = "not_scored"
EVALUATION_STATE_DATA_UNAVAILABLE = "data_unavailable"

EVALUATION_STATE_LABELS = [
    EVALUATION_STATE_EVALUATED,
    EVALUATION_STATE_WAITING_FOR_OUTCOME,
    EVALUATION_STATE_NOT_SCORED,
    EVALUATION_STATE_DATA_UNAVAILABLE,
]

# not_scored
REASON_INITIAL_ACTION_HOLD = "initial_action_hold"
REASON_NEUTRAL_DIRECTION = "neutral_direction"
# waiting_for_outcome
REASON_T1_NOT_AVAILABLE = "t1_not_available"
# data_unavailable
REASON_PRICE_FILE_MISSING = "price_file_missing"
REASON_MALFORMED_PRICE_DATA = "malformed_price_data"
REASON_INVALID_CANDIDATE_IDENTITY = "invalid_candidate_identity"
REASON_INSUFFICIENT_PRICE_HISTORY = "insufficient_price_history"
REASON_PRICE_HISTORY_GAP_TIMEOUT = "price_history_gap_timeout"
# Defined for schema completeness -- no current code path produces this yet.
# main()'s per-row try/except around evaluate_row() drops a candidate
# entirely (no output row at all) if evaluate_row() itself raises, so there
# is nothing to label today. Reserved for if/when that path is changed to
# persist a row instead of silently dropping it.
REASON_COLLECTION_FAILURE = "collection_failure"

# Single source of truth for the waiting_for_outcome -> data_unavailable
# cutoff (see reason_code=price_history_gap_timeout). Chosen from the
# observed age distribution of currently-pending directional predictions:
# resolved cases cluster at 0-3 days, with an essentially empty gap from
# 4-29 days before a second cluster at 30+ days -- so 14 days (comfortably
# past the T+5 horizon this evaluator computes) cleanly separates "still
# plausibly waiting" from "this price history gap isn't closing."
EVALUATION_WAIT_TIMEOUT_DAYS = 14

PRICE_CANDIDATE_COLUMNS = [
    "candidate_id",
    "stock_code",
    "stock_name",
    "corp_name",
    "signal_date",
    "prediction_date",
    "model_version",
    "feature_version",
    "prediction_direction",
    "prediction_score",
    "confidence_score",
    "risk_score",
    "final_price_signal_score",
]

PRICE_EVALUATION_COLUMNS = [
    "candidate_id",
    "stable_prediction_id",
    "initial_candidate_action",
    "latest_candidate_action",
    "action_changed",
    "stock_code",
    "signal_date",
    "prediction_date",
    "evaluation_date",
    "next_open_return",
    "close_t1_return",
    "close_t3_return",
    "close_t5_return",
    "benchmark_return_t1",
    "benchmark_return_t3",
    "benchmark_return_t5",
    "excess_return_t1",
    "excess_return_t3",
    "excess_return_t5",
    "success_close_t1",
    "success_close_t3",
    "success_close_t5",
    "success_excess_t1",
    "success_excess_t3",
    "success_excess_t5",
    "prediction_result",
    "price_candidate_result",
    "evaluation_status",
    "evaluation_state",
    "evaluation_result",
    "reason_code",
]
