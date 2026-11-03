# Social Attention Feature Report - 2026-11-03

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **100**
- High attention rows: **7**
- Medium attention rows: **48**
- Rumor-noise detected rows: **15**
- Risk-noise detected rows: **39**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 389470 | 인벤티지랩 | investment_decision | 17.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 082270 | 젬백스 | major_shareholder_change | 16.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 302550 | 리메드 | convertible_bond | 14.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 017960 | 한국카본 | merger | 13.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 102460 | 이연제약 | convertible_bond | 12.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 036830 | 솔브레인홀딩스 | merger | 12.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 226950 | 올릭스 | investment_decision | 12.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 097230 | HJ중공업 | supply_contract | 9.5 | 4 | 0 | medium_attention | medium_rumor_noise | no_risk_noise |
| 005940 | NH투자증권 | major_shareholder_change | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 207940 | 삼성바이오로직스 | supply_contract | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 207940 | 삼성바이오로직스 | supply_contract | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 295310 | 에이치브이엠 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 000250 | 삼천당제약 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 000250 | 삼천당제약 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 000250 | 삼천당제약 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 000250 | 삼천당제약 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 145720 | 덴티움 | major_shareholder_change | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 950250 | 테라뷰 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 246960 | SCL사이언스 | merger | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 006280 | 녹십자 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
