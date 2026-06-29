# Social Attention Feature Report - 2026-06-29

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **23**
- High attention rows: **1**
- Medium attention rows: **13**
- Rumor-noise detected rows: **1**
- Risk-noise detected rows: **17**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 208640 | 썸에이지 | paid_in_capital_increase | 12.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 445680 | 큐리옥스바이오시스템즈 | convertible_bond | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 006050 | 국영지앤엠 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 006050 | 국영지앤엠 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 006050 | 국영지앤엠 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 006050 | 국영지앤엠 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 260870 | SK시그넷 | paid_in_capital_increase | 8.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 069920 | 엑시온그룹 | disclosure_violation | 7.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 109740 | 디에스케이 | major_shareholder_change | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 214370 | 케어젠 | disclosure_violation | 6.5 | 4 | 3 | medium_attention | medium_rumor_noise | risk_noise_detected |
| 247540 | 에코프로비엠 | lawsuit | 6.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 373200 | 엑스플러스 | disclosure_violation | 6.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 317770 | 엑스페릭스 | convertible_bond | 6.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 245620 | EDGC | major_shareholder_change | 6.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 068240 | 다원시스 | disclosure_violation | 5.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 079940 | 가비아 | lawsuit | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 381970 | 케이카 | investment_decision | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 083660 | CSA 코스믹 | paid_in_capital_increase | 3.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 083660 | CSA 코스믹 | paid_in_capital_increase | 3.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 083660 | CSA 코스믹 | spin_off | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
