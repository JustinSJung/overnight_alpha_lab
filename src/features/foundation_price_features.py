"""Frozen pretrained price patterns: local inference, past windows, explicit fallback."""
from pathlib import Path
import hashlib

import numpy as np
import pandas as pd

from src.features.next_open_dataset import valid_candle
from src.features.price_sequences import PriceSequences

FOUNDATION_COLUMNS = ['foundation_gap', 'foundation_relative_median', 'foundation_relative_low_proxy',
                      'foundation_relative_high_proxy', 'foundation_entry_spread', 'foundation_exit_spread',
                      'foundation_path_change']


def load_frozen_pipeline(root, protocol):
    import torch
    from chronos import BaseChronosPipeline
    root = Path(root)
    for name, expected in protocol['asset_hashes'].items():
        if Path(name).name != name or hashlib.sha256((root / name).read_bytes()).hexdigest() != expected:
            raise ValueError('Pinned 2024 foundation assets changed.')
    torch.set_num_threads(protocol['threads'])
    return BaseChronosPipeline.from_pretrained(str(root), device_map='cpu', dtype=torch.float32,
                                              local_files_only=True, trust_remote_code=False, use_safetensors=True)


class FoundationWindows:
    def __init__(self, inputs, sessions):
        prices = inputs.copy()
        good = valid_candle(prices)
        prices.loc[~good, ['open', 'close']] = np.nan
        self.store = PriceSequences(prices, sessions, columns=['open', 'close'])

    def features(self, candidates, pipeline, batch_size=128):
        import torch
        attached = self.store.attach(candidates).reset_index(drop=True)
        result = attached[['stock_code', 'signal_date']].copy()
        result[FOUNDATION_COLUMNS] = 0.
        result['foundation_available'] = 0.
        available = np.flatnonzero(attached.sequence_available.to_numpy())
        for start in range(0, len(available), batch_size):
            positions = available[start:start + batch_size]
            part = attached.iloc[positions]
            # Do not apply the standardized-feature clipping used by neural experiments to raw prices.
            windows = self.store.windows(part.sequence_end, np.zeros(2), np.ones(2), clip=np.inf)
            origin = part.close.to_numpy(dtype=float)
            context = np.concatenate([windows[:, :, 0] / origin[:, None], windows[:, :, 1] / origin[:, None]])
            with torch.inference_mode():
                quantiles, _ = pipeline.predict_quantiles(torch.as_tensor(context, dtype=torch.float32),
                                                          prediction_length=5, quantile_levels=[.1, .5, .9])
            q = quantiles.detach().cpu().numpy() if hasattr(quantiles, 'detach') else np.asarray(quantiles)
            n = len(part)
            if q.shape != (2 * n, 5, 3):
                raise ValueError('Unexpected frozen forecaster output shape.')
            entry, exit_price = q[:n, 0], q[n:, 4]
            valid = (np.isfinite(q).all(axis=(1, 2)).reshape(2, n).all(axis=0)
                     & (entry > 0).all(axis=1) & (exit_price > 0).all(axis=1)
                     & (np.diff(entry, axis=1) >= 0).all(axis=1) & (np.diff(exit_price, axis=1) >= 0).all(axis=1))
            chosen = positions[valid]
            e, x = entry[valid], exit_price[valid]
            values = np.column_stack([e[:, 1] - 1, x[:, 1] / e[:, 1] - 1,
                                      x[:, 0] / e[:, 1] - 1, x[:, 2] / e[:, 1] - 1,
                                      e[:, 2] - e[:, 0], x[:, 2] - x[:, 0],
                                      x[:, 1] - q[n:, 0, 1][valid]])
            if not np.isfinite(values).all():
                raise ValueError('Invalid frozen forecast features.')
            result.loc[chosen, FOUNDATION_COLUMNS] = values
            result.loc[chosen, 'foundation_available'] = 1.
        return result


def shuffled_foundation(frame, seed=713):
    result = frame.copy()
    for day, part in frame[frame.foundation_available.eq(1)].groupby('signal_date', sort=True):
        ordered = part.sort_values('stock_code')
        rng = np.random.default_rng(np.random.SeedSequence([seed, int(day.strftime('%Y%m%d'))]))
        result.loc[ordered.index, FOUNDATION_COLUMNS] = ordered[FOUNDATION_COLUMNS].to_numpy()[rng.permutation(len(ordered))]
    return result
