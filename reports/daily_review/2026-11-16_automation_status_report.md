# Automation Status Report - 2026-11-16

Generated at: 2026-11-16 02:53:23

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
| Raw DART disclosures | 1733 |
| Parsed DART disclosures | 1733 |
| Selected key events | 52 |
| Scored key events | 52 |
| News feature rows | 52 |
| Error note rows | 131 |
| ML dataset rows | 131 |

## Prediction Result Summary

| Result | Rows |
|---|---:|
| Pending | 0 |
| Success | 43 |
| Failure | 88 |
| Trainable rows | 131 |

## Latest Files

- raw_dart: `data/raw/dart_disclosures_20261113.csv`
- parsed_dart: `data/processed/parsed_dart_disclosures_20261113.csv`
- selected_events: `data/processed/selected_key_events_20261113.csv`
- scored_events: `data/processed/scored_key_events_20261116.csv`
- news_features: `data/processed/event_news_features_20261116.csv`
- ml_dataset: `data/processed/ml_dataset_20261116.csv`
- error_notes: `data/predictions/error_notes_20261116.csv`
- daily_prediction_report: `reports/daily_prediction/2026-11-16_volume_market_adjusted_daily_candidates.md`
- baseline_model_report: `reports/daily_review/2026-11-16_baseline_model_report.md`

## Interpretation

The dataset has enough trainable rows for baseline model training. Model performance should be reviewed carefully.

## Next Step

Continue running the scheduled pipeline or catch-up script. As pending rows are converted into success or failure, the training dataset will grow.
