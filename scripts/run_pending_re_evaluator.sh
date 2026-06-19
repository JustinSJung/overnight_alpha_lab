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

echo "======================================" >> logs/pending_re_evaluator_$TODAY.log
echo "Pending re-evaluator started at $NOW" >> logs/pending_re_evaluator_$TODAY.log
echo "======================================" >> logs/pending_re_evaluator_$TODAY.log

# Run pending re-evaluator
python src/evaluator/pending_re_evaluator.py >> logs/pending_re_evaluator_$TODAY.log 2>&1

echo "" >> logs/pending_re_evaluator_$TODAY.log
echo "Pending re-evaluator finished at $(date +"%Y-%m-%d %H:%M:%S")" >> logs/pending_re_evaluator_$TODAY.log
echo "======================================" >> logs/pending_re_evaluator_$TODAY.log
