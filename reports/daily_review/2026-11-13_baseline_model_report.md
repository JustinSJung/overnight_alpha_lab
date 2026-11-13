# Baseline Model Report

## Dataset Summary

- Total rows: 4764
- Trainable rows: 4764

## Status

Baseline model trained successfully.

## Features

- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

## Accuracy

0.9965

## Classification Report

```text
              precision    recall  f1-score   support

           0       1.00      1.00      1.00      1195
           1       1.00      0.98      0.99       235

    accuracy                           1.00      1430
   macro avg       1.00      0.99      0.99      1430
weighted avg       1.00      1.00      1.00      1430

```