"""Training-only signed lag associations; messages are NOT causal claims."""
from __future__ import annotations

import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix

from src.models.selected_price_model import COLUMNS

PEER_COLUMNS = ['peer_' + name for name in COLUMNS] + ['peer_coverage']


def pairwise_lag_correlation(values, minimum):
    source, target = values[:-1], values[1:]
    a, b = np.isfinite(source).astype(float), np.isfinite(target).astype(float)
    x, y = np.nan_to_num(source), np.nan_to_num(target)
    counts = b.T @ a
    safe = np.maximum(counts, 1)
    sum_x, sum_y = b.T @ x, y.T @ a
    covariance = y.T @ x - sum_x * sum_y / safe
    var_x = np.maximum(0, b.T @ (x * x) - sum_x ** 2 / safe)
    var_y = np.maximum(0, (y * y).T @ a - sum_y ** 2 / safe)
    denominator = np.sqrt(var_x * var_y)
    result = np.divide(covariance, denominator, out=np.zeros_like(covariance), where=denominator > 1e-12)
    result[counts < minimum] = 0
    np.fill_diagonal(result, 0)
    return result


def fit_peer_graph(inputs, training_end, top_k=4, minimum_half_pairs=120, minimum_abs=.08, shuffle_seed=713):
    history = inputs[inputs.signal_date.le(pd.Timestamp(training_end))].copy()
    if history.empty or history.duplicated(['stock_code', 'signal_date']).any():
        raise ValueError('Unique training-only prices required for peer graph.')
    codes = sorted(inputs.stock_code.unique())
    # Remove the contemporaneous observed-universe mean before fitting lag links.
    # Exceptional changes are omitted only from graph estimation, never outcomes.
    values = pd.to_numeric(history.return_1d, errors='coerce')
    valid = history.volume.gt(0) & values.abs().le(.305) & np.isfinite(values)
    history['residual'] = values.where(valid)
    history['residual'] -= history.groupby('signal_date').residual.transform('mean')
    matrix = history.pivot(index='signal_date', columns='stock_code', values='residual').reindex(columns=codes).to_numpy()
    middle = len(matrix) // 2
    first = pairwise_lag_correlation(matrix[:middle], minimum_half_pairs)
    second = pairwise_lag_correlation(matrix[middle:], minimum_half_pairs)
    stable = (np.sign(first) == np.sign(second)) & (np.abs(first) >= minimum_abs) & (np.abs(second) >= minimum_abs)
    scores = np.where(stable, np.sign(first) * np.minimum(np.abs(first), np.abs(second)), 0)
    weights = np.zeros_like(scores)
    for target in range(len(codes)):
        order = np.argsort(-np.abs(scores[target]), kind='stable')[:top_k]
        weights[target, order] = scores[target, order]
    mass = np.abs(weights).sum(axis=1, keepdims=True)
    weights = np.divide(weights, mass, out=np.zeros_like(weights), where=mass > 0)
    shuffled = np.zeros_like(weights)
    for target in range(len(codes)):
        selected = np.flatnonzero(weights[target])
        if not len(selected):
            continue
        rng = np.random.default_rng(np.random.SeedSequence([shuffle_seed, target]))
        sources = rng.permutation(np.delete(np.arange(len(codes)), target))[:len(selected)]
        shuffled[target, sources] = weights[target, selected]
    return dict(codes=codes, weights=weights, shuffled_weights=shuffled,
                training_end=str(pd.Timestamp(training_end).date()),
                source_dates=len(matrix), edges=int(np.count_nonzero(weights)),
                targets_with_edges=int(np.count_nonzero(mass)), top_k=top_k,
                minimum_half_pairs=minimum_half_pairs, minimum_abs=minimum_abs,
                interpretation='Replicated lag associations inside training, not proof of causality or predictive utility')


def add_peer_messages(inputs, graph, shuffled=False):
    codes = graph['codes']
    lookup = {code: i for i, code in enumerate(codes)}
    if not set(inputs.stock_code).issubset(lookup):
        raise ValueError('Peer graph cannot silently change its stock universe.')
    weights = csr_matrix(graph['shuffled_weights'] if shuffled else graph['weights'])
    absolute = abs(weights)
    parts = []
    for _, part in inputs.groupby('signal_date', sort=True):
        part = part.copy()
        positions = np.array([lookup[code] for code in part.stock_code])
        local = part[COLUMNS].to_numpy(dtype=float)
        observed = np.isfinite(local).all(axis=1) & part.volume.gt(0).to_numpy() & part.snapshot_date.le(part.signal_date).to_numpy()
        values = np.zeros((len(codes), len(COLUMNS)))
        present = np.zeros(len(codes))
        values[positions[observed]] = local[observed]
        present[positions[observed]] = 1
        coverage = absolute @ present
        message = weights @ values
        message = np.divide(message, coverage[:, None], out=np.zeros_like(message), where=coverage[:, None] > 0)
        part[PEER_COLUMNS[:-1]] = message[positions]
        part['peer_coverage'] = coverage[positions]
        parts.append(part)
    result = pd.concat(parts, ignore_index=True)
    result.attrs = inputs.attrs.copy()
    return result
