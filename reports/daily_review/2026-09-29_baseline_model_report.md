# Baseline Model Report

## Dataset Summary

- Total rows: 1470
- Trainable rows: 1470

## Status

Baseline model trained successfully.

## Features

- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

## Accuracy

0.9705

## Classification Report

```text
              precision    recall  f1-score   support

           0       0.95      0.97      0.96       167
           1       0.98      0.97      0.98       274

    accuracy                           0.97       441
   macro avg       0.97      0.97      0.97       441
weighted avg       0.97      0.97      0.97       441

```