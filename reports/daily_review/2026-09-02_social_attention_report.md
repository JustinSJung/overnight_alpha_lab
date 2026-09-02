# Social Attention Feature Report - 2026-09-02

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **139**
- High attention rows: **5**
- Medium attention rows: **57**
- Rumor-noise detected rows: **1**
- Risk-noise detected rows: **73**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 378800 | 샤페론 | spin_off | 18.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 012210 | 삼미금속 | supply_contract | 17.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 002990 | 금호건설 | supply_contract | 13.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 321370 | 센서뷰 | supply_contract | 13.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 027740 | 마니커 | major_shareholder_change | 12.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 226340 | 본느 | paid_in_capital_increase | 11.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 226340 | 본느 | paid_in_capital_increase | 11.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 226340 | 본느 | lawsuit | 11.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 226340 | 본느 | lawsuit | 11.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 288980 | 모아데이타 | major_shareholder_change | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 382150 | 온코크로스 | investment_decision | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 009150 | 삼성전기 | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 095190 | 신화프리텍 | convertible_bond | 10.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 030210 | 다올투자증권 | lawsuit | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 320000 | 한울반도체 | paid_in_capital_increase | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 331920 | 셀레믹스 | supply_contract | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 418420 | 라온텍 | supply_contract | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 005880 | 대한해운 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 294870 | IPARK현대산업개발 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 097230 | HJ중공업 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
