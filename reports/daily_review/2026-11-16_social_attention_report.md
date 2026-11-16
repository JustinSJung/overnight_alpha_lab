# Social Attention Feature Report - 2026-11-16

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **58**
- High attention rows: **2**
- Medium attention rows: **28**
- Rumor-noise detected rows: **0**
- Risk-noise detected rows: **31**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 049080 | 기가레인 | supply_contract | 15.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 254120 | 자비스 | supply_contract | 12.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 032790 | 엠젠솔루션 | convertible_bond | 11.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 180060 | 탑선 | supply_contract | 10.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 180060 | 탑선 | supply_contract | 10.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 383930 | 디티앤씨알오 | supply_contract | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 419080 | 엔젯 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 347700 | 스피어 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 070960 | 모나용평 | major_shareholder_change | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 321820 | 아티스트컴퍼니 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 058730 | 다스코 | bond_with_warrant | 8.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 182360 | 큐브엔터 | convertible_bond | 8.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 003470 | 유안타증권 | major_shareholder_change | 8.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 020560 | 아시아나항공 | merger | 8.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 142760 | 모아라이프플러스 | convertible_bond | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 142760 | 모아라이프플러스 | convertible_bond | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 282880 | 코윈로보틱스 | supply_contract | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 142760 | 모아라이프플러스 | major_shareholder_change | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 142760 | 모아라이프플러스 | major_shareholder_change | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 145270 | 케이탑리츠 | major_shareholder_change | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
