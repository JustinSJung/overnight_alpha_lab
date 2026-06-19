# Day 12: Confidence Tracker

## What I Built Today

Today, I added a confidence tracker to Overnight Alpha Lab.

The project already had a machine learning dataset, baseline model report, automation status report, and automation history tracker.

The next important step was to measure whether the system is becoming more reliable over time.

The confidence tracker analyzes the latest ML dataset and generates a confidence report.

## Why This Matters

The final goal of this project is not just to collect market data.

The goal is to create a system that can:

* predict market reactions
* compare predictions with actual outcomes
* learn from mistakes
* track whether prediction confidence improves over time

The confidence tracker is the first step toward measuring that improvement.

## New File

The new confidence tracker is:

```text
src/report_generator/confidence_tracker.py
```

It generates:

```text
reports/daily_review/YYYY-MM-DD_confidence_report.md
```

## What the Confidence Report Measures

The confidence report checks:

```text
total rows
pending rows
success rows
failure rows
trainable rows
overall accuracy
event-type success rate
prediction-direction success rate
model readiness level
```

This helps show whether the system has enough evaluated data to trust the model.

## Model Readiness Levels

The report classifies the current model readiness level.

Examples include:

```text
NOT_READY
DATA_TOO_SMALL
EARLY_STAGE
LOW_CONFIDENCE
WATCHLIST
MODERATE_CONFIDENCE
HIGH_CONFIDENCE
```

At the current stage, the model may still show:

```text
NOT_READY
```

This is expected if most rows are still pending.

## Why Pending Rows Matter

Many events cannot be evaluated immediately because next trading day price data may not be available yet.

Those events stay as:

```text
pending
```

Once price data becomes available, the pending re-evaluation system can convert them into:

```text
success
failure
```

Only success and failure rows are used to measure prediction accuracy.

## Catch-Up Integration

The confidence tracker is now connected to the catch-up script.

The catch-up script now runs:

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

This means that whenever I run:

```text
./scripts/run_catchup.sh
```

the system updates the data, rebuilds the ML dataset, updates history, and generates a confidence report.

## Why This Is Progress

This step moves the project closer to the original goal.

The system is no longer only collecting data.

It is starting to measure whether its own predictions are becoming more reliable.

This is important because a prediction system needs a way to show confidence, not just output predictions.

## Current System Status

The project now includes:

```text
DART disclosure collection
Disclosure event parsing
Key event selection
Rule-based event scoring
Naver news metadata collection
News feature generation
Stock price data collection
Event-price reaction evaluation
Prediction review and error-note generation
Machine learning dataset building
Baseline machine learning model
Pending event re-evaluation
Local automation scripts
Scheduled cron automation
Catch-up execution mode
Automation status report
Automation history tracker
Confidence tracker
Execution log generation
```

## Next Step

The next step is to build a return prediction model.

Until now, the system has focused mainly on whether a prediction was correct or incorrect.

The next step is to estimate:

* expected next-day open return
* expected next-day close return
* expected upside or downside percentage
* confidence level of the expected movement

This will move the project closer to daily stock recommendation and single-stock prediction.

