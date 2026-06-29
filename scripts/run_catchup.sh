#!/bin/bash

cd "$(dirname "$0")/.."

if [ -f ".venv/bin/activate" ]; then
    source .venv/bin/activate
fi

mkdir -p logs

TODAY=$(date +"%Y-%m-%d")
NOW=$(date +"%Y-%m-%d %H:%M:%S")

LOG_FILE="logs/catchup_$TODAY.log"

echo "======================================" >> "$LOG_FILE"
echo "Catch-up execution started at $NOW" >> "$LOG_FILE"
echo "======================================" >> "$LOG_FILE"

echo "" >> "$LOG_FILE"
echo "[1/19] Running daily pipeline..." >> "$LOG_FILE"
python src/pipeline/daily_pipeline.py >> "$LOG_FILE" 2>&1

if grep -q "Daily pipeline will stop gracefully without error." "$LOG_FILE"; then
    echo "" >> "$LOG_FILE"
    echo "No DART data available today." >> "$LOG_FILE"
    echo "Skipping downstream reports and dashboard update to preserve previous dashboard values." >> "$LOG_FILE"
    echo "Catch-up execution completed without new data." >> "$LOG_FILE"
    exit 0
fi

if [ $? -ne 0 ]; then
    echo "Daily pipeline failed." >> "$LOG_FILE"
    exit 1
fi

echo "" >> "$LOG_FILE"
echo "[2/19] Running pending re-evaluator..." >> "$LOG_FILE"
python src/evaluator/pending_re_evaluator.py >> "$LOG_FILE" 2>&1

if [ $? -ne 0 ]; then
    echo "Pending re-evaluator failed." >> "$LOG_FILE"
    exit 1
fi

echo "" >> "$LOG_FILE"
echo "[3/19] Collecting market index data..." >> "$LOG_FILE"
python src/crawler/market_index_collector.py >> "$LOG_FILE" 2>&1

if [ $? -ne 0 ]; then
    echo "Market index collection failed." >> "$LOG_FILE"
    exit 1
fi

echo "" >> "$LOG_FILE"
echo "[4/19] Building market-adjusted features..." >> "$LOG_FILE"
python src/features/market_adjusted_features.py >> "$LOG_FILE" 2>&1

if [ $? -ne 0 ]; then
    echo "Market-adjusted feature generation failed." >> "$LOG_FILE"
    exit 1
fi

echo "" >> "$LOG_FILE"
echo "[5/19] Generating market-adjusted evaluation..." >> "$LOG_FILE"
python src/evaluator/market_adjusted_evaluator.py >> "$LOG_FILE" 2>&1

if [ $? -ne 0 ]; then
    echo "Market-adjusted evaluation failed." >> "$LOG_FILE"
    exit 1
fi

echo "" >> "$LOG_FILE"
echo "[6/19] Generating market-adjusted score adjustments..." >> "$LOG_FILE"
python src/models/market_adjusted_score_integrator.py >> "$LOG_FILE" 2>&1

if [ $? -ne 0 ]; then
    echo "Market-adjusted score integration failed." >> "$LOG_FILE"
    exit 1
fi


echo "" >> "$LOG_FILE"
echo "[7/19] Generating market-adjusted daily candidate report..." >> "$LOG_FILE"
python src/models/market_adjusted_daily_recommender.py >> "$LOG_FILE" 2>&1

if [ $? -ne 0 ]; then
    echo "Market-adjusted daily recommender failed." >> "$LOG_FILE"
    exit 1
fi


echo "" >> "$LOG_FILE"
echo "[8/19] Building trading volume features..." >> "$LOG_FILE"
python src/features/trading_volume_features.py >> "$LOG_FILE" 2>&1

if [ $? -ne 0 ]; then
    echo "Trading volume feature generation failed." >> "$LOG_FILE"
    exit 1
fi


echo "" >> "$LOG_FILE"
echo "[9/19] Generating trading volume score adjustments..." >> "$LOG_FILE"
python src/models/trading_volume_score_integrator.py >> "$LOG_FILE" 2>&1

if [ $? -ne 0 ]; then
    echo "Trading volume score integration failed." >> "$LOG_FILE"
    exit 1
fi


echo "" >> "$LOG_FILE"
echo "[10/19] Generating volume + market-adjusted daily candidate report..." >> "$LOG_FILE"
python src/models/volume_market_adjusted_daily_recommender.py >> "$LOG_FILE" 2>&1

