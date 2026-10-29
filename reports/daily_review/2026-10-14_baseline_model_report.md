# Baseline Model Report

## Dataset Summary

- Total rows: 783
- Trainable rows: 783

## Status

Baseline model trained successfully.

## Features

- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

## Accuracy

0.9745

## Classification Report

```text
              precision    recall  f1-score   support

           0       0.97      1.00      0.99       219
           1       1.00      0.62      0.77        16

    accuracy                           0.97       235
   macro avg       0.99      0.81      0.88       235
weighted avg       0.98      0.97      0.97       235

```