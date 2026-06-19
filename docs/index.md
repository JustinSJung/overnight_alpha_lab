# Overnight Alpha Lab

Overnight Alpha Lab is an AI research portfolio project that analyzes corporate disclosures, news, and market data released after market close, then studies how the market reacts on the next trading day.

The goal is not to predict stock prices directly, but to model market reactions to newly released information through daily prediction logs, review reports, and error notes.

## Project Concept

1. Collect disclosures and market-related data after market close
2. Classify events such as supply contracts, capital increases, convertible bonds, lawsuits, and earnings guidance
3. Generate daily event reports
4. Compare events with next-day opening price reactions
5. Create error notes and improve the model over time

## Current Status

The project currently includes:

- OpenDART API data collection
- DART disclosure event classification
- Markdown daily report generation
- First generated DART event report

## Development Log

- [Day 1: DART API Collector and Event Report](posts/2026-06-18-day-1-dart-api.md)
- [Day 2: Automated Event Scoring Pipeline](posts/2026-06-18-day-2-automated-event-scoring.md)
- [Day 3: Prediction Review and Error Note Generator](posts/2026-06-18-day-3-error-note-generator.md)
- [Day 4: News Features and ML Dataset Builder](posts/2026-06-18-day-4-news-features-ml-dataset.md)
- [Day 5: Baseline Machine Learning Model](posts/2026-06-18-day-5-baseline-ml-model.md)
- [Day 6: Pending Event Re-Evaluation System](posts/2026-06-19-day-6-pending-re-evaluation.md)
- [Day 7: Local Daily Automation Scripts](posts/2026-06-19-day-7-local-daily-automation.md)
- [Day 8: Scheduled Local Automation](posts/2026-06-19-day-8-scheduled-local-automation.md)
- [Day 9: Catch-Up Execution Mode](posts/2026-06-19-day-9-catch-up-execution-mode.md)

## Repository

This project is maintained as a public GitHub repository.
