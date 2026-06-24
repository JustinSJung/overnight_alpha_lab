# Day 15: Single Stock Predictor

## What I Built Today

Today, I added a single stock predictor to Overnight Alpha Lab.

Until now, the project could generate daily stock candidate reports automatically.

That means the system could answer:

```text
What stocks should I look at today?
```

Today, I added another important feature.

The system can now answer:

```text
What does the system think about this specific stock?
```

## Why This Matters

The original goal of this project has two parts.

First, the system should automatically generate daily stock candidates.

Second, the user should be able to enter a specific stock code and receive a focused analysis report.

The single stock predictor is the first version of that second function.

## New File

The new predictor file is:

```text
src/models/single_stock_predictor.py
```

It can be executed like this:

```text
python src/models/single_stock_predictor.py 005930
```

The output report is saved under:

```text
reports/single_stock/YYYY-MM-DD_STOCKCODE_single_stock_report.md
```

## What the Report Includes

The single stock report summarizes:

```text
stock code
company name
latest disclosure event
event type
event score
news count
news sentiment score
news attention score
expected direction
single-stock view
risk level
prediction result status
next open return data
next close return data
recent rows for the stock
interpretation
```

## Current Approach

At this stage, the predictor is rule-based.

It uses the latest ML dataset and calculates a single-stock score using available event and news features.

The score currently considers:

```text
event_score
news_sentiment_score
news_attention_score
negative_keyword_count
prediction_direction
event_type risk
```

The report also classifies the stock into one of several views.

```text
POSITIVE_VIEW
VOLATILE_WATCH
WATCHLIST
RISK_REVIEW
WEAK_SIGNAL
```

## Important Limitation

If the entered stock code does not exist in the latest ML dataset, the report will say that no event data was found.

This does not mean the stock has no market risk or opportunity.

It only means that the current event-driven dataset does not contain a recent collected event for that stock.

## Why This Is Progress

This step makes the project interactive.

The project now supports two prediction modes.

### Daily Candidate Mode

The system automatically generates daily candidate reports.

```text
reports/daily_prediction/YYYY-MM-DD_daily_stock_candidates.md
```

### Single Stock Mode

The user can enter a stock code and generate a focused report.

```text
python src/models/single_stock_predictor.py 005930
```

This brings the project closer to a usable stock research assistant.

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
Daily stock recommender
Single stock predictor
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

The next step is to improve the error-note generator.

The current error-note generator compares prediction direction with actual price reaction.

The next version should explain why the prediction may have failed.

It should consider factors such as:

```text
event type
event score
news sentiment
news attention
negative keywords
recent price reaction
pending status
risk event type
```

This will help the system learn from mistakes more meaningfully.

