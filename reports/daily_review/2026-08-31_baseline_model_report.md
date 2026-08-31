# Baseline Model Report

## Dataset Summary

- Total rows: 951
- Trainable rows: 951

## Status

Baseline model trained successfully.

## Features

- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

## Accuracy

0.9301

## Classification Report

```text
              precision    recall  f1-score   support

           0       0.94      0.98      0.96       243
           1       0.87      0.63      0.73        43

    accuracy                           0.93       286
   macro avg       0.90      0.81      0.84       286
weighted avg       0.93      0.93      0.93       286

```