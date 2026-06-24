# Day 17: Error-Note-Aware Recommender

## What I Built Today

Today, I improved the daily stock recommender so it can use historical error-note data.

Until now, the recommender used a rule-based score based on disclosure events, news sentiment, news attention, and simple risk filters.

Today, I added another layer.

The recommender now reads advanced error notes and applies event-type level confidence adjustments.

## Why This Matters

The long-term goal of Overnight Alpha Lab is to build a system that improves over time.

A system cannot improve only by collecting data.

It needs to compare predictions with actual outcomes, learn from mistakes, and reflect those lessons in future recommendations.

Day 16 created advanced error notes.

Day 17 connects those error notes back into the recommender.

This is the first version of a feedback loop.

## Updated File

The updated file is:

```text
src/models/daily_stock_recommender.py
```

The output report is still generated at:

```text
reports/daily_prediction/YYYY-MM-DD_daily_stock_candidates.md
```

## What Changed

The recommender now loads past error-note files from:

```text
data/predictions/error_notes_YYYYMMDD.csv
```

It then summarizes error-note history by event type.

For each event type, the system calculates:

```text
historical_error_note_count
historical_success_count
historical_failure_count
historical_pending_count
historical_increase_count
historical_decrease_count
historical_slightly_decrease_count
historical_hold_count
error_note_adjustment_score
```

## New Recommendation Score

The previous recommendation score was mainly based on:

```text
event_score
news_sentiment_score
news_attention_score
negative_keyword_count
prediction_direction
risk filters
```

Now the recommender calculates:

```text
base_recommendation_score
error_note_adjustment_score
adjusted_recommendation_score
```

The adjusted score is:

```text
adjusted_recommendation_score
= base_recommendation_score + error_note_adjustment_score
```

## Error-Note Learning Adjustment

The new report includes a section called:

```text
Error-Note Learning Adjustment
```

This section shows how previous error notes affect the current recommender.

For example, if an event type repeatedly receives:

```text
confidence_adjustment: increase
```

then that event type may receive a small positive adjustment.

If an event type repeatedly receives:

```text
confidence_adjustment: decrease
```

or:

```text
confidence_adjustment: slightly_decrease
```

then that event type may receive a conservative penalty.

## Current Limitation

At the current stage, many event rows are still pending.

This means next-day price reaction data is not fully available yet.

Because of that, many adjustment scores may still show:

```text
0.00
```

This is normal.

The important point is that the structure is now ready.

As more success and failure cases accumulate, the adjustment score will become more meaningful.

## Why This Is Progress

This step connects the learning layer to the recommendation layer.

The project now has this loop:

```text
Generate prediction
↓
Observe actual price reaction
↓
Create advanced error note
↓
Classify confidence adjustment
↓
Aggregate error-note history by event type
↓
Adjust future recommendation scores
```

This is the first version of a self-improving recommendation pipeline.

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
Advanced error-note generation
Machine learning dataset building
Baseline machine learning model
Return prediction model
Daily stock recommender
Error-note-aware recommendation adjustment
Single stock predictor
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

The next step is to build an event-type performance report.

The report should summarize which event types have historically performed better or worse.

It should include:

```text
event type
number of evaluated cases
success count
failure count
pending count
success rate
average next open return
average next close return
confidence adjustment trend
```

This will make the learning process easier to monitor.

