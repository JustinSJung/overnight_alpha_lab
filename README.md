# Overnight Alpha Lab

Overnight Alpha Lab is an AI research project that analyzes corporate disclosures, news, and market data released after market close, predicts next-day opening reactions, and improves the model through daily error notes.

This project focuses not on predicting stock prices directly, but on modeling how the market reacts to newly released information.

## Core Concept

1. Collect disclosures, news, and market data after market close
2. Generate next-day opening reaction predictions
3. Compare predictions with actual market results
4. Create daily error notes
5. Improve the model through continuous feedback

## Project Scope

- Korean stock market event analysis
- DART disclosure data
- News and sentiment data
- Next-day opening reaction prediction
- Daily prediction review
- Error-note based model improvement

## Repository Structure

```text
overnight_alpha_lab/
├── data/
│   ├── raw/
│   ├── processed/
│   └── predictions/
├── notebooks/
├── src/
│   ├── crawler/
│   ├── parser/
│   ├── features/
│   ├── models/
│   ├── evaluator/
│   └── report_generator/
├── reports/
│   ├── daily_prediction/
│   ├── daily_review/
│   └── error_notes/
├── blog/
│   └── _posts/
├── README.md
└── requirements.txt

## Status

project setup stage.

## Current Progress

The project currently includes:

- GitHub repository and Python project structure
- OpenDART API disclosure collection
- DART disclosure event parsing
- Daily Markdown report generation
- Korean stock price data collection
- Event-price reaction evaluation
- Automated key event selection pipeline
- Rule-based event scoring model
- Prediction review and error-note generation
- GitHub Pages portfolio blog

## Current Pipeline

```text
DART Disclosure Collection
↓
Disclosure Event Parsing
↓
Key Event Selection
↓
Rule-Based Event Scoring
↓
Stock Price Data Collection
↓
Event-Price Reaction Evaluation
↓
Prediction Review and Error Note Generation
↓
Daily Report and Blog Documentation


## Latest Blog Posts

* Day 1: DART API Collector and Event Report
* Day 2: Automated Event Scoring Pipeline
* Day 3: Prediction Review and Error Note Generator

## Next Steps

- Add news metadata collection
- Connect news events with DART disclosure events
- Add sentiment and investor attention indicators
- Build a machine learning dataset from event-reaction history
- Improve prediction confidence through continuous simulation and error analysis

