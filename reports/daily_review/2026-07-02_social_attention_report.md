# Social Attention Feature Report - 2026-07-02

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **19**
- High attention rows: **2**
- Medium attention rows: **5**
- Rumor-noise detected rows: **0**
- Risk-noise detected rows: **8**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 010960 | 삼호개발 | supply_contract | 18.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 372800 | 아이티아이즈 | supply_contract | 13.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 115160 | 휴맥스 | merger | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 317770 | 엑스페릭스 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 143210 | 핸즈코퍼레이션 | supply_contract | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 001360 | 삼성제약 | investment_decision | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 007280 | 한국특강 | major_shareholder_change | 6.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 159910 | 에코글로우 | convertible_bond | 5.5 | 0 | 9 | low_attention | no_rumor_signal | high_risk_noise |
| 123010 | 알엔티엑스 | spin_off | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 028050 | 삼성E&A | major_shareholder_change | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 019570 | 플루토스 | convertible_bond | 3.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 276730 | 한울앤제주 | convertible_bond | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 276730 | 한울앤제주 | convertible_bond | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 276730 | 한울앤제주 | paid_in_capital_increase | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 276730 | 한울앤제주 | paid_in_capital_increase | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 014680 | 한솔케미칼 | major_shareholder_change | 3.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 014680 | 한솔케미칼 | major_shareholder_change | 3.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 014680 | 한솔케미칼 | major_shareholder_change | 3.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 014680 | 한솔케미칼 | major_shareholder_change | 3.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
