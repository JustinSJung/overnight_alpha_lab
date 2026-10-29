"""Audit real original forecasts against the fixed reliability goal, without approval side effects."""
from __future__ import annotations

import argparse
from datetime import datetime
import hashlib
import json
from pathlib import Path
import re

import numpy as np
import pandas as pd

from src.crawler.market_clock import KST, completed_price_cutoff
from src.crawler.price_learning_history import reusable_entry
from src.evaluator.reliability_goal import certify_goal
from src.evaluator.research_shadow_ledger import grade_shadow
from src.features.next_open_dataset import valid_candle
from src.models.next_open_price_model import grade, load_inputs
from src.models.price_forecaster import json_text
from src.models.relative_price_selection import rank_candidates
from src.models.selected_price_model import ROOT, write_json
from src.pipeline.next_open_learning_cycle import collect_originals

PROFILES = {
    'neural_circuit_v1': ('ml_neural_circuit_forward_', 'neural_circuit', 'price_neural_circuit'),
    'swarm_circuit_v1': ('ml_swarm_circuit_forward_', 'swarm_circuit', 'price_swarm_circuit'),
    'selective_gate_v1': ('ml_selective_forward_', 'selective_gate', 'price_selective_gate'),
    'pairwise_rank_v1': ('ml_pairwise_forward_', 'pairwise_rank', 'price_pairwise_rank_current'),
}


def exact_benchmark(root, calendar, source_id):
    if root is None or not (Path(root) / 'history_manifest.json').exists():
        return None
    root = Path(root)
    m = json.loads((root / 'history_manifest.json').read_text())
    codes = {'069500', '229200'}
    if (not m.get('collection_complete') or not m.get('completed_bars_only')
            or set(m['requested_codes']) != codes or set(row['stock_code'] for row in m['stocks']) != codes):
        raise ValueError('The separate two-ETF benchmark snapshot is incomplete.')
    prices = {}
    for row in m['stocks']:
        if not reusable_entry(row, root / 'raw'):
            raise ValueError('Benchmark checksum or collection status failed.')
        frame = pd.read_csv(root / 'raw' / (row['stock_code'] + '.csv'))
        frame['date'] = pd.to_datetime(frame.date).dt.normalize()
        if frame.date.duplicated().any():
            raise ValueError('Duplicated benchmark session.')
        frame['valid'] = valid_candle(frame)
        prices[row['stock_code']] = frame.set_index('date')
    calendar = pd.DatetimeIndex(sorted(calendar))
    rows = []
    for i, day in enumerate(calendar[:-5]):
        entry, exit_day = calendar[i + 1], calendar[i + 5]
        returns = []
        for frame in prices.values():
            if entry not in frame.index or exit_day not in frame.index or not frame.loc[[entry, exit_day], 'valid'].all():
                break
            returns.append(float(frame.loc[exit_day, 'close'] / frame.loc[entry, 'open'] - 1))
        if len(returns) == 2:
            rows.append(dict(signal_date=day, entry_date=entry, exit_date=exit_day,
                             net_return=float(np.mean(returns) - .003), source=source_id))
    return pd.DataFrame(rows, columns=['signal_date', 'entry_date', 'exit_date', 'net_return', 'source'])


def shadow_originals(ledger_dir, prefix, model_root):
    identities = set()
    for path in Path(model_root).glob('runs/*/model_metadata.json'):
        m = json.loads(path.read_text())
        identities.add((m['dataset_sha256'], m['trained_at']))
    batches = []
    pattern = re.compile(re.escape(prefix) + r'[0-9]{8}_[0-9a-f]{16}\.csv')
    for path in Path(ledger_dir).glob(prefix + '*.csv'):
        if not pattern.fullmatch(path.name):
            continue
        if path.stat().st_size > 10_000_000:
            raise ValueError('Oversized original forecast.')
        frame = pd.read_csv(path, dtype={'stock_code': str})
        if (frame.empty or frame.signal_date.nunique() != 1 or frame.recorded_at.nunique() != 1
                or frame.model_dataset_sha256.nunique() != 1 or frame.model_trained_at.nunique() != 1
                or (frame.model_dataset_sha256.iloc[0], frame.model_trained_at.iloc[0]) not in identities):
            raise ValueError('Shadow original has no unique preserved model provenance.')
        manifest = json.loads(path.with_suffix('.manifest.json').read_text())
        if hashlib.sha256(path.read_bytes()).hexdigest() != manifest['sha256']:
            raise ValueError('Shadow original changed.')
        day = str(pd.Timestamp(frame.signal_date.iloc[0]).normalize().date())
        batches.append((pd.Timestamp(frame.recorded_at.iloc[0]), path.name, day, path))
    chosen, seen, excluded = [], set(), 0
    for _, _, day, path in sorted(batches):
        if day in seen:
            excluded += 1
        else:
            chosen.append(path)
            seen.add(day)
    return chosen, excluded


