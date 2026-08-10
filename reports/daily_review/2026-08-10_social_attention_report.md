# Social Attention Feature Report - 2026-08-10

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **27**
- High attention rows: **0**
- Medium attention rows: **3**
- Rumor-noise detected rows: **0**
- Risk-noise detected rows: **5**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 130660 | 한전산업 | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 012630 | HDC | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 294870 | IPARK현대산업개발 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 215480 | 토박스코리아 | lawsuit | 5.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 065420 | 에스아이리소스 | lawsuit | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 228670 | 레이 | major_shareholder_change | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 228670 | 레이 | major_shareholder_change | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 228670 | 레이 | major_shareholder_change | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 228670 | 레이 | major_shareholder_change | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 383800 | LX홀딩스 | major_shareholder_change | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 383800 | LX홀딩스 | major_shareholder_change | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 003470 | 유안타증권 | major_shareholder_change | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 002420 | 세기상사 | merger | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 002420 | 세기상사 | merger | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 002420 | 세기상사 | merger | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 064400 | LG씨엔에스 | investment_decision | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 383800 | LX홀딩스 | major_shareholder_change | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 383800 | LX홀딩스 | major_shareholder_change | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 069460 | 대호에이엘 | lawsuit | 3.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 007460 | 에이프로젠 | convertible_bond | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
