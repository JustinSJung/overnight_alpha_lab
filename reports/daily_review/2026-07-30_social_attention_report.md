# Social Attention Feature Report - 2026-07-30

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **31**
- High attention rows: **0**
- Medium attention rows: **8**
- Rumor-noise detected rows: **0**
- Risk-noise detected rows: **22**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 007110 | 일신석재 | supply_contract | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 012630 | HDC | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 294870 | IPARK현대산업개발 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 089140 | 넥스턴앤롤코리아 | major_shareholder_change | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 013580 | 계룡건설산업 | investment_decision | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 028100 | 동아지질 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 099750 | 이지케어텍 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 407400 | 꿈비 | lawsuit | 6.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 223220 | 로지스몬 | paid_in_capital_increase | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 223220 | 로지스몬 | paid_in_capital_increase | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 223220 | 로지스몬 | paid_in_capital_increase | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 223220 | 로지스몬 | paid_in_capital_increase | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 069920 | 엑시온그룹 | paid_in_capital_increase | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 069920 | 엑시온그룹 | paid_in_capital_increase | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 073640 | 테라사이언스 | paid_in_capital_increase | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 069920 | 엑시온그룹 | convertible_bond | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 069920 | 엑시온그룹 | convertible_bond | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 000660 | SK하이닉스 | major_shareholder_change | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 003470 | 유안타증권 | major_shareholder_change | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 058450 | 한주에이알티 | paid_in_capital_increase | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
