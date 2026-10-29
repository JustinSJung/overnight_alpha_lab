# Social Attention Feature Report - 2026-10-27

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **97**
- High attention rows: **1**
- Medium attention rows: **76**
- Rumor-noise detected rows: **1**
- Risk-noise detected rows: **34**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 020150 | 롯데에너지머티리얼즈 | major_shareholder_change | 12.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 090150 | 아이윈 | merger | 10.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 311390 | 네오크레마 | major_shareholder_change | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 186230 | 그린플러스 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 186230 | 그린플러스 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 056730 | CNT85 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 065660 | 안트로젠 | investment_decision | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 013360 | 일성건설 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 206650 | 유바이오로직스 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 382480 | 지아이텍 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 900100 | 파이온엑스 | convertible_bond | 9.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 083660 | CSA 코스믹 | paid_in_capital_increase | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 206400 | 베노티앤알 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 003070 | 코오롱글로벌 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 003070 | 코오롱글로벌 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 161000 | 애경케미칼 | merger | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 161000 | 애경케미칼 | merger | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 161000 | 애경케미칼 | merger | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 161000 | 애경케미칼 | merger | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 003070 | 코오롱글로벌 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
