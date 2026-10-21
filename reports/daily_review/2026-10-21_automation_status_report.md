# Automation Status Report - 2026-10-21

Generated at: 2026-10-21 01:15:47

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
| Raw DART disclosures | 545 |
| Parsed DART disclosures | 545 |
| Selected key events | 46 |
| Scored key events | 46 |
| News feature rows | 46 |
| Error note rows | 72 |
| ML dataset rows | 77 |

## Prediction Result Summary

| Result | Rows |
|---|---:|
| Pending | 0 |
| Success | 31 |
| Failure | 46 |
| Trainable rows | 77 |

## Latest Files

- raw_dart: `data/raw/dart_disclosures_20261020.csv`
- parsed_dart: `data/processed/parsed_dart_disclosures_20261020.csv`
- selected_events: `data/processed/selected_key_events_20261020.csv`
- scored_events: `data/processed/scored_key_events_20261021.csv`
- news_features: `data/processed/event_news_features_20261021.csv`
- ml_dataset: `data/processed/ml_dataset_20261021.csv`
- error_notes: `data/predictions/error_notes_20261021.csv`
- daily_prediction_report: `reports/daily_prediction/2026-10-21_volume_market_adjusted_daily_candidates.md`
- baseline_model_report: `reports/daily_review/2026-10-21_baseline_model_report.md`

## Interpretation

The dataset has enough trainable rows for baseline model training. Model performance should be reviewed carefully.

## Next Step

Continue running the scheduled pipeline or catch-up script. As pending rows are converted into success or failure, the training dataset will grow.
