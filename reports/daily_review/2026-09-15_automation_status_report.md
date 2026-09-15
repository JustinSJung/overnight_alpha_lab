# Automation Status Report - 2026-09-15

Generated at: 2026-09-15 01:44:45

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
| Raw DART disclosures | 506 |
| Parsed DART disclosures | 506 |
| Selected key events | 78 |
| Scored key events | 78 |
| News feature rows | 78 |
| Error note rows | 194 |
| ML dataset rows | 106 |

## Prediction Result Summary

| Result | Rows |
|---|---:|
| Pending | 0 |
| Success | 0 |
| Failure | 0 |
| Trainable rows | 0 |

## Latest Files

- raw_dart: `data/raw/dart_disclosures_20260914.csv`
- parsed_dart: `data/processed/parsed_dart_disclosures_20260914.csv`
- selected_events: `data/processed/selected_key_events_20260914.csv`
- scored_events: `data/processed/scored_key_events_20260915.csv`
- news_features: `data/processed/event_news_features_20260915.csv`
- ml_dataset: `data/processed/ml_dataset_20260915.csv`
- error_notes: `data/predictions/error_notes_20260915.csv`
- daily_prediction_report: `reports/daily_prediction/2026-09-15_volume_market_adjusted_daily_candidates.md`
- baseline_model_report: `reports/daily_review/2026-09-15_baseline_model_report.md`

## Interpretation

The ML dataset exists, but there are no trainable rows yet. Most events are still pending because next trading day price data may not be available.

## Next Step

Continue running the scheduled pipeline or catch-up script. As pending rows are converted into success or failure, the training dataset will grow.
