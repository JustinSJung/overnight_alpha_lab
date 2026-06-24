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

## Recommendation Layer

The project now includes a multi-layer recommendation score.

### Daily Stock Recommender

```text
src/models/daily_stock_recommender.py
```

The recommender generates a daily stock candidate report at:

```text
reports/daily_prediction/YYYY-MM-DD_daily_stock_candidates.md
```

The current adjusted recommendation score is calculated as:

```text
base_recommendation_score
+ error_note_adjustment_score
+ event_type_performance_adjustment_score
= adjusted_recommendation_score
```

The recommender now considers:

```text
event score
news sentiment
news attention
negative keyword count
prediction direction
advanced error-note learning
event-type historical success rate
event-type average next-day return
risk filters
```

### Event-Type Success Rate Adjustment

The recommender calculates event-type performance adjustment using:

```text
event_type_success_rate
event_type_avg_next_open_return
event_type_avg_next_close_return
event_type_success_rate_adjustment
event_type_return_adjustment
event_type_performance_adjustment_score
```

This allows event types with better historical performance to receive stronger confidence, while weak event types can receive a conservative penalty.

## Performance Monitoring Layer

The project includes an event-type performance report.

```text
src/report_generator/event_type_performance_report.py
```

The report is generated at:

```text
reports/daily_review/YYYY-MM-DD_event_type_performance_report.md
```

It tracks:

```text
total_count
evaluated_count
success_count
failure_count
pending_count
success_rate
average next open return
average next close return
confidence adjustment bias
```

## Learning Layer

The project includes advanced error-note generation.

```text
src/evaluator/error_note_generator.py
```

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

## Prediction Layer

The project currently includes:

```text
src/models/baseline_model.py
src/models/return_prediction_model.py
src/models/single_stock_predictor.py
```

The single stock predictor can be executed like this:

```text
python src/models/single_stock_predictor.py 005930
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

## Next Steps

* Build stock-specific historical pattern report
* Add stock-level success rate
* Add stock-level average return
* Add stock-specific risk notes
* Add market index and sector movement features
* Add trading volume features
* Add model performance history
* Add automatic Git commit and push
* Add automatic daily blog generation
* Add probability-based prediction output
* Add feature importance analysis
* Expand news sources and sentiment analysis
* Add SNS and investor attention indicators
