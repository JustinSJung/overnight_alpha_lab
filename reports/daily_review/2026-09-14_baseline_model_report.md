# Baseline Model Report

## Dataset Summary

- Total rows: 321
- Trainable rows: 321

## Status

Baseline model trained successfully.

## Features

- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

## Accuracy

0.7526

## Classification Report

```text
              precision    recall  f1-score   support

           0       0.80      0.85      0.82        66
           1       0.63      0.55      0.59        31

    accuracy                           0.75        97
   macro avg       0.71      0.70      0.70        97
weighted avg       0.75      0.75      0.75        97

```