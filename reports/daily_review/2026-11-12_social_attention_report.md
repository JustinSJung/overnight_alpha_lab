# Social Attention Feature Report - 2026-11-12

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **74**
- High attention rows: **2**
- Medium attention rows: **32**
- Rumor-noise detected rows: **0**
- Risk-noise detected rows: **36**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 013120 | 동원개발 | supply_contract | 13.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 046890 | 서울반도체 | earnings_guidance | 12.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 115440 | 우리넷 | lawsuit | 11.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 032680 | 소프트센 | paid_in_capital_increase | 11.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 064480 | 브리지텍 | supply_contract | 11.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 097230 | HJ중공업 | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 065450 | 빅텍 | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 086520 | 에코프로 | paid_in_capital_increase | 10.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 030530 | 원익홀딩스 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 189860 | 서전기전 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 388050 | 지투파워 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 159910 | 에코글로우 | paid_in_capital_increase | 9.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 002990 | 금호건설 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 340360 | 다보링크 | disclosure_violation | 8.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 142760 | 모아라이프플러스 | major_shareholder_change | 8.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 142760 | 모아라이프플러스 | major_shareholder_change | 8.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 025890 | 한국주강 | major_shareholder_change | 8.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 091440 | 한울소재과학 | lawsuit | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 065650 | 하이퍼코퍼레이션 | paid_in_capital_increase | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 224060 | 더코디 | paid_in_capital_increase | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
