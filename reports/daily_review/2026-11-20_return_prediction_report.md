# Return Prediction Report - 2026-11-20

Generated at: 2026-11-20 04:02:21

ML dataset: `data/processed/ml_dataset_20261120.csv`

## Purpose

This report tests whether the current dataset can be used to predict next-day return values.

The target variables are:

- next_open_return
- next_close_return

## Dataset Summary

- Total rows: 406

## Target: next_open_return

- Valid training samples: 406
- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

Status: **TRAINED**

| Metric | Value |
|---|---:|
| MAE | 0.036778 |
| MSE | 0.015952 |
| R2 | 0.444214 |

## Target: next_close_return

- Valid training samples: 406
- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

Status: **TRAINED**

| Metric | Value |
|---|---:|
| MAE | 0.021177 |
| MSE | 0.016025 |
| R2 | 0.541496 |

## Interpretation

This is the first regression layer of the project. The goal is to move beyond success/failure classification and begin estimating how much a stock may move after a disclosure or news event.

## Next Step

Continue collecting evaluated event-reaction samples. Once enough valid return samples exist, this model can be used as the foundation for expected return prediction and daily stock recommendation.
