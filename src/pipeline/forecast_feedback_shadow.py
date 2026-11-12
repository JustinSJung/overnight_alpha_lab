"""Freeze and grade a research-only error learner alongside the unchanged daily forecaster."""
import hashlib
import json
import os
from pathlib import Path
import tempfile

import pandas as pd

from src.crawler.market_clock import KST, completed_price_cutoff
from src.evaluator.forward_price_forecast import valid_record_time
from src.models import forecast_error_feedback as learner
from src.models.forecast_error_feedback import PROB, describe_base, fit_feedback, predict_feedback, prepare
from src.models.selected_price_model import ROOT, write_json


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()).hexdigest()


def identity(frame):
    return digest(list(frame[['prediction_id', 'stock_code', PROB, 'validation_base_rate', 'recorded_at']]
                       .itertuples(index=False, name=None)))


def seal(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=path.parent, delete=False, mode='w') as tmp:
        name = tmp.name
        try:
            json.dump(dict(payload=payload, sha256=digest(payload)), tmp, allow_nan=False, separators=(',', ':'))
            tmp.flush()
            os.link(name, path)  # Atomic first writer wins, never replace an earlier forecast.
        finally:
            os.unlink(name)


def load_batch(path, frame, version, now):
    record = json.loads(path.read_text())
    b = record['payload']
    issue = pd.Timestamp(b['issued_at'])
    day = pd.Timestamp(b['price_date'])
    if (record['sha256'] != digest(b) or b['version'] != version or issue > now
            or path.stem != str(day.date()) or not valid_record_time(day, issue)
            or frame.empty or not frame.signal_date.eq(day).all()
            or b['originals'] != identity(frame) or len(b['predictions']) != len(frame)
            or issue < pd.to_datetime(frame.recorded_at, utc=True).max()
            or not pd.Series(b['predictions']).between(0., 1.).all()):
        raise ValueError('Feedback batch is not a timely, unchanged match to the original pool.')
    return frame.assign(shadow=b['predictions'])


def comparison(cohort):
    scores = {}
    for col in (PROB, 'shadow', 'validation_base_rate'):
        obs = cohort.dropna(subset=['target'])
        daily_brier = (obs[col] - obs.target).pow(2).groupby(obs.signal_date).mean()
        scores[col] = dict(date_brier=float(daily_brier.mean()) if len(daily_brier) else None)
        if col != 'validation_base_rate':
            ranked = cohort.sort_values(['signal_date', col, 'stock_code'], ascending=[True, False, True])
            for name, pool in [('top_5', ranked), ('at_least_60pct_top_5', ranked[ranked[col].ge(.6)])]:
                picked = pool.groupby('signal_date').head(5)
                scores[col][name] = dict(issued=len(picked), resolved=int(picked.target.count()),
                                         success_count=int(picked.target.eq(1).sum()),
                                         hit_rate=float(picked.target.mean()) if picked.target.count() else None)
    return dict(issued=len(cohort), resolved=int(cohort.target.count()),
                resolved_dates=int(cohort.dropna(subset=['target']).signal_date.nunique()), models=scores)


def run(rows, price_date, archive, now=None):
    clock = (lambda: pd.Timestamp.now(tz=KST)) if now is None else lambda: pd.Timestamp(now)
    origin = pd.Timestamp(price_date)
    if origin.date() > completed_price_cutoff(clock()):
        raise ValueError('Cannot learn from uncompleted prices.')
    f = prepare(rows, origin).sort_values('prediction_id')
    state = fit_feedback(f, origin)
    archive = Path(archive)
    version = digest([hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in (learner.__file__, __file__)])
    groups = {str(k.date()): v for k, v in f.groupby('signal_date')}
    pairs = []
    for path in sorted(archive.glob('*.json')):
        if path.stem not in groups:
            raise ValueError('Missing original cohort for archived feedback predictions.')
        pairs.append(load_batch(path, groups[path.stem], version, clock()))
    latest = groups.get(price_date)
    dest = archive / (price_date + '.json')
    if dest.exists():
        recording = 'first_batch_preserved'
    elif latest is None:
        recording = 'no_timely_primary_original'
    elif not state['ready']:
        recording = 'insufficient_mature_training_dates'
    else:
        probs = predict_feedback(latest, state).tolist()
        issue = clock()
        if (not valid_record_time(origin, issue) or not valid_record_time(origin, issue + pd.Timedelta(minutes=1))
                or pd.to_datetime(latest.recorded_at, utc=True).max() > issue):
            recording = 'outside_recording_window'
        else:
            batch = dict(version=version, price_date=price_date, issued_at=issue.isoformat(),
                         originals=identity(latest), trained_through=state['latest_label'], predictions=probs)
            seal(dest, batch)
            pairs.append(load_batch(dest, latest, version, clock()))
            recording = 'new_prospective_shadow'
    paired = pd.concat(pairs) if pairs else f.iloc[:0].assign(shadow=pd.Series(dtype=float))
    return dict(schema='forecast_error_feedback_v1', price_date=price_date, version=version,
                recording=recording, training={k: state[k] for k in ('dates', 'cases', 'latest_label', 'ready', 'offset')},
                base_diagnostics=describe_base(f), prospective=comparison(paired),
                automatic_promotion=False, recommendation_enabled=False)


def main():
    publication = json.loads((ROOT / 'docs/price_model.json').read_text())
    generated = pd.Timestamp(publication['generated_at'])
    now = pd.Timestamp.now(tz=KST)
    if generated.tzinfo is None or not pd.Timedelta(0) <= now - generated <= pd.Timedelta(hours=4):
        raise ValueError('Expected the current ML Beta publication.')
    day = generated.tz_convert(KST).strftime('%Y%m%d')
    rows = pd.read_csv(ROOT / f'data/predictions/ml_next_open_system_evaluation_{day}.csv',
                       dtype={'stock_code': str, 'prediction_id': str}, float_precision='round_trip')
    if len(rows) != publication['forward']['recorded'] or rows.target.count() != publication['forward']['resolved']:
        raise ValueError('Graded originals do not match current publication.')
    report = run(rows, publication['price_date'], ROOT / 'data/forecast_feedback/v1')
    write_json(report, ROOT / 'reports/daily_review/forecast_feedback_status.json')
    print(json.dumps({k: report[k] for k in ('price_date', 'recording', 'training')}))


if __name__ == '__main__':
    main()
