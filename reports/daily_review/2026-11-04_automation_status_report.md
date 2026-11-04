# Automation Status Report - 2026-11-04

Generated at: 2026-11-04 02:54:14

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
| Raw DART disclosures | 518 |
| Parsed DART disclosures | 518 |
| Selected key events | 56 |
| Scored key events | 56 |
| News feature rows | 56 |
| Error note rows | 126 |
| ML dataset rows | 213 |

## Prediction Result Summary

| Result | Rows |
|---|---:|
| Pending | 0 |
| Success | 57 |
| Failure | 156 |
| Trainable rows | 213 |

## Latest Files

- raw_dart: `data/raw/dart_disclosures_20261103.csv`
- parsed_dart: `data/processed/parsed_dart_disclosures_20261103.csv`
- selected_events: `data/processed/selected_key_events_20261103.csv`
- scored_events: `data/processed/scored_key_events_20261104.csv`
- news_features: `data/processed/event_news_features_20261104.csv`
- ml_dataset: `data/processed/ml_dataset_20261104.csv`
- error_notes: `data/predictions/error_notes_20261104.csv`
- daily_prediction_report: `reports/daily_prediction/2026-11-04_volume_market_adjusted_daily_candidates.md`
- baseline_model_report: `reports/daily_review/2026-11-04_baseline_model_report.md`

## Interpretation

The dataset has enough trainable rows for baseline model training. Model performance should be reviewed carefully.

## Next Step

Continue running the scheduled pipeline or catch-up script. As pending rows are converted into success or failure, the training dataset will grow.
