# Social Attention Feature Report - 2026-09-01

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **143**
- High attention rows: **3**
- Medium attention rows: **85**
- Rumor-noise detected rows: **1**
- Risk-noise detected rows: **70**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 219550 | 디와이디 | convertible_bond | 14.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 282720 | 금양그린파워 | supply_contract | 13.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 480370 | 씨케이솔루션 | supply_contract | 12.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 083660 | CSA 코스믹 | paid_in_capital_increase | 11.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 012450 | 한화에어로스페이스 | supply_contract | 11.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 002460 | HS화성 | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 002460 | HS화성 | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 115530 | 씨엔플러스 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 115450 | HLB테라퓨틱스 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 418620 | E8 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 174900 | 앱클론 | supply_contract | 9.5 | 4 | 0 | medium_attention | medium_rumor_noise | no_risk_noise |
| 106240 | 파인테크닉스 | convertible_bond | 9.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 291230 | 컴투스엔 | convertible_bond | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 002020 | 코오롱 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 003070 | 코오롱글로벌 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 047810 | 한국항공우주 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 016380 | KG스틸 | merger | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 024900 | 디와이덕양 | major_shareholder_change | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 010960 | 삼호개발 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 010960 | 삼호개발 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
