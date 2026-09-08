# Baseline Model Report

## Dataset Summary

- Total rows: 441
- Trainable rows: 441

## Status

Baseline model trained successfully.

## Features

- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

## Accuracy

0.9248

## Classification Report

```text
              precision    recall  f1-score   support

           0       0.94      0.81      0.87        42
           1       0.92      0.98      0.95        91

    accuracy                           0.92       133
   macro avg       0.93      0.89      0.91       133
weighted avg       0.93      0.92      0.92       133

```