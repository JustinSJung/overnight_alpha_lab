# Automation Status Report - 2026-10-30

Generated at: 2026-10-30 02:32:18

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
| Raw DART disclosures | 854 |
| Parsed DART disclosures | 854 |
| Selected key events | 87 |
| Scored key events | 87 |
| News feature rows | 87 |
| Error note rows | 313 |
| ML dataset rows | 2799 |

## Prediction Result Summary

| Result | Rows |
|---|---:|
| Pending | 0 |
| Success | 2308 |
| Failure | 491 |
| Trainable rows | 2799 |

## Latest Files

- raw_dart: `data/raw/dart_disclosures_20261029.csv`
- parsed_dart: `data/processed/parsed_dart_disclosures_20261029.csv`
- selected_events: `data/processed/selected_key_events_20261029.csv`
- scored_events: `data/processed/scored_key_events_20261030.csv`
- news_features: `data/processed/event_news_features_20261030.csv`
- ml_dataset: `data/processed/ml_dataset_20261030.csv`
- error_notes: `data/predictions/error_notes_20261030.csv`
- daily_prediction_report: `reports/daily_prediction/2026-10-30_volume_market_adjusted_daily_candidates.md`
- baseline_model_report: `reports/daily_review/2026-10-30_baseline_model_report.md`

## Interpretation

The dataset has enough trainable rows for baseline model training. Model performance should be reviewed carefully.

## Next Step

Continue running the scheduled pipeline or catch-up script. As pending rows are converted into success or failure, the training dataset will grow.
