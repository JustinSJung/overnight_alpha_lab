# Day 6: Pending Event Re-Evaluation System

## What I Built Today

Today, I added a pending event re-evaluation system to Overnight Alpha Lab.

This system checks previously pending events and attempts to re-evaluate them when new stock price data becomes available.

This is an important step because many disclosure events cannot be judged immediately on the same day.

## Why Pending Events Exist

When a disclosure is collected today, the next trading day price reaction may not be available yet.

In that case, the system cannot decide whether the initial prediction was correct or incorrect.

Those rows are marked as:

```text
pending
```

This means the event is not ignored.

It means the event is waiting for future price data.

## New Re-Evaluation Logic

The new script checks the latest machine learning dataset and finds rows where:

```text
prediction_result = pending
```

Then it performs the following steps:

```text
Find pending rows
↓
Extract related stock codes
↓
Collect updated price data
↓
Re-run event-price reaction evaluation
↓
Regenerate error notes
↓
Rebuild the machine learning dataset
↓
Run the baseline model again
```

## Why This Matters

This changes the project from a one-time daily analysis tool into a learning loop.

Before this step, the system could collect and evaluate today’s events, but events without next-day price data remained pending.

Now, those events can be revisited later.

When the required price data becomes available, pending rows can eventually become:

```text
success
failure
```

This allows the training dataset to grow over time.

## Current Pipeline

```text
Daily Pipeline
↓
DART Disclosure Collection
↓
Disclosure Event Parsing
↓
Key Event Selection
↓
Rule-Based Event Scoring
↓
Naver News Metadata Collection
↓
News Feature Generation
↓
Stock Price Data Collection
↓
Event-Price Reaction Evaluation
↓
Prediction Review and Error Note Generation
↓
Machine Learning Dataset Building
↓
Baseline Machine Learning Model
```

The new pending re-evaluation system works alongside the daily pipeline.

```text
Pending Re-Evaluation
↓
Find old pending events
↓
Update price data
↓
Re-evaluate reactions
↓
Update error notes
↓
Rebuild ML dataset
↓
Re-run baseline model
```

## System Design Meaning

This step is important because real-world market data does not arrive all at once.

A reliable prediction system needs to handle delayed outcomes.

The pending re-evaluation system makes the project more realistic because it separates:

* events that are ready to evaluate
* events that are still waiting for market reaction data
* events that can later become training samples

## Current Status

The system can now detect pending rows and re-run the evaluation process.

At this stage, many events may still remain pending if the next trading day price data is not available yet.

That is expected.

The important point is that the system now has a mechanism to check again later.

## Why This Is Progress

This is the beginning of a daily learning loop.

The project can now:

* collect new events
* create features
* evaluate available reactions
* store pending cases
* revisit old pending cases
* convert them into training samples later
* rebuild the ML dataset
* re-run the baseline model

This makes the system more than a simple crawler.

It is becoming a repeatable event-reaction learning framework.

## Next Step

The next step is to improve automation.

Future work may include:

* running the daily pipeline automatically
* running pending re-evaluation automatically
* generating daily blog posts automatically
* adding model prediction probability output
* adding feature importance analysis
* improving duplicate handling
* expanding news and investor attention indicators

The long-term goal is to build a system that learns from daily market reactions and improves its confidence over time.

