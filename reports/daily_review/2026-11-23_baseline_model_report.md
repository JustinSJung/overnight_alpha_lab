# Baseline Model Report

## Dataset Summary

- Total rows: 471
- Trainable rows: 471

## Status

Baseline model trained successfully.

## Features

- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

## Accuracy

0.9507

## Classification Report

```text
              precision    recall  f1-score   support

           0       0.95      0.93      0.94        58
           1       0.95      0.96      0.96        84

    accuracy                           0.95       142
   macro avg       0.95      0.95      0.95       142
weighted avg       0.95      0.95      0.95       142

```