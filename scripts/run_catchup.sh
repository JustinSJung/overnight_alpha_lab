#!/bin/bash

set -u

cd "$(dirname "$0")/.."

if [ -f ".venv/bin/activate" ]; then
    source .venv/bin/activate
fi

mkdir -p logs

TODAY=$(date +"%Y-%m-%d")
NOW=$(date +"%Y-%m-%d %H:%M:%S")

LOG_FILE="logs/catchup_$TODAY.log"

log() {
    echo "$*" | tee -a "$LOG_FILE"
}

run_required() {
    local step="$1"
    local description="$2"
    shift 2

    log ""
    log "[$step] $description"

    "$@" >> "$LOG_FILE" 2>&1
    local exit_code=$?

    if [ "$exit_code" -ne 0 ]; then
        log "Required step failed with exit code $exit_code: $description"
        return "$exit_code"
    fi

    return 0
}

run_optional() {
    local description="$1"
    shift

    log ""
    log "$description"

    "$@" >> "$LOG_FILE" 2>&1
    local exit_code=$?

    if [ "$exit_code" -ne 0 ]; then
        log "Optional step skipped or failed with exit code $exit_code: $description"
        return 0
    fi

    return 0
}

finish_success() {
    log ""
    log "[24/24] Catch-up execution completed."
    log "Finished at $(date +"%Y-%m-%d %H:%M:%S")"
    log "======================================"
    log "Catch-up completed successfully."
    log "Log file: $LOG_FILE"
    exit 0
}

handle_term() {
    log ""
    log "Catch-up received termination signal."
    log "Generated logs and partial outputs will be preserved for the workflow commit step."
    exit 143
}

trap handle_term TERM INT

log "======================================"
log "Catch-up execution started at $NOW"
log "======================================"

log ""
log "[1/24] Running daily pipeline..."
python src/pipeline/daily_pipeline.py >> "$LOG_FILE" 2>&1
DAILY_EXIT_CODE=$?
DART_DATA_AVAILABLE=1

if grep -q "Daily pipeline will stop gracefully without error." "$LOG_FILE"; then
    log ""
    log "No DART data available today."
    log "DART, Naver news, and DART-dependent supplementary steps will be skipped."
    DART_DATA_AVAILABLE=0
fi

if [ "$DAILY_EXIT_CODE" -ne 0 ]; then
    log "Daily pipeline failed with exit code $DAILY_EXIT_CODE."
    exit "$DAILY_EXIT_CODE"
fi

run_required "2/24" "Collecting KIS-first daily price data..." python src/crawler/kis_price_collector.py || exit $?
run_required "3/24" "Building daily price signals..." python src/features/daily_price_signals.py || exit $?
run_required "4/24" "Generating price-based daily candidates..." python src/models/price_based_daily_recommender.py || exit $?
run_required "5/24" "Evaluating price-based candidates..." python src/evaluator/price_candidate_evaluator.py || exit $?

if [ "$DART_DATA_AVAILABLE" = "1" ]; then
    run_required "6/24" "Running pending re-evaluator..." python src/evaluator/pending_re_evaluator.py || exit $?
    run_required "7/24" "Collecting market index data..." python src/crawler/market_index_collector.py || exit $?
    run_required "8/24" "Building market-adjusted features..." python src/features/market_adjusted_features.py || exit $?
    run_required "9/24" "Generating market-adjusted evaluation..." python src/evaluator/market_adjusted_evaluator.py || exit $?
    run_required "10/24" "Generating market-adjusted score adjustments..." python src/models/market_adjusted_score_integrator.py || exit $?
    run_required "11/24" "Generating market-adjusted daily candidate report..." python src/models/market_adjusted_daily_recommender.py || exit $?
    run_required "12/24" "Building trading volume features..." python src/features/trading_volume_features.py || exit $?
    run_required "13/24" "Generating trading volume score adjustments..." python src/models/trading_volume_score_integrator.py || exit $?
    run_required "14/24" "Generating volume + market-adjusted daily candidate report..." python src/models/volume_market_adjusted_daily_recommender.py || exit $?
    run_required "15/24" "Generating model performance history report..." python src/report_generator/model_performance_history_report.py || exit $?
    run_required "16/24" "Generating automation status report..." python src/report_generator/automation_status_report.py || exit $?
    run_required "17/24" "Updating automation history..." python src/report_generator/automation_history_tracker.py || exit $?
    run_required "18/24" "Generating confidence report..." python src/report_generator/confidence_tracker.py || exit $?
    run_required "19/24" "Generating return prediction report..." python src/models/return_prediction_model.py || exit $?
    run_required "20/24" "Generating daily stock candidate report..." python src/models/daily_stock_recommender.py || exit $?
    run_required "21/24" "Generating event-type performance report..." python src/report_generator/event_type_performance_report.py || exit $?
    run_required "22/24" "Generating stock-specific pattern report..." python src/report_generator/stock_pattern_report.py || exit $?
else
    log ""
    log "[6/24-22/24] Skipping DART-dependent supplementary steps because no fresh DART data is available."
fi

run_optional "Collecting Snacks market digest..." python src/crawler/snacks_collector.py
run_optional "Generating Snacks market features..." python src/features/snacks_market_features.py
run_optional "Generating social attention features..." python src/features/social_attention_features.py
run_optional "Generating learned event rules..." python src/models/auto_rule_updater.py
run_optional "Generating learned-rule daily candidate report..." python src/models/learned_rule_daily_recommender.py
run_optional "[23/24] Generating GitHub Pages dashboard..." python src/report_generator/dashboard_generator.py

finish_success
