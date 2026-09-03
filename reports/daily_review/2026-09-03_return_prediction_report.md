# Return Prediction Report - 2026-09-03

Generated at: 2026-09-03 00:55:18

ML dataset: `data/processed/ml_dataset_20260903.csv`

## Purpose

This report tests whether the current dataset can be used to predict next-day return values.

The target variables are:

- next_open_return
- next_close_return

## Dataset Summary

- Total rows: 2275

## Target: next_open_return

- Valid training samples: 2275
- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

Status: **TRAINED**

| Metric | Value |
|---|---:|
| MAE | 0.000607 |
| MSE | 0.000112 |
| R2 | 0.924439 |

## Target: next_close_return

- Valid training samples: 2275
- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

Status: **TRAINED**

| Metric | Value |
|---|---:|
| MAE | 0.000301 |
| MSE | 0.000002 |
| R2 | 0.999079 |

## Interpretation

This is the first regression layer of the project. The goal is to move beyond success/failure classification and begin estimating how much a stock may move after a disclosure or news event.

## Next Step

Continue collecting evaluated event-reaction samples. Once enough valid return samples exist, this model can be used as the foundation for expected return prediction and daily stock recommendation.
