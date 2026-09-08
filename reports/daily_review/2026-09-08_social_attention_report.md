# Social Attention Feature Report - 2026-09-08

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **75**
- High attention rows: **3**
- Medium attention rows: **29**
- Rumor-noise detected rows: **3**
- Risk-noise detected rows: **30**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 000210 | DL | supply_contract | 13.5 | 8 | 0 | high_attention | high_rumor_noise | no_risk_noise |
| 375500 | DL이앤씨 | supply_contract | 13.5 | 8 | 0 | high_attention | high_rumor_noise | no_risk_noise |
| 045100 | 한양이엔지 | supply_contract | 13.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 033790 | 피노 | paid_in_capital_increase | 11.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 320000 | 한울반도체 | major_shareholder_change | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 288980 | 모아데이타 | major_shareholder_change | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 083790 | CG인바이츠 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 040910 | 아이씨디 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 016610 | DB증권 | major_shareholder_change | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 046940 | 우원개발 | supply_contract | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 002780 | 진흥기업 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 001230 | 동국홀딩스 | major_shareholder_change | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 056090 | 시지메드텍 | spin_off | 8.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 0126Z0 | 삼성에피스홀딩스 | major_shareholder_change | 8.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 294870 | IPARK현대산업개발 | disclosure_violation | 7.5 | 8 | 3 | medium_attention | high_rumor_noise | risk_noise_detected |
| 023440 | 제이스코홀딩스 | major_shareholder_change | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 310210 | 보로노이 | investment_decision | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 067080 | 대화제약 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 004410 | 서울식품공업 | major_shareholder_change | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 033310 | 엠투엔 | major_shareholder_change | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
