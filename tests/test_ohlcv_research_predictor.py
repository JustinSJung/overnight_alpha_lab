from datetime import datetime
import unittest
from unittest.mock import Mock

import numpy as np
import pandas as pd

from src.crawler.market_clock import KST
from src.features.completed_price_dataset import HISTORY_FEATURE_VERSION, history_features
from src.features.ohlcv_information import OHLCV_FEATURES
from src.features.price_learning_dataset import FEATURES
from src.models.ohlcv_research_predictor import research_forecast
from test_completed_price_history import prices


def model():
    classifier, calibrator, regressor = Mock(), Mock(), Mock()
    classifier.predict_proba.return_value = np.array([[.3, .7]])
    calibrator.predict_proba.return_value = np.array([[.1, .9]])
    regressor.predict.return_value = np.array([.1])
    return {'metadata': {'schema': 'research_ohlcv_information_v1', 'recommendation_gate_passed': False,
                          'trained_at': '2026-10-20T09:00:00+00:00', 'as_of': '2025-10-17'},
            'models': {'enriched': {'classifier': classifier, 'calibrator': calibrator,
                                     'regressor': regressor, 'features': FEATURES + OHLCV_FEATURES}}}


class ResearchQueryTests(unittest.TestCase):
    def setUp(self):
        self.raw = history_features(prices())
        self.raw.attrs['feature_version'] = HISTORY_FEATURE_VERSION
        self.now = datetime(2026, 10, 21, 10, tzinfo=KST)

    def test_high_research_probability_is_still_abstention(self):
        result = research_forecast(model(), self.raw, '005930', now=self.now)
        self.assertEqual(result['probability_above_cost'], .9)
        self.assertEqual(result['recommendation'], 'ABSTAIN')
        self.assertEqual(result['signal_date'], '2026-10-20')
        self.assertEqual(result['model_status'], 'RESEARCH_ONLY')

    def test_unfinished_or_wrong_schema_inputs_are_not_accepted(self):
        future = self.raw.tail(1).copy()
        future['signal_date'] = pd.Timestamp('2026-10-21')
        future['snapshot_date'] = pd.Timestamp('2026-10-21')
        raw = pd.concat([self.raw, future], ignore_index=True)
        raw.attrs = self.raw.attrs.copy()
        result = research_forecast(model(), raw, '005930', now=self.now)
        self.assertEqual(result['signal_date'], '2026-10-20')
        wrong = model()
        wrong['models']['enriched']['features'] = FEATURES
        with self.assertRaises(ValueError):
            research_forecast(wrong, raw, '005930', now=self.now)

    def test_future_model_time_or_inactive_stock_is_rejected(self):
        future = model()
        future['metadata']['trained_at'] = '2099-01-01T00:00:00+00:00'
        with self.assertRaises(ValueError):
            research_forecast(future, self.raw, '005930', now=self.now)
        raw = self.raw.copy()
        raw['volume_ratio_20d'] = 0
        with self.assertRaises(ValueError):
            research_forecast(model(), raw, '005930', now=self.now)


if __name__ == '__main__':
    unittest.main()
