# Automation Status Report - 2026-06-29

Generated at: 2026-06-29 01:54:47

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
| Raw DART disclosures | 100 |
| Parsed DART disclosures | 100 |
| Selected key events | 6 |
| Scored key events | 6 |
| News feature rows | 6 |
| Error note rows | 9 |
| ML dataset rows | 11 |

## Prediction Result Summary

| Result | Rows |
|---|---:|
| Pending | 11 |
| Success | 0 |
| Failure | 0 |
| Trainable rows | 0 |

## Latest Files

- raw_dart: `data/raw/dart_disclosures_20260629.csv`
- parsed_dart: `data/processed/parsed_dart_disclosures_20260629.csv`
- selected_events: `data/processed/selected_key_events_20260629.csv`
- scored_events: `data/processed/scored_key_events_20260629.csv`
- news_features: `data/processed/event_news_features_20260629.csv`
- ml_dataset: `data/processed/ml_dataset_20260629.csv`
- error_notes: `data/predictions/error_notes_20260629.csv`
- daily_prediction_report: `reports/daily_prediction/2026-06-29_volume_market_adjusted_daily_candidates.md`
- baseline_model_report: `reports/daily_review/2026-06-29_baseline_model_report.md`

## Interpretation

The ML dataset exists, but there are no trainable rows yet. Most events are still pending because next trading day price data may not be available.

## Next Step

Continue running the scheduled pipeline or catch-up script. As pending rows are converted into success or failure, the training dataset will grow.
