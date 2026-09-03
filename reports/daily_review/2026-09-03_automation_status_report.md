# Automation Status Report - 2026-09-03

Generated at: 2026-09-03 00:55:16

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
| Raw DART disclosures | 450 |
| Parsed DART disclosures | 450 |
| Selected key events | 60 |
| Scored key events | 60 |
| News feature rows | 60 |
| Error note rows | 250 |
| ML dataset rows | 2275 |

## Prediction Result Summary

| Result | Rows |
|---|---:|
| Pending | 0 |
| Success | 2003 |
| Failure | 272 |
| Trainable rows | 2275 |

## Latest Files

- raw_dart: `data/raw/dart_disclosures_20260902.csv`
- parsed_dart: `data/processed/parsed_dart_disclosures_20260902.csv`
- selected_events: `data/processed/selected_key_events_20260902.csv`
- scored_events: `data/processed/scored_key_events_20260903.csv`
- news_features: `data/processed/event_news_features_20260903.csv`
- ml_dataset: `data/processed/ml_dataset_20260903.csv`
- error_notes: `data/predictions/error_notes_20260903.csv`
- daily_prediction_report: `reports/daily_prediction/2026-09-03_volume_market_adjusted_daily_candidates.md`
- baseline_model_report: `reports/daily_review/2026-09-03_baseline_model_report.md`

## Interpretation

The dataset has enough trainable rows for baseline model training. Model performance should be reviewed carefully.

## Next Step

Continue running the scheduled pipeline or catch-up script. As pending rows are converted into success or failure, the training dataset will grow.
