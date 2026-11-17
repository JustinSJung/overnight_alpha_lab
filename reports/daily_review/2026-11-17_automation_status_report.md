# Automation Status Report - 2026-11-17

Generated at: 2026-11-17 05:39:51

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
| Raw DART disclosures | 2415 |
| Parsed DART disclosures | 2415 |
| Selected key events | 68 |
| Scored key events | 68 |
| News feature rows | 68 |
| Error note rows | 197 |
| ML dataset rows | 628 |

## Prediction Result Summary

| Result | Rows |
|---|---:|
| Pending | 0 |
| Success | 370 |
| Failure | 258 |
| Trainable rows | 628 |

## Latest Files

- raw_dart: `data/raw/dart_disclosures_20261116.csv`
- parsed_dart: `data/processed/parsed_dart_disclosures_20261116.csv`
- selected_events: `data/processed/selected_key_events_20261116.csv`
- scored_events: `data/processed/scored_key_events_20261117.csv`
- news_features: `data/processed/event_news_features_20261117.csv`
- ml_dataset: `data/processed/ml_dataset_20261117.csv`
- error_notes: `data/predictions/error_notes_20261117.csv`
- daily_prediction_report: `reports/daily_prediction/2026-11-17_volume_market_adjusted_daily_candidates.md`
- baseline_model_report: `reports/daily_review/2026-11-17_baseline_model_report.md`

## Interpretation

The dataset has enough trainable rows for baseline model training. Model performance should be reviewed carefully.

## Next Step

Continue running the scheduled pipeline or catch-up script. As pending rows are converted into success or failure, the training dataset will grow.
