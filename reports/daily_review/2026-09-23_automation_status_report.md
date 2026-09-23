# Automation Status Report - 2026-09-23

Generated at: 2026-09-23 02:02:31

## Execution Summary

| Item | Status |
|---|---|
| Raw DART disclosure file | YES |
| Parsed DART file | YES |
| Selected key events file | YES |
| Scored key events file | YES |
| News features file | YES |
| Error notes file | YES |
| ML dataset file | YES |
| Baseline model report | YES |

## Data Summary

| Dataset | Rows |
|---|---:|
| Raw DART disclosures | 531 |
| Parsed DART disclosures | 531 |
| Selected key events | 81 |
| Scored key events | 81 |
| News feature rows | 81 |
| Error note rows | 148 |
| ML dataset rows | 638 |

## Prediction Result Summary

| Result | Rows |
|---|---:|
| Pending | 0 |
| Success | 108 |
| Failure | 530 |
| Trainable rows | 638 |

## Latest Files

- raw_dart: `data/raw/dart_disclosures_20260922.csv`
- parsed_dart: `data/processed/parsed_dart_disclosures_20260922.csv`
- selected_events: `data/processed/selected_key_events_20260922.csv`
- scored_events: `data/processed/scored_key_events_20260923.csv`
- news_features: `data/processed/event_news_features_20260923.csv`
- ml_dataset: `data/processed/ml_dataset_20260923.csv`
- error_notes: `data/predictions/error_notes_20260923.csv`
- daily_prediction_report: `reports/daily_prediction/2026-09-23_volume_market_adjusted_daily_candidates.md`
- baseline_model_report: `reports/daily_review/2026-09-23_baseline_model_report.md`

## Interpretation

The dataset has enough trainable rows for baseline model training. Model performance should be reviewed carefully.

## Next Step

Continue running the scheduled pipeline or catch-up script. As pending rows are converted into success or failure, the training dataset will grow.
