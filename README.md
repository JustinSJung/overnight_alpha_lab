# Overnight Alpha Lab

Overnight Alpha Lab is an AI research project that analyzes corporate disclosures, news, and market data released after market close, predicts next-day opening reactions, and improves the model through daily error notes.

This project focuses not on predicting stock prices directly, but on modeling how the market reacts to newly released information.

## Core Concept

1. Collect disclosures, news, and market data after market close
2. Generate next-day opening reaction predictions
3. Compare predictions with actual market results
4. Create daily error notes
5. Improve the model through continuous feedback

## Project Scope

- Korean stock market event analysis
- DART disclosure data
- News and sentiment data
- Next-day opening reaction prediction
- Daily prediction review
- Error-note based model improvement

## Repository Structure

```text
overnight_alpha_lab/
├── data/
│   ├── raw/
│   ├── processed/
│   └── predictions/
├── notebooks/
├── src/
│   ├── crawler/
│   ├── parser/
│   ├── features/
│   ├── models/
│   ├── evaluator/
│   └── report_generator/
├── reports/
│   ├── daily_prediction/
│   ├── daily_review/
│   └── error_notes/
├── blog/
│   └── _posts/
├── README.md
└── requirements.txt

## Status

project setup stage.

## Current Progress

The project currently includes:

* GitHub repository and Python project structure
* OpenDART API disclosure collection
* DART disclosure event parsing
* Daily Markdown report generation
* Korean stock price data collection
* Event-price reaction evaluation
* Automated key event selection pipeline
* Rule-based event scoring model
* Naver news metadata collection
* News feature generation
* Advanced prediction review and error-note generation
* Machine learning dataset builder
* Baseline machine learning model
* Return prediction model
* Daily stock recommender
* Single stock predictor
* Daily model report generation
* Pending event re-evaluation system
* Local daily automation scripts
* Execution log generation
* Scheduled local automation with cron
* Catch-up execution mode
* Automation status report generator
* Automation history tracker
* Confidence tracker
* GitHub Pages portfolio blog

## Learning Layer

The project now includes an advanced learning-note layer.

### Advanced Error Note Generator

```text
src/evaluator/error_note_generator.py
```

The error-note generator compares predicted direction with actual next-day price reaction and creates structured learning notes.

The output is saved at:

```text
data/predictions/error_notes_YYYYMMDD.csv
```

The advanced error notes include:

```text
prediction_result
error_category
detailed_error_reason
learning_point
next_rule_adjustment
confidence_adjustment
```

This allows the system to record not only whether a prediction was right or wrong, but also why the result may have happened and how future rules should be adjusted.

## Prediction Layer

The project now includes four early prediction layers.

### Baseline Classification Model

```text
src/models/baseline_model.py
```

This model checks whether evaluated predictions can be classified as success or failure.

### Return Prediction Model

```text
src/models/return_prediction_model.py
```

This model is designed to predict:

```text
next_open_return
next_close_return
```

At the current stage, the model may report `NOT_ENOUGH_DATA` because many event rows are still pending.

### Daily Stock Recommender

```text
src/models/daily_stock_recommender.py
```

This module generates a daily stock candidate report.

The report separates candidates into:

```text
Positive Candidates
Volatile Watchlist
General Watchlist
Risk / Avoid Review List
```

### Single Stock Predictor

```text
src/models/single_stock_predictor.py
```

This module generates a focused report for a user-provided stock code.

Example:

```text
python src/models/single_stock_predictor.py 005930
```

The report is generated at:

```text
reports/single_stock/YYYY-MM-DD_STOCKCODE_single_stock_report.md
```

## Latest Blog Posts

* Day 1: DART API Collector and Event Report
* Day 2: Automated Event Scoring Pipeline
* Day 3: Prediction Review and Error Note Generator
* Day 4: News Features and ML Dataset Builder
* Day 5: Baseline Machine Learning Model
* Day 6: Pending Event Re-Evaluation System
* Day 7: Local Daily Automation Scripts
* Day 8: Scheduled Local Automation
* Day 9: Catch-Up Execution Mode
* Day 10: Automation Status Report
* Day 11: Automation History Tracker
* Day 12: Confidence Tracker
* Day 13: Return Prediction Model
* Day 14: Daily Stock Recommender
* Day 15: Single Stock Predictor
* Day 16: Advanced Error Note Generator

## Next Steps

* Apply error-note learning results to recommendation scoring
* Reduce confidence for repeatedly failed event patterns
* Increase confidence for repeatedly successful event patterns
* Add event-type based success rates
* Add confidence-adjusted recommendation scores
* Add model performance history
* Add automatic Git commit and push
* Add automatic daily blog generation
* Add probability-based prediction output
* Add feature importance analysis
* Expand news sources and sentiment analysis
* Add SNS and investor attention indicators

