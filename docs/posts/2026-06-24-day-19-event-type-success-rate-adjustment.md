# Day 19: Event-Type Success Rate Adjustment

## What I Built Today

Today, I improved the daily stock recommender again.

Until now, the recommender could use advanced error-note signals to adjust recommendation scores.

Today, I added another adjustment layer.

The recommender now uses event-type performance data such as historical success rate and average next-day return.

## Why This Matters

Not every disclosure event type should be treated equally.

Some event types may historically produce stronger price reactions.

Some event types may often remain pending or fail to generate meaningful next-day movement.

Some event types may repeatedly show weak or negative reactions.

The system needs to reflect these differences in the recommendation score.

## Updated File

The updated recommender file is:

```text
src/models/daily_stock_recommender.py
```

The output report is still generated at:

```text
reports/daily_prediction/YYYY-MM-DD_daily_stock_candidates.md
```

## What Changed

The recommender now calculates additional event-type performance features.

```text
event_type_success_rate
event_type_avg_next_open_return
event_type_avg_next_close_return
event_type_success_rate_adjustment
event_type_return_adjustment
event_type_performance_adjustment_score
```

These values are calculated from historical error-note data.

## New Scoring Structure

The recommendation score now has three main parts.

```text
base_recommendation_score
+ error_note_adjustment_score
+ event_type_performance_adjustment_score
= adjusted_recommendation_score
```

This means the recommender now considers:

```text
current event and news signals
historical error-note learning
event-type success rate
event-type average return
```

## Event-Type Success Rate Adjustment

The system checks whether an event type has enough evaluated historical cases.

If an event type has a strong success rate, it can receive a small positive adjustment.

If an event type has a weak success rate, it can receive a conservative penalty.

For small sample sizes, the adjustment is intentionally light.

This prevents the system from overreacting to very limited data.

## Event-Type Return Adjustment

The system also checks average next-day close return by event type.

If an event type has a positive average next-day close return, it can receive a positive return adjustment.

If an event type has a negative average next-day close return, it can receive a negative return adjustment.

## Current Limitation

At the current stage, many rows are still pending.

That means many event types may still show:

```text
Evaluated: 0
Success Rate: N/A
Avg Next Close: Not available
Total Adj: 0.00
```

This is normal.

The structure is now ready, and the adjustment values will become more meaningful after more next-day price reactions are evaluated.

## Why This Is Progress

This step makes the recommendation system more data-driven.

The recommender no longer relies only on current disclosure and news signals.

It also begins to use historical performance patterns.

The learning loop now looks like this:

```text
Collect disclosures and news
↓
Generate candidates
↓
Evaluate next-day price reaction
↓
Create advanced error notes
↓
Summarize event-type performance
↓
Apply event-type success rate and return adjustment
↓
Generate adjusted daily candidates
```

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
Event-type success rate adjustment
Single stock predictor
Event-type performance report
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

The next step is to build a stock-specific historical pattern report.

Event-type performance is useful, but different stocks may react differently to the same type of disclosure.

The next report should summarize how each stock has historically reacted to events.

It should include:

```text
stock code
company name
number of historical events
success count
failure count
pending count
average next open return
average next close return
most common event types
stock-specific risk notes
```

This will help the system distinguish between general event-type behavior and stock-level behavior.

