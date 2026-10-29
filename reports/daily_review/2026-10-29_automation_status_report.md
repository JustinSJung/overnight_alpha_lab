# Automation Status Report - 2026-10-29

Generated at: 2026-10-29 02:25:48

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
| Raw DART disclosures | 665 |
| Parsed DART disclosures | 665 |
| Selected key events | 79 |
| Scored key events | 79 |
| News feature rows | 79 |
| Error note rows | 385 |
| ML dataset rows | 136 |

## Prediction Result Summary

| Result | Rows |
|---|---:|
| Pending | 0 |
| Success | 0 |
| Failure | 0 |
| Trainable rows | 0 |

## Latest Files

- raw_dart: `data/raw/dart_disclosures_20261028.csv`
- parsed_dart: `data/processed/parsed_dart_disclosures_20261028.csv`
- selected_events: `data/processed/selected_key_events_20261028.csv`
- scored_events: `data/processed/scored_key_events_20261029.csv`
- news_features: `data/processed/event_news_features_20261029.csv`
- ml_dataset: `data/processed/ml_dataset_20261029.csv`
- error_notes: `data/predictions/error_notes_20261029.csv`
- daily_prediction_report: `reports/daily_prediction/2026-10-29_volume_market_adjusted_daily_candidates.md`
- baseline_model_report: `reports/daily_review/2026-10-29_baseline_model_report.md`

## Interpretation

The ML dataset exists, but there are no trainable rows yet. Most events are still pending because next trading day price data may not be available.

## Next Step

Continue running the scheduled pipeline or catch-up script. As pending rows are converted into success or failure, the training dataset will grow.
