# Baseline Model Report

## Dataset Summary

- Total rows: 446
- Trainable rows: 446

## Status

Baseline model trained successfully.

## Features

- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

## Accuracy

0.8582

## Classification Report

```text
              precision    recall  f1-score   support

           0       0.89      0.90      0.89        87
           1       0.80      0.79      0.80        47

    accuracy                           0.86       134
   macro avg       0.85      0.84      0.84       134
weighted avg       0.86      0.86      0.86       134

```