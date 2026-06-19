#!/bin/bash

# Move to project root
cd "$(dirname "$0")/.."

# Activate virtual environment
source .venv/bin/activate

# Create log directory
mkdir -p logs

TODAY=$(date +"%Y-%m-%d")
NOW=$(date +"%Y-%m-%d %H:%M:%S")

LOG_FILE="logs/catchup_$TODAY.log"

echo "======================================" >> "$LOG_FILE"
echo "Catch-up execution started at $NOW" >> "$LOG_FILE"
echo "======================================" >> "$LOG_FILE"

echo "" >> "$LOG_FILE"
echo "[1/3] Running daily pipeline..." >> "$LOG_FILE"
python src/pipeline/daily_pipeline.py >> "$LOG_FILE" 2>&1

DAILY_STATUS=$?

if [ $DAILY_STATUS -ne 0 ]; then
    echo "" >> "$LOG_FILE"
    echo "Daily pipeline failed." >> "$LOG_FILE"
    echo "Catch-up stopped at $(date +"%Y-%m-%d %H:%M:%S")" >> "$LOG_FILE"
    echo "======================================" >> "$LOG_FILE"
    exit 1
fi

echo "" >> "$LOG_FILE"
echo "[2/3] Running pending re-evaluator..." >> "$LOG_FILE"
python src/evaluator/pending_re_evaluator.py >> "$LOG_FILE" 2>&1

PENDING_STATUS=$?

if [ $PENDING_STATUS -ne 0 ]; then
    echo "" >> "$LOG_FILE"
    echo "Pending re-evaluator failed." >> "$LOG_FILE"
    echo "Catch-up stopped at $(date +"%Y-%m-%d %H:%M:%S")" >> "$LOG_FILE"
    echo "======================================" >> "$LOG_FILE"
    exit 1
fi

echo "" >> "$LOG_FILE"
echo "[3/5] Generating automation status report..." >> "$LOG_FILE"
python src/report_generator/automation_status_report.py >> "$LOG_FILE" 2>&1

STATUS_REPORT_STATUS=$?

if [ $STATUS_REPORT_STATUS -ne 0 ]; then
    echo "" >> "$LOG_FILE"
    echo "Automation status report generation failed." >> "$LOG_FILE"
    echo "Catch-up stopped at $(date +"%Y-%m-%d %H:%M:%S")" >> "$LOG_FILE"
    echo "======================================" >> "$LOG_FILE"
    exit 1
fi

echo "" >> "$LOG_FILE"
echo "[4/5] Updating automation history..." >> "$LOG_FILE"
python src/report_generator/automation_history_tracker.py >> "$LOG_FILE" 2>&1

HISTORY_STATUS=$?

if [ $HISTORY_STATUS -ne 0 ]; then
    echo "" >> "$LOG_FILE"
    echo "Automation history update failed." >> "$LOG_FILE"
    echo "Catch-up stopped at $(date +"%Y-%m-%d %H:%M:%S")" >> "$LOG_FILE"
    echo "======================================" >> "$LOG_FILE"
    exit 1
fi

echo "" >> "$LOG_FILE"
echo "[5/5] Catch-up execution completed." >> "$LOG_FILE"
echo "Finished at $(date +"%Y-%m-%d %H:%M:%S")" >> "$LOG_FILE"
echo "======================================" >> "$LOG_FILE"

echo "Catch-up completed successfully."
echo "Log file: $LOG_FILE"

