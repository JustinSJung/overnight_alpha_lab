# Baseline Model Report

## Dataset Summary

- Total rows: 499
- Trainable rows: 499

## Status

Baseline model trained successfully.

## Features

- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

## Accuracy

0.9733

## Classification Report

```text
              precision    recall  f1-score   support

           0       0.97      0.99      0.98       106
           1       0.98      0.93      0.95        44

    accuracy                           0.97       150
   macro avg       0.97      0.96      0.97       150
weighted avg       0.97      0.97      0.97       150

```