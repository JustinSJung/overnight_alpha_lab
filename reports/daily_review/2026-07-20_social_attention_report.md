# Social Attention Feature Report - 2026-07-20

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **19**
- High attention rows: **1**
- Medium attention rows: **11**
- Rumor-noise detected rows: **0**
- Risk-noise detected rows: **10**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 224060 | 더코디 | convertible_bond | 12.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 033310 | 엠투엔 | major_shareholder_change | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 078350 | 한양디지텍 | major_shareholder_change | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 033540 | 파라텍 | convertible_bond | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 389680 | 유디엠텍 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 354200 | 엔젠바이오 | paid_in_capital_increase | 7.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 354200 | 엔젠바이오 | paid_in_capital_increase | 7.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 354200 | 엔젠바이오 | paid_in_capital_increase | 7.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 354200 | 엔젠바이오 | paid_in_capital_increase | 7.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 144510 | 지씨셀 | investment_decision | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 003470 | 유안타증권 | major_shareholder_change | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 018470 | 조일알미늄 | major_shareholder_change | 6.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 142760 | 모아라이프플러스 | convertible_bond | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 082270 | 젬백스 | major_shareholder_change | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 950160 | 코오롱티슈진 | investment_decision | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 230360 | 에코마케팅 | merger | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 290720 | 푸드나무 | paid_in_capital_increase | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 055550 | 신한지주 | major_shareholder_change | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 112610 | 씨에스윈드 | major_shareholder_change | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
