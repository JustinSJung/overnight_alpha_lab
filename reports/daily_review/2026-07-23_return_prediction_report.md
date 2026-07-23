# Return Prediction Report - 2026-07-23

Generated at: 2026-07-23 00:17:26

ML dataset: `data/processed/ml_dataset_20260723.csv`

## Purpose

This report tests whether the current dataset can be used to predict next-day return values.

The target variables are:

- next_open_return
- next_close_return

## Dataset Summary

- Total rows: 2

## Target: next_open_return

- Valid training samples: 0
- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

Status: **NOT_ENOUGH_DATA**

There are not enough valid return samples to train a reliable return prediction model yet.

This is expected in the early stage because many events are still pending.

## Target: next_close_return

- Valid training samples: 0
- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

Status: **NOT_ENOUGH_DATA**

There are not enough valid return samples to train a reliable return prediction model yet.

This is expected in the early stage because many events are still pending.

## Interpretation

This is the first regression layer of the project. The goal is to move beyond success/failure classification and begin estimating how much a stock may move after a disclosure or news event.

## Next Step

Continue collecting evaluated event-reaction samples. Once enough valid return samples exist, this model can be used as the foundation for expected return prediction and daily stock recommendation.
