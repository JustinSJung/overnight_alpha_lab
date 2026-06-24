# Day 22: Market Index and Market-Adjusted Return Features

## What I Built Today

Today, I added market index and market-adjusted return features to Overnight Alpha Lab.

Until now, the system evaluated stock reactions mainly by checking next-day stock returns.

That was useful, but it had an important limitation.

A stock may rise not because the disclosure event was meaningful, but because the entire market moved up.

Today, I added a feature layer that helps separate stock-specific reaction from broader market movement.

## Why This Matters

A good event-driven prediction system should not only ask:

```text
Did the stock go up?
```

It should also ask:

```text
Did the stock outperform the market?
```

For example:

```text
Stock next-day return: +2.00%
Market next-day return: +1.50%
Market-adjusted return: +0.50%
```

In this case, the stock rose, but only slightly more than the market.

This distinction is important for evaluating whether the event signal was actually meaningful.

## New Files

I added two new files.

```text
src/crawler/market_index_collector.py
src/features/market_adjusted_features.py
```

## Market Index Collector

The market index collector generates market reference data.

It first tries to collect direct KOSPI and KOSDAQ index data.

If direct index collection fails, it uses ETF proxy data as a fallback.

The fallback proxies are:

```text
KOSPI proxy: KODEX 200
KOSDAQ proxy: KODEX KOSDAQ 150
```

This makes the pipeline more stable even when direct index data collection fails.

## Stock Market Lookup

The collector also tries to create a stock market lookup table.

The purpose is to identify whether each stock belongs to KOSPI or KOSDAQ.

If full ticker lookup fails, the system uses fallback logic based on the stocks currently appearing in error-note data.

The lookup source is recorded so the system can distinguish between direct lookup and fallback estimation.

## Generated Raw Files

The collector generates:

```text
data/raw/market_index_YYYYMMDD.csv
data/raw/stock_market_lookup_YYYYMMDD.csv
```

The raw files may not always be committed to GitHub depending on `.gitignore`, but they are used locally to build processed features.

## Market-Adjusted Feature Builder

The market-adjusted feature builder joins error-note data with market index data.

It calculates:

```text
market_next_open_return
market_next_close_return
market_adjusted_next_open_return
market_adjusted_next_close_return
```

The key calculation is:

```text
market_adjusted_next_close_return
= stock_next_close_return - market_next_close_return
```

## Generated Processed File

The processed output is:

```text
data/processed/market_adjusted_features_YYYYMMDD.csv
```

This file allows future models and reports to compare stock performance against the broader market.

## Catch-Up Integration

The catch-up script now includes market data collection and market-adjusted feature generation.

The current catch-up flow is:

```text
[1/12] Daily Pipeline
[2/12] Pending Re-Evaluator
[3/12] Market Index Collection
[4/12] Market-Adjusted Features
[5/12] Automation Status Report
[6/12] Automation History
[7/12] Confidence Report
[8/12] Return Prediction Report
[9/12] Daily Stock Candidate Report
[10/12] Event-Type Performance Report
[11/12] Stock-Specific Pattern Report
[12/12] Completed
```

## Why This Is Progress

This step improves the quality of prediction evaluation.

The system can now separate:

```text
stock-specific reaction
market-wide movement
event-driven movement
```

This is an important step toward more accurate model training.

Without market-adjusted returns, the system may incorrectly treat a market-wide rally as a successful stock-specific prediction.

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

The next step is to use market-adjusted return features in the evaluation and recommendation logic.

For example, a prediction should be judged more strongly if the stock outperformed the market after the event.

A stock that rises with the market but does not outperform it should receive a more conservative evaluation.

This will make the system more accurate and more realistic.

