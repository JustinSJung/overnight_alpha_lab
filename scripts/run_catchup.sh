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
    log "[19/19] Catch-up execution completed."
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
log "[1/19] Running daily pipeline..."
python src/pipeline/daily_pipeline.py >> "$LOG_FILE" 2>&1
DAILY_EXIT_CODE=$?

if grep -q "Daily pipeline will stop gracefully without error." "$LOG_FILE"; then
    log ""
    log "No DART data available today."
    log "Skipping downstream reports and dashboard update to preserve previous dashboard values."
    log "Catch-up execution completed without new data."
    exit 0
fi

if [ "$DAILY_EXIT_CODE" -ne 0 ]; then
    log "Daily pipeline failed with exit code $DAILY_EXIT_CODE."
    exit "$DAILY_EXIT_CODE"
fi

run_required "2/19" "Running pending re-evaluator..." python src/evaluator/pending_re_evaluator.py || exit $?
run_required "3/19" "Collecting market index data..." python src/crawler/market_index_collector.py || exit $?
run_required "4/19" "Building market-adjusted features..." python src/features/market_adjusted_features.py || exit $?
run_required "5/19" "Generating market-adjusted evaluation..." python src/evaluator/market_adjusted_evaluator.py || exit $?
run_required "6/19" "Generating market-adjusted score adjustments..." python src/models/market_adjusted_score_integrator.py || exit $?
run_required "7/19" "Generating market-adjusted daily candidate report..." python src/models/market_adjusted_daily_recommender.py || exit $?
run_required "8/19" "Building trading volume features..." python src/features/trading_volume_features.py || exit $?
run_required "9/19" "Generating trading volume score adjustments..." python src/models/trading_volume_score_integrator.py || exit $?
run_required "10/19" "Generating volume + market-adjusted daily candidate report..." python src/models/volume_market_adjusted_daily_recommender.py || exit $?
run_required "11/19" "Generating model performance history report..." python src/report_generator/model_performance_history_report.py || exit $?
run_required "12/19" "Generating automation status report..." python src/report_generator/automation_status_report.py || exit $?
run_required "13/19" "Updating automation history..." python src/report_generator/automation_history_tracker.py || exit $?
run_required "14/19" "Generating confidence report..." python src/report_generator/confidence_tracker.py || exit $?
run_required "15/19" "Generating return prediction report..." python src/models/return_prediction_model.py || exit $?
run_required "16/19" "Generating daily stock candidate report..." python src/models/daily_stock_recommender.py || exit $?
run_required "17/19" "Generating event-type performance report..." python src/report_generator/event_type_performance_report.py || exit $?
run_required "18/19" "Generating stock-specific pattern report..." python src/report_generator/stock_pattern_report.py || exit $?

run_optional "Collecting Snacks market digest..." python src/crawler/snacks_collector.py
run_optional "Generating Snacks market features..." python src/features/snacks_market_features.py
run_optional "Generating social attention features..." python src/features/social_attention_features.py
run_optional "Generating learned event rules..." python src/models/auto_rule_updater.py
run_optional "Generating learned-rule daily candidate report..." python src/models/learned_rule_daily_recommender.py
run_optional "Generating GitHub Pages dashboard..." python src/report_generator/dashboard_generator.py

finish_success
