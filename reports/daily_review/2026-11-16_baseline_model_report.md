# Baseline Model Report

## Dataset Summary

- Total rows: 131
- Trainable rows: 131

## Status

Baseline model trained successfully.

## Features

- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

## Accuracy

0.6

## Classification Report

```text
              precision    recall  f1-score   support

           0       0.67      0.81      0.73        27
           1       0.29      0.15      0.20        13

    accuracy                           0.60        40
   macro avg       0.48      0.48      0.47        40
weighted avg       0.54      0.60      0.56        40

```