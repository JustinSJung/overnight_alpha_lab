# Baseline Model Report

## Dataset Summary

- Total rows: 213
- Trainable rows: 213

## Status

Baseline model trained successfully.

## Features

- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

## Accuracy

0.9375

## Classification Report

```text
              precision    recall  f1-score   support

           0       0.94      0.98      0.96        47
           1       0.93      0.82      0.88        17

    accuracy                           0.94        64
   macro avg       0.94      0.90      0.92        64
weighted avg       0.94      0.94      0.94        64

```