"""Fixed, purged price-only vs price+news comparison; never promotes a model."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import brier_score_loss
from threadpoolctl import threadpool_limits

from src.features.news_learning import NEWS_COLUMNS, add_news_features, read_archive
from src.features.next_open_dataset import TARGET_VERSION, build_next_open_dataset
from src.models.next_open_price_model import load_inputs
from src.models.price_forecaster import date_weights, fit_estimator
from src.models.selected_price_model import COLUMNS, ROOT, factories, partition_info, to_logits, write_json

PROTOCOL = dict(schema='price_news_shadow_v1', decision_time='16:30 Asia/Seoul',
    target_version=TARGET_VERSION, minimum_train_dates=20, calibration_dates=10, evaluation_dates=10,
    threshold=.6, daily_cap=5, promotion_enabled=False, feature_columns=COLUMNS + NEWS_COLUMNS)


def split_shadow(frame):
    days = pd.DatetimeIndex(sorted(frame.signal_date.unique()))
    if len(days) < 40:
        return None
    test_start, calibration_start = days[-10], days[-20]
    train = frame[frame.signal_date.lt(calibration_start) & frame.label_available_date.lt(calibration_start)].copy()
    calibration = frame[frame.signal_date.ge(calibration_start) & frame.signal_date.lt(test_start)
                        & frame.label_available_date.lt(test_start)].copy()
    test = frame[frame.signal_date.ge(test_start)].copy()
    if (train.signal_date.nunique() < 20 or calibration.signal_date.nunique() < 5
            or test.signal_date.nunique() < 10 or train.target.nunique() != 2
            or calibration.target.nunique() != 2):
        return None
    return train, calibration, test


def compare_news(frame):
    if frame.duplicated(['stock_code', 'signal_date']).any():
        raise ValueError('Duplicate shadow candidate keys.')
    eligible = frame[frame.news_collection_observed.eq(1)].copy()
    known = eligible[eligible.target.notna()].copy()
    summary = dict(protocol=PROTOCOL, status='accumulating_point_in_time_news',
        input_candidates=len(frame), news_observed_candidates=len(eligible), mature_news_rows=len(known),
        mature_news_dates=int(known.signal_date.nunique()),
        recommendation_enabled=False, production_model_changed=False,
        interpretation='Development comparison only; not independent high-confidence certification')
    split = split_shadow(known)
    if split is None:
        return summary
    train, calibration, test_known = split
    test = eligible[eligible.signal_date.ge(test_known.signal_date.min())].copy()
    if (train.label_available_date.max() >= calibration.signal_date.min()
            or calibration.label_available_date.max() >= test.signal_date.min()):
        raise ValueError('Shadow label purge failed.')
    summary['status'] = 'matched_development_comparison'
    summary['partitions'] = {name: partition_info(part) for name, part in
                             [('train', train), ('calibration', calibration), ('test_resolved', test_known)]}
    summary['results'] = {}
    for name, columns in [('price_only', COLUMNS), ('price_plus_news', COLUMNS + NEWS_COLUMNS)]:
        with threadpool_limits(limits=2):
            model = fit_estimator(factories()['extra_trees'], train[columns], train.target, date_weights(train))
            calibrator = LogisticRegression(C=1., solver='liblinear', max_iter=1000, random_state=42)
            calibrator.fit(to_logits(model.predict_proba(calibration[columns])[:, 1]), calibration.target,
                           sample_weight=date_weights(calibration))
            scored = test.copy()
            scored['probability'] = calibrator.predict_proba(to_logits(model.predict_proba(test[columns])[:, 1]))[:, 1]
        evaluated = scored[scored.target.notna()]
        picks = (scored[scored.probability.ge(.6)].sort_values(['signal_date', 'probability', 'stock_code'],
                 ascending=[True, False, True]).groupby('signal_date', sort=False).head(5))
        resolved_picks = picks[picks.target.notna()]
        summary['results'][name] = dict(input_candidates=len(test), evaluated_cases=len(evaluated),
            date_brier=float(brier_score_loss(evaluated.target, evaluated.probability, sample_weight=date_weights(evaluated))),
            selected_cases=len(picks), selected_dates=int(picks.signal_date.nunique()),
            unresolved_selected=int(picks.target.isna().sum()),
            conditional_selected_success_rate=float(resolved_picks.target.mean()) if len(resolved_picks) else None,
            conditional_mean_net_return=float(resolved_picks.net_return_proxy.mean()) if len(resolved_picks) else None)
    return summary


def run_shadow(data_root, archive, output, as_of):
    articles, requests, manifests = read_archive(archive)
    # No archive dates before the first real observation may become synthetic zero-news training rows.
    first_day = (pd.Timestamp(min(m['observed_at'] for m in manifests)).tz_convert('Asia/Seoul').tz_localize(None).normalize()
                 if manifests else None)
    if first_day is not None and first_day <= pd.Timestamp(as_of):
        inputs, _ = load_inputs(data_root, as_of)
        cohort, _ = build_next_open_dataset(inputs, as_of)
        cohort = cohort[cohort.signal_date.ge(first_day)].copy()
    else:
        cohort = pd.DataFrame(columns=['stock_code', 'signal_date', 'target'] + COLUMNS)
    frame = add_news_features(cohort, articles, requests)
    summary = compare_news(frame)
    summary.update(generated_at=datetime.now(timezone.utc).isoformat(), as_of=str(as_of),
                   archive_batches=len(manifests), archived_headlines=len(articles),
                   linked_headlines=sum(bool(row['stock_codes']) for row in articles),
                   global_headlines=sum(row['topic'] != 'company' for row in articles),
                   social_media_collected=False,
                   news_archive_sha256=hashlib.sha256(json.dumps(manifests, sort_keys=True).encode()).hexdigest(),
                   implementation_sha256=hashlib.sha256(Path(__file__).read_bytes() +
                       (ROOT / 'src/features/news_learning.py').read_bytes()).hexdigest())
    write_json(summary, output)
    return summary


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data-root', type=Path, required=True)
    parser.add_argument('--archive', type=Path, default=ROOT / 'data/news_learning')
    parser.add_argument('--as-of', required=True)
    parser.add_argument('--output', type=Path, default=ROOT / 'reports/daily_review/news_learning_status.json')
    args = parser.parse_args()
    result = run_shadow(args.data_root, args.archive, args.output, args.as_of)
    print(json.dumps({key: result[key] for key in ['status', 'mature_news_rows', 'mature_news_dates', 'recommendation_enabled']}))


if __name__ == '__main__':
    main()
