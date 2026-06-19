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
* GitHub Pages portfolio blog

## Current Pipeline

```text
DART Disclosure Collection
↓
Disclosure Event Parsing
↓
Key Event Selection
↓
Rule-Based Event Scoring
↓
Naver News Metadata Collection
↓
News Feature Generation
↓
Stock Price Data Collection
↓
Event-Price Reaction Evaluation
↓
Prediction Review and Error Note Generation
↓
Machine Learning Dataset Building
↓
Baseline Machine Learning Model
↓
Model Report Generation
↓
Daily Report and Blog Documentation
```

## Local Automation

```text
scripts/run_daily_pipeline.sh
scripts/run_pending_re_evaluator.sh
```

The local automation scripts activate the virtual environment, run the relevant pipeline, and save logs under the `logs/` directory.

The `logs/` directory is excluded from GitHub.

## Additional Re-Evaluation Flow

```text
Pending Event Detection
↓
Updated Price Data Collection
↓
Event Reaction Re-Evaluation
↓
Error Note Regeneration
↓
ML Dataset Rebuilding
↓
Baseline Model Re-Execution
```

## Latest Blog Posts

* Day 1: DART API Collector and Event Report
* Day 2: Automated Event Scoring Pipeline
* Day 3: Prediction Review and Error Note Generator
* Day 4: News Features and ML Dataset Builder
* Day 5: Baseline Machine Learning Model
* Day 6: Pending Event Re-Evaluation System
* Day 7: Local Daily Automation Scripts

## Next Steps

* Register local scripts with macOS launchd or cron
* Continue daily pipeline execution after new price data becomes available
* Re-evaluate pending rows and convert them into success/failure samples
* Add model evaluation metrics
* Add probability-based prediction output
* Add feature importance analysis
* Add automatic daily blog generation
* Add GitHub Actions or local scheduled automation
* Expand news sources and sentiment analysis
* Add SNS and investor attention indicators
