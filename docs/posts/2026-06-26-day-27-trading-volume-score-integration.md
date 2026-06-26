# Day 27: Trading Volume Score Integration

## What I Built Today

Today, I added a trading volume score integration layer to Overnight Alpha Lab.

On Day 26, the system learned how to calculate trading volume reaction features around disclosure events.

Today, I converted those volume reaction labels into recommendation score adjustment signals.

This means the system can now use trading volume as a structured scoring signal.

## Why This Matters

Price movement alone is not enough.

A disclosure event may look meaningful, but if trading volume does not increase, the market may not have paid much attention.

On the other hand, if trading volume increases sharply after a disclosure, it may indicate stronger investor attention.

For example:

```text
Positive disclosure + strong volume spike = stronger confirmation
Positive disclosure + weak volume = weaker confidence
Negative disclosure + strong volume spike = stronger risk signal
Volatile disclosure + strong volume spike = volatility confirmation
```

This helps the system avoid overvaluing quiet events and better identify events that attracted real market participation.

## New File

I added a new score integration module.

```text
src/models/trading_volume_score_integrator.py
```

## Input Data

The module uses the trading volume feature file generated on Day 26.

```text
data/processed/trading_volume_features_YYYYMMDD.csv
```

This file contains event-level trading volume reaction features such as event-day volume, next-day volume, 20-day average volume, and volume reaction labels.

## Output Files

The module generates:

```text
data/processed/trading_volume_score_adjustments_YYYYMMDD.csv
reports/daily_review/YYYY-MM-DD_trading_volume_score_report.md
```

The processed CSV may be ignored by Git depending on `.gitignore`, but the Markdown report is committed to the portfolio repository.

## New Score Fields

The new module creates:

```text
trading_volume_score_adjustment
trading_volume_adjustment_label
trading_volume_adjustment_reason
```

These fields convert volume reaction into a score signal that can later be connected to the daily candidate report.

## Score Logic

The scoring logic depends on both prediction direction and volume reaction.

For positive or neutral-positive events:

```text
extreme_volume_spike: +12
strong_volume_spike: +10
moderate_volume_increase: +5
normal_or_weak_volume: -3
```

For negative events:

```text
extreme_volume_spike: -12
strong_volume_spike: -10
moderate_volume_increase: -5
normal_or_weak_volume: 0
```

For volatile events:

```text
extreme_volume_spike: +8
strong_volume_spike: +6
moderate_volume_increase: +3
normal_or_weak_volume: -2
```

Missing or insufficient volume data receives no adjustment.

## Adjustment Labels

The system also converts numeric scores into readable labels.

```text
strong_positive_volume_adjustment
mild_positive_volume_adjustment
neutral_volume_adjustment
mild_negative_volume_adjustment
strong_negative_volume_adjustment
```

This makes the report easier to interpret.

## Current Result

In the current run, all rows were classified as:

```text
neutral_volume_adjustment
```

This is acceptable at the current stage.

The current data still has limited price and volume coverage, so the system may not yet detect strong volume spikes.

The important part is that the scoring structure is now ready.

As more price files and event history accumulate, this layer can start producing stronger positive or negative volume-based adjustments.

## Catch-Up Integration

The catch-up script now includes trading volume score integration.

The current catch-up flow is:

```text
[1/17] Daily Pipeline
[2/17] Pending Re-Evaluator
[3/17] Market Index Collection
[4/17] Market-Adjusted Features
[5/17] Market-Adjusted Evaluation
[6/17] Market-Adjusted Score Integration
[7/17] Market-Adjusted Daily Candidate Report
[8/17] Trading Volume Features
[9/17] Trading Volume Score Integration
[10/17] Automation Status Report
[11/17] Automation History
[12/17] Confidence Report
[13/17] Return Prediction Report
[14/17] Daily Stock Candidate Report
[15/17] Event-Type Performance Report
[16/17] Stock-Specific Pattern Report
[17/17] Completed
```

## Why This Is Progress

This step turns trading volume from a descriptive feature into a usable scoring signal.

The system now has the following learning chain:

```text
disclosure event
→ event score
→ news signal
→ price reaction
→ market-adjusted return
→ market-adjusted score
→ trading volume reaction
→ trading volume score
```

This makes the candidate evaluation more realistic.

A strong event should ideally be supported not only by price movement, but also by market-adjusted outperformance and meaningful trading volume.

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
Trading volume score integration
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

The next step is to connect trading volume score adjustment into the market-adjusted daily candidate report.

The final candidate score should eventually include:

```text
base recommendation score
market-adjusted score adjustment
trading volume score adjustment
error-note adjustment score
event-type performance adjustment score
stock-specific pattern adjustment score
```

This will allow the system to rank candidates using event strength, market context, and trading activity together.

