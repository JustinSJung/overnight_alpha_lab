# Baseline Model Report

## Dataset Summary

- Total rows: 301
- Trainable rows: 301

## Status

Baseline model trained successfully.

## Features

- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

## Accuracy

0.8791

## Classification Report

```text
              precision    recall  f1-score   support

           0       0.74      0.97      0.84        29
           1       0.98      0.84      0.90        62

    accuracy                           0.88        91
   macro avg       0.86      0.90      0.87        91
weighted avg       0.90      0.88      0.88        91

```