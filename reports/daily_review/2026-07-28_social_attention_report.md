# Social Attention Feature Report - 2026-07-28

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **22**
- High attention rows: **0**
- Medium attention rows: **10**
- Rumor-noise detected rows: **0**
- Risk-noise detected rows: **13**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 028260 | 삼성물산 | supply_contract | 11.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 341170 | 퓨쳐메디신 | disclosure_violation | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 047040 | 대우건설 | investment_decision | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 223220 | 로지스몬 | disclosure_violation | 8.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 226330 | 신테카바이오 | major_shareholder_change | 8.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 064350 | 현대로템 | investment_decision | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 130660 | 한전산업 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 069920 | 엑시온그룹 | paid_in_capital_increase | 6.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 071200 | 인피니트헬스케어 | lawsuit | 6.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 010060 | OCI홀딩스 | major_shareholder_change | 6.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 082270 | 젬백스 | major_shareholder_change | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 217730 | 강스템바이오텍 | investment_decision | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 083640 | 인콘 | investment_decision | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 210980 | SK디앤디 | paid_in_capital_increase | 3.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 069460 | 대호에이엘 | lawsuit | 3.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 060900 | 에이전트AI | paid_in_capital_increase | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 340810 | 시선AI | paid_in_capital_increase | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 032800 | 판타지오 | paid_in_capital_increase | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 004780 | 대륙제관 | disclosure_violation | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 009810 | 플레이그램 | paid_in_capital_increase | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
