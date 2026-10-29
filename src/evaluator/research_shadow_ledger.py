"""Seal all prespecified control forecasts and grade only the original probabilities."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd

from src.models.next_open_price_model import evaluate, grade
from src.models.price_forecaster import json_text


def existing_full_tree_shadow(inputs, now):
    from src.models.next_open_price_model import ROOT, load_model, predict_probability
    root = ROOT / 'data/models/price_next_open'
    if not (root / 'latest.json').exists():
        return None
    bundle = load_model(root)
    metadata = bundle['metadata']
    if (pd.Timestamp(metadata['trained_at']) > pd.Timestamp(now)
            or pd.Timestamp(metadata['as_of']) > inputs.signal_date.min()):
        raise ValueError('Existing-tree shadow would use future fitted data.')
    return predict_probability(bundle, inputs), metadata['dataset_sha256'], metadata['trained_at']


def seal_ledger(path, family, metadata, primary_arm, arms):
    path = Path(path)
    manifest = dict(schema='research_shadow_ledger_v1', family=family, ledger_file=path.name,
                    sha256=hashlib.sha256(path.read_bytes()).hexdigest(), primary_arm=primary_arm, arms=list(arms),
                    model_dataset_sha256=metadata['dataset_sha256'], model_trained_at=metadata['trained_at'])
    with path.with_suffix('.manifest.json').open('x', encoding='utf-8') as handle:
        handle.write(json_text(manifest) + '\n')
    return manifest


def grade_shadow(path, inputs, as_of, family, now=None):
    path = Path(path)
    manifest = json.loads(path.with_suffix('.manifest.json').read_text())
    if (manifest.get('schema') != 'research_shadow_ledger_v1' or manifest.get('family') != family
            or manifest.get('ledger_file') != path.name
            or hashlib.sha256(path.read_bytes()).hexdigest() != manifest.get('sha256')):
        raise ValueError('Original shadow forecast identity/hash changed.')
    original = pd.read_csv(path, dtype={'stock_code': str})
    if (not original.model_dataset_sha256.eq(manifest['model_dataset_sha256']).all()
            or not original.model_trained_at.eq(manifest['model_trained_at']).all()
            or manifest['primary_arm'] not in manifest['arms']):
        raise ValueError('Original shadow model identity mismatch.')
    for name in manifest['arms']:
        values = original['probability_' + name].to_numpy(dtype=float)
        if not np.isfinite(values).all() or np.any((values < 0) | (values > 1)):
            raise ValueError('Invalid original control probabilities.')
    if not np.allclose(original.probability_above_cost, original['probability_' + manifest['primary_arm']], rtol=0, atol=1e-12):
        raise ValueError('Prespecified primary forecast was changed.')
    graded, summary = grade(original, inputs, as_of, now)
    if original.validation_base_rate.nunique() != 1:
        raise ValueError('A shadow batch requires one frozen known baseline.')
    summary['shadow_models'] = {}
    for name in manifest['arms']:
        _, metrics = evaluate(graded, graded['probability_' + name].to_numpy(), float(original.validation_base_rate.iloc[0]))
        summary['shadow_models'][name] = metrics
    return graded, summary
