# Baseline Model Report

## Dataset Summary

- Total rows: 723
- Trainable rows: 723

## Status

Baseline model trained successfully.

## Features

- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

## Accuracy

0.9401

## Classification Report

```text
              precision    recall  f1-score   support

           0       0.96      0.97      0.96       175
           1       0.85      0.83      0.84        42

    accuracy                           0.94       217
   macro avg       0.91      0.90      0.90       217
weighted avg       0.94      0.94      0.94       217

```