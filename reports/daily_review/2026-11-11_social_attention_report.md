# Social Attention Feature Report - 2026-11-11

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **98**
- High attention rows: **2**
- Medium attention rows: **49**
- Rumor-noise detected rows: **2**
- Risk-noise detected rows: **58**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 281820 | 케이씨텍 | supply_contract | 14.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 081180 | 쎄크 | supply_contract | 14.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 009540 | HD한국조선해양 | supply_contract | 11.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 412350 | 레이저쎌 | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 298060 | 풍전약품 | paid_in_capital_increase | 10.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 101360 | 에코앤드림 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 247540 | 에코프로비엠 | paid_in_capital_increase | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 069640 | 한세엠케이 | major_shareholder_change | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 457600 | 벡트로보틱스 | paid_in_capital_increase | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 010960 | 삼호개발 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 267250 | HD현대 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 347700 | 스피어 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 307180 | 아이엘 | convertible_bond | 8.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 001200 | 유진증권 | investment_decision | 8.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 191410 | 육일씨엔에쓰 | merger | 8.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 000390 | SP삼화 | investment_decision | 8.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 119610 | 인터로조 | major_shareholder_change | 8.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 001520 | 동양 | investment_decision | 7.5 | 4 | 0 | medium_attention | medium_rumor_noise | no_risk_noise |
| 224060 | 더코디 | convertible_bond | 7.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 224060 | 더코디 | convertible_bond | 7.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
