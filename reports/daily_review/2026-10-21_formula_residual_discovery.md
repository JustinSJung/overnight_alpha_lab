# AI Formula Discovery Research

RESEARCH_ONLY. Genetic programming synthesizes formula candidates; novelty or high-reliability completion is NOT claimed.
Library: gplearn 0.4.3. Separate scikit-learn 1.8.0 runtime; original model runtime unchanged.
Within-date ranks are computed from eligible INPUTS before outcomes. Formula orientation is prefix-only. Survival uses three later TRAIN-only blocks.
Discovery mode: crossfit_residual
Residual mode evolves against purged out-of-fold residuals and rejects linear-span copies; survival IC then concerns residuals, not raw returns.
No eval/exec or externally supplied Python programs; only fixed library arithmetic primitives.

## Discovery Audit

Retained formula count: 2
Discovery/survival: {'sample': {'rows': 22272, 'dates': 348, 'start': '2023-07-20', 'end': '2024-12-20', 'latest_label': '2024-12-30'}, 'prefix': {'rows': 376763, 'dates': 464, 'start': '2023-02-01', 'end': '2024-12-20', 'latest_label': '2024-12-30'}, 'survival': {'rows': 235606, 'dates': 275, 'start': '2025-01-02', 'end': '2026-02-20', 'latest_label': '2026-02-27'}}

| Candidate | Nodes | Prefix correlation | Nonlinear fraction | Later training block ICs | Retained | Formula |
|---:|---:|---:|---:|---|---|---|
| 0 | 9 | -0.04816467332404586 | 0.5408172984845336 | [0.022960217106338655, -0.0058455893756196335, -0.004681217227017997] | False | `min(min(rank__gap_volatility_20d, sub(rank__ma5_vs_ma20, max(rank__volume_trend_5_20, rank__ma5_vs_ma20))), rank__volatility_20d)` |
| 1 | 9 | -0.047155911561795515 | 0.2843252169832804 | [0.02253651351226899, -0.0037254086408842176, -0.005539677974405024] | False | `min(rank__gap_volatility_20d, sub(add(rank__gap_volatility_20d, rank__ma5_vs_ma20), max(rank__volume_trend_5_20, rank__ma5_vs_ma20)))` |
| 2 | 11 | -0.04645833888713652 | 0.20836413756725644 | [0.0361790691146751, 0.009936732473567562, 0.0037699789892837823] | True | `add(min(rank__gap_volatility_20d, sub(rank__ma5_vs_ma20, max(rank__volume_trend_5_20, rank__ma5_vs_ma20))), add(rank__range_mean_20d, rank__ma5_vs_ma20))` |
| 3 | 9 | -0.045823503350839456 | 0.36473122888281073 | [0.019943241360992955, -0.0012134459124049728, -0.011175742519447222] | False | `min(rank__gap_volatility_20d, sub(add(rank__distance_ma20, rank__volatility_20d), max(rank__volume_trend_5_20, rank__ma5_vs_ma20)))` |
| 4 | 5 | -0.044450580726422016 | 0.3216974501021286 | [0.02613490236379185, -0.014134338701086133, -0.009508940143074296] | False | `min(rank__gap_volatility_20d, add(rank__downside_volatility_20d, rank__ma5_vs_ma20))` |
| 5 | 7 | -0.04326793878091109 | 0.2231700325402851 | [0.026072084464964316, -0.013874426306415612, -0.017944576546781627] | False | `add(rank__gap_volatility_20d, min(min(rank__ma5_vs_ma20, rank__gap_volatility_20d), rank__volatility_20d))` |
| 6 | 7 | -0.042838671607487486 | 0.22414052765393416 | [0.0392210247967702, 0.0005635553344667915, 0.008095622118645925] | True | `add(rank__range_mean_20d, min(min(rank__ma5_vs_ma20, rank__gap_volatility_20d), rank__volatility_20d))` |
| 7 | 5 | -0.042545633702051444 | 0.4303543509878272 | [0.028972167436624653, -0.010929004024214692, -0.018529628639257435] | False | `min(min(rank__ma5_vs_ma20, rank__gap_volatility_20d), rank__volatility_20d)` |

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
        "date_brier": 0.25614948340343324,
        "known_constant_date_brier": 0.2568844953363994,
        "mean_daily_auc": 0.509726600974343,
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
        "date_brier_delta": -0.00020319561857987085,
        "lower_95": -0.0004771930289704078,
        "upper_95": 0.00010053777565936537
      },
      "tree_control": {
        "date_brier_delta": 0.006290652486979395,
        "lower_95": 0.003887356902468591,
        "upper_95": 0.008861225451515667
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
        "absolute_success_rate": 0.39680851063829786,
        "net_return_proxy": 0.007816311853474816,
        "excess_vs_pool": 0.01094094488192633
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
        "mean": 0.004568087223384908,
        "lower": -0.005329813903758801,
        "upper": 0.018346178460427
      },
      "tree_control": {
        "mean": -0.005611447476868771,
        "lower": -0.026434034088502333,
        "upper": 0.016150241303214005
      },
      "return_20d": {
        "mean": 0.03506267148570959,
        "lower": -0.014813742413876509,
        "upper": 0.09022440789908588
      },
      "random_mean": {
        "mean": 0.010566718601286261,
        "lower": -0.022174468148568105,
        "upper": 0.04329317863381502
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
      "success_count": 44,
      "failure_count": 126,
      "pooled_success_rate": 0.25882352941176473,
      "date_success_rate": 0.25882352941176473,
      "date_success_lower": 0.15294117647058825,
      "all_date_net_proxy": -0.08190581333418122,
      "all_date_net_lower": -0.14288730857683843,
      "alpha": 0.00625
    },
    "passed": false
  },
  {
    "threshold": 0.6,
    "metrics": {
      "cases": 158,
      "dates": 34,
      "success_count": 38,
      "failure_count": 120,
      "pooled_success_rate": 0.24050632911392406,
      "date_success_rate": 0.22745098039215686,
      "date_success_lower": 0.1325919117647059,
      "all_date_net_proxy": -0.09362698633239978,
      "all_date_net_lower": -0.14639726753994464,
      "alpha": 0.00625
    },
    "passed": false
  },
  {
    "threshold": 0.65,
    "metrics": {
      "cases": 88,
      "dates": 24,
      "success_count": 30,
      "failure_count": 58,
      "pooled_success_rate": 0.3409090909090909,
      "date_success_rate": 0.3611111111111111,
      "date_success_lower": 0.24725961538461536,
      "all_date_net_proxy": -0.047623152295176024,
      "all_date_net_lower": -0.08433778876250571,
      "alpha": 0.00625
    },
    "passed": false
  },
  {
    "threshold": 0.7,
    "metrics": {
      "cases": 12,
      "dates": 9,
      "success_count": 5,
      "failure_count": 7,
      "pooled_success_rate": 0.4166666666666667,
      "date_success_rate": 0.3333333333333333,
      "date_success_lower": null,
      "all_date_net_proxy": -0.019700779300570754,
      "all_date_net_lower": -0.07842741542574759,
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
Protocol SHA256: 8ac5476d2ac65269a8f557ded4e40c011429a381107f6baf630e2abf160a211e
Ignored run: /Users/justin/Desktop/overnight_alpha_lab/data/models/price_formula_residual_discovery/runs/20261021T062334Z_a9e9df69
