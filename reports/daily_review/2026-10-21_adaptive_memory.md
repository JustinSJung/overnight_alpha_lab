# Delayed-Feedback Case Memory Router

RESEARCH_ONLY. Inspired by retrieval augmentation and discounted expert advice; NOT a TabR/AgACI replication, proof, world-first discovery or reliable trading system.
Historical prequential DEVELOPMENT replay: earlier evaluation labels may enter memory/weights only after strict availability. Not static holdout evidence.
Each issue batch is predicted before outcomes are joined. Router updates require every original case in that batch to resolve; once per date, not once per stock.
Case votes aggregate by source date. Neighbor support and agreement are heuristics, NOT calibrated confidence bounds.

## Fixed Fit and Policy

{
  "train": {
    "rows": 616595,
    "dates": 744,
    "start": "2023-02-01",
    "end": "2026-02-20",
    "latest_label": "2026-02-27"
  },
  "probability_calibration": {
    "rows": 32332,
    "dates": 38,
    "start": "2026-03-03",
    "end": "2026-04-23",
    "latest_label": "2026-04-30"
  },
  "policy_calibration": {
    "rows": 28360,
    "dates": 34,
    "start": "2026-05-04",
    "end": "2026-06-23",
    "latest_label": "2026-06-30"
  }
}

Selected policy: None
Policy trials: [
  {
    "threshold": 0.55,
    "metrics": {
      "cases": 20,
      "dates": 7,
      "success_count": 2,
      "failure_count": 18,
      "pooled_success_rate": 0.1,
      "date_success_rate": 0.07619047619047618,
      "date_success_lower": null,
      "all_date_net_proxy": -0.015268596224386796,
      "all_date_net_lower": -0.04288573889219599,
      "alpha": 0.00625
    },
    "passed": false
  },
  {
    "threshold": 0.6,
    "metrics": {
      "cases": 0,
      "dates": 0,
      "success_count": 0,
      "failure_count": 0,
      "pooled_success_rate": null,
      "date_success_rate": null,
      "date_success_lower": null,
      "all_date_net_proxy": 0.0,
      "all_date_net_lower": 0.0,
      "alpha": 0.00625
    },
    "passed": false
  },
  {
    "threshold": 0.65,
    "metrics": {
      "cases": 0,
      "dates": 0,
      "success_count": 0,
      "failure_count": 0,
      "pooled_success_rate": null,
      "date_success_rate": null,
      "date_success_lower": null,
      "all_date_net_proxy": 0.0,
      "all_date_net_lower": 0.0,
      "alpha": 0.00625
    },
    "passed": false
  },
  {
    "threshold": 0.7,
    "metrics": {
      "cases": 0,
      "dates": 0,
      "success_count": 0,
      "failure_count": 0,
      "pooled_success_rate": null,
      "date_success_rate": null,
      "date_success_lower": null,
      "all_date_net_proxy": 0.0,
      "all_date_net_lower": 0.0,
      "alpha": 0.00625
    },
    "passed": false
  }
]

## Historical Evaluation

