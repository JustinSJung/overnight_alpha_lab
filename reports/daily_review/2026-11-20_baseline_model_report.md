# Baseline Model Report

## Dataset Summary

- Total rows: 406
- Trainable rows: 406

## Status

Baseline model trained successfully.

## Features

- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

## Accuracy

0.9262

## Classification Report

```text
              precision    recall  f1-score   support

           0       0.95      0.84      0.89        44
           1       0.92      0.97      0.94        78

    accuracy                           0.93       122
   macro avg       0.93      0.91      0.92       122
weighted avg       0.93      0.93      0.93       122

```