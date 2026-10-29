# Baseline Model Report

## Dataset Summary

- Total rows: 486
- Trainable rows: 486

## Status

Baseline model trained successfully.

## Features

- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

## Accuracy

0.911

## Classification Report

```text
              precision    recall  f1-score   support

           0       0.80      0.77      0.79        31
           1       0.94      0.95      0.94       115

    accuracy                           0.91       146
   macro avg       0.87      0.86      0.87       146
weighted avg       0.91      0.91      0.91       146

```