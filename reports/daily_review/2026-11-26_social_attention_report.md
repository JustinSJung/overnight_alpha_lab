# Social Attention Feature Report - 2026-11-26

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **83**
- High attention rows: **6**
- Medium attention rows: **47**
- Rumor-noise detected rows: **0**
- Risk-noise detected rows: **28**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 178320 | 서진시스템 | supply_contract | 18.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 129920 | 대성하이텍 | supply_contract | 16.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 048410 | 현대바이오 | investment_decision | 15.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 478340 | 나라스페이스테크놀로지 | supply_contract | 13.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 180060 | 탑선 | supply_contract | 12.5 | 0 | 6 | high_attention | no_rumor_signal | risk_noise_detected |
| 223220 | 로지스몬 | lawsuit | 12.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 034730 | SK | merger | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 355390 | 크라우드웍스 | major_shareholder_change | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 010170 | 대한광통신 | merger | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 010170 | 대한광통신 | merger | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 010170 | 대한광통신 | merger | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 010170 | 대한광통신 | merger | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 010170 | 대한광통신 | merger | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 010170 | 대한광통신 | merger | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 010170 | 대한광통신 | merger | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 010170 | 대한광통신 | merger | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 010170 | 대한광통신 | merger | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 013580 | 계룡건설산업 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 065650 | 하이퍼코퍼레이션 | convertible_bond | 9.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 003470 | 유안타증권 | major_shareholder_change | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
