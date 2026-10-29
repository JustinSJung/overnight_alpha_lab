"""Portable, public-safe provenance for immutable next-open forecast files."""
import hashlib
import json
from pathlib import Path
import re

from src.features.next_open_dataset import TARGET_VERSION

ORIGINAL_NAME = re.compile(r'ml_next_open_forward_[0-9]{8}_[0-9a-f]{16}\.csv')
FIELDS = ['dataset_sha256', 'trained_at', 'as_of', 'target_version', 'baseline_probability']


def read_provenance(path):
    path = Path(path)
    sidecar = path.with_suffix('.manifest.json')
    if sidecar.stat().st_size > 100_000 or not ORIGINAL_NAME.fullmatch(path.name):
        raise ValueError('Invalid next-open provenance file.')
    data = json.loads(sidecar.read_text())
    metadata = data['model']
    if (data['schema'] != 'next_open_original_v1' or data['ledger_file'] != path.name
            or data['sha256'] != hashlib.sha256(path.read_bytes()).hexdigest()
            or set(metadata) != set(FIELDS) or metadata['target_version'] != TARGET_VERSION
            or not re.fullmatch(r'[0-9a-f]{64}', metadata['dataset_sha256'])
            or not 0 <= metadata['baseline_probability'] <= 1):
        raise ValueError('Next-open original provenance or checksum changed.')
    return metadata


def seal_provenance(path, metadata):
    path = Path(path)
    safe = {key: metadata[key] for key in FIELDS}
    data = dict(schema='next_open_original_v1', ledger_file=path.name,
                sha256=hashlib.sha256(path.read_bytes()).hexdigest(), model=safe)
    sidecar = path.with_suffix('.manifest.json')
    if sidecar.exists():
        if read_provenance(path) != safe:
            raise ValueError('Do not replace original model provenance.')
        return
    with sidecar.open('x', encoding='utf-8') as handle:
        json.dump(data, handle, indent=2, allow_nan=False)
        handle.write('\n')
    read_provenance(path)
