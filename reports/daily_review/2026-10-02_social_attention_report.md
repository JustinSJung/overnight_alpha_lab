# Social Attention Feature Report - 2026-10-02

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **84**
- High attention rows: **5**
- Medium attention rows: **37**
- Rumor-noise detected rows: **2**
- Risk-noise detected rows: **34**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 138080 | 오이솔루션 | major_shareholder_change | 21.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 399720 | 가온칩스 | supply_contract | 19.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 003160 | 디아이 | supply_contract | 19.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 431190 | 케이쓰리아이 | paid_in_capital_increase | 15.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 358570 | 지아이이노베이션 | investment_decision | 12.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 224060 | 더코디 | paid_in_capital_increase | 11.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 224060 | 더코디 | paid_in_capital_increase | 11.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 224060 | 더코디 | convertible_bond | 11.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 224060 | 더코디 | convertible_bond | 11.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 118000 | 메타케어 | merger | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 480370 | 씨케이솔루션 | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 0126Z0 | 삼성에피스홀딩스 | investment_decision | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 082270 | 젬백스 | major_shareholder_change | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 028050 | 삼성E&A | major_shareholder_change | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 000250 | 삼천당제약 | supply_contract | 9.5 | 4 | 3 | medium_attention | medium_rumor_noise | risk_noise_detected |
| 034020 | 두산에너빌리티 | supply_contract | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 010950 | S-Oil | major_shareholder_change | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 010950 | S-Oil | major_shareholder_change | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 214430 | 아이쓰리시스템 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 036810 | 에프에스티 | major_shareholder_change | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
