# Day 2: Building an Automated Event Scoring Pipeline

## What I Built Today

Today, I expanded Overnight Alpha Lab from a simple DART disclosure collection project into an automated event analysis pipeline.

The system now can:

1. Collect DART disclosures automatically
2. Parse disclosure titles into event types
3. Select key market-moving events
4. Collect stock price data for selected companies
5. Evaluate whether next-day price reaction data is available
6. Assign rule-based prediction scores to each event

## Why This Matters

The long-term goal of this project is to build an AI-based market reaction prediction system.

The system is not designed to simply guess stock prices from past charts. Instead, it focuses on how the market reacts to newly released information such as disclosures, news, and sentiment data.

Today’s work created the first version of the decision-making layer.

## Current Automated Pipeline

```text
DART Disclosure Collection
↓
Disclosure Event Parsing
↓
Key Event Selection
↓
Rule-Based Event Scoring
↓
Stock Price Data Collection
↓
Event-Price Reaction Evaluation
```

## Event Scoring Logic

The first scoring model is rule-based.

Examples:

| Event Type               | Direction | Score | Confidence |
| ------------------------ | --------: | ----: | ---------: |
| supply_contract          |  positive |    70 |          C |
| paid_in_capital_increase |  negative |   -70 |          C |
| convertible_bond         |  negative |   -60 |          C |
| lawsuit                  |  negative |   -75 |          C |
| major_shareholder_change |  volatile |    10 |          C |
| merger                   |  volatile |    30 |          C |

At this stage, all confidence levels are intentionally low because the model has not yet learned from historical prediction errors.

## Important Design Choice

The project does not treat every disclosure equally.

Instead, it selects events that are more likely to affect market reactions, such as:

* Supply contracts
* Capital increases
* Convertible bonds
* Lawsuits
* Earnings guidance
* Major shareholder changes
* Mergers and spin-offs

This reduces noise and prepares the dataset for future model training.

## Current Limitation

For disclosures collected today, next-day price reaction may not be available yet.

In that case, the system records:

```text
No next trading day price data available yet.
```

This is expected behavior. The reaction can only be evaluated after the next trading day’s price data becomes available.

## Next Step

The next step is to build an error-note generator.

The error-note generator will compare predicted direction with actual next-day market reaction and classify each result as:

* Success
* Failure
* Pending

It will also generate possible failure reasons and improvement rules.

This is the foundation for improving model reliability over time.

