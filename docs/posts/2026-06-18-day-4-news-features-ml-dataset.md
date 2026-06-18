# Day 4: Adding News Features and Building the ML Dataset

## What I Built Today

Today, I expanded Overnight Alpha Lab by adding news metadata collection, news feature generation, and a machine-learning dataset builder.

The system now combines:

* DART disclosure events
* Rule-based event scores
* Naver news metadata
* News sentiment and attention features
* Stock price reaction results
* Prediction review and error-note outputs

This is an important step because the project now has a structured dataset that can later be used for machine learning.

## Why This Matters

Stock price reactions are not driven only by official disclosures.

Market reactions are also influenced by:

* How much media attention a company receives
* Whether news headlines are positive or negative
* Whether the event has already been widely discussed
* Whether investors are reacting to official facts or market narratives

For this reason, the project now includes a news feature layer.

## Current Pipeline

```text
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
```

## News Metadata Collection

The news collector uses the Naver Search API to collect metadata for selected companies.

The system stores:

* Company name
* News title
* News summary
* Original link
* Naver link
* Publication date
* Collection time

The system does not store full article bodies. It focuses on metadata and summary-level information for research and feature extraction.

## News Feature Generation

The first version of the news feature generator creates simple features such as:

| Feature                | Meaning                                            |
| ---------------------- | -------------------------------------------------- |
| news_count             | Number of collected news items                     |
| positive_keyword_count | Count of positive keywords                         |
| negative_keyword_count | Count of negative keywords                         |
| news_sentiment_score   | Positive keywords minus negative keywords          |
| news_attention_score   | Current version uses news count as attention score |

This is still a basic rule-based approach, but it creates a foundation for future sentiment analysis.

## Machine Learning Dataset

The ML dataset builder combines multiple pipeline outputs into a single dataset.

The dataset includes:

* stock_code
* corp_name
* event_type
* prediction_direction
* event_score
* initial_confidence
* news_count
* positive_keyword_count
* negative_keyword_count
* news_sentiment_score
* news_attention_score
* next_open_return
* next_close_return
* prediction_result
* error_reason
* improvement_rule

This creates the first machine-learning-ready structure for the project.

## Current Limitation

Many current samples are still marked as:

```text
pending
```

This is expected because next-day price data is not available immediately after the disclosure date.

Once the next trading day data becomes available, these rows can be re-evaluated and converted into success or failure cases.

## Why This Is Important

This step changes the project from a data collection pipeline into a learning system.

The project can now collect event data, create features, evaluate market reactions, generate error notes, and store everything in a structured dataset.

This dataset will later be used to train models that estimate the probability of positive or negative next-day market reactions.

## Next Step

The next step is to build the first baseline machine learning model.

The initial model will likely be simple and interpretable, using features such as:

* event_score
* news_count
* news_sentiment_score
* news_attention_score
* event_type

The goal is not to create a perfect prediction model immediately.

The goal is to create a baseline model and improve it through daily simulation, review, and error-note based learning.

