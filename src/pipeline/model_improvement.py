"""Prespecified prospective champion/challenger learning, not self-modifying code."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re

import numpy as np
import pandas as pd

from src.crawler.market_clock import KST, completed_price_cutoff
from src.evaluator.forward_price_forecast import valid_record_time
from src.evaluator.reliability_goal import certify_goal, date_block_bounds
from src.features.next_open_dataset import TARGET_VERSION, build_next_open_dataset
from src.models.improvement_families import BASELINE, FAMILIES, family_spec
from src.models.monthly_price_walkforward import monthly_split
from src.models.next_open_price_model import fit_current, grade, implementation_digest, load_inputs, load_model, predict_probability
from src.models.relative_price_selection import rank_candidates
from src.models.selected_price_model import COLUMNS, ROOT, fit_data_digest, write_json

PROTOCOL_PATH = ROOT / 'docs/model_experiments/model_improvement_20261029.json'
ARCHIVE = ROOT / 'data/model_improvement/originals'
SCHEMA = 'model_improvement_original_v1'
NAME = re.compile(r'model_improvement_[0-9]{8}_[0-9a-f]{16}\.csv')
SAFE_MODEL = ['dataset_sha256', 'trained_at', 'as_of', 'target_version', 'baseline_probability', 'model_family']
PINNED_FILES = {
    'requirements-ml.txt', 'src/models/improvement_families.py', 'src/pipeline/model_improvement.py',
    'src/models/next_open_price_model.py', 'src/pipeline/next_open_learning_cycle.py',
    'src/evaluator/reliability_goal.py', 'src/evaluator/forward_price_forecast.py',
    'src/features/next_open_dataset.py', 'src/features/price_learning_dataset.py',
    'src/features/ohlcv_information.py', 'src/models/selected_price_model.py',
    'src/models/price_forecaster.py', 'src/models/monthly_price_walkforward.py',
}


def digest_json(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, allow_nan=False).encode()).hexdigest()


def load_protocol(path=PROTOCOL_PATH):
    protocol = json.loads(Path(path).read_text())
    goal_path = ROOT / protocol['goal_file']
    if (protocol['schema'] != 'model_improvement_protocol_v1' or protocol['families'] != FAMILIES
            or protocol['target_version'] != TARGET_VERSION or protocol['features'] != COLUMNS
            or protocol['threshold'] != .6 or protocol['daily_cap'] != 5
            or protocol['minimum_candidates'] != 100 or protocol['pairwise_comparison_budget'] != 12
            or protocol['paired_outcome_coverage'] != .99 or protocol['automatic_orders'] is not False
            or set(protocol['source_hashes']) != PINNED_FILES
            or protocol['automatic_recommendation_activation'] is not False
            or protocol['goal_sha256'] != hashlib.sha256(goal_path.read_bytes()).hexdigest()):
        raise ValueError('Self-improvement protocol changed; never relax a gate after outcomes.')
    registered = pd.Timestamp(protocol['registered_at'])
    if registered.tzinfo is None:
        raise ValueError('A prospective registration timestamp is required.')
    for relative, digest in protocol['source_hashes'].items():
        path = ROOT / relative
        if path.resolve().is_relative_to(ROOT) is False or hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            raise ValueError('Registered implementation changed: ' + relative)
    goal = json.loads(goal_path.read_text())
    if (goal['success_rate_minimum'] < .6 or goal['success_lower_minimum'] < .6
            or goal['minimum_signal_dates'] < 60 or goal['minimum_evaluated_cases'] < 300
            or goal['minimum_outcome_coverage'] != 1 or goal['minimum_issue_date_coverage'] < .5
            or goal['minimum_net_return_lower'] < 0 or goal['minimum_benchmark_excess_lower'] < 0
            or goal['confidence_alpha'] > .05 or goal['maximum_policy_families'] > 8
            or goal['bootstrap_block_sessions'] != 5):
        raise ValueError('User-agreed conservative quality gates cannot be weakened.')
    goal['registered_policy_ids'] = goal['registered_policy_ids'] + [name for name in FAMILIES if name != BASELINE]
    goal['certification_signal_start'] = str(registered.tz_convert(KST).date())
    if len(set(goal['registered_policy_ids'])) != len(goal['registered_policy_ids']) or len(goal['registered_policy_ids']) > goal['maximum_policy_families']:
        raise ValueError('The preregistered family budget is exhausted.')
    return protocol, goal


def selection(frame, probability):
    candidate = frame[['stock_code', 'signal_date']].copy()
    candidate['probability'] = np.asarray(probability, dtype=float)
    return candidate.index.isin(rank_candidates(candidate[candidate.probability.ge(.6)], 'probability', 5).index)


def validate_trial_frame(frame, manifest, protocol):
    frame = frame.copy()
    frame['signal_date'] = pd.to_datetime(frame.signal_date, format='mixed')
    if (len(frame) < protocol['minimum_candidates'] or len(frame) != manifest['candidate_count']
            or frame.stock_code.duplicated().any() or frame.signal_date.nunique() != 1
            or str(frame.signal_date.iloc[0].date()) != manifest['signal_date']
            or frame.signal_date.dt.tz is not None
            or not frame.signal_date.equals(frame.signal_date.dt.normalize())
            or not frame.stock_code.str.fullmatch(r'[0-9A-Z]{6}').all()
            or not np.isfinite(frame.origin_close).all() or frame.origin_close.le(0).any()
            or set(manifest['models']) != set(FAMILIES)):
        raise ValueError('Incomplete or conflicting common candidate pool.')
    recorded = pd.Timestamp(manifest['recorded_at'])
    if (recorded.tzinfo is None or recorded < pd.Timestamp(protocol['registered_at'])
            or not valid_record_time(frame.signal_date.iloc[0], recorded)):
        raise ValueError('An original was not recorded prospectively.')
    for name, metadata in manifest['models'].items():
        probability = pd.to_numeric(frame[name + '_probability'], errors='raise')
        flags = frame[name + '_selected'].map({True: True, False: False, 'True': True, 'False': False})
        if (set(metadata) != set(SAFE_MODEL) or metadata['model_family'] != name
                or metadata['target_version'] != TARGET_VERSION
                or not re.fullmatch(r'[0-9a-f]{64}', metadata['dataset_sha256'])
                or not 0 <= metadata['baseline_probability'] <= 1
                or not np.isfinite(probability).all() or not probability.between(0, 1).all()
                or flags.isna().any() or not np.array_equal(flags, selection(frame, probability))
                or pd.Timestamp(metadata['trained_at']).tzinfo is None
                or pd.Timestamp(metadata['trained_at']) > recorded
                or pd.Timestamp(metadata['as_of']) > frame.signal_date.iloc[0]):
            raise ValueError('Invalid original model timing, probability or fixed selection.')
        frame[name + '_selected'] = flags.astype(bool)
    return frame


def read_trials(archive, protocol):
    archive = Path(archive)
    paths = sorted(archive.glob('*.csv'))
    if set(p.stem for p in paths) != set(p.name.removesuffix('.manifest.json') for p in archive.glob('*.manifest.json')):
        raise ValueError('Incomplete self-improvement originals.')
    batches = []
    for path in paths:
        if not NAME.fullmatch(path.name) or path.stat().st_size > 2_000_000:
            raise ValueError('Invalid or oversized self-improvement original.')
        manifest_path = path.with_suffix('.manifest.json')
        if manifest_path.stat().st_size > 100_000:
            raise ValueError('Oversized self-improvement provenance.')
        manifest = json.loads(manifest_path.read_text())
        if (manifest['schema'] != SCHEMA or manifest['ledger_file'] != path.name
                or manifest['sha256'] != hashlib.sha256(path.read_bytes()).hexdigest()
                or manifest['protocol_sha256'] != digest_json(protocol)
                or set(manifest['models']) != set(FAMILIES)):
            raise ValueError('Self-improvement original/protocol checksum mismatch.')
        frame = validate_trial_frame(pd.read_csv(path, dtype={'stock_code': str}), manifest, protocol)
        recorded = pd.Timestamp(manifest['recorded_at'])
        batches.append((recorded, path.name, frame, manifest))
    chosen, dates, later = [], set(), 0
    for _, _, frame, manifest in sorted(batches, key=lambda row: (row[0], row[1])):
        day = manifest['signal_date']
        if day in dates:
            later += 1
        else:
            chosen.append((frame, manifest))
            dates.add(day)
    return chosen, later


def grade_trials(batches, inputs, as_of, now):
    results = {}
    for name in FAMILIES:
        parts = []
        for frame, manifest in batches:
            m = manifest['models'][name]
            part = frame[['stock_code', 'signal_date', 'origin_close']].copy()
            part['probability_above_cost'] = frame[name + '_probability']
            part['fixed_policy_selected'] = frame[name + '_selected']
            part['recorded_at'], part['model_trained_at'] = manifest['recorded_at'], m['trained_at']
            part['model_dataset_sha256'], part['validation_base_rate'] = m['dataset_sha256'], m['baseline_probability']
            part['target_version'], part['horizon_sessions'], part['cost_assumption'] = TARGET_VERSION, 5, .003
            part['prediction_id'] = [hashlib.sha256((manifest['sha256'] + name + code).encode()).hexdigest()[:24] for code in part.stock_code]
            parts.append(part)
        if not parts:
            results[name] = pd.DataFrame()
            continue
        original = pd.concat(parts, ignore_index=True)
        graded, _ = grade(original, inputs, as_of, now)
        current = graded.merge(inputs[['stock_code', 'signal_date', 'close']], on=['stock_code', 'signal_date'], how='left', validate='1:1')
        graded['origin_price_revised'] = ~np.isclose(current.origin_close, current.close, rtol=1e-7, atol=1e-4)
        results[name] = graded
    return results


def paired_advantage(candidate, reference, calendar, goal_status, protocol, goal):
    result = dict(passed=False, daily_brier_improvement=None, lower=None, dates=0, outcome_coverage=None)
    look = goal_status['certification_look']
    if look is None:
        return result
    counts = candidate[candidate.fixed_policy_selected.astype(bool)].groupby('signal_date').size().sort_index().cumsum()
    end = counts[counts.ge(look)].index[0]
    a = candidate[candidate.signal_date.le(end)].copy().sort_values(['signal_date', 'stock_code']).reset_index(drop=True)
    b = reference[reference.signal_date.le(end)].copy().sort_values(['signal_date', 'stock_code']).reset_index(drop=True)
    if not a[['stock_code', 'signal_date', 'target']].equals(b[['stock_code', 'signal_date', 'target']]):
        raise ValueError('Champion/challenger comparison must use identical candidate outcomes.')
    known = a.target.notna()
    result['outcome_coverage'] = float(known.mean())
    daily = pd.DataFrame(dict(signal_date=a.loc[known, 'signal_date'],
        advantage=(b.loc[known, 'probability_above_cost'] - a.loc[known, 'target']) ** 2
                  - (a.loc[known, 'probability_above_cost'] - a.loc[known, 'target']) ** 2)).groupby('signal_date').advantage.mean()
    dates = pd.DatetimeIndex(calendar)
    dates = dates[(dates >= pd.Timestamp(goal['certification_signal_start'])) & (dates <= end)]
    daily = daily.reindex(dates)
    result['dates'] = int(daily.notna().sum())
    if result['dates'] < goal['minimum_signal_dates'] or result['outcome_coverage'] < protocol['paired_outcome_coverage']:
        return result
    number = goal['certification_case_looks'].index(look) + 1
    alpha = goal['confidence_alpha'] / protocol['pairwise_comparison_budget'] / (number * (number + 1))
    lower = date_block_bounds(daily.to_numpy(), alpha, block=goal['bootstrap_block_sessions'])
    result.update(daily_brier_improvement=float(daily.mean()), lower=lower, one_sided_alpha=alpha,
                  passed=lower is not None and lower > 0)
    return result


def choose_family(graded, calendar, goal, protocol, benchmark, now, previous=BASELINE):
    previous = previous if previous in FAMILIES else BASELINE
    goals, comparisons, eligible = {}, {}, []
    for name in FAMILIES:
        if name == BASELINE:
            continue
        frame = graded[name]
        status = certify_goal(frame, calendar, 'fixed_policy_selected', goal, now,
                              'hash_verified_timely_originals', name, benchmark)
        if not frame.empty and frame.origin_price_revised.any():
            status['goal_passed'] = False
            status['status'] = 'price_revision_requires_review'
            status['reasons'].append('original_signal_prices_revised')
        goals[name] = status
        if status['goal_passed']:
            paired = paired_advantage(frame, graded[BASELINE], calendar, status, protocol, goal)
            comparisons[name + '_vs_baseline'] = paired
            if paired['passed']:
                eligible.append(name)
    active = previous if previous in eligible else BASELINE
    replacements = []
    for name in eligible:
        if name == active:
            continue
        if active == BASELINE:
            replacements.append(name)
        else:
            paired = paired_advantage(graded[name], graded[active], calendar, goals[name], protocol, goal)
            comparisons[name + '_vs_incumbent'] = paired
            if paired['passed']:
                replacements.append(name)
    if replacements:
        active = max(replacements, key=lambda name: (comparisons[name + '_vs_baseline']['lower'], name))
    action = 'retain' if active == previous else 'rollback' if active == BASELINE else 'promote'
    return dict(schema='model_improvement_status_v1', generated_at=now.isoformat(),
        status='validated_challenger_active' if active != BASELINE else 'collecting_forward_evidence',
        active_family=active, previous_family=previous, action=action, protocol_sha256=digest_json(protocol),
        challenger_count=len(FAMILIES) - 1, candidate_goals=goals, comparisons=comparisons,
        automatic_model_replacement=True, recommendation_enabled=False, automatic_orders=False)


def permitted_serving_family(decision, price_date):
    name = decision.get('active_family', BASELINE)
    if name == BASELINE:
        return BASELINE
    evidence = decision.get('candidate_goals', {}).get(name, {})
    paired = decision.get('comparisons', {}).get(name + '_vs_baseline', {})
    lower = evidence.get('success_lower')
    if (name not in FAMILIES or decision.get('price_date') != str(pd.Timestamp(price_date).date())
            or not re.fullmatch(r'[0-9a-f]{64}', str(decision.get('protocol_sha256', '')))
            or evidence.get('goal_passed') is not True or paired.get('passed') is not True
            or evidence.get('evaluated_cases', 0) < 300 or evidence.get('selected_signal_dates', 0) < 60
            or not isinstance(lower, (int, float)) or not np.isfinite(lower) or lower < .6):
        raise ValueError('A nonbaseline serving model needs a fresh, passing prospective audit.')
    return name


def audit_improvement(data_root, benchmark_root, archive, protocol_path, report_path, now=None):
    now = now or datetime.now(KST)
    protocol, goal = load_protocol(protocol_path)
    inputs, _ = load_inputs(data_root, completed_price_cutoff(now))
    batches, later = read_trials(archive, protocol)
    graded = grade_trials(batches, inputs, completed_price_cutoff(now), now)
    calendar = pd.DatetimeIndex(sorted(inputs.signal_date.unique()))
    from src.report_generator.reliability_goal_report import exact_benchmark
    benchmark = exact_benchmark(benchmark_root, calendar, goal['benchmark_source_id'])
    previous = BASELINE
    report_path = Path(report_path)
    if report_path.exists():
        old = json.loads(report_path.read_text())
        if old.get('protocol_sha256') == digest_json(protocol):
            previous = old.get('active_family', BASELINE)
    result = choose_family(graded, calendar, goal, protocol, benchmark, now, previous)
    result.update(original_batches=len(batches), later_batches_excluded=later,
                  price_date=str(calendar.max().date()),
                  original_sha256=[manifest['sha256'] for _, manifest in batches])
    write_json(result, report_path)
    return result


def freeze_trials(forecasts, metadata, protocol, archive, now):
    origin = forecasts.signal_date.max()
    if (not valid_record_time(origin, pd.Timestamp(now))
            or not valid_record_time(origin, pd.Timestamp(now) + pd.Timedelta(seconds=60))
            or pd.Timestamp(now) < pd.Timestamp(protocol['registered_at'])):
        raise ValueError('Outside prospective trial recording window; never backdate.')
    archive = Path(archive)
    archive.mkdir(parents=True, exist_ok=True)
    existing, _ = read_trials(archive, protocol)
    if any(manifest['signal_date'] == str(origin.date()) for _, manifest in existing):
        return 'original_batch_preserved'
    safe = {name: {key: data[key] for key in SAFE_MODEL} for name, data in metadata.items()}
    identity = digest_json(dict(models=safe, protocol=digest_json(protocol)))[:16]
    path = archive / f'model_improvement_{origin:%Y%m%d}_{identity}.csv'
    payload = forecasts.to_csv(index=False).encode('utf-8')
    if len(payload) > 2_000_000:
        raise ValueError('Oversized model-improvement forecast batch.')
    manifest = dict(schema=SCHEMA, ledger_file=path.name, sha256=hashlib.sha256(payload).hexdigest(),
                    protocol_sha256=digest_json(protocol), recorded_at=now.isoformat(),
                    signal_date=str(origin.date()), candidate_count=len(forecasts), models=safe)
    validate_trial_frame(forecasts, manifest, protocol)
    with path.open('xb') as target:
        target.write(payload)
    with path.with_suffix('.manifest.json').open('x') as target:
        json.dump(manifest, target, indent=2, allow_nan=False)
        target.write('\n')
    read_trials(archive, protocol)
    return 'new_prospective_batch_recorded'


def record_challengers(data_root, state_dir, archive, protocol_path=PROTOCOL_PATH, core_model_dir=None, now=None):
    live_clock = now is None
    clock = now or datetime.now(KST)
    protocol, _ = load_protocol(protocol_path)
    inputs, _ = load_inputs(data_root, completed_price_cutoff(clock))
    origin = inputs.signal_date.max()
    batches, _ = read_trials(archive, protocol)
    if any(m['signal_date'] == str(origin.date()) for _, m in batches):
        return dict(recording='original_batch_preserved', trained_families=0, candidate_count=len(batches[-1][0]))
    latest = inputs[inputs.signal_date.eq(origin) & inputs.volume.gt(0) & np.isfinite(inputs[COLUMNS]).all(axis=1)].copy().sort_values('stock_code').reset_index(drop=True)
    if len(latest) < protocol['minimum_candidates']:
        raise ValueError('Do not replace a broad comparison with a smaller pool.')
    cohort, _ = build_next_open_dataset(inputs, origin)
    known = cohort[cohort.target.notna()]
    frame, models = latest[['stock_code', 'signal_date', 'close']].rename(columns={'close': 'origin_close'}).copy(), {}
    core = load_model(core_model_dir) if core_model_dir is not None and (Path(core_model_dir) / 'latest.json').exists() else None
    trained = 0
    for name in FAMILIES:
        spec = family_spec(name)
        train, calibration = monthly_split(known, origin, spec['training_sessions'], spec['calibration_sessions'])
        digest = fit_data_digest(train, calibration, COLUMNS)
        destination = Path(state_dir) / name
        cached = load_model(destination) if (destination / 'latest.json').exists() else None
        bundle = None
        for candidate in [core, cached]:
            if (candidate is not None and candidate['metadata'].get('model_family', BASELINE) == name
                    and candidate['metadata']['dataset_sha256'] == digest
                    and candidate['metadata'].get('implementation_sha256') == implementation_digest()):
                bundle = candidate
                break
        if bundle is None:
            print('Training registered forward challenger: ' + name, flush=True)
            fit_current(data_root, destination, origin, family=name)
            bundle = load_model(destination)
            trained += 1
        models[name] = bundle['metadata'] | {'model_family': name}
        frame[name + '_probability'] = predict_probability(bundle, latest)
        frame[name + '_selected'] = selection(frame, frame[name + '_probability'])
        from src.pipeline.ml_beta_release import compact_cached_models
        compact_cached_models(state_dir, destination)
    if live_clock:
        clock = datetime.now(KST)
    if valid_record_time(origin, pd.Timestamp(clock)):
        state = freeze_trials(frame, models, protocol, archive, clock)
    else:
        state = 'outside_recording_window_models_prepared_only'
    return dict(recording=state, trained_families=trained, candidate_count=len(frame))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data-root', type=Path, required=True)
    parser.add_argument('--benchmark-root', type=Path)
    parser.add_argument('--state-dir', type=Path, default=ROOT / 'data/ml_beta_state/challengers')
    parser.add_argument('--archive', type=Path, default=ARCHIVE)
    parser.add_argument('--protocol', type=Path, default=PROTOCOL_PATH)
    parser.add_argument('--report', type=Path, default=ROOT / 'reports/daily_review/model_improvement_status.json')
    args = parser.parse_args()
    status = audit_improvement(args.data_root, args.benchmark_root, args.archive, args.protocol, args.report)
    recording = record_challengers(args.data_root, args.state_dir, args.archive, args.protocol)
    status.update(recording)
    write_json(status, args.report)
    print(json.dumps({key: status[key] for key in ['status', 'active_family', 'action', 'recording', 'trained_families']}))


if __name__ == '__main__':
    main()
