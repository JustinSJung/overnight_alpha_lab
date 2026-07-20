# NAVER API Migration Plan

## 1. Current Dependency

Overnight Alpha Lab currently has a Naver Developers Search API based news layer through the existing news collector.

This path is useful as a supplementary news signal, but it should not be treated as a permanent single point of dependency. The current API surface, quota, access path, or product packaging may change over time.

## 2. Migration Target

If needed, the target migration path is NAVER API HUB.

The system should keep a provider abstraction so the research dashboard is not locked into a single news vendor. Price learning remains based on Korea Investment API price-candidate evaluation; news providers are supplementary context only.

## 3. Fallback Providers

- Google News RSS
- Official news RSS feeds
- Snacks/global market digest
- DART/KRX official data
- Future NAVER API HUB provider

## 4. Design Rules

- Provider failures must not kill the main KIS price pipeline.
- News and SNS data are supplementary, not the primary learning engine.
- No unofficial login scraping.
- No personal data collection.
- No aggressive page scraping.
- Missing provider data should be shown as insufficient data, not as a pipeline failure.

## 5. Reserved Environment Variables

These names are reserved for future migration work. Do not commit secret values.

```text
NAVER_API_HUB_CLIENT_ID
NAVER_API_HUB_CLIENT_SECRET
NEWS_PROVIDER_MODE
```

## 6. Near-Term Plan

1. Keep the current Naver collector if it still works.
2. Add Google News RSS as a conservative fallback provider.
3. Keep all provider failures optional in the catch-up pipeline.
4. Add a NAVER API HUB provider later if credentials become available.
5. Keep dashboard wording clear: news is a supplementary signal, not a trading trigger.

## Korean Summary

현재 Naver Developers Search API 기반 뉴스 수집기는 유지하되, 장기적으로 NAVER API HUB 전환 가능성을 열어둡니다. Google News RSS는 보조 fallback으로 사용하며, 어떤 뉴스 provider도 KIS 가격 기반 학습 파이프라인을 중단시키면 안 됩니다. 이 프로젝트는 연구/포트폴리오 대시보드이며 투자 조언이나 자동매매 시스템이 아닙니다.
