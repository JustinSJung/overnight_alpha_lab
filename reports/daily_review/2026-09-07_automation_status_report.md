# Automation Status Report - 2026-09-07

Generated at: 2026-09-07 00:27:30

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
| Raw DART disclosures | 637 |
| Parsed DART disclosures | 637 |
| Selected key events | 77 |
| Scored key events | 77 |
| News feature rows | 77 |
| Error note rows | 191 |
| ML dataset rows | 446 |

## Prediction Result Summary

| Result | Rows |
|---|---:|
| Pending | 0 |
| Success | 156 |
| Failure | 290 |
| Trainable rows | 446 |

## Latest Files

- raw_dart: `data/raw/dart_disclosures_20260904.csv`
- parsed_dart: `data/processed/parsed_dart_disclosures_20260904.csv`
- selected_events: `data/processed/selected_key_events_20260904.csv`
- scored_events: `data/processed/scored_key_events_20260906.csv`
- news_features: `data/processed/event_news_features_20260906.csv`
- ml_dataset: `data/processed/ml_dataset_20260907.csv`
- error_notes: `data/predictions/error_notes_20260907.csv`
- daily_prediction_report: `reports/daily_prediction/2026-09-07_volume_market_adjusted_daily_candidates.md`
- baseline_model_report: `reports/daily_review/2026-09-07_baseline_model_report.md`

## Interpretation

The dataset has enough trainable rows for baseline model training. Model performance should be reviewed carefully.

## Next Step

Continue running the scheduled pipeline or catch-up script. As pending rows are converted into success or failure, the training dataset will grow.
