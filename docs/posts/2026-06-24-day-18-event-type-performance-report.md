# Day 18: Event-Type Performance Report

## What I Built Today

Today, I added an event-type performance report to Overnight Alpha Lab.

Until now, the system could generate daily stock candidates, create advanced error notes, and apply error-note learning signals back into the recommender.

Today, I added a new report that summarizes prediction performance by disclosure event type.

## Why This Matters

The project needs to understand which types of disclosure events are actually useful for prediction.

Not every disclosure event has the same market impact.

For example, a supply contract may behave differently from a convertible bond, a lawsuit, or a disclosure violation.

The event-type performance report helps the system track which event types have historically produced stronger or weaker results.

## New File

The new report generator is:

```text
src/report_generator/event_type_performance_report.py
```

It generates:

```text
reports/daily_review/YYYY-MM-DD_event_type_performance_report.md
```

## What the Report Tracks

The report summarizes each event type using:

```text
total_count
evaluated_count
success_count
failure_count
pending_count
success_rate
average next open return
average next close return
confidence adjustment bias
```

This makes it easier to see which event types are performing well and which ones require more conservative treatment.

## Event-Type Performance Table

The report includes an event-type performance table.

For each event type, it shows:

```text
Event Type
Total
Evaluated
Success
Failure
Pending
Success Rate
Avg Next Open
Avg Next Close
Bias
```

At the current stage, many rows may still be pending.

That is normal because next-day price reaction data is not always available immediately.

## Why This Is Progress

This report adds a monitoring layer for the learning loop.

The system can now follow this process:

```text
Generate prediction
↓
Observe actual price reaction
↓
Create advanced error notes
↓
Adjust recommendation score
↓
Summarize event-type performance
↓
Use performance history for future model improvement
```

This makes the project more transparent.

It is no longer only producing outputs.

It is also measuring which event patterns are working.

## Catch-Up Integration

The event-type performance report is now connected to the catch-up script.

The catch-up flow now runs:

```text
[1/9] Daily Pipeline
[2/9] Pending Re-Evaluator
[3/9] Automation Status Report
[4/9] Automation History
[5/9] Confidence Report
[6/9] Return Prediction Report
[7/9] Daily Stock Candidate Report
[8/9] Event-Type Performance Report
[9/9] Catch-up Completed
```

This means the event-type performance report is automatically updated whenever the catch-up script runs.

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

The next step is to use event-type performance results more directly in recommendation scoring.

For example, if an event type has a low historical success rate, the recommender should become more conservative.

If an event type has a strong success rate and positive average next-day return, the recommender can assign a stronger confidence score.

This will make the recommendation logic more data-driven over time.

