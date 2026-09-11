# Baseline Model Report

## Dataset Summary

- Total rows: 856
- Trainable rows: 856

## Status

Baseline model trained successfully.

## Features

- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

## Accuracy

0.786

## Classification Report

```text
              precision    recall  f1-score   support

           0       0.82      0.85      0.84       164
           1       0.72      0.67      0.69        93

    accuracy                           0.79       257
   macro avg       0.77      0.76      0.76       257
weighted avg       0.78      0.79      0.78       257

```