# Social Attention Feature Report - 2026-08-06

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **19**
- High attention rows: **2**
- Medium attention rows: **4**
- Rumor-noise detected rows: **0**
- Risk-noise detected rows: **10**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 215570 | 크로넥스 | paid_in_capital_increase | 15.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 296640 | 이노에이엑스 | supply_contract | 12.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 042370 | 비츠로테크 | supply_contract | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 457600 | 벡트 | major_shareholder_change | 8.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 488900 | 비츠로넥스텍 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 199800 | 툴젠 | paid_in_capital_increase | 6.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 043260 | 성호전자 | convertible_bond | 5.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 163730 | 핑거 | paid_in_capital_increase | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 079950 | 인베니아 | disclosure_violation | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 069640 | 한세엠케이 | major_shareholder_change | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 009190 | 대양금속 | investment_decision | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 009190 | 대양금속 | investment_decision | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 084180 | 수성웹툰 | major_shareholder_change | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 003470 | 유안타증권 | major_shareholder_change | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 376270 | HEM파마 | convertible_bond | 3.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 064800 | 포니링크 | lawsuit | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 115450 | HLB테라퓨틱스 | convertible_bond | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 009190 | 대양금속 | major_shareholder_change | 3.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 009190 | 대양금속 | major_shareholder_change | 3.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
