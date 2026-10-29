# AI Formula Discovery Research

RESEARCH_ONLY. Genetic programming synthesizes formula candidates; novelty or high-reliability completion is NOT claimed.
Library: gplearn 0.4.3. Separate scikit-learn 1.8.0 runtime; original model runtime unchanged.
Within-date ranks are computed from eligible INPUTS before outcomes. Formula orientation is prefix-only. Survival uses three later TRAIN-only blocks.
No eval/exec or externally supplied Python programs; only fixed library arithmetic primitives.

## Discovery Audit

Retained formula count: 3
Discovery/survival: {'sample': {'rows': 29696, 'dates': 464, 'start': '2023-02-01', 'end': '2024-12-20', 'latest_label': '2024-12-30'}, 'prefix': {'rows': 376763, 'dates': 464, 'start': '2023-02-01', 'end': '2024-12-20', 'latest_label': '2024-12-30'}, 'survival': {'rows': 235606, 'dates': 275, 'start': '2025-01-02', 'end': '2026-02-20', 'latest_label': '2026-02-27'}}

| Candidate | Nodes | Prefix correlation | Later training block ICs | Retained | Formula |
|---:|---:|---:|---|---|---|
| 0 | 5 | -0.10693920068779586 | [0.11555803711872675, 0.08344902342898287, 0.08145706695005263] | True | `add(add(rank__range_mean_20d, rank__downside_volatility_20d), rank__distance_ma20)` |
| 1 | 3 | -0.10257060085736762 | [0.1179102976947775, 0.08329040696561027, 0.09198532488477282] | True | `add(rank__range_mean_20d, rank__volatility_20d)` |
| 2 | 5 | -0.10248007558803558 | [0.11205281905789717, 0.08280535253476869, 0.0765446402802014] | True | `add(add(rank__range_mean_20d, rank__volatility_20d), rank__distance_ma20)` |
| 3 | 1 | -0.10192813286250288 | [0.12337966589919681, 0.09017435947112516, 0.10340402531370718] | False | `rank__range_mean_20d` |
| 4 | 1 | -0.10192813286250288 | [0.12337966589919681, 0.09017435947112516, 0.10340402531370718] | False | `rank__range_mean_20d` |
| 5 | 1 | -0.10192813286250288 | [0.12337966589919681, 0.09017435947112516, 0.10340402531370718] | False | `rank__range_mean_20d` |
| 6 | 1 | -0.10192813286250288 | [0.12337966589919681, 0.09017435947112516, 0.10340402531370718] | False | `rank__range_mean_20d` |
| 7 | 1 | -0.10192813286250288 | [0.12337966589919681, 0.09017435947112516, 0.10340402531370718] | False | `rank__range_mean_20d` |

## Same-Cohort External Historical Diagnostics

