"""Past-only, same-stock session windows; absent history is never invented."""
from __future__ import annotations

import numpy as np
import pandas as pd

from src.models.selected_price_model import COLUMNS


class PriceSequences:
    def __init__(self, inputs, length=20, columns=None):
        if length < 2 or inputs.empty or inputs.duplicated(['stock_code', 'signal_date']).any():
            raise ValueError('Unique stock/date history and a sequence length >= 2 required.')
        if inputs.snapshot_date.gt(inputs.signal_date).any():
            raise ValueError('Sequence inputs were unavailable at their stated signal time.')
        self.length = length
        self.columns = list(COLUMNS if columns is None else columns)
        self.frame = inputs[['stock_code', 'signal_date'] + self.columns].sort_values(['stock_code', 'signal_date']).reset_index(drop=True)
        self.values = self.frame[self.columns].to_numpy(dtype=np.float32)
        self.keys = pd.MultiIndex.from_frame(self.frame[['stock_code', 'signal_date']])
        calendar = pd.DatetimeIndex(sorted(self.frame.signal_date.unique()))
        sessions = calendar.get_indexer(self.frame.signal_date)
        ends = np.arange(len(self.frame))
        starts = np.maximum(0, ends - length + 1)
        codes = self.frame.stock_code.to_numpy()
        finite = np.isfinite(self.values).all(axis=1)
        failures = np.r_[0, np.cumsum(~finite)]
        self.available = ((ends >= length - 1) & (codes[starts] == codes[ends])
                          & (sessions[ends] - sessions[starts] == length - 1)
                          & (failures[ends + 1] - failures[starts] == 0))

    def attach(self, candidates):
        frame = candidates.copy()
        ends = self.keys.get_indexer(pd.MultiIndex.from_frame(frame[['stock_code', 'signal_date']]))
        if np.any(ends < 0):
            raise ValueError('Candidate not present in the same input history.')
        frame['sequence_end'] = ends
        frame['sequence_available'] = self.available[ends]
        return frame

    def windows(self, ends, mean, scale, clip=8.):
        ends = np.asarray(ends, dtype=int)
        if np.any(ends < 0) or np.any(ends >= len(self.values)) or not self.available[ends].all():
            raise ValueError('An unavailable sequence cannot be filled or stretched.')
        rows = ends[:, None] - np.arange(self.length - 1, -1, -1)
        values = (self.values[rows] - mean) / scale
        return np.clip(values, -clip, clip).astype(np.float32)


def sample_input_candidates(frame, per_date, seed=42):
    if per_date < 1 or frame.duplicated(['stock_code', 'signal_date']).any():
        raise ValueError('Positive sample budget and unique input keys required.')
    parts = []
    for day, part in frame.groupby('signal_date', sort=True):
        ordered = part.sort_values('stock_code')
        rng = np.random.default_rng(np.random.SeedSequence([seed, int(pd.Timestamp(day).strftime('%Y%m%d'))]))
        positions = rng.permutation(len(ordered))[:per_date]
        parts.append(ordered.iloc[positions])
    if not parts:
        raise ValueError('No input candidates to sample.')
    return pd.concat(parts).sort_values(['signal_date', 'stock_code']).reset_index(drop=True)
