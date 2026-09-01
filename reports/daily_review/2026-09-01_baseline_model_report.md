# Baseline Model Report

## Dataset Summary

- Total rows: 945
- Trainable rows: 945

## Status

Baseline model trained successfully.

## Features

- Numeric features: ['event_score', 'news_count', 'positive_keyword_count', 'negative_keyword_count', 'news_sentiment_score', 'news_attention_score']
- Categorical features: ['event_type', 'prediction_direction', 'initial_confidence']

## Accuracy

0.7782

## Classification Report

```text
              precision    recall  f1-score   support

           0       0.70      0.90      0.78       127
           1       0.89      0.68      0.77       157

    accuracy                           0.78       284
   macro avg       0.79      0.79      0.78       284
weighted avg       0.80      0.78      0.78       284

```