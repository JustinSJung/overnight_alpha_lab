# Day 1: Building the DART API Collector and Event Report Generator

## What I Built Today

Today, I set up the initial pipeline for Overnight Alpha Lab.

The first version of the system can:

1. Connect to the OpenDART API
2. Collect daily corporate disclosure data
3. Classify disclosures into event types
4. Generate a Markdown-based daily event report

## Why This Matters

The purpose of this project is not to predict stock prices directly.

Instead, the goal is to analyze how the market reacts to newly released information, especially disclosures and news released after market close.

By collecting daily events and comparing them with next-day price reactions, the system will gradually build an error-note based learning process.

## Current Pipeline

```text
OpenDART API
↓
DART disclosure collector
↓
Disclosure event parser
↓
Daily Markdown report generator
↓
Future: next-day price reaction review
