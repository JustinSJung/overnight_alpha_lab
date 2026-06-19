#!/bin/bash

# Move to project root
cd "$(dirname "$0")/.."

# Activate virtual environment
source .venv/bin/activate

# Create log directory
mkdir -p logs

# Current timestamp
TODAY=$(date +"%Y-%m-%d")
NOW=$(date +"%Y-%m-%d %H:%M:%S")

echo "======================================" >> logs/daily_pipeline_$TODAY.log
echo "Daily pipeline started at $NOW" >> logs/daily_pipeline_$TODAY.log
echo "======================================" >> logs/daily_pipeline_$TODAY.log

# Run daily pipeline
python src/pipeline/daily_pipeline.py >> logs/daily_pipeline_$TODAY.log 2>&1

echo "" >> logs/daily_pipeline_$TODAY.log
echo "Daily pipeline finished at $(date +"%Y-%m-%d %H:%M:%S")" >> logs/daily_pipeline_$TODAY.log
echo "======================================" >> logs/daily_pipeline_$TODAY.log
