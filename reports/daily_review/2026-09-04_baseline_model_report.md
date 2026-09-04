# Baseline Model Report

## Dataset Summary

- Total rows: 1547
- Trainable rows: 1547

## Status

Baseline model trained successfully.

## Features

- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

## Accuracy

0.9118

## Classification Report

```text
              precision    recall  f1-score   support

           0       0.97      0.65      0.78       113
           1       0.90      0.99      0.94       352

    accuracy                           0.91       465
   macro avg       0.94      0.82      0.86       465
weighted avg       0.92      0.91      0.91       465

```