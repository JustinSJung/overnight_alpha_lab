# Selective Payoff-Distribution Research

RESEARCH_ONLY. No new algorithm discovery, financial guarantee, conformal guarantee or independent final validation is claimed.
Four payoff bins, three calibrated seed models, pessimistic ensemble utility and a separately fitted abstention policy.
This is an engineering experiment inspired by selective prediction, not an implementation or proof of Deep Gamblers or conformal risk control.
The ensemble floor/ceiling are model disagreement heuristics, NOT statistical confidence bounds.
Clipped within-bin utility is a coarse train-derived proxy, NOT expected executable profit.

Selected policy: None

## Four Disjoint Partitions

{'train': {'rows': 616595, 'dates': 744, 'start': '2023-02-01', 'end': '2026-02-20', 'latest_label': '2026-02-27'}, 'probability_calibration': {'rows': 32332, 'dates': 38, 'start': '2026-03-03', 'end': '2026-04-23', 'latest_label': '2026-04-30'}, 'policy_calibration': {'rows': 28360, 'dates': 34, 'start': '2026-05-04', 'end': '2026-06-23', 'latest_label': '2026-06-30'}}

## Nine Policy-Calibration Trials

| Probability floor | Loss ceiling | Cases | Dates | Date success | Simultaneous success lower | All-date net lower | Passed |
|---:|---:|---:|---:|---:|---:|---:|---|
| 0.55 | 0.1 | 0 | 0 | None | None | 0.0 | False |
| 0.55 | 0.2 | 1 | 1 | 1.0 | None | 0.0 | False |
| 0.55 | 0.3 | 121 | 27 | 0.328395061728395 | 0.13320242656449552 | -0.1087413187300323 | False |
| 0.6 | 0.1 | 0 | 0 | None | None | 0.0 | False |
| 0.6 | 0.2 | 0 | 0 | None | None | 0.0 | False |
| 0.6 | 0.3 | 41 | 16 | 0.34375 | None | -0.0937231835401641 | False |
| 0.65 | 0.1 | 0 | 0 | None | None | 0.0 | False |
| 0.65 | 0.2 | 0 | 0 | None | None | 0.0 | False |
| 0.65 | 0.3 | 0 | 0 | None | None | 0.0 | False |

Five-session circular block bootstrap, 5,000 samples. Nine policies x two bounds use Bonferroni correction; approximate historical diagnostics, not an assumption-free guarantee.

## Fixed Top20 Diagnostic, Not Activated Recommendations

| Period | Method | Date success | Five-session net proxy | Excess vs pool |
|---|---|---:|---:|---:|
| development_audit | distribution_utility | 47.0213% | 2.2374% | 2.5499% |
| development_audit | binary_control | 47.3404% | 1.3428% | 1.6552% |
| development_audit | momentum | 36.2766% | -2.7246% | -2.4122% |
| development_audit | random_mean | 41.1564% | -0.2750% | 0.0374% |

## External Policy/Probability Evidence

{
  "development_audit": {
    "status": "historical_development_only",
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
    "probability": {
      "target": "target",
      "date_brier": 0.23914851645033425,
      "known_constant_date_brier": 0.2568844953363994,
      "mean_daily_auc": 0.5395894766382876,
      "auc_dates": 47,
      "known_calibration_prior": 0.5320397058997834
    },
    "binary_probability": {
      "target": "target",
      "date_brier": 0.24985883091645383,
      "known_constant_date_brier": 0.2568844953363994,
      "mean_daily_auc": 0.5375744793266889,
      "auc_dates": 47,
      "known_calibration_prior": 0.5320397058997834
    },
    "top20": {
      "distribution_utility": {
        "absolute_success_rate": 0.47021276595744677,
        "net_return_proxy": 0.022373926179673705,
        "excess_vs_pool": 0.025498559208125212
      },
      "binary_control": {
        "absolute_success_rate": 0.47340425531914887,
        "net_return_proxy": 0.013427759330343594,
        "excess_vs_pool": 0.0165523923587951
      },
      "momentum": {
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
    "paired_top20": {
      "binary_control": {
        "mean": 0.008946166849330108,
        "lower": -0.0022917855158290984,
        "upper": 0.0218778097878979
      },
      "momentum": {
        "mean": 0.04962028581190846,
        "lower": 0.009248541223768428,
        "upper": 0.09363744227403765
      },
      "random_mean": {
        "mean": 0.025124332927485147,
        "lower": -0.002481041765753514,
        "upper": 0.05403087420921228
      }
    }
  },
  "short_recent_tail": {
    "status": "unavailable_no_complete_outcome_dates"
  }
}

Screen reasons: no_policy_passed_separate_policy_calibration, insufficient_external_policy_cases_or_dates, external_60_percent_success_lower_not_established, external_positive_net_proxy_not_established, top20_advantage_over_all_references_not_established
Recommendation gate: False. No policy passing calibration means no forced recommendations.
Complete-date coverage (all data, including immature tail): {'eligible_dates': 905, 'complete_dates': 878, 'included_rows': 729313, 'by_period': {'development_audit': {'eligible_dates': 62, 'complete_dates': 47, 'evaluated_rows': 39463}, 'short_recent_tail': {'eligible_dates': 7, 'complete_dates': 0, 'evaluated_rows': 0}}}
Whole incomplete dates are excluded; no resolving-stock-only hindsight ranking. This complete-date filter remains a limitation.
Current-universe, adjusted-history, dependent and overlapping close-to-close outcome limitations remain.
Existing broad candidate pool, scoring, public model and original forward records unchanged.

Inspiration, not replication or claimed theoretical guarantee:
- https://arxiv.org/abs/1907.00208
- https://arxiv.org/abs/2310.01262

Protocol SHA256: 7013a9f3cbecd26a93379a7a6acfd981878ed6ffcdb7f313b55c000c28fd9621
Ignored run: /Users/justin/Desktop/overnight_alpha_lab/data/models/price_distribution_selector/runs/20261021T060422Z_0e4c251e
