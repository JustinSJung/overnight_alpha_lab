# Baseline Model Report

## Dataset Summary

- Total rows: 577
- Trainable rows: 577

## Status

Baseline model trained successfully.

## Features

- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

## Accuracy

0.9483

## Classification Report

```text
              precision    recall  f1-score   support

           0       0.97      0.97      0.97       142
           1       0.87      0.84      0.86        32

    accuracy                           0.95       174
   macro avg       0.92      0.91      0.91       174
weighted avg       0.95      0.95      0.95       174

```