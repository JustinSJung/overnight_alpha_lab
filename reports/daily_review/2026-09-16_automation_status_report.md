# Automation Status Report - 2026-09-16

Generated at: 2026-09-16 01:20:07

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
| Raw DART disclosures | 561 |
| Parsed DART disclosures | 561 |
| Selected key events | 88 |
| Scored key events | 88 |
| News feature rows | 88 |
| Error note rows | 367 |
| ML dataset rows | 1362 |

## Prediction Result Summary

| Result | Rows |
|---|---:|
| Pending | 0 |
| Success | 1003 |
| Failure | 359 |
| Trainable rows | 1362 |

## Latest Files

- raw_dart: `data/raw/dart_disclosures_20260915.csv`
- parsed_dart: `data/processed/parsed_dart_disclosures_20260915.csv`
- selected_events: `data/processed/selected_key_events_20260915.csv`
- scored_events: `data/processed/scored_key_events_20260916.csv`
- news_features: `data/processed/event_news_features_20260916.csv`
- ml_dataset: `data/processed/ml_dataset_20260916.csv`
- error_notes: `data/predictions/error_notes_20260916.csv`
- daily_prediction_report: `reports/daily_prediction/2026-09-16_volume_market_adjusted_daily_candidates.md`
- baseline_model_report: `reports/daily_review/2026-09-16_baseline_model_report.md`

## Interpretation

The dataset has enough trainable rows for baseline model training. Model performance should be reviewed carefully.

## Next Step

Continue running the scheduled pipeline or catch-up script. As pending rows are converted into success or failure, the training dataset will grow.
