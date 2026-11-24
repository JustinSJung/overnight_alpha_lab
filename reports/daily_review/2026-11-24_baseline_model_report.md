# Baseline Model Report

## Dataset Summary

- Total rows: 825
- Trainable rows: 825

## Status

Baseline model trained successfully.

## Features

- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

## Accuracy

0.9234

## Classification Report

```text
              precision    recall  f1-score   support

           0       0.88      0.73      0.80        52
           1       0.93      0.97      0.95       196

    accuracy                           0.92       248
   macro avg       0.91      0.85      0.88       248
weighted avg       0.92      0.92      0.92       248

```