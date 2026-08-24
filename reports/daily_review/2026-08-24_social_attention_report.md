# Social Attention Feature Report - 2026-08-24

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **32**
- High attention rows: **1**
- Medium attention rows: **12**
- Rumor-noise detected rows: **0**
- Risk-noise detected rows: **21**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 038530 | 케이바이오랩스 | spin_off | 17.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 291230 | 컴투스엔 | convertible_bond | 11.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 288980 | 모아데이타 | major_shareholder_change | 10.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 490470 | 세미파이브 | supply_contract | 10.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 003470 | 유안타증권 | major_shareholder_change | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 019490 | 엑시큐어하이트론 | supply_contract | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 389500 | 에스비비테크 | supply_contract | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 005960 | 동부건설 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 002020 | 코오롱 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 003070 | 코오롱글로벌 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 002460 | HS화성 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 130660 | 한전산업 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 333620 | 엔시스 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 351320 | 넥사다이내믹스 | convertible_bond | 5.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 351320 | 넥사다이내믹스 | convertible_bond | 5.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 351320 | 넥사다이내믹스 | convertible_bond | 5.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 351320 | 넥사다이내믹스 | paid_in_capital_increase | 5.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 351320 | 넥사다이내믹스 | paid_in_capital_increase | 5.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 351320 | 넥사다이내믹스 | paid_in_capital_increase | 5.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 178320 | 서진시스템 | convertible_bond | 5.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
