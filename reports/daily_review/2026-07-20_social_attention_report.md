# Social Attention Feature Report - 2026-07-20

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **22**
- High attention rows: **3**
- Medium attention rows: **6**
- Rumor-noise detected rows: **0**
- Risk-noise detected rows: **17**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 065420 | 에스아이리소스 | supply_contract | 13.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 065420 | 에스아이리소스 | supply_contract | 13.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 224060 | 더코디 | convertible_bond | 12.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 033310 | 엠투엔 | major_shareholder_change | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 065420 | 에스아이리소스 | paid_in_capital_increase | 9.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 065420 | 에스아이리소스 | paid_in_capital_increase | 9.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 389680 | 유디엠텍 | supply_contract | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 144510 | 지씨셀 | investment_decision | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 431190 | 케이쓰리아이 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 354200 | 엔젠바이오 | paid_in_capital_increase | 5.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 290560 | 파라택시스이더리움 | merger | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 052770 | 아이톡시 | disclosure_violation | 3.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 087260 | 모바일어플라이언스 | disclosure_violation | 3.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 018700 | 졸스 | convertible_bond | 3.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 018700 | 졸스 | convertible_bond | 3.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 018700 | 졸스 | paid_in_capital_increase | 3.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 018700 | 졸스 | paid_in_capital_increase | 3.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 005710 | 대원산업 | lawsuit | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 255220 | SG | paid_in_capital_increase | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 290720 | 푸드나무 | paid_in_capital_increase | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
