# Baseline Model Report

## Dataset Summary

- Total rows: 468
- Trainable rows: 468

## Status

Baseline model trained successfully.

## Features

- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

## Accuracy

0.9149

## Classification Report

```text
              precision    recall  f1-score   support

           0       0.96      0.91      0.93        93
           1       0.85      0.92      0.88        48

    accuracy                           0.91       141
   macro avg       0.90      0.92      0.91       141
weighted avg       0.92      0.91      0.92       141

```