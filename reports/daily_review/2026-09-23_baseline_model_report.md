# Baseline Model Report

## Dataset Summary

- Total rows: 638
- Trainable rows: 638

## Status

Baseline model trained successfully.

## Features

- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

## Accuracy

0.9271

## Classification Report

```text
              precision    recall  f1-score   support

           0       0.93      0.99      0.96       159
           1       0.91      0.64      0.75        33

    accuracy                           0.93       192
   macro avg       0.92      0.81      0.85       192
weighted avg       0.93      0.93      0.92       192

```