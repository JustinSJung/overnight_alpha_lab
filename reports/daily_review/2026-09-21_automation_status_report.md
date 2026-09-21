# Automation Status Report - 2026-09-21

Generated at: 2026-09-21 01:03:35

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
| Raw DART disclosures | 695 |
| Parsed DART disclosures | 695 |
| Selected key events | 82 |
| Scored key events | 82 |
| News feature rows | 82 |
| Error note rows | 208 |
| ML dataset rows | 1120 |

## Prediction Result Summary

| Result | Rows |
|---|---:|
| Pending | 0 |
| Success | 88 |
| Failure | 1032 |
| Trainable rows | 1120 |

## Latest Files

- raw_dart: `data/raw/dart_disclosures_20260918.csv`
- parsed_dart: `data/processed/parsed_dart_disclosures_20260918.csv`
- selected_events: `data/processed/selected_key_events_20260918.csv`
- scored_events: `data/processed/scored_key_events_20260921.csv`
- news_features: `data/processed/event_news_features_20260921.csv`
- ml_dataset: `data/processed/ml_dataset_20260921.csv`
- error_notes: `data/predictions/error_notes_20260921.csv`
- daily_prediction_report: `reports/daily_prediction/2026-09-21_volume_market_adjusted_daily_candidates.md`
- baseline_model_report: `reports/daily_review/2026-09-21_baseline_model_report.md`

## Interpretation

The dataset has enough trainable rows for baseline model training. Model performance should be reviewed carefully.

## Next Step

Continue running the scheduled pipeline or catch-up script. As pending rows are converted into success or failure, the training dataset will grow.
