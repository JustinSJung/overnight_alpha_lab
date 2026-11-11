# Baseline Model Report

## Dataset Summary

- Total rows: 1290
- Trainable rows: 1290

## Status

Baseline model trained successfully.

## Features

- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

## Accuracy

0.8811

## Classification Report

```text
              precision    recall  f1-score   support

           0       0.81      0.67      0.74        95
           1       0.90      0.95      0.92       292

    accuracy                           0.88       387
   macro avg       0.85      0.81      0.83       387
weighted avg       0.88      0.88      0.88       387

```