# Signed Peer Communication / 종목 간 정보 교환 실험

RESEARCH_ONLY. A design hypothesis inspired by decentralized communication, not a biological simulation, causal discovery or a high-confidence finance claim.

The parent local NCP is fixed. Peer models use the same fitting endpoints, labels, seeds, epochs and calibration period.
Edges use only pre-calibration training inputs. Positive and negative lag associations must replicate in two training halves. No evaluation outcome chooses an edge.
The shuffled control preserves each target degree and signed weights but changes source identities. The real-message GRU controls whether any benefit needs the biological circuit.
All candidates remain present; missing peer information is explicitly encoded as zero coverage, not a fabricated stock price.

## Graph Audit

```json
{
  "training_end": "2026-02-20",
  "source_dates": 764,
  "edges": 3086,
  "targets_with_edges": 816,
  "top_k": 4,
  "minimum_half_pairs": 120,
  "minimum_abs": 0.08,
  "interpretation": "Replicated lag associations inside training, not proof of causality or predictive utility",
  "stocks": 901
}
```

## Historical Development

| Period | Arm | Candidates | Resolved | Unknown | Date Brier | Daily AUC | Top20 conditional daily success | Top20 conditional net proxy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| earlier_development | local_ncp | 32590 | 32420 | 170 | 0.25583757325386064 | 0.5351671824982883 | 0.35285650022492127 | -0.03181606974409695 |
| earlier_development | peer_ncp_real | 32590 | 32420 | 170 | 0.25305443800709226 | 0.5252110164580877 | 0.3434098065677013 | -0.02876887231278343 |
| earlier_development | peer_ncp_shuffled | 32590 | 32420 | 170 | 0.2569597760815545 | 0.5207349468260649 | 0.3385665017243964 | -0.025787820170037973 |
| earlier_development | peer_gru_real | 32590 | 32420 | 170 | 0.2570430752434499 | 0.5291390670374522 | 0.33424801319538167 | -0.03013808857091289 |
| primary_development | local_ncp | 52017 | 51483 | 534 | 0.2474954039068679 | 0.5333759298730282 | 0.4366534616110168 | -0.0023892659900334088 |
| primary_development | peer_ncp_real | 52017 | 51483 | 534 | 0.24889857037649116 | 0.5245903431771235 | 0.44785889454819844 | 0.0030293233967634003 |
| primary_development | peer_ncp_shuffled | 52017 | 51483 | 534 | 0.24899527707510935 | 0.5191366271205611 | 0.4616939645128001 | 0.005704610319897712 |
| primary_development | peer_gru_real | 52017 | 51483 | 534 | 0.2486732760484267 | 0.523173387058547 | 0.452895680060366 | 0.006286380393243865 |
| recent_tail | local_ncp | 6703 | 6612 | 91 | 0.2548150923228831 | 0.5177076496231461 | 0.24527272531819744 | -0.056099783629338915 |
| recent_tail | peer_ncp_real | 6703 | 6612 | 91 | 0.2523785002389254 | 0.5256843716197086 | 0.24984950120399035 | -0.04996707049741129 |
| recent_tail | peer_ncp_shuffled | 6703 | 6612 | 91 | 0.2535247856587566 | 0.5118749474324238 | 0.23647392070863432 | -0.055251877871714816 |
| recent_tail | peer_gru_real | 6703 | 6612 | 91 | 0.25217259815964504 | 0.5258926472083126 | 0.25683694530443757 | -0.044408976914565954 |

Unknown selected outcomes are not replaced; conditional returns do not establish full policy performance.

## Primary Real Peer NCP Minus Controls

Three prespecified family-adjusted five-session-block intervals. Previously inspected periods remain development evidence, not independent validation.
```json
{
  "local_ncp": {
    "mean": 0.0014031664696232354,
    "lower": -0.00048568150958492955,
    "upper": 0.0035337906735808514
  },
  "peer_ncp_shuffled": {
    "mean": -9.670669861821069e-05,
    "lower": -0.002038029427489269,
    "upper": 0.002403596232948212
  },
  "peer_gru_real": {
    "mean": 0.00022529432806440877,
    "lower": -0.0007150828138837017,
    "upper": 0.001534713586628109
  }
}
```

No production model, scoring formula, old original ledger or public confidence metric was replaced. All recommendations remain ABSTAIN.
Lag correlations are associations, not causal evidence. Current-universe and retrospectively adjusted-price biases remain. The graph is frozen, not an online ant-colony optimizer.
