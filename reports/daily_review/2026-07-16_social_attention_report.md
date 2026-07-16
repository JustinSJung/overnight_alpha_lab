# Social Attention Feature Report - 2026-07-16

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **12**
- High attention rows: **0**
- Medium attention rows: **3**
- Rumor-noise detected rows: **1**
- Risk-noise detected rows: **8**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 054940 | 엑사이엔씨 | spin_off | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 097230 | HJ중공업 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 011300 | 우성머티리얼스 | paid_in_capital_increase | 6.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 080010 | 이상네트웍스 | disclosure_violation | 5.5 | 4 | 3 | low_attention | medium_rumor_noise | risk_noise_detected |
| 011000 | 진원생명과학 | investment_decision | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 009320 | 아진전자부품 | major_shareholder_change | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 002810 | 삼영무역 | merger | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 004890 | 동일산업 | major_shareholder_change | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 066790 | 씨씨에스 | lawsuit | 3.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 340810 | 시선AI | paid_in_capital_increase | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 042940 | 상지건설 | paid_in_capital_increase | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 320000 | 한울반도체 | paid_in_capital_increase | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
