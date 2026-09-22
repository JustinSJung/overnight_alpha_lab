# Baseline Model Report

## Dataset Summary

- Total rows: 2575
- Trainable rows: 2575

## Status

Baseline model trained successfully.

## Features

- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

## Accuracy

0.9884

## Classification Report

```text
              precision    recall  f1-score   support

           0       1.00      0.99      0.99       690
           1       0.92      0.98      0.95        83

    accuracy                           0.99       773
   macro avg       0.96      0.98      0.97       773
weighted avg       0.99      0.99      0.99       773

```