# Baseline Model Report

## Dataset Summary

- Total rows: 551
- Trainable rows: 551

## Status

Baseline model trained successfully.

## Features

- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

## Accuracy

0.8795

## Classification Report

```text
              precision    recall  f1-score   support

           0       0.94      0.83      0.88        89
           1       0.83      0.94      0.88        77

    accuracy                           0.88       166
   macro avg       0.88      0.88      0.88       166
weighted avg       0.89      0.88      0.88       166

```