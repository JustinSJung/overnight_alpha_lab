# Social Attention Feature Report - 2026-08-29

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **15**
- High attention rows: **1**
- Medium attention rows: **6**
- Rumor-noise detected rows: **0**
- Risk-noise detected rows: **11**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 253590 | 네오셈 | supply_contract | 13.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 227610 | 아우딘퓨쳐스 | major_shareholder_change | 11.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 004440 | 삼일씨엔에스 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 009410 | 태영건설 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 210980 | SK디앤디 | supply_contract | 7.5 | 0 | 9 | medium_attention | no_rumor_signal | high_risk_noise |
| 105550 | 엣지파운드리 | convertible_bond | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 004960 | 한신공영 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 079950 | 인베니아 | disclosure_violation | 3.5 | 0 | 9 | low_attention | no_rumor_signal | high_risk_noise |
| 175250 | 아이큐어 | major_shareholder_change | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 175250 | 아이큐어 | major_shareholder_change | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 175250 | 아이큐어 | major_shareholder_change | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 175250 | 아이큐어 | major_shareholder_change | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 065420 | 에스아이리소스 | disclosure_violation | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 033790 | 피노 | paid_in_capital_increase | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 053060 | 세동 | lawsuit | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