if [ $? -ne 0 ]; then
    echo "Volume + market-adjusted daily recommender failed." >> "$LOG_FILE"
    exit 1
fi


echo "" >> "$LOG_FILE"
echo "[11/19] Generating model performance history report..." >> "$LOG_FILE"
python src/report_generator/model_performance_history_report.py >> "$LOG_FILE" 2>&1

if [ $? -ne 0 ]; then
    echo "Model performance history report generation failed." >> "$LOG_FILE"
    exit 1
fi

echo "" >> "$LOG_FILE"
echo "[12/19] Generating automation status report..." >> "$LOG_FILE"
python src/report_generator/automation_status_report.py >> "$LOG_FILE" 2>&1

if [ $? -ne 0 ]; then
    echo "Automation status report generation failed." >> "$LOG_FILE"
    exit 1
fi

echo "" >> "$LOG_FILE"
echo "[13/19] Updating automation history..." >> "$LOG_FILE"
python src/report_generator/automation_history_tracker.py >> "$LOG_FILE" 2>&1

if [ $? -ne 0 ]; then
    echo "Automation history update failed." >> "$LOG_FILE"
    exit 1
fi

echo "" >> "$LOG_FILE"
echo "[14/19] Generating confidence report..." >> "$LOG_FILE"
python src/report_generator/confidence_tracker.py >> "$LOG_FILE" 2>&1

if [ $? -ne 0 ]; then
    echo "Confidence report generation failed." >> "$LOG_FILE"
    exit 1
fi

echo "" >> "$LOG_FILE"
echo "[15/19] Generating return prediction report..." >> "$LOG_FILE"
python src/models/return_prediction_model.py >> "$LOG_FILE" 2>&1

if [ $? -ne 0 ]; then
    echo "Return prediction report generation failed." >> "$LOG_FILE"
    exit 1
fi

echo "" >> "$LOG_FILE"
echo "[16/19] Generating daily stock candidate report..." >> "$LOG_FILE"
python src/models/daily_stock_recommender.py >> "$LOG_FILE" 2>&1

if [ $? -ne 0 ]; then
    echo "Daily stock candidate report generation failed." >> "$LOG_FILE"
    exit 1
fi

echo "" >> "$LOG_FILE"
echo "[17/19] Generating event-type performance report..." >> "$LOG_FILE"
python src/report_generator/event_type_performance_report.py >> "$LOG_FILE" 2>&1

if [ $? -ne 0 ]; then
    echo "Event-type performance report generation failed." >> "$LOG_FILE"
    exit 1
fi

echo "" >> "$LOG_FILE"
echo "[18/19] Generating stock-specific pattern report..." >> "$LOG_FILE"
python src/report_generator/stock_pattern_report.py >> "$LOG_FILE" 2>&1

if [ $? -ne 0 ]; then
    echo "Stock-specific pattern report generation failed." >> "$LOG_FILE"
    exit 1
fi

echo "" >> "$LOG_FILE"
echo "Generating social attention features..." >> "$LOG_FILE"
python src/features/social_attention_features.py >> "$LOG_FILE" 2>&1 || echo "Social attention feature generation skipped or failed." >> "$LOG_FILE"

echo "" >> "$LOG_FILE"
echo "Generating learned event rules..." >> "$LOG_FILE"
python src/models/auto_rule_updater.py >> "$LOG_FILE" 2>&1 || echo "Learned event rule generation skipped or failed." >> "$LOG_FILE"

echo "" >> "$LOG_FILE"
echo "Generating learned-rule daily candidate report..." >> "$LOG_FILE"
python src/models/learned_rule_daily_recommender.py >> "$LOG_FILE" 2>&1 || echo "Learned-rule daily candidate report skipped or failed." >> "$LOG_FILE"

echo "" >> "$LOG_FILE"
echo "Generating GitHub Pages dashboard..." >> "$LOG_FILE"
python src/report_generator/dashboard_generator.py >> "$LOG_FILE" 2>&1 || echo "Dashboard generation skipped or failed." >> "$LOG_FILE"

echo "" >> "$LOG_FILE"
echo "[19/19] Catch-up execution completed." >> "$LOG_FILE"
echo "Finished at $(date +"%Y-%m-%d %H:%M:%S")" >> "$LOG_FILE"
echo "======================================" >> "$LOG_FILE"

echo "Catch-up completed successfully."
echo "Log file: $LOG_FILE"

exit 0
