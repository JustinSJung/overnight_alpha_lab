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
    from test_market_context_experiment import panel
    from src.models.selected_price_model import COLUMNS, ROOT, prepare_selected_features
    from src.models.neural_circuit_price_model import prepare_experiment, run_experiment as train_parent
    from src.models.swarm_circuit_experiment import load_swarm, predict_variants, run_experiment


@unittest.skipUnless(AVAILABLE, 'Optional isolated neural-circuit runtime not installed')
class SwarmCircuitTests(unittest.TestCase):
    def test_matched_peer_training_roundtrip_and_parent_pointer_preservation(self):
        inputs = prepare_selected_features(panel(), COLUMNS)
        days = sorted(inputs.signal_date.unique())
        p = json.loads((ROOT / 'docs/model_experiments/neural_circuit_protocol_20261022.json').read_text())
        p.update(epochs=1, seeds=[17], sequence_sessions=5, training_candidates_per_date=8,
                 labels_as_of=str(pd.Timestamp(days[-1]).date()), calibration_start=str(pd.Timestamp(days[60]).date()),
                 evaluation_start=str(pd.Timestamp(days[95]).date()), primary_period='primary',
                 periods={'primary': [str(pd.Timestamp(days[95]).date()), str(pd.Timestamp(days[-1]).date())]})
        e = json.loads((ROOT / 'docs/model_experiments/swarm_circuit_protocol_20261022.json').read_text())
        e.update(minimum_half_pairs=10, minimum_abs_correlation=.01)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with patch('src.models.neural_circuit_price_model.load_inputs', return_value=(inputs, {})), patch('builtins.print'):
                train_parent('/unused', root / 'parent', p, root / 'parent.md')
            with patch('src.models.swarm_circuit_experiment.load_inputs', return_value=(inputs, {})), patch('builtins.print'):
                summary = run_experiment('/unused', root / 'parent', root / 'model', e, root / 'report.md')
            self.assertFalse(summary['recommendation_gate_passed'])
            bundle = load_swarm(root / 'model')
            self.assertFalse(bundle['metadata']['recommendation_enabled'])
            self.assertLess(bundle['graph']['training_end'], p['calibration_start'])
            store, cohort, _, _, _ = prepare_experiment(inputs, p)
            frame = cohort[cohort.signal_date.ge(p['evaluation_start'])].reset_index(drop=True)
            values = predict_variants(bundle, inputs, frame, store)
            (root / 'parent/latest.json').write_text('{}')
            reloaded = load_swarm(root / 'model')
            repeated = predict_variants(reloaded, inputs, frame, store)
            for name in values:
                self.assertEqual(len(values[name]), len(frame))
                np.testing.assert_allclose(values[name], repeated[name], rtol=0, atol=1e-12)
                self.assertEqual(summary['results']['primary'][name]['input_candidates'], len(frame))
            run = Path(summary['run_dir'])
            with (run / 'peer_ncp_real_17.pt').open('ab') as handle:
                handle.write(b'tampered')
            with self.assertRaises(ValueError):
                load_swarm(root / 'model')


if __name__ == '__main__':
    unittest.main()
