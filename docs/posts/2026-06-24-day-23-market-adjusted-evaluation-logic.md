# Day 23: Market-Adjusted Evaluation Logic

## What I Built Today

Today, I added market-adjusted evaluation logic to Overnight Alpha Lab.

Until now, prediction results were mainly evaluated using absolute stock returns.

For example, if the prediction direction was positive and the stock price increased the next day, the case could be treated as a success.

However, this approach has a limitation.

A stock may increase simply because the entire market increased.

To improve this, I added a new evaluation layer that compares stock returns against market returns.

## Why This Matters

A stronger evaluation system should not only ask:

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

In this case, the stock rose and also outperformed the market.

But if the result were:

```text
Stock next-day return: +2.00%
Market next-day return: +3.00%
Market-adjusted return: -1.00%
```

The stock rose in absolute terms, but underperformed the market.

This should not be treated as a strong event-driven success.

## New File

I added a new evaluator.

```text
src/evaluator/market_adjusted_evaluator.py
```

## Input Data

The evaluator uses the market-adjusted feature file generated on Day 22.

```text
data/processed/market_adjusted_features_YYYYMMDD.csv
```

This file contains:

```text
stock next-day return
market next-day return
market-adjusted next-day return
market group
market data source type
market proxy information
```

## Output Files

The evaluator generates:

```text
data/predictions/market_adjusted_evaluation_YYYYMMDD.csv
reports/daily_review/YYYY-MM-DD_market_adjusted_evaluation_report.md
```

The CSV file may be ignored by Git depending on `.gitignore`, but the Markdown report is committed to the portfolio repository.

## New Evaluation Categories

The evaluator adds a new column:

```text
market_adjusted_result
```

Possible results include:

```text
market_adjusted_success
market_driven_weak_success
relative_success_but_absolute_loss
market_adjusted_failure
relative_failure_despite_absolute_gain
market_adjusted_volatility_success
market_driven_volatility
volatility_overestimated
market_data_missing
pending
```

## Example Logic

For positive predictions:

```text
If stock return > 0 and market-adjusted return > 0:
    market_adjusted_success

If stock return > 0 but market-adjusted return <= 0:
    market_driven_weak_success

If stock return <= 0 but market-adjusted return > 0:
    relative_success_but_absolute_loss

Otherwise:
    market_adjusted_failure
```

For negative predictions:

```text
If stock return < 0 and market-adjusted return < 0:
    market_adjusted_success

If stock return < 0 but market-adjusted return >= 0:
    market_driven_weak_success

If stock return >= 0 but market-adjusted return < 0:
    relative_failure_despite_absolute_gain

Otherwise:
    market_adjusted_failure
```

For volatile predictions:

```text
If absolute market-adjusted return is large:
    market_adjusted_volatility_success

If absolute stock movement is large but excess movement is small:
    market_driven_volatility

Otherwise:
    volatility_overestimated
```

## Explanation Layer

The evaluator also generates:

```text
market_adjusted_reason
market_adjusted_learning_point
market_adjusted_confidence_adjustment
```

This means the system does not only classify the result.

It also explains why the result should be treated as strong, weak, pending, or market-driven.

## Catch-Up Integration

The catch-up script now includes market-adjusted evaluation.

The current catch-up flow is:

```text
[1/13] Daily Pipeline
[2/13] Pending Re-Evaluator
[3/13] Market Index Collection
[4/13] Market-Adjusted Features
[5/13] Market-Adjusted Evaluation
[6/13] Automation Status Report
[7/13] Automation History
[8/13] Confidence Report
[9/13] Return Prediction Report
[10/13] Daily Stock Candidate Report
[11/13] Event-Type Performance Report
[12/13] Stock-Specific Pattern Report
[13/13] Completed
```

## Why This Is Progress

This step improves the quality of prediction review.

Previously, a prediction could look successful simply because the entire market moved in the same direction.

Now, the system can distinguish:

```text
true event-driven success
market-driven weak success
relative strength during weak markets
absolute gain with weak relative performance
market-adjusted failure
```

This makes the evaluation logic more realistic.

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

The next step is to connect market-adjusted evaluation results to the confidence tracker and daily recommendation score.

The system should reward predictions that outperform the market and reduce confidence when a stock only moved because the broader market moved.

