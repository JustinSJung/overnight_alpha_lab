# Social Attention Feature Report - 2026-08-18

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **22**
- High attention rows: **0**
- Medium attention rows: **13**
- Rumor-noise detected rows: **1**
- Risk-noise detected rows: **13**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 010960 | 삼호개발 | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 095270 | 웨이브일렉트로 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 033310 | 엠투엔 | major_shareholder_change | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 288980 | 모아데이타 | paid_in_capital_increase | 8.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 950220 | 네오이뮨텍 | investment_decision | 8.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 033540 | 파라텍 | convertible_bond | 7.5 | 4 | 6 | medium_attention | medium_rumor_noise | risk_noise_detected |
| 0009K0 | 에임드바이오 | investment_decision | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 363280 | 티와이홀딩스 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 009410 | 태영건설 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 340810 | 시선AI | paid_in_capital_increase | 6.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 038880 | 아이에이 | paid_in_capital_increase | 6.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 418620 | E8 | paid_in_capital_increase | 6.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 069920 | 엑시온그룹 | paid_in_capital_increase | 6.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 294090 | 이오플로우 | convertible_bond | 5.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 175250 | 아이큐어 | paid_in_capital_increase | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 001740 | SK네트웍스 | major_shareholder_change | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 003470 | 유안타증권 | major_shareholder_change | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 062970 | 한국첨단소재 | paid_in_capital_increase | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 142760 | 모아라이프플러스 | convertible_bond | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 196450 | 코아시아씨엠 | spin_off | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
