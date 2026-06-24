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
* Error-note-aware recommendation adjustment
* Event-type success rate adjustment
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

## Stock-Level Learning Layer

The project now includes a stock-specific historical pattern report.

### Stock-Specific Historical Pattern Report

```text
src/report_generator/stock_pattern_report.py
```

This report summarizes historical prediction and event-reaction patterns by stock code.

The report is generated at:

```text
reports/daily_review/YYYY-MM-DD_stock_pattern_report.md
```

The report tracks:

```text
stock_code
corp_name
total_count
evaluated_count
success_count
failure_count
pending_count
success_rate
average next open return
average next close return
most common event type
risk_note
```

This helps identify whether specific stocks have historically shown stronger, weaker, or mostly pending reactions to disclosure events.

## Event-Type Learning Layer

The project also includes an event-type performance report.

```text
src/report_generator/event_type_performance_report.py
```

The report is generated at:

```text
reports/daily_review/YYYY-MM-DD_event_type_performance_report.md
```

It tracks event-type level performance such as success rate and average next-day return.

## Recommendation Layer

The current recommendation score is calculated as:

```text
base_recommendation_score
+ error_note_adjustment_score
+ event_type_performance_adjustment_score
= adjusted_recommendation_score
```

The next step is to add stock-specific historical adjustment to this score.

## Operating Modes

The catch-up script now runs:

```text
[1/10] Daily Pipeline
[2/10] Pending Re-Evaluator
[3/10] Automation Status Report
[4/10] Automation History
[5/10] Confidence Report
[6/10] Return Prediction Report
[7/10] Daily Stock Candidate Report
[8/10] Event-Type Performance Report
[9/10] Stock-Specific Pattern Report
[10/10] Catch-up Completed
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

## Next Steps

* Apply stock-specific historical pattern adjustment to recommendation scoring
* Add stock-level success rate adjustment
* Add stock-level average return adjustment
* Add stock-specific risk notes to daily candidate reports
* Add market index and sector movement features
* Add trading volume features
* Add model performance history
* Add automatic Git commit and push
* Add automatic daily blog generation
* Add probability-based prediction output
* Add feature importance analysis
* Expand news sources and sentiment analysis
* Add SNS and investor attention indicators
