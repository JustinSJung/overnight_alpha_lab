# Baseline Model Report

## Dataset Summary

- Total rows: 2861
- Trainable rows: 2861

## Status

Baseline model trained successfully.

## Features

- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

## Accuracy

0.9895

## Classification Report

```text
              precision    recall  f1-score   support

           0       0.90      0.88      0.89        43
           1       0.99      1.00      0.99       816

    accuracy                           0.99       859
   macro avg       0.95      0.94      0.94       859
weighted avg       0.99      0.99      0.99       859

```