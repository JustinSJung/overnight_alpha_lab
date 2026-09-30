# Automation Status Report - 2026-09-30

Generated at: 2026-09-30 02:55:42

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
| Raw DART disclosures | 837 |
| Parsed DART disclosures | 837 |
| Selected key events | 92 |
| Scored key events | 92 |
| News feature rows | 92 |
| Error note rows | 206 |
| ML dataset rows | 1015 |

## Prediction Result Summary

| Result | Rows |
|---|---:|
| Pending | 0 |
| Success | 423 |
| Failure | 592 |
| Trainable rows | 1015 |

## Latest Files

- raw_dart: `data/raw/dart_disclosures_20260929.csv`
- parsed_dart: `data/processed/parsed_dart_disclosures_20260929.csv`
- selected_events: `data/processed/selected_key_events_20260929.csv`
- scored_events: `data/processed/scored_key_events_20260930.csv`
- news_features: `data/processed/event_news_features_20260930.csv`
- ml_dataset: `data/processed/ml_dataset_20260930.csv`
- error_notes: `data/predictions/error_notes_20260930.csv`
- daily_prediction_report: `reports/daily_prediction/2026-09-30_volume_market_adjusted_daily_candidates.md`
- baseline_model_report: `reports/daily_review/2026-09-30_baseline_model_report.md`

## Interpretation

The dataset has enough trainable rows for baseline model training. Model performance should be reviewed carefully.

## Next Step

Continue running the scheduled pipeline or catch-up script. As pending rows are converted into success or failure, the training dataset will grow.
