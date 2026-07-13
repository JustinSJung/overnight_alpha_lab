# Social Attention Feature Report - 2026-07-13

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **25**
- High attention rows: **0**
- Medium attention rows: **5**
- Rumor-noise detected rows: **1**
- Risk-noise detected rows: **20**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 079190 | 케스피온 | merger | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 465770 | STX그린로지스 | investment_decision | 8.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 375500 | DL이앤씨 | supply_contract | 7.5 | 4 | 3 | medium_attention | medium_rumor_noise | risk_noise_detected |
| 001840 | 이화공영 | supply_contract | 7.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 020710 | 시공테크 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 023440 | 제이스코홀딩스 | convertible_bond | 5.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 018500 | 동원금속 | disclosure_violation | 5.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 003490 | 대한항공 | merger | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 020560 | 아시아나항공 | merger | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 368970 | 오에스피 | paid_in_capital_increase | 3.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 318060 | 그래피 | convertible_bond | 3.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 007460 | 에이프로젠 | convertible_bond | 3.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 084180 | 수성웹툰 | convertible_bond | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 084180 | 수성웹툰 | convertible_bond | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 084180 | 수성웹툰 | convertible_bond | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 010130 | 고려아연 | lawsuit | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 084180 | 수성웹툰 | convertible_bond | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 084180 | 수성웹툰 | convertible_bond | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 084180 | 수성웹툰 | convertible_bond | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 084180 | 수성웹툰 | convertible_bond | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
