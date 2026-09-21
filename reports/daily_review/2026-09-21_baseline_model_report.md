# Baseline Model Report

## Dataset Summary

- Total rows: 1120
- Trainable rows: 1120

## Status

Baseline model trained successfully.

## Features

- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

## Accuracy

0.9554

## Classification Report

```text
              precision    recall  f1-score   support

           0       0.97      0.98      0.98       310
           1       0.76      0.62      0.68        26

    accuracy                           0.96       336
   macro avg       0.87      0.80      0.83       336
weighted avg       0.95      0.96      0.95       336

```