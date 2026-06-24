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
* Market index collection
* Stock market lookup
* Market-adjusted return feature generation
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
* Error-note-aware recommendation adjustment
* Event-type success rate adjustment
* Stock-specific pattern adjustment
* Single stock predictor
* Event-type performance report
* Stock-specific historical pattern report
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

## Market Adjustment Layer

The project now includes market index and market-adjusted return features.

### Market Index Collector

```text
src/crawler/market_index_collector.py
```

This module collects market reference data.

It first tries to collect direct KOSPI and KOSDAQ index data.

If direct index collection fails, it uses ETF proxy data as a fallback.

The fallback proxies are:

```text
KOSPI proxy: KODEX 200
KOSDAQ proxy: KODEX KOSDAQ 150
```

It also creates a stock market lookup table to identify whether stocks belong to KOSPI or KOSDAQ.

Generated raw files:

```text
data/raw/market_index_YYYYMMDD.csv
data/raw/stock_market_lookup_YYYYMMDD.csv
```

### Market-Adjusted Feature Builder

```text
src/features/market_adjusted_features.py
```

This module joins error-note data with market index data and calculates market-adjusted returns.

Generated processed file:

```text
data/processed/market_adjusted_features_YYYYMMDD.csv
```

The main features are:

```text
market_next_open_return
market_next_close_return
market_adjusted_next_open_return
market_adjusted_next_close_return
market_group
market_group_source
market_source_type
market_proxy_name
```

The core calculation is:

```text
market_adjusted_next_close_return
= stock_next_close_return - market_next_close_return
```

## Recommendation Layer

The current recommendation score is calculated as:

```text
base_recommendation_score
+ error_note_adjustment_score
+ event_type_performance_adjustment_score
+ stock_specific_pattern_adjustment_score
= adjusted_recommendation_score
```

The next step is to incorporate market-adjusted returns into evaluation and recommendation logic.

## Stock-Level Learning Layer

The project includes a stock-specific historical pattern report.

```text
src/report_generator/stock_pattern_report.py
```

The report is generated at:

```text
reports/daily_review/YYYY-MM-DD_stock_pattern_report.md
```

## Event-Type Learning Layer

The project includes an event-type performance report.

```text
src/report_generator/event_type_performance_report.py
```

The report is generated at:

```text
reports/daily_review/YYYY-MM-DD_event_type_performance_report.md
```

## Operating Modes

The catch-up script currently runs:

```text
[1/12] Daily Pipeline
[2/12] Pending Re-Evaluator
[3/12] Market Index Collection
[4/12] Market-Adjusted Features
[5/12] Automation Status Report
[6/12] Automation History
[7/12] Confidence Report
[8/12] Return Prediction Report
[9/12] Daily Stock Candidate Report
[10/12] Event-Type Performance Report
[11/12] Stock-Specific Pattern Report
[12/12] Completed
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
* Day 17: Error-Note-Aware Recommender
* Day 18: Event-Type Performance Report
* Day 19: Event-Type Success Rate Adjustment
* Day 20: Stock-Specific Historical Pattern Report
* Day 21: Stock-Specific Pattern Adjustment
* Day 22: Market Index and Market-Adjusted Return Features

## Next Steps

* Use market-adjusted returns in error-note evaluation
* Add market-adjusted success/failure logic
* Separate stock-specific reaction from market-wide movement
* Add sector-level return comparison
* Add trading volume features
* Add model performance history
* Add automatic Git commit and push
* Add automatic daily blog generation
* Add probability-based prediction output
* Add feature importance analysis
* Expand news sources and sentiment analysis
* Add SNS and investor attention indicators
