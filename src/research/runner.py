"""Offline research coordinator; immutable memory, bounded trials, no live routing."""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

from src.crawler.market_clock import completed_price_cutoff
from src.research.memory import append_event, digest, locked_memory, read_memory
from src.research.programs import canonical, program_id, propose, validate_program

ROOT = Path(__file__).resolve().parents[2]
POLICY_PATH = ROOT / 'docs/model_experiments/algorithm_research_v1.json'
MEMORY = ROOT / 'data/algorithm_research'
STATUS = ROOT / 'reports/daily_review/algorithm_research_status.json'
REPORT = ROOT / 'reports/daily_review/algorithm_research_report.md'


def load_policy():
    policy = json.loads(POLICY_PATH.read_text())
    expected = dict(schema='offline_algorithm_research_v1',
                    proposal_mode='memory_guided_numerical_program_search',
                    training_sessions=252, calibration_sessions=60, folds=3, screen_sessions=20,
                    horizon_sessions=5, cost_assumption=.003, probability_threshold=.6, daily_selection_cap=5,
                    max_trials_per_snapshot=2, max_trials_total=120, worker_timeout_seconds=300,
                    paid_api_calls=False, production_promotion=False, recommendation_enabled=False,
                    automatic_orders=False)
    if canonical(policy) != canonical(expected):
        raise ValueError('Research protocol changed; explicit review and registration are required.')
    return policy


def implementation_fingerprint():
    paths = ['src/research/programs.py', 'src/research/memory.py', 'src/research/evaluation.py',
             'src/research/runner.py', 'src/models/selected_price_model.py',
             'src/models/next_open_price_model.py', 'src/models/price_forecaster.py',
             'src/models/monthly_price_walkforward.py', 'src/features/next_open_dataset.py',
             'src/features/price_learning_dataset.py', 'src/features/completed_price_dataset.py',
             'src/features/ohlcv_information.py', 'requirements-ml.txt']
    return {path: hashlib.sha256((ROOT / path).read_bytes()).hexdigest() for path in paths}


def context(events):
    trials = [event['payload'] for event in events if event['kind'] == 'trial']
    complete = [row for row in trials if row['status'] == 'completed']
    ranked = sorted(complete, key=lambda row: (-row['metrics']['development_brier_improvement'], row['program_id']))
    reasons = Counter(reason for row in complete for reason in row['metrics']['screen_reasons'])
    return dict(mode='offline_program_search_not_llm_reasoning',
                trials_reserved=sum(event['kind'] == 'proposal' for event in events),
                trials_completed=len(complete), trials_failed=sum(row['status'] != 'completed' for row in trials),
                trials_incomplete=sum(event['kind'] == 'proposal' for event in events) - len(trials),
                research_screen_passed=sum(row['metrics']['research_screen_passed'] for row in complete),
                common_failures=dict(reasons.most_common()),
                promising_programs=[dict(program_id=row['program_id'], program=row['program'],
                                         development_brier_improvement=row['metrics']['development_brier_improvement'])
                                    for row in ranked[:5]],
                production_promotion=False, recommendation_enabled=False)


def write_status(events, phase, output=STATUS, report=REPORT):
    memory = context(events)
    data = dict(schema='algorithm_research_status_v1', generated_at=datetime.now(timezone.utc).isoformat(),
                status=phase, llm_enabled=False, paid_api_calls=False, future_validation_required=True,
                automatic_orders=False, **{key: memory[key] for key in [
                    'trials_reserved', 'trials_completed', 'trials_failed', 'trials_incomplete', 'research_screen_passed',
                    'production_promotion', 'recommendation_enabled']})
    for destination in [Path(output), Path(report)]:
        if destination.is_symlink():
            raise ValueError('Unsafe research publication path.')
        destination.parent.mkdir(parents=True, exist_ok=True)
    Path(output).write_text(json.dumps(data, ensure_ascii=False, indent=2, allow_nan=False) + '\n')
    lines = ['# Algorithm Research / 알고리즘 연구', '',
             'RESEARCH_ONLY. Offline program search, not autonomous LLM reasoning or verified investment performance.', '',
             '운영 모델과 분리된 연구입니다. 유료 API 호출과 LLM 연결은 없으며 추천·자동 주문은 하지 않습니다.',
             '과거 개발 데이터는 반복 탐색에 사용됩니다. 점수가 좋아도 독립 검증이나 신뢰도 상승으로 해석할 수 없습니다.', '',
             '```json', json.dumps(data, ensure_ascii=False, indent=2), '```', '',
             '## Remembered Failures / 누적 실험의 한계', '',
             '```json', json.dumps(memory['common_failures'], ensure_ascii=False, indent=2), '```', '',
             '## Current Development Candidates / 다음 연구 후보', '',
             '| Program | Date Brier improvement vs matched control |', '|---|---:|']
    lines += [f"| {row['program_id'][:12]} | {row['development_brier_improvement']:.8f} |"
              for row in memory['promising_programs']]
    lines += ['', 'All attempts, including failures, consume the fixed 120-trial budget. '
              'The best development result is not a production approval. '
              'No candidate is inserted into the existing registered eight-family competition.', '',
              'New algorithms need separate prospective registration, multiplicity accounting, '
              'immutable forecasts and future evaluation before deployment. '
              'Existing production thresholds, confidence scores, candidate pools and forecast originals are unchanged.', '']
    Path(report).write_text('\n'.join(lines), encoding='utf-8')
    return data


