# Baseline Model Report

## Dataset Summary

- Total rows: 818
- Trainable rows: 818

## Status

Baseline model trained successfully.

## Features

- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

## Accuracy

0.935

## Classification Report

```text
              precision    recall  f1-score   support

           0       0.93      0.95      0.94       132
           1       0.94      0.92      0.93       114

    accuracy                           0.93       246
   macro avg       0.94      0.93      0.93       246
weighted avg       0.93      0.93      0.93       246

```