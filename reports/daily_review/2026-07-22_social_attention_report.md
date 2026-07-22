# Social Attention Feature Report - 2026-07-22

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **19**
- High attention rows: **0**
- Medium attention rows: **7**
- Rumor-noise detected rows: **0**
- Risk-noise detected rows: **7**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 0009K0 | 에임드바이오 | investment_decision | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 475040 | 스트라드비젼 | supply_contract | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 475040 | 스트라드비젼 | supply_contract | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 009420 | 한올바이오파마 | investment_decision | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 475040 | 스트라드비젼 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 475040 | 스트라드비젼 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 137400 | 피엔티 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 005960 | 동부건설 | investment_decision | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 002990 | 금호건설 | investment_decision | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 061040 | 알에프텍 | merger | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 061040 | 알에프텍 | merger | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 061040 | 알에프텍 | merger | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 061040 | 알에프텍 | merger | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 203650 | 드림시큐리티 | convertible_bond | 3.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 183490 | 엔지켐생명과학 | lawsuit | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 183490 | 엔지켐생명과학 | lawsuit | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 183490 | 엔지켐생명과학 | lawsuit | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 183490 | 엔지켐생명과학 | lawsuit | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 114450 | 그린생명과학 | major_shareholder_change | 3.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
