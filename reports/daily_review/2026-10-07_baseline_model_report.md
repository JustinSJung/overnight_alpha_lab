# Baseline Model Report

## Dataset Summary

- Total rows: 952
- Trainable rows: 952

## Status

Baseline model trained successfully.

## Features

- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

## Accuracy

0.951

## Classification Report

```text
              precision    recall  f1-score   support

           0       0.97      0.97      0.97       224
           1       0.89      0.89      0.89        62

    accuracy                           0.95       286
   macro avg       0.93      0.93      0.93       286
weighted avg       0.95      0.95      0.95       286

```