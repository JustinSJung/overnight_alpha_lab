# Baseline Model Report

## Dataset Summary

- Total rows: 77
- Trainable rows: 77

## Status

Baseline model trained successfully.

## Features

- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

## Accuracy

0.6667

## Classification Report

```text
              precision    recall  f1-score   support

           0       0.75      0.64      0.69        14
           1       0.58      0.70      0.64        10

    accuracy                           0.67        24
   macro avg       0.67      0.67      0.66        24
weighted avg       0.68      0.67      0.67        24

```