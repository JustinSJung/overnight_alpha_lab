# Social Attention Feature Report - 2026-07-06

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **25**
- High attention rows: **0**
- Medium attention rows: **4**
- Rumor-noise detected rows: **0**
- Risk-noise detected rows: **13**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 276730 | 한울앤제주 | convertible_bond | 9.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 049950 | 미래컴퍼니 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 187870 | 디바이스 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 321370 | 센서뷰 | paid_in_capital_increase | 6.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 023440 | 제이스코홀딩스 | convertible_bond | 5.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 419540 | 비스토스 | convertible_bond | 5.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 003490 | 대한항공 | merger | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 020560 | 아시아나항공 | merger | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 018260 | 삼성에스디에스 | major_shareholder_change | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 002780 | 진흥기업 | investment_decision | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 006730 | 서부T&D | major_shareholder_change | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 088790 | 진도 | lawsuit | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 322780 | 코퍼스코리아 | lawsuit | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 004990 | 롯데지주 | paid_in_capital_increase | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 025980 | 아난티 | convertible_bond | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 069460 | 대호에이엘 | lawsuit | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 0126Z0 | 삼성에피스홀딩스 | major_shareholder_change | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 115480 | 씨유메디칼 | convertible_bond | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 038530 | 케이바이오랩스 | paid_in_capital_increase | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 036630 | 세종텔레콤 | paid_in_capital_increase | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
