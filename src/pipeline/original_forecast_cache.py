"""Redundant original forecast recovery; never replace conflicting original bytes."""
from pathlib import Path

from src.evaluator.next_open_provenance import ORIGINAL_NAME, read_provenance


def copy_pairs(pairs):
    for original, target in pairs:
        if original.is_symlink() or target.is_symlink():
            raise ValueError('Original forecast cache entries must not be symbolic links.')
        if target.exists() and target.read_bytes() != original.read_bytes():
            raise ValueError('Conflicting original forecast; never overwrite to repair publication.')
    copied = 0
    for original, target in pairs:
        if not target.exists():
            target.parent.mkdir(parents=True, exist_ok=True)
            with target.open('xb') as handle:
                handle.write(original.read_bytes())
            copied += 1
    return copied


def copy_primary_originals(source, destination):
    source, destination = Path(source), Path(destination)
    pairs = []
    for path in sorted(source.glob('ml_next_open_forward_[0-9]*.csv')):
        if not ORIGINAL_NAME.fullmatch(path.name) or path.stat().st_size > 2_000_000:
            raise ValueError('Invalid original forecast cache entry.')
        read_provenance(path)
        for original in [path, path.with_suffix('.manifest.json')]:
            target = destination / original.name
            pairs.append((original, target))
    return copy_pairs(pairs)


def copy_improvement_originals(source, destination, protocol):
    from src.pipeline.model_improvement import read_trials
    source, destination = Path(source), Path(destination)
    read_trials(source, protocol)
    pairs = [(path, destination / path.name) for original in sorted(source.glob('*.csv'))
             for path in [original, original.with_suffix('.manifest.json')]]
    return copy_pairs(pairs)
