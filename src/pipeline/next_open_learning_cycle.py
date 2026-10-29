"""Feedback-driven research learning; no scheduling, orders or automatic approval."""
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
from src.evaluator.forward_price_forecast import valid_record_time
from src.evaluator.next_open_provenance import read_provenance
from src.features.next_open_dataset import TARGET_VERSION, build_next_open_dataset
from src.models.monthly_price_walkforward import monthly_split
from src.models.improvement_families import BASELINE, family_spec
from src.models.next_open_price_model import (
    ROOT, fit_current, freeze, grade, implementation_digest, load_inputs, load_model,
)
from src.models.price_forecaster import json_text
from src.models.selected_price_model import COLUMNS, fit_data_digest, write_json

ORIGINAL_NAME = re.compile(r'ml_next_open_forward_[0-9]{8}_[0-9a-f]{16}\.csv')


def collect_originals(ledger_dir, model_root, registry):
    """Keep original bytes; primary issuance per date is chosen BEFORE grading."""
    if any(not (Path(ledger_dir) / name).is_file() for name in registry):
        raise ValueError('Registered originals are missing; synchronize or recover them before learning.')
    identities = {}
    for path in sorted((Path(model_root) / 'runs').glob('*/model_metadata.json')):
        metadata = json.loads(path.read_text())
        identities[(metadata['dataset_sha256'], metadata['trained_at'])] = metadata
    parts, entries, excluded = [], dict(registry), 0
    for path in sorted(Path(ledger_dir).glob('ml_next_open_forward_*.csv')):
        if not ORIGINAL_NAME.fullmatch(path.name):
            continue
        if path.stat().st_size > 10_000_000:
            raise ValueError('Oversized original forecast ledger.')
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if path.name in entries and entries[path.name] != digest:
            raise ValueError('Original forecast ledger changed: ' + path.name)
        frame = pd.read_csv(path, dtype={'stock_code': str})
        required = {'model_dataset_sha256', 'model_trained_at', 'target_version', 'recorded_at',
                    'signal_date', 'stock_code', 'prediction_id', 'validation_base_rate'}
        if frame.empty or not required.issubset(frame):
            raise ValueError('Incomplete original forecast ledger: ' + path.name)
        if (frame.model_dataset_sha256.nunique() != 1 or frame.model_trained_at.nunique() != 1
                or frame.signal_date.nunique() != 1 or frame.recorded_at.nunique() != 1
                or frame.stock_code.duplicated().any() or frame.prediction_id.duplicated().any()
                or not frame.target_version.eq(TARGET_VERSION).all()):
            raise ValueError('Conflicting original forecast identity: ' + path.name)
        key = (frame.model_dataset_sha256.iloc[0], frame.model_trained_at.iloc[0])
        metadata = identities.get(key)
        if path.with_suffix('.manifest.json').exists():
            portable = read_provenance(path)
            if (portable['dataset_sha256'], portable['trained_at']) != key:
                raise ValueError('Original forecast portable model identity mismatch.')
            if metadata is not None and any(metadata[field] != value for field, value in portable.items()):
                raise ValueError('Preserved model and portable provenance disagree.')
            metadata = portable
        if metadata is None:
            raise ValueError('Original forecast model provenance is unavailable: ' + path.name)
        issued, trained = pd.Timestamp(frame.recorded_at.iloc[0]), pd.Timestamp(metadata['trained_at'])
        if (issued.tzinfo is None or trained.tzinfo is None or trained > issued
                or not valid_record_time(pd.Timestamp(frame.signal_date.iloc[0]), issued)):
            raise ValueError('Original forecast was not recorded before the next opening: ' + path.name)
        if (metadata['target_version'] != TARGET_VERSION
                or not np.isclose(frame.validation_base_rate.astype(float), metadata['baseline_probability'], rtol=0, atol=1e-12).all()
                or pd.Timestamp(metadata['as_of']) > pd.Timestamp(frame.signal_date.iloc[0])):
            raise ValueError('Original forecast target/baseline mismatch: ' + path.name)
        frame['original_file'] = path.name
        parts.append(frame)
        entries[path.name] = digest
    if not parts:
        return pd.DataFrame(), entries, excluded
    batches = sorted(parts, key=lambda f: (pd.Timestamp(f.recorded_at.iloc[0]), f.original_file.iloc[0]))
    chosen, dates = [], set()
    for frame in batches:
        day = pd.Timestamp(frame.signal_date.iloc[0]).normalize()
        if day in dates:
            excluded += len(frame)
        else:
            chosen.append(frame)
            dates.add(day)
    return pd.concat(chosen, ignore_index=True), entries, excluded