{
  "development_audit": {
    "status": "historical_development_only",
    "probabilities": {
      "rank_control": {
        "target": "target",
        "date_brier": 0.2563526790220131,
        "known_constant_date_brier": 0.2568844953363994,
        "mean_daily_auc": 0.5115216671648737,
        "auc_dates": 47,
        "known_calibration_prior": 0.5320397058997834
      },
      "formula_augmented": {
        "target": "target",
        "date_brier": 0.2563532046866338,
        "known_constant_date_brier": 0.2568844953363994,
        "mean_daily_auc": 0.5115297209800079,
        "auc_dates": 47,
        "known_calibration_prior": 0.5320397058997834
      },
      "tree_control": {
        "target": "target",
        "date_brier": 0.24985883091645383,
        "known_constant_date_brier": 0.2568844953363994,
        "mean_daily_auc": 0.5375744793266889,
        "auc_dates": 47,
        "known_calibration_prior": 0.5320397058997834
      }
    },
    "paired_brier": {
      "rank_control": {
        "date_brier_delta": 5.256646207072718e-07,
        "lower_95": -1.8987063209898139e-06,
        "upper_95": 2.46008577059579e-06
      },
      "tree_control": {
        "date_brier_delta": 0.00649437377017999,
        "lower_95": 0.003977511731926352,
        "upper_95": 0.00916555197587018
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
      "formula_augmented": {
        "absolute_success_rate": 0.4053191489361702,
        "net_return_proxy": 0.0032482246300899156,
        "excess_vs_pool": 0.006372857658541421
      },
      "rank_control": {
        "absolute_success_rate": 0.4053191489361702,
        "net_return_proxy": 0.0032482246300899156,
        "excess_vs_pool": 0.006372857658541421
      },
      "tree_control": {
        "absolute_success_rate": 0.47340425531914887,
        "net_return_proxy": 0.013427759330343594,
        "excess_vs_pool": 0.0165523923587951
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
      "rank_control": {
        "mean": 0.0,
        "lower": 0.0,
        "upper": 0.0
      },
      "tree_control": {
        "mean": -0.010179534700253682,
        "lower": -0.03085039882632864,
        "upper": 0.01334782387319983
      },
      "return_20d": {
        "mean": 0.030494584262324674,
        "lower": -0.013835139148820258,
        "upper": 0.08238403229907028
      },
      "random_mean": {
        "mean": 0.0059986313779013525,
        "lower": -0.023636211903686755,
        "upper": 0.03599774819792202
      }
    }
  },
  "short_recent_tail": {
    "status": "unavailable_no_complete_outcome_dates"
  }
}

Fixed Top20 tables are diagnostics, NOT recommended stocks. Cost is a 0.3% proxy; overlapping close-to-close returns are not executable/compounded strategy returns.
Sampled prefix rows are only an evolution compute budget, not a reduced live candidate pool. No final candidate generation is changed.
Calibration policy trials: [
  {
    "threshold": 0.55,
    "metrics": {
      "cases": 170,
      "dates": 34,
      "success_count": 46,
      "failure_count": 124,
      "pooled_success_rate": 0.27058823529411763,
      "date_success_rate": 0.27058823529411763,
      "date_success_lower": 0.15882352941176475,
      "all_date_net_proxy": -0.0721568461714039,
      "all_date_net_lower": -0.1377456108440865,
      "alpha": 0.00625
    },
    "passed": false
  },
  {
    "threshold": 0.6,
    "metrics": {
      "cases": 162,
      "dates": 34,
      "success_count": 40,
      "failure_count": 122,
      "pooled_success_rate": 0.24691358024691357,
      "date_success_rate": 0.2392156862745098,
      "date_success_lower": 0.13725490196078433,
      "all_date_net_proxy": -0.08288621288035841,
      "all_date_net_lower": -0.14008550404846745,
      "alpha": 0.00625
    },
    "passed": false
  },
  {
    "threshold": 0.65,
    "metrics": {
      "cases": 98,
      "dates": 26,
      "success_count": 33,
      "failure_count": 65,
      "pooled_success_rate": 0.336734693877551,
      "date_success_rate": 0.34102564102564104,
      "date_success_lower": 0.2088515625,
      "all_date_net_proxy": -0.05150109698703437,
      "all_date_net_lower": -0.11513856985969044,
      "alpha": 0.00625
    },
    "passed": false
  },
  {
    "threshold": 0.7,
    "metrics": {
      "cases": 15,
      "dates": 11,
      "success_count": 7,
      "failure_count": 8,
      "pooled_success_rate": 0.4666666666666667,
      "date_success_rate": 0.37878787878787873,
      "date_success_lower": null,
      "all_date_net_proxy": -0.018231446431215652,
      "all_date_net_lower": -0.07622570740706673,
      "alpha": 0.00625
    },
    "passed": false
  }
]
Selected policy threshold: None
Screen reasons: no_high_reliability_policy_passed_policy_calibration, insufficient_external_policy_evidence, external_60_percent_success_lower_not_established, external_positive_net_proxy_not_established, probability_advantage_over_both_controls_not_established, top20_advantage_over_all_references_not_established
Recommendation gate: False. Historical dates were repeatedly inspected; future validation remains required.
Coverage: {'development_audit': {'eligible_dates': 62, 'complete_dates': 47, 'evaluated_rows': 39463}, 'short_recent_tail': {'eligible_dates': 7, 'complete_dates': 0, 'evaluated_rows': 0}}
Partitions: {'train': {'rows': 616595, 'dates': 744, 'start': '2023-02-01', 'end': '2026-02-20', 'latest_label': '2026-02-27'}, 'probability_calibration': {'rows': 32332, 'dates': 38, 'start': '2026-03-03', 'end': '2026-04-23', 'latest_label': '2026-04-30'}, 'policy_calibration': {'rows': 28360, 'dates': 34, 'start': '2026-05-04', 'end': '2026-06-23', 'latest_label': '2026-06-30'}}
Current-universe, retrospectively adjusted prices and complete-date selection limitations remain.
Protocol SHA256: 34267efa3ad3294b3fcc0743751d4bd9d283a9e540db06a99f53e04bc28c76e8
Ignored run: /Users/justin/Desktop/overnight_alpha_lab/data/models/price_formula_discovery/runs/20261021T061858Z_046af611
