# Baseline Model Report

## Dataset Summary

- Total rows: 320
- Trainable rows: 320

## Status

Baseline model trained successfully.

## Features

- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

## Accuracy

0.8021

## Classification Report

```text
              precision    recall  f1-score   support

           0       0.84      0.90      0.87        71
           1       0.65      0.52      0.58        25

    accuracy                           0.80        96
   macro avg       0.75      0.71      0.72        96
weighted avg       0.79      0.80      0.79        96

```