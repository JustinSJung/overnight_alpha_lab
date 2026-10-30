# Baseline Model Report

## Dataset Summary

- Total rows: 2799
- Trainable rows: 2799

## Status

Baseline model trained successfully.

## Features

- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

## Accuracy

0.981

## Classification Report

```text
              precision    recall  f1-score   support

           0       0.93      0.96      0.95       147
           1       0.99      0.99      0.99       693

    accuracy                           0.98       840
   macro avg       0.96      0.97      0.97       840
weighted avg       0.98      0.98      0.98       840

```