# Baseline Model Report

## Dataset Summary

- Total rows: 441
- Trainable rows: 441

## Status

Baseline model trained successfully.

## Features

- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

## Accuracy

0.9398

## Classification Report

```text
              precision    recall  f1-score   support

           0       0.94      0.85      0.89        39
           1       0.94      0.98      0.96        94

    accuracy                           0.94       133
   macro avg       0.94      0.91      0.93       133
weighted avg       0.94      0.94      0.94       133

```