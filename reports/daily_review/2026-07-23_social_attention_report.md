# Social Attention Feature Report - 2026-07-23

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **25**
- High attention rows: **2**
- Medium attention rows: **6**
- Rumor-noise detected rows: **1**
- Risk-noise detected rows: **12**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 045390 | 대아티아이 | supply_contract | 13.5 | 4 | 0 | high_attention | medium_rumor_noise | no_risk_noise |
| 089140 | 넥스턴앤롤코리아 | major_shareholder_change | 12.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 234300 | 에스트래픽 | major_shareholder_change | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 297890 | HB솔루션 | supply_contract | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 025560 | 미래산업 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 028080 | 휴맥스홀딩스 | merger | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 017670 | SK텔레콤 | investment_decision | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 069920 | 엑시온그룹 | convertible_bond | 6.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 005940 | NH투자증권 | major_shareholder_change | 5.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 001420 | 태원물산 | lawsuit | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 034730 | SK | investment_decision | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 002990 | 금호건설 | investment_decision | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 039200 | 오스코텍 | major_shareholder_change | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 039200 | 오스코텍 | major_shareholder_change | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 001260 | 남광토건 | investment_decision | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 115160 | 휴맥스 | merger | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 309930 | 조이웍스앤코 | convertible_bond | 3.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 309930 | 조이웍스앤코 | convertible_bond | 3.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 309930 | 조이웍스앤코 | convertible_bond | 3.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 309930 | 조이웍스앤코 | convertible_bond | 3.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
