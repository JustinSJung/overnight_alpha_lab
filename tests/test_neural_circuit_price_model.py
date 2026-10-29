import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import numpy as np
import pandas as pd

AVAILABLE = importlib.util.find_spec('torch') is not None and importlib.util.find_spec('ncps') is not None
if AVAILABLE:
    import torch
    from test_market_context_experiment import panel
    from src.models.selected_price_model import COLUMNS, ROOT, prepare_selected_features
    from src.models.neural_circuit_price_model import (
        ARMS, SequenceClassifier, calibrated_probabilities, fit_normalizer, freeze_research,
        load_research, prepare_experiment, raw_probabilities, run_experiment,
    )


@unittest.skipUnless(AVAILABLE, 'Optional isolated neural-circuit runtime not installed')
class NeuralCircuitTests(unittest.TestCase):
    def protocol(self):
        p = json.loads((ROOT / 'docs/model_experiments/neural_circuit_protocol_20261022.json').read_text())
        p.update(epochs=1, seeds=[17], sequence_sessions=5, training_candidates_per_date=8)
        return p

    def test_snapshot_control_ignores_past_but_sequence_models_use_it(self):
        p = self.protocol()
        torch.manual_seed(17)
        values = torch.randn(4, 5, len(COLUMNS))
        changed = values.clone()
        changed[:, :-1] += 2
        for kind in ARMS:
            model = SequenceClassifier(kind, p).eval()
            a, b = model(values), model(changed)
            self.assertEqual(tuple(a.shape), (4,))
            self.assertTrue(torch.isfinite(a).all())
            if kind == 'last_mlp':
                torch.testing.assert_close(a, b, rtol=0, atol=0)
            else:
                self.assertGreater(float((a - b).abs().max().detach()), 1e-7)

    def test_training_roundtrip_fallback_and_full_pool_are_preserved(self):
        inputs = prepare_selected_features(panel(), COLUMNS)
        days = sorted(inputs.signal_date.unique())
        p = self.protocol()
        p.update(labels_as_of=str(pd.Timestamp(days[-1]).date()), calibration_start=str(pd.Timestamp(days[60]).date()),
                 evaluation_start=str(pd.Timestamp(days[95]).date()), primary_period='primary',
                 periods={'primary': [str(pd.Timestamp(days[95]).date()), str(pd.Timestamp(days[-1]).date())]})
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with patch('src.models.neural_circuit_price_model.load_inputs', return_value=(inputs, {})), patch('builtins.print'):
                summary = run_experiment('/unused', root / 'model', p, root / 'report.md')
            self.assertFalse(summary['recommendation_gate_passed'])
            bundle = load_research(root / 'model')
            self.assertFalse(bundle['metadata']['recommendation_enabled'])
            store, cohort, train, calibration, _ = prepare_experiment(inputs, p)
            self.assertLess(train.label_available_date.max(), calibration.signal_date.min())
            a = fit_normalizer(train)
            altered = inputs.copy()
            altered.loc[altered.signal_date.ge(p['evaluation_start']), COLUMNS] = 99999
            _, _, altered_train, _, _ = prepare_experiment(altered, p)
            b = fit_normalizer(altered_train)
            np.testing.assert_array_equal(a.mean_, b.mean_)
            frame = cohort[cohort.signal_date.ge(p['evaluation_start'])].reset_index(drop=True)
            first, _ = calibrated_probabilities(bundle, frame, store)
            second, _ = calibrated_probabilities(load_research(root / 'model'), frame, store)
            for name in first:
                np.testing.assert_allclose(first[name], second[name], rtol=0, atol=1e-12)
                self.assertEqual(len(first[name]), len(frame))
            absent = frame.copy()
            absent['sequence_available'] = False
            raw = raw_probabilities(bundle, absent, store)
            for name in ARMS[1:]:
                np.testing.assert_allclose(raw[name][0], raw['last_mlp'].mean(axis=0))
            for name, metrics in summary['results']['primary'].items():
                self.assertEqual(metrics['input_candidates'], len(frame))
                self.assertGreater(metrics['unresolved_cases'], 0)
            run = Path(summary['run_dir'])
            metadata = json.loads((run / 'model_metadata.json').read_text())
            self.assertNotIn('results', metadata)
            with (run / 'cfc_ncp_17.pt').open('ab') as handle:
                handle.write(b'tampered')
            with self.assertRaises(ValueError):
                load_research(root / 'model')

    def test_freeze_requires_timely_record_and_seals_controls_without_overwrite(self):
        origin = pd.Timestamp('2026-10-22')
        now = origin.tz_localize('Asia/Seoul') + pd.Timedelta(hours=18)
        frame = pd.DataFrame({'stock_code': ['005930'], 'signal_date': [origin], 'probability_above_cost': [.6],
                              **{'probability_' + name: [.6] for name in ARMS + ['extra_trees']}})
        metadata = dict(dataset_sha256='a' * 64, trained_at=(now - pd.Timedelta(hours=1)).isoformat(), baseline_probability=.5)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'history_manifest.json').write_text('{}')
            with patch('src.models.neural_circuit_price_model.current_predictions', return_value=frame):
                result = freeze_research({'metadata': metadata}, root, root, now)
                original = Path(result['ledger']).read_bytes()
                self.assertTrue(Path(result['ledger']).with_suffix('.manifest.json').exists())
                with self.assertRaises(FileExistsError):
                    freeze_research({'metadata': metadata}, root, root, now)
                self.assertEqual(Path(result['ledger']).read_bytes(), original)
                with self.assertRaises(ValueError):
                    freeze_research({'metadata': metadata}, root, root, now + pd.Timedelta(hours=18))

    def test_live_recording_clock_is_rechecked_after_inference(self):
        origin = pd.Timestamp('2026-10-22')
        before_open = pd.Timestamp('2026-10-23 08:58:00', tz='Asia/Seoul')
        after_open = pd.Timestamp('2026-10-23 09:00:01', tz='Asia/Seoul')
        frame = pd.DataFrame({'stock_code': ['005930'], 'signal_date': [origin], 'probability_above_cost': [.6]})
        with patch('src.models.neural_circuit_price_model.datetime') as clock, \
                patch('src.models.neural_circuit_price_model.current_predictions', return_value=frame):
            clock.now.side_effect = [before_open, after_open]
            with self.assertRaises(ValueError):
                freeze_research({'metadata': {}}, '/unused', '/unused')


if __name__ == '__main__':
    unittest.main()
