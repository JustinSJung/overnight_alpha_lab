# Day 25: Market-Adjusted Daily Candidate Report

## What I Built Today

Today, I added a market-adjusted daily candidate report to Overnight Alpha Lab.

Until now, the project had a main daily stock recommender that used event scores, error-note learning, event-type performance, and stock-specific patterns.

On Day 24, I created a separate market-adjusted score integration layer.

Today, I connected that market-adjusted score adjustment into a new v2-style daily candidate report.

This does not replace the existing daily recommender yet.

Instead, it creates a safer comparison report so I can review how market-adjusted scoring changes candidate ranking.

## Why This Matters

A daily stock candidate report should not only rank stocks by event type or rule-based score.

It should also consider whether previous reactions were strong after adjusting for market movement.

For example:

```text
Stock return: +2.00%
Market return: +3.00%
Market-adjusted return: -1.00%
```

Even though the stock went up, it underperformed the broader market.

A model that ignores this may overestimate weak signals.

The new report helps reduce that problem.

## New File

I added a new recommender module.

```text
src/models/market_adjusted_daily_recommender.py
```

## Input Data

The report uses two main inputs.

```text
data/processed/ml_dataset_YYYYMMDD.csv
data/processed/market_adjusted_score_adjustments_YYYYMMDD.csv
```

The ML dataset provides the basic event, news, and reaction data.

The market-adjusted score adjustment file provides the market-aware scoring signal created on Day 24.

## Output Report

The new report is generated at:

```text
reports/daily_prediction/YYYY-MM-DD_market_adjusted_daily_candidates.md
```

## Score Formula

The current v2 score formula is:

```text
base_recommendation_score_v2
+ market_adjusted_score_adjustment
= final_market_adjusted_score
```

This is intentionally conservative.

The existing daily stock recommender remains unchanged.

The purpose of this v2 report is to compare the old ranking logic with the new market-adjusted ranking logic before merging them.

## Candidate Buckets

The new report classifies rows into candidate buckets.

```text
strong_market_adjusted_candidate
positive_candidate
watchlist_candidate
volatile_watchlist
risk_or_avoid_review
general_review
```

This makes the daily report easier to read.

Instead of showing one long table, the report groups candidates by quality and risk.

## Why This Is Progress

This step connects market-adjusted learning to practical candidate selection.

The project now has a chain that looks like this:

```text
market index data
→ market-adjusted return
→ market-adjusted evaluation
→ market-adjusted score adjustment
→ market-adjusted daily candidate report
```

This is important because the system is no longer only asking whether a stock moved.

It is starting to ask whether the movement was meaningful relative to the market.

## Catch-Up Integration

The catch-up script now includes the market-adjusted daily candidate report.

The current catch-up flow is:

```text
[1/15] Daily Pipeline
[2/15] Pending Re-Evaluator
[3/15] Market Index Collection
[4/15] Market-Adjusted Features
[5/15] Market-Adjusted Evaluation
[6/15] Market-Adjusted Score Integration
[7/15] Market-Adjusted Daily Candidate Report
[8/15] Automation Status Report
[9/15] Automation History
[10/15] Confidence Report
[11/15] Return Prediction Report
[12/15] Daily Stock Candidate Report
[13/15] Event-Type Performance Report
[14/15] Stock-Specific Pattern Report
[15/15] Completed
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
Market index collection
Stock market lookup
Market-adjusted return feature generation
Market-adjusted evaluation logic
Market-adjusted score integration
Market-adjusted daily candidate report
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

The next step is to compare the original daily candidate report with the market-adjusted v2 report.

After that, the market-adjusted score can be merged into the main daily recommender.

The final recommender score should eventually include:

```text
base recommendation score
error-note adjustment score
event-type performance adjustment score
stock-specific pattern adjustment score
market-adjusted score adjustment
```

This will make the daily candidate ranking more realistic and more robust.

