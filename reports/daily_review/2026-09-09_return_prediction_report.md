# Return Prediction Report - 2026-09-09

Generated at: 2026-09-09 00:53:50

ML dataset: `data/processed/ml_dataset_20260909.csv`

## Purpose

This report tests whether the current dataset can be used to predict next-day return values.

The target variables are:

- next_open_return
- next_close_return

## Dataset Summary

- Total rows: 499

## Target: next_open_return

- Valid training samples: 499
- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

Status: **TRAINED**

| Metric | Value |
|---|---:|
| MAE | 0.022874 |
| MSE | 0.011564 |
| R2 | 0.534102 |

## Target: next_close_return

- Valid training samples: 499
- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

Status: **TRAINED**

| Metric | Value |
|---|---:|
| MAE | 0.009018 |
| MSE | 0.001230 |
| R2 | 0.736188 |

## Interpretation

This is the first regression layer of the project. The goal is to move beyond success/failure classification and begin estimating how much a stock may move after a disclosure or news event.

## Next Step

Continue collecting evaluated event-reaction samples. Once enough valid return samples exist, this model can be used as the foundation for expected return prediction and daily stock recommendation.
