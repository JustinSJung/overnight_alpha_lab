# Baseline Model Report

## Dataset Summary

- Total rows: 2275
- Trainable rows: 2275

## Status

Baseline model trained successfully.

## Features

- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

## Accuracy

0.9898

## Classification Report

```text
              precision    recall  f1-score   support

           0       0.99      0.93      0.96        82
           1       0.99      1.00      0.99       601

    accuracy                           0.99       683
   macro avg       0.99      0.96      0.98       683
weighted avg       0.99      0.99      0.99       683

```