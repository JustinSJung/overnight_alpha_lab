# Baseline Model Report

## Dataset Summary

- Total rows: 467
- Trainable rows: 467

## Status

Baseline model trained successfully.

## Features

- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

## Accuracy

0.9291

## Classification Report

```text
              precision    recall  f1-score   support

           0       0.95      0.96      0.95       108
           1       0.87      0.82      0.84        33

    accuracy                           0.93       141
   macro avg       0.91      0.89      0.90       141
weighted avg       0.93      0.93      0.93       141

```