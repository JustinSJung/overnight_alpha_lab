# Day 20: Stock-Specific Historical Pattern Report

## What I Built Today

Today, I added a stock-specific historical pattern report to Overnight Alpha Lab.

Until now, the project could summarize performance by disclosure event type.

That means the system could analyze questions such as:

```text
How has the supply contract event type performed historically?
```

Today, I added another perspective.

The system can now analyze historical patterns by stock code.

That means it can start answering:

```text
How has this specific stock reacted to previous events?
```

## Why This Matters

Event-type analysis is useful, but it is not enough.

The same type of disclosure can affect different stocks differently.

For example, two companies may both announce a supply contract, but the market reaction may differ depending on company size, investor attention, past credibility, sector, or recent trading behavior.

That is why the system needs stock-level historical pattern tracking.

## New File

The new report generator is:

```text
src/report_generator/stock_pattern_report.py
```

It generates:

```text
reports/daily_review/YYYY-MM-DD_stock_pattern_report.md
```

## What the Report Tracks

The report summarizes each stock using:

```text
stock_code
corp_name
total_count
evaluated_count
success_count
failure_count
pending_count
success_rate
average next open return
average next close return
most common event type
risk_note
```

This makes it easier to see whether a specific stock has historically shown strong, weak, or mostly pending reactions.

## Stock Pattern Table

The report includes a stock pattern table.

For each stock, it shows:

```text
Stock
Company
Total
Evaluated
Success
Failure
Pending
Success Rate
Avg Next Open
Avg Next Close
Common Event
Risk Note
```

At the current stage, many rows may still be pending.

That is normal because the system needs next-day price reaction data to classify rows as success or failure.

## Risk Notes

The report also creates a simple stock-level risk note.

Examples include:

```text
mostly_pending
weak_historical_reaction
relatively_positive_history
conservative_confidence_bias
not_enough_data
```

These labels are not final investment conclusions.

They are simple research notes that help the system understand whether a stock has enough historical reaction data.

## Catch-Up Integration

The stock-specific historical pattern report is now connected to the catch-up script.

The catch-up flow now runs:

```text
[1/10] Daily Pipeline
[2/10] Pending Re-Evaluator
[3/10] Automation Status Report
[4/10] Automation History
[5/10] Confidence Report
[6/10] Return Prediction Report
[7/10] Daily Stock Candidate Report
[8/10] Event-Type Performance Report
[9/10] Stock-Specific Pattern Report
[10/10] Catch-up Completed
```

This means the stock pattern report is automatically updated whenever the catch-up script runs.

## Why This Is Progress

This step adds a stock-level learning layer.

The project can now compare two different dimensions:

```text
event_type-level behavior
stock_code-level behavior
```

This is important because future recommendation logic should not only ask:

```text
Is this event type historically strong?
```

It should also ask:

```text
Has this specific stock historically reacted well to similar events?
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

The next step is to apply stock-specific historical patterns to the daily recommender.

For example, if a stock repeatedly shows weak historical reactions, the recommender should apply a conservative adjustment.

If a stock has a relatively positive reaction history, the recommender can assign a slightly stronger confidence score.

This will make the recommendation system more personalized at the stock level.

