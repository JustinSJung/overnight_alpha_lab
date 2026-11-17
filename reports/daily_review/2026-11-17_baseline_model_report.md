# Baseline Model Report

## Dataset Summary

- Total rows: 628
- Trainable rows: 628

## Status

Baseline model trained successfully.

## Features

- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

## Accuracy

0.9101

## Classification Report

```text
              precision    recall  f1-score   support

           0       0.92      0.86      0.89        78
           1       0.91      0.95      0.93       111

    accuracy                           0.91       189
   macro avg       0.91      0.90      0.91       189
weighted avg       0.91      0.91      0.91       189

```