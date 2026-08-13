# Social Attention Feature Report - 2026-08-13

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **15**
- High attention rows: **0**
- Medium attention rows: **3**
- Rumor-noise detected rows: **0**
- Risk-noise detected rows: **12**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 009160 | SIMPAC | investment_decision | 8.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 028050 | 삼성E&A | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 001340 | PKC | major_shareholder_change | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 215480 | 토박스코리아 | lawsuit | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 407400 | 꿈비 | lawsuit | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 071050 | 한국금융지주 | investment_decision | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 107640 | 한중엔시에스 | convertible_bond | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 248070 | 솔루엠 | paid_in_capital_increase | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 043260 | 성호전자 | convertible_bond | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 043260 | 성호전자 | convertible_bond | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 043260 | 성호전자 | convertible_bond | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 043260 | 성호전자 | convertible_bond | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 069460 | 대호에이엘 | lawsuit | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 001040 | CJ | lawsuit | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 079160 | CJ CGV | lawsuit | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
