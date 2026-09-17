# Social Attention Feature Report - 2026-09-17

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **75**
- High attention rows: **1**
- Medium attention rows: **29**
- Rumor-noise detected rows: **0**
- Risk-noise detected rows: **41**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 014970 | 삼륭물산 | disclosure_violation | 12.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 228670 | 레이 | major_shareholder_change | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 083470 | 이엠앤아이 | major_shareholder_change | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 083470 | 이엠앤아이 | major_shareholder_change | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 006730 | 서부T&D | major_shareholder_change | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 455180 | 케이지에이 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 031820 | 아이티센씨티에스 | paid_in_capital_increase | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 226950 | 올릭스 | investment_decision | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 065450 | 빅텍 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 083650 | 비에이치아이 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 257370 | 피엔티엠에스 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 288980 | 모아데이타 | paid_in_capital_increase | 8.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 092600 | 앤씨앤 | paid_in_capital_increase | 8.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 083470 | 이엠앤아이 | paid_in_capital_increase | 8.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 083470 | 이엠앤아이 | paid_in_capital_increase | 8.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 000430 | 대원강업 | major_shareholder_change | 8.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 011810 | STX | investment_decision | 8.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 011810 | STX | investment_decision | 8.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 033310 | 엠투엔 | major_shareholder_change | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 354200 | 엔젠바이오 | paid_in_capital_increase | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
