# Baseline Model Report

## Dataset Summary

- Total rows: 1015
- Trainable rows: 1015

## Status

Baseline model trained successfully.

## Features

- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

## Accuracy

0.9115

## Classification Report

```text
              precision    recall  f1-score   support

           0       0.92      0.93      0.92       178
           1       0.90      0.89      0.89       127

    accuracy                           0.91       305
   macro avg       0.91      0.91      0.91       305
weighted avg       0.91      0.91      0.91       305

```