# Day 13: Return Prediction Model

## What I Built Today

Today, I added the first return prediction model to Overnight Alpha Lab.

Until now, the project mainly focused on classification:

```text
success
failure
pending
```

That means the system could evaluate whether a prediction was directionally correct or incorrect.

Today, I started adding the next layer: estimating how much a stock may move after a disclosure or news event.

## Why This Matters

The original goal of this project is not only to say whether a stock may go up or down.

The goal is to eventually estimate:

```text
expected next-day open return
expected next-day close return
expected upside or downside percentage
confidence level
```

The return prediction model is the first step toward that goal.

## New File

The new model file is:

```text
src/models/return_prediction_model.py
```

It generates:

```text
reports/daily_review/YYYY-MM-DD_return_prediction_report.md
```

## Target Variables

The model is designed to predict two return targets.

```text
next_open_return
next_close_return
```

These values come from the event-price reaction evaluation process.

## Input Features

The current model uses the same basic feature structure from the ML dataset.

```text
event_score
news_count
positive_keyword_count
negative_keyword_count
news_sentiment_score
news_attention_score
event_type
prediction_direction
initial_confidence
```

These features combine disclosure characteristics, news attention, and initial rule-based judgment.

## Current Model

The first return prediction model uses a simple regression pipeline.

The goal is not to create a perfect return model immediately.

The goal is to create the structure that can later learn from accumulated event-reaction samples.

## Current Result

At the current stage, the report shows:

```text
Status: NOT_ENOUGH_DATA
Valid training samples: 0
```

This is expected.

Many events are still pending because next trading day price data is not available yet.

The model structure is ready, but it needs more valid return samples before it can train.

## Catch-Up Integration

The return prediction model is now connected to the catch-up script.

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
Return Prediction Report
↓
Log Generation
```

Whenever I run:

```text
./scripts/run_catchup.sh
```

the system updates data, checks pending events, rebuilds reports, and generates the return prediction report.

## Why This Is Progress

This step moves the project closer to the original vision.

The system is no longer limited to asking:

```text
Was the prediction right or wrong?
```

It is now preparing to answer:

```text
How much could the stock move?
```

This is the foundation for daily stock recommendations and single-stock prediction.

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
Return prediction model
Execution log generation
```

## Next Step

The next step is to build a daily stock recommender.

Even before the return prediction model has enough training data, the system can still generate rule-based recommendation candidates.

The recommender should provide:

```text
candidate stock
expected direction
event score
news score
confidence level
reason
risk warning
data readiness status
```

This will become the first version of a daily recommendation layer.