{
  "development_audit": {
    "status": "prequential_historical_development_only",
    "probabilities": {
      "fixed_base": {
        "target": "target",
        "date_brier": 0.2498588309164541,
        "known_constant_date_brier": 0.2568844953363994,
        "mean_daily_auc": 0.5375744793266889,
        "auc_dates": 47,
        "known_calibration_prior": 0.5320397058997834
      },
      "case_memory": {
        "target": "target",
        "date_brier": 0.24471631955490294,
        "known_constant_date_brier": 0.2568844953363994,
        "mean_daily_auc": 0.5146503302834028,
        "auc_dates": 47,
        "known_calibration_prior": 0.5320397058997834
      },
      "recent_prior": {
        "target": "target",
        "date_brier": 0.24665693631975688,
        "known_constant_date_brier": 0.2568844953363994,
        "mean_daily_auc": 0.5,
        "auc_dates": 47,
        "known_calibration_prior": 0.5320397058997834
      },
      "fixed_average": {
        "target": "target",
        "date_brier": 0.24157446766207355,
        "known_constant_date_brier": 0.2568844953363994,
        "mean_daily_auc": 0.5371482870753099,
        "auc_dates": 47,
        "known_calibration_prior": 0.5320397058997834
      },
      "adaptive": {
        "target": "target",
        "date_brier": 0.24387189616186788,
        "known_constant_date_brier": 0.2568844953363994,
        "mean_daily_auc": 0.5296236416049283,
        "auc_dates": 47,
        "known_calibration_prior": 0.5320397058997834
      }
    },
    "paired_brier": {
      "fixed_base": {
        "date_brier_delta": -0.0059869347545861845,
        "lower_95": -0.029813931396400192,
        "upper_95": 0.02575995788920232
      },
      "case_memory": {
        "date_brier_delta": -0.000844423393035054,
        "lower_95": -0.0021742537223963933,
        "upper_95": 0.0005297469180918408
      },
      "recent_prior": {
        "date_brier_delta": -0.0027850401578889475,
        "lower_95": -0.009917075727929055,
        "upper_95": 0.0022974011748464504
      },
      "fixed_average": {
        "date_brier_delta": 0.0022974284997943433,
        "lower_95": -0.004235983869176681,
        "upper_95": 0.01189722718945914
      }
    },
    "policy": {
      "cases": 0,
      "dates": 0,
      "success_count": 0,
      "failure_count": 0,
      "pooled_success_rate": null,
      "date_success_rate": null,
      "date_success_lower": null,
      "all_date_net_proxy": 0.0,
      "all_date_net_lower": 0.0,
      "alpha": 0.05
    },
    "top20": {
      "fixed_base": {
        "absolute_success_rate": 0.47340425531914887,
        "net_return_proxy": 0.013427759330343594,
        "excess_vs_pool": 0.0165523923587951
      },
      "case_memory": {
        "absolute_success_rate": 0.4521276595744681,
        "net_return_proxy": -0.0024960265480899004,
        "excess_vs_pool": 0.0006286064803616073
      },
      "fixed_average": {
        "absolute_success_rate": 0.448936170212766,
        "net_return_proxy": 0.016432722620779418,
        "excess_vs_pool": 0.019557355649230914
      },
      "adaptive": {
        "absolute_success_rate": 0.45744680851063835,
        "net_return_proxy": 0.005343036595060169,
        "excess_vs_pool": 0.00846766962351168
      },
      "return_20d": {
        "absolute_success_rate": 0.3627659574468085,
        "net_return_proxy": -0.02724635963223476,
        "excess_vs_pool": -0.024121726603783256
      },
      "random_mean": {
        "absolute_success_rate": 0.4115638297872341,
        "net_return_proxy": -0.002750406747811436,
        "excess_vs_pool": 0.00037422628064007034
      }
    },
    "paired_top20_returns": {
      "fixed_base": {
        "mean": -0.008084722735283422,
        "lower": -0.032191561349266304,
        "upper": 0.014589745001996135
      },
      "case_memory": {
        "mean": 0.007839063143150072,
        "lower": 0.002297902262309242,
        "upper": 0.014317449551602237
      },
      "fixed_average": {
        "mean": -0.011089686025719239,
        "lower": -0.03976400531341576,
        "upper": 0.01330943422491061
      },
      "return_20d": {
        "mean": 0.03258939622729493,
        "lower": 0.005992019609266302,
        "upper": 0.05741231914611782
      },
      "random_mean": {
        "mean": 0.00809344334287161,
        "lower": -0.005489354220241678,
        "upper": 0.018882775005066025
      }
    }
  },
  "short_recent_tail": {
    "status": "unavailable_no_complete_outcome_dates"
  }
}

## Availability Audit

{
  "issued_dates": 113,
  "issued_predictions": 94639,
  "resolved_batch_updates": 86,
  "last_weights": [
    0.19092635959477722,
    0.40653422086866514,
    0.4025394195365576
  ]
}
Coverage: {
  "development_audit": {
    "issued_dates": 62,
    "complete_dates": 47,
    "evaluated_rows": 39463
  },
  "short_recent_tail": {
    "issued_dates": 7,
    "complete_dates": 0,
    "evaluated_rows": 0
  }
}
No incomplete-date reranking. Complete-date evaluation and partially observed past case memory retain missing-outcome bias limitations.
Fixed Top20 is diagnostic only. Overlapping close-to-close cost proxies are not executable/compounded returns or a tradable index.
Screen reasons: no_policy_passed_separate_policy_calibration, insufficient_external_policy_evidence, external_60_percent_success_lower_not_established, external_positive_net_proxy_not_established, weak_daily_discrimination, probability_advantage_over_all_controls_not_established, top20_advantage_over_all_references_not_established
Production recommendation gate: False.

References (inspiration, not assumed guarantees):
- https://arxiv.org/abs/2307.14338
- https://arxiv.org/abs/1005.1918
- https://proceedings.mlr.press/v162/zaffran22a.html

Current-universe, retrospectively adjusted prices and repeatedly viewed historical data limitations remain.
Protocol SHA256: 16ca3f9942ef6eba0d30518a026e723dab8a9bac771945fe8af65f18c695531e
Ignored run: /Users/justin/Desktop/overnight_alpha_lab/data/models/price_memory_router/runs/20261021T064727Z_35a382c3
