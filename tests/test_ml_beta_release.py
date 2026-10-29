import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch

from src.crawler.price_learning_history import file_digest
from src.evaluator.next_open_provenance import read_provenance, seal_provenance
from src.features.next_open_dataset import TARGET_VERSION
from src.pipeline.ml_beta_release import compact_snapshots, configured_codes, refresh_snapshot, release_beta
from src.pipeline.next_open_learning_cycle import collect_originals


def snapshot(path, codes, end='2026-10-28'):
    (path / 'raw').mkdir(parents=True, exist_ok=True)
    entries = []
    for code in codes:
        target = path / 'raw' / (code + '.csv')
        target.write_text('date,close\n2026-10-28,100\n')
        entries.append(dict(stock_code=code, status='success', sha256=file_digest(target)))
    data = dict(source='kis_adjusted_daily', completed_bars_only=True, collection_complete=True,
                requested_codes=codes, stocks=entries, end=end)
    (path / 'history_manifest.json').write_text(json.dumps(data))
    return data


class MLBetaReleaseTests(unittest.TestCase):
    def test_explicit_universe_is_not_reduced_to_selected_stocks(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'universe.json'
            codes = [str(n).zfill(6) for n in range(901)]
            path.write_text(json.dumps(dict(schema='ml_beta_universe_v1', stock_codes=codes)))
            self.assertEqual(len(configured_codes(path)), 901)
            for invalid in [codes[:20], codes + codes[:1], codes[:-1] + ['wrong']]:
                path.write_text(json.dumps(dict(schema='ml_beta_universe_v1', stock_codes=invalid)))
                with self.assertRaises(ValueError):
                    configured_codes(path)

    def test_cache_reuse_is_checksum_checked_and_needs_no_collection(self):
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            path = folder / 'snapshot_20261028'
            snapshot(path, ['005930'])
            with patch('src.pipeline.ml_beta_release.collect_history') as collect:
                self.assertEqual(refresh_snapshot(Mock(), folder, ['005930'], '2026-10-28'), path)
                collect.assert_not_called()
            (path / 'raw/005930.csv').write_text('changed')
            with self.assertRaisesRegex(ValueError, 'changed'):
                refresh_snapshot(Mock(), folder, ['005930'], '2026-10-28')

    def test_update_uses_a_separate_resumable_snapshot(self):
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            parent = folder / 'snapshot_20261028'
            snapshot(parent, ['005930'])
            before = (parent / 'raw/005930.csv').read_bytes()
            def update(client, old, new, end, workers):
                self.assertEqual(old, parent)
                self.assertNotEqual(old, new)
                return snapshot(new, ['005930'], end)
            with patch('src.pipeline.ml_beta_release.update_history', side_effect=update):
                result = refresh_snapshot(Mock(), folder, ['005930'], '2026-10-29')
            self.assertEqual(result.name, 'snapshot_20261029')
            self.assertEqual((parent / 'raw/005930.csv').read_bytes(), before)

    def test_partial_collection_cannot_train_or_replace_publication(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            public = root / 'public.json'
            public.write_text('{"previous":true}')
            with patch('src.pipeline.ml_beta_release.configured_codes', return_value=['005930']), \
                    patch('src.pipeline.ml_beta_release.collect_history', return_value={'stocks': [{'status': 'failed'}]}), \
                    patch('src.pipeline.ml_beta_release.run_cycle') as learn:
                with self.assertRaisesRegex(ValueError, 'failed'):
                    release_beta(root / 'state', None, root / 'models', root / 'ledgers',
                                 public, root / 'goal.json', root / 'report.json', None, client=Mock())
                learn.assert_not_called()
            self.assertEqual(public.read_text(), '{"previous":true}')

    def test_only_old_disposable_snapshot_folders_are_compacted(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name in ['snapshot_20261026', 'snapshot_20261027', 'snapshot_20261028', 'original_forecasts']:
                (root / name).mkdir()
            compact_snapshots(root, root / 'snapshot_20261028')
            self.assertEqual(sorted(path.name for path in root.iterdir()),
                             ['original_forecasts', 'snapshot_20261027', 'snapshot_20261028'])

    def test_public_provenance_has_no_private_fields_and_survives_model_cache_eviction(self):
        import pandas as pd
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            m = dict(dataset_sha256='a' * 64, trained_at='2026-10-21T15:00:00+09:00',
                     as_of='2026-10-20', baseline_probability=.5, target_version=TARGET_VERSION,
                     private_path='/do/not/publish', app_secret='DO_NOT_PUBLISH')
            path = root / ('ml_next_open_forward_20261021_' + 'a' * 16 + '.csv')
            pd.DataFrame([dict(model_dataset_sha256=m['dataset_sha256'], model_trained_at=m['trained_at'],
                signal_date='2026-10-21', recorded_at='2026-10-21T17:00:00+09:00',
                stock_code='005930', prediction_id='original', target_version=TARGET_VERSION,
                validation_base_rate=.5)]).to_csv(path, index=False)
            seal_provenance(path, m)
            text = path.with_suffix('.manifest.json').read_text()
            self.assertNotIn('DO_NOT_PUBLISH', text)
            self.assertNotIn('/do/not/publish', text)
            original, _, _ = collect_originals(root, root / 'evicted-model-cache', {})
            self.assertEqual(len(original), 1)
            path.write_text(path.read_text() + '\n')
            with self.assertRaisesRegex(ValueError, 'changed'):
                read_provenance(path)


if __name__ == '__main__':
    unittest.main()