def report_goal(data_root, ledger_dir, benchmark_root, goal_path, public_output, report_path, now=None):
    now = now or datetime.now(KST)
    cutoff = completed_price_cutoff(now)
    inputs, _ = load_inputs(data_root, cutoff)
    calendar = pd.DatetimeIndex(sorted(inputs.signal_date.unique()))
    goal = json.loads(Path(goal_path).read_text())
    benchmark = exact_benchmark(benchmark_root, calendar, goal['benchmark_source_id'])
    reports = {}
    for policy in goal['registered_policy_ids']:
        evidence, exclusions, original_hashes = pd.DataFrame(), 0, {}
        if policy == 'next_open_current_v1':
            model_root = ROOT / 'data/models/price_next_open_current'
            registry_path = model_root / 'forward_registry.json'
            registry = json.loads(registry_path.read_text()) if registry_path.exists() else {}
            originals, hashes, exclusions = collect_originals(ledger_dir, model_root, registry)
            if not originals.empty:
                evidence, _ = grade(originals, inputs, cutoff, now)
                evidence['goal_selected'] = evidence.fixed_policy_selected
                original_hashes = hashes
        else:
            if policy not in PROFILES:
                raise ValueError('Registered policy has no audited original reader: ' + policy)
            prefix, family, model_name = PROFILES[policy]
            paths, exclusions = shadow_originals(ledger_dir, prefix, ROOT / 'data/models' / model_name)
            parts = []
            for path in paths:
                frame, _ = grade_shadow(path, inputs, cutoff, family, now)
                if policy == 'selective_gate_v1':
                    from src.models.selective_price_model import grade_selective
                    p = json.loads((ROOT / 'docs/model_experiments/selective_price_protocol_20261023.json').read_text())
                    frame, _ = grade_selective(path, inputs, cutoff, p, now)
                    frame['goal_selected'] = frame.matched_policy_learned_gate
                elif policy == 'pairwise_rank_v1':
                    from src.models.pairwise_price_model import grade_original
                    p = json.loads((ROOT / 'docs/model_experiments/pairwise_price_protocol_20261026.json').read_text())
                    frame, _ = grade_original(path, inputs, cutoff, p, now)
                    frame['goal_selected'] = frame.matched_policy_pairwise_cross_section
                else:
                    picks = rank_candidates(frame[frame.probability_above_cost.ge(.6)], 'probability_above_cost', 5)
                    frame['goal_selected'] = frame.index.isin(picks.index)
                parts.append(frame)
                original_hashes[path.name] = hashlib.sha256(path.read_bytes()).hexdigest()
            if parts:
                evidence = pd.concat(parts, ignore_index=True)
        status = certify_goal(evidence, calendar, 'goal_selected', goal, now,
                              'hash_verified_timely_originals', policy, benchmark)
        status['recorded_candidates'] = len(evidence)
        status['recorded_issue_dates'] = int(evidence.signal_date.nunique()) if len(evidence) else 0
        status['later_duplicate_batches_or_candidates_excluded'] = exclusions
        status['original_hashes'] = original_hashes
        if len(evidence) and 'origin_close' in evidence:
            reference = inputs[['stock_code', 'signal_date', 'close']]
            check = evidence.assign(signal_date=pd.to_datetime(evidence.signal_date)).merge(reference, on=['stock_code', 'signal_date'], how='left', validate='1:1')
            status['recorded_origin_price_revised_rows'] = int((~np.isclose(check.origin_close, check.close, rtol=1e-7, atol=1e-4)).sum())
        reports[policy] = status
    result = dict(schema='price_reliability_goal_report_v1', generated_at=now.isoformat(),
                  price_date=str(calendar.max().date()), goal=goal, policies=reports,
                  any_goal_passed=any(s['goal_passed'] for s in reports.values()),
                  automatic_promotion=False, automatic_orders=False,
                  limitations='Locally hash-checked original timestamps, not externally attested records. Block-independence and executable fill assumptions remain limitations.')
    write_json(result, report_path)
    primary = reports['next_open_current_v1']
    public = dict(schema='public_reliability_goal_v1', generated_at=now.isoformat(), price_date=result['price_date'],
                  target_success_rate=goal['success_rate_minimum'], target_lower=goal['success_lower_minimum'],
                  minimum_cases=goal['minimum_evaluated_cases'], minimum_dates=goal['minimum_signal_dates'],
                  primary_policy='next_open_current_v1', status=primary['status'], goal_passed=primary['goal_passed'],
                  evaluated_cases=primary['evaluated_cases'], selected_signal_dates=primary['selected_signal_dates'],
                  recorded_candidates=primary['recorded_candidates'], actual_success_rate=primary['pooled_success_rate'],
                  actual_success_lower=primary['success_lower'], recommendation_enabled=False)
    write_json(public, public_output)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data-root', type=Path, required=True)
    parser.add_argument('--ledger-dir', type=Path, default=ROOT / 'data/predictions')
    parser.add_argument('--benchmark-root', type=Path)
    parser.add_argument('--goal', type=Path, default=ROOT / 'docs/model_experiments/reliability_goal_20261026.json')
    parser.add_argument('--output', type=Path, default=ROOT / 'docs/reliability_goal.json')
    parser.add_argument('--report', type=Path, default=ROOT / 'reports/daily_review' / f'{datetime.now(KST):%Y-%m-%d}_reliability_goal_status.json')
    args = parser.parse_args()
    result = report_goal(args.data_root, args.ledger_dir, args.benchmark_root, args.goal, args.output, args.report)
    print(json_text(dict(price_date=result['price_date'], goal_passed=result['any_goal_passed'],
                        policies={name: {key: s[key] for key in ['status', 'evaluated_cases', 'selected_signal_dates', 'recorded_candidates']}
                                  for name, s in result['policies'].items()})))


if __name__ == '__main__':
    main()
