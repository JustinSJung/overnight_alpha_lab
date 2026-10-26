# Baseline Model Report

## Dataset Summary

- Total rows: 457
- Trainable rows: 457

## Status

Baseline model trained successfully.

## Features

- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

## Accuracy

0.9493

## Classification Report

```text
              precision    recall  f1-score   support

           0       0.93      0.97      0.95        66
           1       0.97      0.93      0.95        72

    accuracy                           0.95       138
   macro avg       0.95      0.95      0.95       138
weighted avg       0.95      0.95      0.95       138

```