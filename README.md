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
* Prediction review and error-note generation
* Machine learning dataset builder
* Baseline machine learning model
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

## Monitoring Layer

The project includes three monitoring outputs.

### Daily Status Report

```text
reports/daily_review/YYYY-MM-DD_automation_status_report.md
```

This report summarizes the latest execution state in a human-readable format.

### Automation History

```text
data/processed/automation_history.csv
```

This file stores cumulative operating metrics over time.

### Confidence Report

```text
reports/daily_review/YYYY-MM-DD_confidence_report.md
```

This report summarizes prediction readiness, trainable rows, overall accuracy, event-type success rate, and prediction-direction success rate.

## Operating Modes

The project currently supports two local operating modes.

### Scheduled Mode

Scheduled mode uses cron.

```text
16:10 every day - run_daily_pipeline.sh
16:40 every day - run_pending_re_evaluator.sh
```

### Catch-Up Mode

Catch-up mode is used when the scheduled job was missed.

```text
./scripts/run_catchup.sh
```

The catch-up script runs:

```text
Daily Pipeline
↓
Pending Re-Evaluation
↓
Automation Status Report
↓
Automation History Update
↓
Confidence Report
↓
Log Generation
```

## Local Automation Scripts

```text
scripts/run_daily_pipeline.sh
scripts/run_pending_re_evaluator.sh
scripts/run_catchup.sh
```

Execution logs are saved under:

```text
logs/
```

The `logs/` directory is excluded from GitHub.

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

## Next Steps

* Build return prediction model
* Predict expected next-day open return
* Predict expected next-day close return
* Add daily stock recommender
* Add single stock predictor
* Improve advanced error-note reasoning
* Track confidence improvement over time
* Add model performance history
* Add automatic Git commit and push
* Add automatic daily blog generation
* Add probability-based prediction output
* Add feature importance analysis
* Expand news sources and sentiment analysis
* Add SNS and investor attention indicators
