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
]
