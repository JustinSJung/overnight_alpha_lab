# Day 21: Stock-Specific Pattern Adjustment

## What I Built Today

Today, I improved the daily stock recommender by adding stock-specific historical pattern adjustment.

Until now, the recommender could use event-type performance and advanced error-note learning.

That means the system could ask:

```text
Has this event type worked well historically?
```

Today, I added another question:

```text
Has this specific stock historically reacted well to previous events?
```

## Why This Matters

The same disclosure event type can produce different market reactions depending on the stock.

For example, two companies may both announce a supply contract, but the market may react very differently.

One stock may have a history of strong reactions to disclosure events.

Another stock may have a history of weak reactions or repeated failed signals.

That is why stock-specific historical behavior should be part of the recommendation score.

## Updated File

The updated file is:

```text
src/models/daily_stock_recommender.py
```

The daily candidate report is generated at:

```text
reports/daily_prediction/YYYY-MM-DD_daily_stock_candidates.md
```

## What Changed

The recommender now calculates stock-specific historical adjustment features.

```text
stock_pattern_total_count
stock_pattern_evaluated_count
stock_pattern_success_count
stock_pattern_failure_count
stock_pattern_pending_count
stock_pattern_success_rate
stock_pattern_avg_next_open_return
stock_pattern_avg_next_close_return
stock_pattern_success_rate_adjustment
stock_pattern_return_adjustment
stock_pattern_confidence_bias_adjustment
stock_specific_pattern_adjustment_score
stock_pattern_label
```

These values are calculated from historical advanced error-note data.

## New Scoring Structure

The adjusted recommendation score now includes four layers.

```text
base_recommendation_score
+ error_note_adjustment_score
+ event_type_performance_adjustment_score
+ stock_specific_pattern_adjustment_score
= adjusted_recommendation_score
```

This means the recommender now considers:

```text
current event and news signals
historical error-note learning
event-type success rate and average return
stock-specific success rate and average return
stock-specific confidence bias
risk filters
```

## Stock-Specific Pattern Labels

The system also creates a simple stock-level pattern label.

Examples include:

```text
mostly_pending
relatively_positive_history
weak_historical_reaction
conservative_confidence_bias
not_enough_data
```

These labels are not final investment conclusions.

They are research indicators that help the system understand how much historical evidence exists for each stock.

## Current Limitation

At the current stage, many rows are still pending.

This means stock-specific adjustment scores may still show:

```text
0.00
```

or success rates may show:

```text
N/A
```

This is normal.

The important point is that the structure is now ready.

As more evaluated event-reaction samples accumulate, the stock-specific adjustment score will become more meaningful.

## Why This Is Progress

This step adds a stock-level learning layer to the recommendation system.

The system now combines both:

```text
event_type-level learning
stock_code-level learning
```

This makes the recommender more specific.

It no longer only asks whether an event type is historically strong.

It also asks whether the individual stock has historically reacted well.

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
Stock-specific pattern adjustment
Single stock predictor
Event-type performance report
Stock-specific historical pattern report
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

The next step is to add market index and sector movement features.

This is important because a stock may rise not because the event prediction was correct, but because the entire market or sector moved up.

The system should eventually distinguish between:

```text
stock-specific reaction
event-driven reaction
market-wide movement
sector-wide movement
```

Adding market and sector features will make future prediction evaluation more accurate.

