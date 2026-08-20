# Social Attention Feature Report - 2026-08-20

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **22**
- High attention rows: **0**
- Medium attention rows: **7**
- Rumor-noise detected rows: **0**
- Risk-noise detected rows: **13**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 288980 | 모아데이타 | major_shareholder_change | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 003470 | 유안타증권 | major_shareholder_change | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 226340 | 본느 | lawsuit | 8.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 104460 | 디와이피엔에프 | supply_contract | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 192820 | 코스맥스 | merger | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 484870 | 엠앤씨솔루션 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 261200 | 덴티스 | major_shareholder_change | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 089140 | 넥스턴앤롤코리아 | convertible_bond | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 089140 | 넥스턴앤롤코리아 | convertible_bond | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 089140 | 넥스턴앤롤코리아 | convertible_bond | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 089140 | 넥스턴앤롤코리아 | convertible_bond | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 305090 | 마이크로디지탈 | convertible_bond | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 062970 | 한국첨단소재 | paid_in_capital_increase | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 366030 | 나인앤컴퍼니 | major_shareholder_change | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 366030 | 나인앤컴퍼니 | major_shareholder_change | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 366030 | 나인앤컴퍼니 | major_shareholder_change | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 366030 | 나인앤컴퍼니 | major_shareholder_change | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 276730 | 한울앤제주 | spin_off | 3.5 | 0 | 9 | low_attention | no_rumor_signal | high_risk_noise |
| 083470 | 이엠앤아이 | paid_in_capital_increase | 3.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 900300 | 오가닉티코스메틱 | paid_in_capital_increase | 3.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
