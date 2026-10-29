"""Refresh verified KIS history, learn and publish the unapproved price-model beta."""
from __future__ import annotations

import argparse
from datetime import datetime
import json
from pathlib import Path
import re
import shutil

from src.crawler.kis_client import KISClient, KISCredentialsMissing
from src.crawler.market_clock import KST, completed_price_cutoff
from src.crawler.price_learning_history import PacedHistoryClient, collect_history, reusable_entry
from src.crawler.update_completed_history import update_history
from src.models.selected_price_model import ROOT, write_json
from src.pipeline.next_open_learning_cycle import run_cycle
from src.report_generator.reliability_goal_report import report_goal


def configured_codes(path):
    data = json.loads(Path(path).read_text())
    codes = data['stock_codes']
    if (data['schema'] != 'ml_beta_universe_v1' or len(codes) < 901
            or len(set(codes)) != len(codes)
            or any(not isinstance(code, str) or not re.fullmatch(r'[0-9]{6}', code) for code in codes)):
        raise ValueError('The broad, explicit beta universe must not be reduced.')
    return sorted(codes)


def complete_snapshot(path, codes):
    manifest = json.loads((Path(path) / 'history_manifest.json').read_text())
    if (manifest.get('source') != 'kis_adjusted_daily' or not manifest.get('completed_bars_only')
            or not manifest.get('collection_complete') or sorted(manifest['requested_codes']) != sorted(codes)
            or len(manifest['stocks']) != len(codes)
            or sorted(row['stock_code'] for row in manifest['stocks']) != sorted(codes)
            or any(not reusable_entry(row, Path(path) / 'raw') for row in manifest['stocks'])):
        raise ValueError('Incomplete or changed beta price snapshot; keep the last public output.')
    return manifest


def refresh_snapshot(client, folder, codes, end):
    folder = Path(folder)
    destination = folder / ('snapshot_' + end.replace('-', ''))
    parents = []
    for path in sorted(folder.glob('snapshot_*/history_manifest.json')):
        metadata = json.loads(path.read_text())
        if metadata.get('collection_complete') and all(s['status'] == 'success' for s in metadata['stocks']):
            if metadata['end'] <= end:
                complete_snapshot(path.parent, codes)
                parents.append((metadata['end'], path.parent))
    if parents:
        previous_end, parent = max(parents)
        if previous_end == end:
            return parent
        result = update_history(client, parent, destination, end, workers=8)
    else:
        result = collect_history(client, codes, destination, '2023-01-01', end, workers=8)
    if any(s['status'] != 'success' for s in result['stocks']):
        raise ValueError('Some KIS series failed; retry the resumable snapshot, not a smaller universe.')
    complete_snapshot(destination, codes)
    return destination


def compact_snapshots(folder, active):
    """Bound the dedicated disposable CI cache; never touch original ledgers."""
    folder, active = Path(folder).resolve(), Path(active).resolve()
    candidates = sorted(path for path in folder.iterdir()
                        if path.is_dir() and not path.is_symlink()
                        and re.fullmatch(r'snapshot_[0-9]{8}', path.name))
    keep = set(candidates[-2:]) | {active}
    for path in candidates:
        if path not in keep:
            shutil.rmtree(path)


def release_beta(state_dir, universe, model_dir, ledger_dir, public_output, goal_output,
                 report_path, goal_path, client=None, now=None):
    live_clock = now is None
    now = now or datetime.now(KST)
    if now.tzinfo is None:
        raise ValueError('Timezone-aware beta clock required.')
    state_dir = Path(state_dir)
    codes = configured_codes(universe)
    if client is None:
        api = KISClient()
        api.get_access_token()
        client = PacedHistoryClient(api, .55 if api.base_url.endswith(':29443') else .15)
    end = completed_price_cutoff(now).isoformat()
    history = refresh_snapshot(client, state_dir / 'prices', codes, end)
    benchmark = refresh_snapshot(client, state_dir / 'benchmark', ['069500', '229200'], end)
    # A long cold-start backfill may cross the daily completion cutoff.
    if live_clock and completed_price_cutoff().isoformat() > end:
        end = completed_price_cutoff().isoformat()
        history = refresh_snapshot(client, state_dir / 'prices', codes, end)
        benchmark = refresh_snapshot(client, state_dir / 'benchmark', ['069500', '229200'], end)
    report_path = Path(report_path)
    publication = state_dir / 'publication'
    publication.mkdir(parents=True, exist_ok=True)
    staged_price, staged_goal = publication / 'price_model.json', publication / 'reliability_goal.json'
    learning = run_cycle(history, model_dir, ledger_dir, staged_price,
                         report_path.with_name(report_path.stem + '_learning.json'), now=None if live_clock else now)
    goal = report_goal(history, ledger_dir, benchmark, goal_path, staged_goal,
                       report_path.with_name(report_path.stem + '_goal.json'), now=None if live_clock else now)
    from src.report_generator.price_model_panel import load_public_forecast
    from src.report_generator.supervised_forecast_report import write_payload
    if load_public_forecast(staged_price) is None:
        raise ValueError('Invalid beta publication; previous public output retained.')
    write_payload(json.loads(staged_price.read_text()), public_output)
    write_json(json.loads(staged_goal.read_text()), goal_output)
    result = dict(schema='ml_beta_release_v1', generated_at=datetime.now(KST).isoformat(),
                  status='beta_under_validation', universe_count=len(codes), price_date=learning['price_date'],
                  new_mature_labels=learning['new_mature_labels'], learning_state=learning['learning_state'],
                  recording_state=learning['recording_state'], new_frozen_predictions=learning['new_frozen_predictions'],
                  model_trained_at=learning['model_trained_at'], dataset_sha256=learning['dataset_sha256'],
                  history_manifest=str(history / 'history_manifest.json'),
                  goal_passed=goal['any_goal_passed'], recommendation_enabled=False, automatic_orders=False)
    write_json(result, report_path)
    compact_snapshots(state_dir / 'prices', history)
    compact_snapshots(state_dir / 'benchmark', benchmark)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--state-dir', type=Path, default=ROOT / 'data/ml_beta_state')
    parser.add_argument('--universe', type=Path, default=ROOT / 'docs/model_experiments/ml_beta_universe.json')
    parser.add_argument('--model-dir', type=Path, default=ROOT / 'data/models/price_next_open_current')
    parser.add_argument('--ledger-dir', type=Path, default=ROOT / 'data/predictions')
    parser.add_argument('--output', type=Path, default=ROOT / 'docs/price_model.json')
    parser.add_argument('--goal-output', type=Path, default=ROOT / 'docs/reliability_goal.json')
    parser.add_argument('--goal', type=Path, default=ROOT / 'docs/model_experiments/reliability_goal_20261026.json')
    parser.add_argument('--report', type=Path, default=ROOT / 'reports/daily_review' / f'{datetime.now(KST):%Y-%m-%d}_ml_beta_release.json')
    args = parser.parse_args()
    try:
        result = release_beta(args.state_dir, args.universe, args.model_dir, args.ledger_dir,
                              args.output, args.goal_output, args.report, args.goal)
    except KISCredentialsMissing:
        parser.exit(2, 'KIS credentials missing: beta refresh skipped; previous publication retained.\n')
    except Exception as error:
        parser.exit(2, 'Beta refresh failed safely: ' + type(error).__name__ + '. Previous GitHub publication is retained.\n')
    print(json.dumps({key: result[key] for key in ['status', 'universe_count', 'price_date',
        'new_mature_labels', 'learning_state', 'recording_state', 'new_frozen_predictions', 'recommendation_enabled']}))


if __name__ == '__main__':
    main()
