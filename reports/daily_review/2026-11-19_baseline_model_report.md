# Baseline Model Report

## Dataset Summary

- Total rows: 255
- Trainable rows: 255

## Status

Baseline model trained successfully.

## Features

- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

## Accuracy

0.8831

## Classification Report

```text
              precision    recall  f1-score   support

           0       0.71      0.67      0.69        15
           1       0.92      0.94      0.93        62

    accuracy                           0.88        77
   macro avg       0.82      0.80      0.81        77
weighted avg       0.88      0.88      0.88        77

```