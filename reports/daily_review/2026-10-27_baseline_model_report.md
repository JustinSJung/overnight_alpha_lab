# Baseline Model Report

## Dataset Summary

- Total rows: 964
- Trainable rows: 964

## Status

Baseline model trained successfully.

## Features

- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

## Accuracy

0.9448

## Classification Report

```text
              precision    recall  f1-score   support

           0       0.93      0.96      0.94       137
           1       0.96      0.93      0.95       153

    accuracy                           0.94       290
   macro avg       0.94      0.95      0.94       290
weighted avg       0.95      0.94      0.94       290

```