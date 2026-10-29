import os
from pathlib import Path
import subprocess
import tempfile
import unittest


class NextOpenPipelineWiringTests(unittest.TestCase):
    def run_block(self, history=None, benchmark=None):
        source = (Path(__file__).resolve().parents[1] / 'scripts/run_catchup.sh').read_text()
        start = source.index('if [ -n "${PRICE_ML_HISTORY_ROOT:-}" ]; then')
        end = source.index('run_optional "Collecting market index data', start)
        block = source[start:end]
        env = dict(os.environ)
        for name in ['PRICE_ML_HISTORY_ROOT', 'PRICE_ML_BENCHMARK_ROOT']:
            env.pop(name, None)
        if history is not None:
            env['PRICE_ML_HISTORY_ROOT'] = history
        if benchmark is not None:
            env['PRICE_ML_BENCHMARK_ROOT'] = benchmark
        harness = '''set -eu
TODAY=2026-10-29
log() { printf '%s\\n' "$*"; }
run_optional() { shift; printf 'CALL'; printf ' <%s>' "$@"; printf '\\n'; }
'''
        with tempfile.TemporaryDirectory() as directory:
            return subprocess.run(['bash', '-c', harness + block], cwd=directory, env=env,
                                  text=True, capture_output=True, check=True).stdout

    def test_verified_history_drives_current_learning_and_goal_audit(self):
        output = self.run_block('/history with spaces', '/benchmark with spaces')
        self.assertIn('<learn-next-open> <--data-root> </history with spaces>', output)
        self.assertIn('<goal-audit> <--data-root> </history with spaces>', output)
        self.assertIn('<--benchmark-root> </benchmark with spaces>', output)
        self.assertEqual(output.count('CALL'), 2)
        self.assertNotIn('<cycle>', output)
        self.assertNotIn('<train>', output)

    def test_missing_benchmark_is_not_a_fake_benchmark(self):
        output = self.run_block('/history')
        self.assertIn('<goal-audit>', output)
        self.assertNotIn('<--benchmark-root>', output)

    def test_missing_history_preserves_original_publication_dates(self):
        output = self.run_block()
        self.assertNotIn('CALL', output)
        self.assertIn('without refreshing their dates', output)


if __name__ == '__main__':
    unittest.main()
