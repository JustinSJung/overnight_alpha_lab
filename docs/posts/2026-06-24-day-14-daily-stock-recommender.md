# Day 14: Daily Stock Recommender

## What I Built Today

Today, I added the first daily stock recommender to Overnight Alpha Lab.

Until now, the project could collect disclosures, classify events, generate scores, evaluate price reactions, create ML datasets, and generate several monitoring reports.

Today, I added a recommendation candidate layer.

This does not mean the system is giving financial advice.

It means the project can now generate research-based daily stock candidate reports from collected disclosure and news data.

## Why This Matters

The original goal of this project is to eventually identify stocks that may react meaningfully after public disclosures and news events.

To reach that goal, the system needs a layer that can convert event data into daily candidates.

The new recommender is the first version of that layer.

## New File

The new recommender file is:

```text
src/models/daily_stock_recommender.py
```

It generates:

```text
reports/daily_prediction/YYYY-MM-DD_daily_stock_candidates.md
```

## Current Approach

At this stage, the recommender is rule-based.

The return prediction model is still in the early stage and currently may show:

```text
NOT_ENOUGH_DATA
```

Therefore, the recommender does not yet rely on trained return prediction outputs.

Instead, it uses available features such as:

```text
event_score
news_count
positive_keyword_count
negative_keyword_count
news_sentiment_score
news_attention_score
prediction_direction
event_type
risk indicators
```

## Candidate Sections

The report separates candidates into several groups.

```text
Positive Candidates
Volatile Watchlist
General Watchlist
Risk / Avoid Review List
```

This is important because not every important stock event is a buy candidate.

Some events may be positive.

Some events may be volatile.

Some events may be worth monitoring.

Some events may be high-risk and should be reviewed carefully or avoided.

## Positive Candidates

Positive candidates are events with relatively favorable event scores, positive direction, and supportive news conditions.

These are not automatic buy recommendations.

They are research candidates that may deserve closer review.

## Volatile Watchlist

Volatile watchlist items are events that may create meaningful price movement, but the direction is uncertain.

These may include major investment decisions, restructuring events, or events with mixed signals.

## General Watchlist

General watchlist items are events worth monitoring, but not strong enough to be classified as positive candidates.

This section helps keep track of less obvious but potentially relevant events.

## Risk / Avoid Review List

The risk section includes negative or high-risk events such as:

```text
paid capital increase
convertible bond
bond with warrant
lawsuit
disclosure violation
negative prediction direction
```

This section is important because a good prediction system should identify both opportunities and risks.

## Catch-Up Integration

The daily stock recommender is now connected to the catch-up script.

The catch-up script now runs:

```text
Daily Pipeline
↓
Pending Re-Evaluation
↓
Automation Status Report
↓
Automation History Update
↓
Confidence Report
↓
Return Prediction Report
↓
Daily Stock Candidate Report
↓
Log Generation
```

Whenever I run:

```text
./scripts/run_catchup.sh
```

the system updates the full pipeline and generates the daily candidate report.

## Why This Is Progress

This step moves the project closer to its original purpose.

The system is no longer only collecting and evaluating data.

It is now starting to generate daily candidate outputs.

This is the first version of a recommendation layer.

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
Prediction review and error-note generation
Machine learning dataset building
Baseline machine learning model
Return prediction model
Pending event re-evaluation
Local automation scripts
Scheduled cron automation
Catch-up execution mode
Automation status report
Automation history tracker
Confidence tracker
Daily stock recommender
Execution log generation
```

## Next Step

The next step is to build a single stock predictor.

The single stock predictor should allow a user to enter a stock code and generate a focused report for that stock.

For example:

```text
python src/models/single_stock_predictor.py 005930
```

The report should summarize:

```text
recent disclosure events
news sentiment
event score
candidate classification
expected direction
risk level
data readiness
research notes
```

This will make the system more interactive and closer to the original vision.

