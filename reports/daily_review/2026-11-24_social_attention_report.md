# Social Attention Feature Report - 2026-11-24

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **87**
- High attention rows: **2**
- Medium attention rows: **44**
- Rumor-noise detected rows: **2**
- Risk-noise detected rows: **38**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 320000 | 한울반도체 | major_shareholder_change | 16.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 223220 | 로지스몬 | lawsuit | 12.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 003470 | 유안타증권 | major_shareholder_change | 10.5 | 4 | 0 | medium_attention | medium_rumor_noise | no_risk_noise |
| 003480 | 한진중공업홀딩스 | supply_contract | 10.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 000880 | 한화 | merger | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 012630 | HDC | investment_decision | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 417860 | 오브젠 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 375500 | DL이앤씨 | investment_decision | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 270520 | 앱튼 | paid_in_capital_increase | 8.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 362990 | 드림인사이트 | major_shareholder_change | 8.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 034730 | SK | merger | 8.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 348370 | 엔켐 | major_shareholder_change | 8.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 329180 | HD현대중공업 | major_shareholder_change | 8.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 009830 | 한화솔루션 | merger | 7.5 | 4 | 0 | medium_attention | medium_rumor_noise | no_risk_noise |
| 299660 | 셀리드 | lawsuit | 7.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 299660 | 셀리드 | lawsuit | 7.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 299660 | 셀리드 | paid_in_capital_increase | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 299660 | 셀리드 | paid_in_capital_increase | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 009730 | 이렘 | paid_in_capital_increase | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 009730 | 이렘 | paid_in_capital_increase | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