def run_cycle(data_root, model_root, ledger_dir, public_output, report_path, now=None, family=BASELINE, promotion=None):
    live_clock = now is None
    now = now or datetime.now(KST)
    if now.tzinfo is None:
        raise ValueError('Timezone-aware learning clock required.')
    now = now.astimezone(KST)
    cutoff = completed_price_cutoff(now)
    inputs, _ = load_inputs(data_root, cutoff)
    origin = inputs.signal_date.max()
    cutoff = min(pd.Timestamp(cutoff), pd.Timestamp(origin)).date()
    if family != BASELINE:
        from src.pipeline.model_improvement import permitted_serving_family
        if promotion is None or permitted_serving_family(promotion, cutoff) != family:
            raise ValueError('Cannot serve an unvalidated challenger.')
    model_root, ledger_dir = Path(model_root), Path(ledger_dir)
    registry_path = model_root / 'forward_registry.json'
    registry = json.loads(registry_path.read_text()) if registry_path.exists() else {}
    ledger, registry, duplicates = collect_originals(ledger_dir, model_root, registry)
    # Validate original predictions BEFORE any model/publication replacement.
    graded, evidence = None, dict(recorded_candidates=0, evaluated_cases=0, unresolved_cases=0,
                                 states={}, recommendation_enabled=False)
    if not ledger.empty:
        graded, evidence = grade(ledger, inputs, cutoff, now)
    cohort, _ = build_next_open_dataset(inputs, cutoff)
    known = cohort[cohort.target.notna()].copy()
    spec = family_spec(family)
    train, calibration = monthly_split(known, cutoff, spec['training_sessions'], spec['calibration_sessions'])
    expected_digest = fit_data_digest(train, calibration, COLUMNS)
    previous = load_model(model_root) if (model_root / 'latest.json').exists() else None
    previous_cutoff = None
    repair_cutoff_metadata = False
    if previous is not None:
        metadata = previous['metadata']
        previous_cutoff = pd.Timestamp(metadata.get('partitions', {}).get('calibration', {}).get('latest_label', metadata['as_of']))
        repair_cutoff_metadata = pd.Timestamp(metadata['as_of']) > previous_cutoff
    if previous_cutoff is not None and previous_cutoff > pd.Timestamp(cutoff):
        raise ValueError('Do not replace a newer learning state with an older cutoff.')
    new_labels = int(known.label_available_date.gt(previous_cutoff).sum()) if previous is not None else len(known)
    implementation_changed = (previous is not None and previous['metadata'].get('implementation_sha256') != implementation_digest())
    family_changed = previous is not None and previous['metadata'].get('model_family', BASELINE) != family
    if previous is not None and previous['metadata']['dataset_sha256'] == expected_digest and not repair_cutoff_metadata and not implementation_changed and not family_changed:
        learning_state = 'no_new_fit_rows_model_preserved'
        bundle = previous
    else:
        if family == BASELINE:
            fit_current(data_root, model_root, cutoff)
        else:
            fit_current(data_root, model_root, cutoff, family=family)
        bundle = load_model(model_root)
        learning_state = ('fit_cutoff_metadata_repaired' if repair_cutoff_metadata and not new_labels
                          else 'new_mature_labels_learned' if new_labels
                          else 'validated_model_family_changed' if family_changed
                          else 'implementation_changed_retrained' if implementation_changed else 'revised_fit_data_relearned')
    if live_clock:
        now = datetime.now(KST)
    if pd.Timestamp(bundle['metadata']['trained_at']) > pd.Timestamp(now):
        raise ValueError('A newly fitted model cannot be published before its actual creation time.')
    recording = 'outside_recording_window_originals_preserved'
    fresh = 0
    if valid_record_time(origin, pd.Timestamp(now)):
        matching = (not ledger.empty and pd.to_datetime(ledger.signal_date).eq(origin).any())
        if matching:
            recording = 'date_already_recorded_first_original_preserved'
        else:
            frozen = freeze(bundle, data_root, ledger_dir, None if live_clock else now)
            if live_clock:
                now = datetime.now(KST)
            fresh = frozen['predictions']
            recording = 'new_timely_original_recorded'
            ledger, registry, duplicates = collect_originals(ledger_dir, model_root, registry)
            graded, evidence = grade(ledger, inputs, cutoff, now)
    if graded is not None:
        evaluation = ledger_dir / f'ml_next_open_system_evaluation_{now:%Y%m%d}.csv'
        temporary = evaluation.with_suffix('.csv.tmp')
        graded.to_csv(temporary, index=False)
        temporary.replace(evaluation)
    write_json(registry, registry_path)
    # Import here to keep publication optional for callers that only test learning.
    if public_output is not None:
        from src.report_generator.next_open_forecast_report import build_payload
        from src.report_generator.supervised_forecast_report import write_payload
        payload = build_payload(bundle, data_root, evidence, graded, now)
        write_payload(payload, public_output)
    current_original = (ledger[pd.to_datetime(ledger.signal_date).eq(origin)] if not ledger.empty else pd.DataFrame())
    publication_uses_current = (current_original.empty or
        (current_original.model_dataset_sha256.eq(bundle['metadata']['dataset_sha256']).all()
         and current_original.model_trained_at.eq(bundle['metadata']['trained_at']).all()))
    summary = dict(generated_at=now.isoformat(), price_date=str(origin.date()),
                   learning_state=learning_state, new_mature_labels=new_labels, serving_family=family,
                   publication_uses_current_model=bool(publication_uses_current),
                   fit_label_cutoff=bundle['metadata']['as_of'], model_trained_at=bundle['metadata']['trained_at'],
                   dataset_sha256=bundle['metadata']['dataset_sha256'],
                   recording_state=recording, new_frozen_predictions=fresh,
                   original_registry_files=len(registry), later_duplicate_candidates_not_used=duplicates,
                   evidence_scope='First timely recorded model batch per signal date, same next-open target; evolving learning system, not one static model',
                   forward=evidence, recommendation_enabled=False)
    write_json(summary, report_path)
    return summary


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data-root', type=Path, required=True)
    parser.add_argument('--model-dir', type=Path, default=ROOT / 'data/models/price_next_open_current')
    parser.add_argument('--ledger-dir', type=Path, default=ROOT / 'data/predictions')
    parser.add_argument('--output', type=Path, default=ROOT / 'docs/price_model.json')
    parser.add_argument('--report', type=Path, default=ROOT / 'reports/daily_review' / f'{datetime.now(KST):%Y-%m-%d}_next_open_learning_cycle.json')
    args = parser.parse_args()
    print(json_text(run_cycle(args.data_root, args.model_dir, args.ledger_dir, args.output, args.report)))


if __name__ == '__main__':
    main()
