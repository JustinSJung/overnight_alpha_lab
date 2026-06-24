# Day 26: Trading Volume Feature Report

## What I Built Today

Today, I added a trading volume feature report to Overnight Alpha Lab.

Until now, the system mainly evaluated disclosure events using price movement, news signals, market-adjusted returns, and prediction review notes.

Today, I added a new layer that checks whether trading volume increased after a disclosure event.

This helps the system understand whether the market actually paid attention to the event.

## Why This Matters

Price movement alone is not enough.

A stock may move slightly, but if trading volume does not increase, the market reaction may be weak.

On the other hand, if a disclosure event is followed by a large volume spike, it may indicate stronger investor attention.

For example:

```text
Good disclosure + strong volume spike = stronger market attention
Good disclosure + weak volume = weaker response
Bad disclosure + strong volume spike = possible risk spread
```

This feature helps distinguish quiet events from events that attracted real market participation.

## New File

I added a new feature builder.

```text
src/features/trading_volume_features.py
```

## Input Data

The trading volume feature builder uses:

```text
data/processed/ml_dataset_YYYYMMDD.csv
data/raw/price_STOCK_START_END.csv
```

The ML dataset provides the event rows.

The price files provide historical trading volume data for each stock.

## Output Files

The script generates:

```text
data/processed/trading_volume_features_YYYYMMDD.csv
reports/daily_review/YYYY-MM-DD_trading_volume_feature_report.md
```

The processed CSV may be ignored by Git depending on `.gitignore`, but the Markdown report is committed to the portfolio repository.

## New Volume Features

The new feature builder calculates:

```text
event_day_volume
next_day_volume
avg_volume_5d_before
avg_volume_20d_before
event_volume_ratio_5d
event_volume_ratio_20d
next_volume_ratio_5d
next_volume_ratio_20d
volume_reaction_label
```

The key idea is to compare event-day and next-day volume against recent average volume.

## Volume Reaction Labels

The system classifies volume reaction strength as:

```text
extreme_volume_spike
strong_volume_spike
moderate_volume_increase
normal_or_weak_volume
insufficient_volume_baseline
price_file_missing
```

The current rule is:

```text
extreme_volume_spike: at least 5x the 20-day average
strong_volume_spike: at least 3x the 20-day average
moderate_volume_increase: at least 1.5x the 20-day average
normal_or_weak_volume: below meaningful spike level
```

## Catch-Up Integration

The catch-up script now includes trading volume feature generation.

The current catch-up flow is:

```text
[1/16] Daily Pipeline
[2/16] Pending Re-Evaluator
[3/16] Market Index Collection
[4/16] Market-Adjusted Features
[5/16] Market-Adjusted Evaluation
[6/16] Market-Adjusted Score Integration
[7/16] Market-Adjusted Daily Candidate Report
[8/16] Trading Volume Features
[9/16] Automation Status Report
[10/16] Automation History
[11/16] Confidence Report
[12/16] Return Prediction Report
[13/16] Daily Stock Candidate Report
[14/16] Event-Type Performance Report
[15/16] Stock-Specific Pattern Report
[16/16] Completed
```

## Why This Is Progress

This step adds another dimension to event analysis.

The system can now compare:

```text
event score
news signal
price reaction
market-adjusted return
trading volume reaction
```

This helps prevent overvaluing quiet events that did not attract meaningful market participation.

It also helps identify events where attention increased sharply after disclosure.

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
Market index collection
Stock market lookup
Market-adjusted return feature generation
Market-adjusted evaluation logic
Market-adjusted score integration
Market-adjusted daily candidate report
Trading volume feature generation
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
GitHub Pages portfolio blog
```

## Next Step

The next step is to convert trading volume reaction labels into score adjustment signals.

For example:

```text
strong_volume_spike after positive event → positive score adjustment
weak volume after positive event → conservative score adjustment
strong volume after negative event → risk score adjustment
```

This will allow the daily candidate report to consider not only price and market-adjusted movement, but also whether real trading activity supported the signal.

