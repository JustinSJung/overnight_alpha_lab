# Baseline Model Report

## Dataset Summary

- Total rows: 1362
- Trainable rows: 1362

## Status

Baseline model trained successfully.

## Features

- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

## Accuracy

0.8826

## Classification Report

```text
              precision    recall  f1-score   support

           0       0.87      0.66      0.75       108
           1       0.89      0.96      0.92       301

    accuracy                           0.88       409
   macro avg       0.88      0.81      0.84       409
weighted avg       0.88      0.88      0.88       409

```