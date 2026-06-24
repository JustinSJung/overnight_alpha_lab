#!/bin/bash

cd "$(dirname "$0")/.."

source .venv/bin/activate

mkdir -p logs

TODAY=$(date +"%Y-%m-%d")
NOW=$(date +"%Y-%m-%d %H:%M:%S")

LOG_FILE="logs/catchup_$TODAY.log"

echo "======================================" >> "$LOG_FILE"
echo "Catch-up execution started at $NOW" >> "$LOG_FILE"
echo "======================================" >> "$LOG_FILE"

echo "" >> "$LOG_FILE"
echo "[1/13] Running daily pipeline..." >> "$LOG_FILE"
python src/pipeline/daily_pipeline.py >> "$LOG_FILE" 2>&1

if [ $? -ne 0 ]; then
    echo "Daily pipeline failed." >> "$LOG_FILE"
    exit 1
fi

echo "" >> "$LOG_FILE"
echo "[2/13] Running pending re-evaluator..." >> "$LOG_FILE"
python src/evaluator/pending_re_evaluator.py >> "$LOG_FILE" 2>&1

if [ $? -ne 0 ]; then
    echo "Pending re-evaluator failed." >> "$LOG_FILE"
    exit 1
fi

echo "" >> "$LOG_FILE"
echo "[3/13] Collecting market index data..." >> "$LOG_FILE"
python src/crawler/market_index_collector.py >> "$LOG_FILE" 2>&1

if [ $? -ne 0 ]; then
    echo "Market index collection failed." >> "$LOG_FILE"
    exit 1
fi

echo "" >> "$LOG_FILE"
echo "[4/13] Building market-adjusted features..." >> "$LOG_FILE"
python src/features/market_adjusted_features.py >> "$LOG_FILE" 2>&1

if [ $? -ne 0 ]; then
    echo "Market-adjusted feature generation failed." >> "$LOG_FILE"
    exit 1
fi

echo "" >> "$LOG_FILE"
echo "[5/13] Generating market-adjusted evaluation..." >> "$LOG_FILE"
python src/evaluator/market_adjusted_evaluator.py >> "$LOG_FILE" 2>&1

if [ $? -ne 0 ]; then
    echo "Market-adjusted evaluation failed." >> "$LOG_FILE"
    exit 1
fi

echo "" >> "$LOG_FILE"
echo "[6/13] Generating automation status report..." >> "$LOG_FILE"
python src/report_generator/automation_status_report.py >> "$LOG_FILE" 2>&1

if [ $? -ne 0 ]; then
    echo "Automation status report generation failed." >> "$LOG_FILE"
    exit 1
fi

echo "" >> "$LOG_FILE"
echo "[7/13] Updating automation history..." >> "$LOG_FILE"
python src/report_generator/automation_history_tracker.py >> "$LOG_FILE" 2>&1

if [ $? -ne 0 ]; then
    echo "Automation history update failed." >> "$LOG_FILE"
    exit 1
fi

echo "" >> "$LOG_FILE"
echo "[8/13] Generating confidence report..." >> "$LOG_FILE"
python src/report_generator/confidence_tracker.py >> "$LOG_FILE" 2>&1

if [ $? -ne 0 ]; then
    echo "Confidence report generation failed." >> "$LOG_FILE"
    exit 1
fi

echo "" >> "$LOG_FILE"
echo "[9/13] Generating return prediction report..." >> "$LOG_FILE"
python src/models/return_prediction_model.py >> "$LOG_FILE" 2>&1

if [ $? -ne 0 ]; then
    echo "Return prediction report generation failed." >> "$LOG_FILE"
    exit 1
fi

echo "" >> "$LOG_FILE"
echo "[10/13] Generating daily stock candidate report..." >> "$LOG_FILE"
python src/models/daily_stock_recommender.py >> "$LOG_FILE" 2>&1

if [ $? -ne 0 ]; then
    echo "Daily stock candidate report generation failed." >> "$LOG_FILE"
    exit 1
fi

echo "" >> "$LOG_FILE"
echo "[11/13] Generating event-type performance report..." >> "$LOG_FILE"
python src/report_generator/event_type_performance_report.py >> "$LOG_FILE" 2>&1

if [ $? -ne 0 ]; then
    echo "Event-type performance report generation failed." >> "$LOG_FILE"
    exit 1
fi

echo "" >> "$LOG_FILE"
echo "[12/13] Generating stock-specific pattern report..." >> "$LOG_FILE"
python src/report_generator/stock_pattern_report.py >> "$LOG_FILE" 2>&1

if [ $? -ne 0 ]; then
    echo "Stock-specific pattern report generation failed." >> "$LOG_FILE"
    exit 1
fi

echo "" >> "$LOG_FILE"
echo "[13/13] Catch-up execution completed." >> "$LOG_FILE"
echo "Finished at $(date +"%Y-%m-%d %H:%M:%S")" >> "$LOG_FILE"
echo "======================================" >> "$LOG_FILE"

echo "Catch-up completed successfully."
echo "Log file: $LOG_FILE"
