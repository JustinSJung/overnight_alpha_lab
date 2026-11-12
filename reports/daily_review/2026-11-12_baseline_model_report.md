# Baseline Model Report

## Dataset Summary

- Total rows: 434
- Trainable rows: 434

## Status

Baseline model trained successfully.

## Features

- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

## Accuracy

0.8855

## Classification Report

```text
              precision    recall  f1-score   support

           0       0.89      0.91      0.90        75
           1       0.87      0.86      0.86        56

    accuracy                           0.89       131
   macro avg       0.88      0.88      0.88       131
weighted avg       0.89      0.89      0.89       131

```