def latest_history(cache):
    candidates = []
    for path in sorted(Path(cache).glob('snapshot_*/history_manifest.json')):
        if path.is_symlink() or path.stat().st_size > 5_000_000:
            raise ValueError('Unsafe cached research manifest.')
        manifest = json.loads(path.read_text())
        if manifest.get('collection_complete'):
            candidates.append((manifest['end'], path.parent))
    return max(candidates)[1] if candidates else None


def execute_trial(data_root, as_of, program, expected_manifest, timeout):
    """Only the trusted interpreter runs; generated data cannot import/execute code."""
    with tempfile.TemporaryDirectory(prefix='price-algorithm-research-') as temporary:
        folder = Path(temporary)
        candidate, result = folder / 'program.json', folder / 'result.json'
        candidate.write_text(canonical(program))
        environment = {key: os.environ[key] for key in ('PATH', 'SYSTEMROOT', 'TMPDIR') if key in os.environ}
        environment.update(PYTHONDONTWRITEBYTECODE='1', OPENBLAS_NUM_THREADS='2', OMP_NUM_THREADS='2',
                           LOKY_MAX_CPU_COUNT='2', HOME=temporary)
        try:
            run = subprocess.run([sys.executable, '-m', 'src.research.runner', '--worker',
                                  '--data-root', str(Path(data_root).resolve()), '--as-of', as_of,
                                  '--proposal', str(candidate), '--worker-output', str(result),
                                  '--expected-manifest', expected_manifest],
                                 cwd=ROOT, env=environment, capture_output=True, timeout=timeout, check=False)
        except subprocess.TimeoutExpired:
            return dict(status='failed', failure_type='worker_time_budget_exceeded')
        if run.returncode or not result.is_file() or result.stat().st_size > 30_000:
            return dict(status='failed', failure_type='worker_failed_or_invalid_output')
        outcome = json.loads(result.read_text())
        if (outcome.get('evidence') != 'reused_historical_development_only'
                or outcome.get('production_promotion') is not False
                or outcome.get('recommendation_enabled') is not False
                or outcome.get('future_validation_required') is not True):
            return dict(status='failed', failure_type='invalid_evidence_contract')
        canonical(outcome)
        return dict(status='completed', **outcome)


