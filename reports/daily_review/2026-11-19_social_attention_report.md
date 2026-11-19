# Social Attention Feature Report - 2026-11-19

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **68**
- High attention rows: **2**
- Medium attention rows: **31**
- Rumor-noise detected rows: **0**
- Risk-noise detected rows: **33**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 464080 | 에스오에스랩 | supply_contract | 14.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 077970 | STX엔진 | supply_contract | 13.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 010960 | 삼호개발 | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 900100 | 파이온엑스 | paid_in_capital_increase | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 208640 | 썸에이지 | paid_in_capital_increase | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 277410 | 인산가 | paid_in_capital_increase | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 320000 | 한울반도체 | major_shareholder_change | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 361390 | 제노코 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 310210 | 보로노이 | investment_decision | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 002810 | 삼영무역 | major_shareholder_change | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 032800 | 판타지오 | paid_in_capital_increase | 8.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 317770 | 엑스페릭스 | paid_in_capital_increase | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 437730 | 삼현 | supply_contract | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 372320 | 큐로셀 | investment_decision | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 003470 | 유안타증권 | major_shareholder_change | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 282880 | 코윈로보틱스 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 083650 | 비에이치아이 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 065450 | 빅텍 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 065450 | 빅텍 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 065450 | 빅텍 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
