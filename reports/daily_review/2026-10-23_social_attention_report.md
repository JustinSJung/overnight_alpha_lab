# Social Attention Feature Report - 2026-10-23

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **73**
- High attention rows: **2**
- Medium attention rows: **31**
- Rumor-noise detected rows: **5**
- Risk-noise detected rows: **36**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 335870 | 윙스풋 | convertible_bond | 12.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 019170 | 신풍제약 | investment_decision | 12.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 129920 | 대성하이텍 | major_shareholder_change | 11.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 028050 | 삼성E&A | earnings_guidance | 10.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 004150 | 한솔홀딩스 | major_shareholder_change | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 026910 | 광진실업 | paid_in_capital_increase | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 143540 | 영우디에스피 | supply_contract | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 396470 | 워트 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 078130 | 에스엠국일 | merger | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 078130 | 에스엠국일 | merger | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 000720 | 현대건설 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 460470 | 아이빔테크놀로지 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 003380 | 하림지주 | supply_contract | 7.5 | 4 | 0 | medium_attention | medium_rumor_noise | no_risk_noise |
| 083640 | 인콘 | convertible_bond | 7.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 012450 | 한화에어로스페이스 | supply_contract | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 028670 | 팬오션 | supply_contract | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 068270 | 셀트리온 | investment_decision | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 011560 | 세보엠이씨 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 078130 | 에스엠국일 | investment_decision | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 078130 | 에스엠국일 | investment_decision | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