def run_research(data_root, state_dir=MEMORY, output=STATUS, report=REPORT, proposal=None):
    policy = load_policy()
    with locked_memory(state_dir) as events:
        registration = dict(policy=policy, implementation=implementation_fingerprint())
        if not events:
            append_event(state_dir, events, 'registration', registration)
        if events[0]['kind'] != 'registration' or events[0]['payload'] != registration:
            raise ValueError('Research implementation changed; preserve memory and request a reviewed migration.')
        if data_root is None:
            return write_status(events, 'waiting_for_price_history', output, report)
        manifest_path = Path(data_root) / 'history_manifest.json'
        manifest = json.loads(manifest_path.read_text())
        as_of = manifest['end']
        if (not manifest.get('collection_complete') or not manifest.get('completed_bars_only')
                or manifest.get('source') != 'kis_adjusted_daily' or as_of > completed_price_cutoff().isoformat()):
            raise ValueError('Research needs verified completed KIS history, never future bars.')
        source = hashlib.sha256(manifest_path.read_bytes()).hexdigest()
        reservations = [event['payload'] for event in events if event['kind'] == 'cycle_reserved']
        prior = [row for row in reservations if row['price_date'] == as_of]
        if prior:
            if prior[0]['source_sha256'] != source:
                raise ValueError('Previously researched input snapshot was revised; review instead of rerunning.')
            finished = any(event['kind'] == 'cycle_completed' and event['payload']['price_date'] == as_of for event in events)
            phase = 'snapshot_already_researched' if finished else 'interrupted_research_requires_review'
            return write_status(events, phase, output, report)
        reserved = sum(event['kind'] == 'proposal' for event in events)
        if reserved >= policy['max_trials_total']:
            return write_status(events, 'research_budget_requires_review', output, report)
        append_event(state_dir, events, 'cycle_reserved', dict(price_date=as_of, source_sha256=source))
        for _ in range(min(policy['max_trials_per_snapshot'], policy['max_trials_total'] - reserved)):
            number = sum(event['kind'] == 'proposal' for event in events)
            if proposal is not None:
                program, parent = validate_program(proposal), None
                if any(event['kind'] == 'proposal' and event['payload']['program_id'] == program_id(program) for event in events):
                    raise ValueError('This program was already attempted; failures cannot be erased or retried as new ideas.')
            else:
                program, parent = propose(events, seed=42 + number)
            identity = program_id(program)
            origin = 'imported_numerical_program' if proposal is not None else 'offline_memory_guided_search'
            record = dict(program=program, program_id=identity, parent_id=parent, origin=origin,
                          price_date=as_of, source_sha256=source,
                          memory_head=events[-1]['sha256'], trial_number=number + 1)
            append_event(state_dir, events, 'proposal', record)
            outcome = execute_trial(data_root, as_of, program, source, policy['worker_timeout_seconds'])
            append_event(state_dir, events, 'trial', dict(**record, **outcome))
            print(f"Research trial {number + 1}: {outcome['status']}", flush=True)
            if proposal is not None:
                break
        append_event(state_dir, events, 'cycle_completed', dict(price_date=as_of, source_sha256=source))
        return write_status(events, 'researching_not_production_validated', output, report)


def worker(args):
    import resource
    resource.setrlimit(resource.RLIMIT_CPU, (240, 245))
    if sys.platform == 'linux':
        resource.setrlimit(resource.RLIMIT_AS, (6 * 1024 ** 3, 6 * 1024 ** 3))
    from src.research.evaluation import evaluate_program
    manifest = args.data_root / 'history_manifest.json'
    if hashlib.sha256(manifest.read_bytes()).hexdigest() != args.expected_manifest:
        raise ValueError('Worker input manifest changed.')
    if args.proposal.stat().st_size > 20_000:
        raise ValueError('Oversized research proposal.')
    program = validate_program(json.loads(args.proposal.read_text()))
    result = evaluate_program(args.data_root, args.as_of, program, load_policy())
    if hashlib.sha256(manifest.read_bytes()).hexdigest() != args.expected_manifest:
        raise ValueError('Input prices changed during research.')
    args.worker_output.write_text(canonical(result))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', nargs='?', choices=['run', 'context'], default='run')
    parser.add_argument('--data-root', type=Path)
    parser.add_argument('--input-cache', type=Path, default=ROOT / 'data/ml_beta_state/prices')
    parser.add_argument('--state-dir', type=Path, default=MEMORY)
    parser.add_argument('--output', type=Path, default=STATUS)
    parser.add_argument('--report', type=Path, default=REPORT)
    parser.add_argument('--proposal', type=Path)
    parser.add_argument('--worker', action='store_true', help=argparse.SUPPRESS)
    parser.add_argument('--worker-output', type=Path, help=argparse.SUPPRESS)
    parser.add_argument('--expected-manifest', help=argparse.SUPPRESS)
    parser.add_argument('--as-of', help=argparse.SUPPRESS)
    args = parser.parse_args()
    try:
        if args.worker:
            worker(args)
        elif args.command == 'context':
            print(json.dumps(context(read_memory(args.state_dir)), ensure_ascii=False, indent=2))
        else:
            if args.proposal and args.proposal.stat().st_size > 20_000:
                raise ValueError('Oversized research proposal.')
            proposal = json.loads(args.proposal.read_text()) if args.proposal else None
            result = run_research(args.data_root or latest_history(args.input_cache), args.state_dir,
                                  args.output, args.report, proposal)
            print(json.dumps(result, ensure_ascii=False, indent=2))
    except Exception as error:
        print('Research stopped safely: ' + type(error).__name__ + '. Review retained research memory.', file=sys.stderr)
        raise SystemExit(1) from None


if __name__ == '__main__':
    main()
