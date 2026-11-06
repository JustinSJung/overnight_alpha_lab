# Baseline Model Report

## Dataset Summary

- Total rows: 1062
- Trainable rows: 1062

## Status

Baseline model trained successfully.

## Features

- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

## Accuracy

0.9467

## Classification Report

```text
              precision    recall  f1-score   support

           0       0.92      0.96      0.94       136
           1       0.97      0.93      0.95       183

    accuracy                           0.95       319
   macro avg       0.94      0.95      0.95       319
weighted avg       0.95      0.95      0.95       319

```