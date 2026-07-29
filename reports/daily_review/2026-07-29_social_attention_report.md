# Social Attention Feature Report - 2026-07-29

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **13**
- High attention rows: **1**
- Medium attention rows: **4**
- Rumor-noise detected rows: **1**
- Risk-noise detected rows: **6**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 054220 | 비츠로시스 | supply_contract | 21.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 047040 | 대우건설 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 001260 | 남광토건 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 114190 | 강원에너지 | supply_contract | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 010780 | 아이에스동서 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 043260 | 성호전자 | major_shareholder_change | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 121440 | 골프존홀딩스 | disclosure_violation | 3.5 | 4 | 6 | low_attention | medium_rumor_noise | risk_noise_detected |
| 340360 | 다보링크 | paid_in_capital_increase | 3.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 115530 | 씨엔플러스 | convertible_bond | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 017810 | 풀무원 | paid_in_capital_increase | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 027040 | 서울전자통신 | paid_in_capital_increase | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 066790 | 씨씨에스 | major_shareholder_change | 3.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 003470 | 유안타증권 | major_shareholder_change | 3.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
