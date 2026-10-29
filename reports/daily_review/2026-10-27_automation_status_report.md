# Automation Status Report - 2026-10-27

Generated at: 2026-10-27 02:03:10

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
| Raw DART disclosures | 526 |
| Parsed DART disclosures | 526 |
| Selected key events | 79 |
| Scored key events | 79 |
| News feature rows | 79 |
| Error note rows | 234 |
| ML dataset rows | 964 |

## Prediction Result Summary

| Result | Rows |
|---|---:|
| Pending | 0 |
| Success | 509 |
| Failure | 455 |
| Trainable rows | 964 |

## Latest Files

- raw_dart: `data/raw/dart_disclosures_20261026.csv`
- parsed_dart: `data/processed/parsed_dart_disclosures_20261026.csv`
- selected_events: `data/processed/selected_key_events_20261026.csv`
- scored_events: `data/processed/scored_key_events_20261027.csv`
- news_features: `data/processed/event_news_features_20261027.csv`
- ml_dataset: `data/processed/ml_dataset_20261027.csv`
- error_notes: `data/predictions/error_notes_20261027.csv`
- daily_prediction_report: `reports/daily_prediction/2026-10-27_volume_market_adjusted_daily_candidates.md`
- baseline_model_report: `reports/daily_review/2026-10-27_baseline_model_report.md`

## Interpretation

The dataset has enough trainable rows for baseline model training. Model performance should be reviewed carefully.

## Next Step

Continue running the scheduled pipeline or catch-up script. As pending rows are converted into success or failure, the training dataset will grow.
