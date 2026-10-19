# Baseline Model Report

## Dataset Summary

- Total rows: 1913
- Trainable rows: 1913

## Status

Baseline model trained successfully.

## Features

- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

## Accuracy

0.9756

## Classification Report

```text
              precision    recall  f1-score   support

           0       0.96      0.90      0.93       100
           1       0.98      0.99      0.99       474

    accuracy                           0.98       574
   macro avg       0.97      0.95      0.96       574
weighted avg       0.98      0.98      0.98       574

```