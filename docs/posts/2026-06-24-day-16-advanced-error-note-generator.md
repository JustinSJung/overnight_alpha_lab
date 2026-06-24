# Day 16: Advanced Error Note Generator

## What I Built Today

Today, I improved the error-note generator in Overnight Alpha Lab.

Until now, the system could compare prediction direction with actual next-day price reaction and classify the result as:

```text
success
failure
pending
```

That was useful, but it was still too simple.

Today, I upgraded the error-note system so it can explain why a prediction may have failed and what should be adjusted in future rules.

## Why This Matters

The long-term goal of this project is not only to generate stock candidates.

The goal is to build a system that can learn from its own prediction results.

To do that, the system needs more than a success/failure label.

It needs structured feedback.

The advanced error-note generator is the first version of that feedback layer.

## Updated File

The updated file is:

```text
src/evaluator/error_note_generator.py
```

The output file is still saved under:

```text
data/predictions/error_notes_YYYYMMDD.csv
```

## What Changed

The previous error-note generator mainly checked whether the prediction direction matched the actual next-day return.

The new version adds more detailed columns.

```text
error_category
detailed_error_reason
learning_point
next_rule_adjustment
confidence_adjustment
```

## New Error Categories

The system now classifies prediction outcomes into more specific patterns.

Examples include:

```text
pending_price_data
positive_signal_confirmed
negative_signal_confirmed
volatility_signal_confirmed
weak_positive_signal
positive_signal_with_negative_noise
low_attention_positive_signal
risk_event_misclassified
negative_signal_reversed
volatility_overestimated
volatility_direction_mismatch
general_prediction_failure
```

This makes the error-note output more useful for future learning.

## Example

A simple failure case used to look like this:

```text
prediction_result: failure
```

Now it can look like this:

```text
prediction_result: failure
error_category: weak_positive_signal
detailed_error_reason: The prediction was positive, but news sentiment was weak and the actual next close return was negative.
learning_point: Positive event predictions should be treated more conservatively when news sentiment is weak.
next_rule_adjustment: Decrease confidence for positive events when news_sentiment_score is less than or equal to zero.
confidence_adjustment: decrease
```

This is much more useful because it tells the system what kind of mistake happened.

## How It Works

The generator combines information from:

```text
scored key events
news feature data
event-price reaction data
```

Then it evaluates each prediction using:

```text
prediction_direction
event_type
event_score
news_sentiment_score
news_attention_score
negative_keyword_count
next_open_return
next_close_return
```

Based on these values, it creates a more detailed learning note.

## Why This Is Progress

This step moves the project from simple prediction tracking to structured learning.

The project can now follow this loop:

```text
Predict
↓
Observe actual price reaction
↓
Classify success/failure/pending
↓
Explain why it may have succeeded or failed
↓
Suggest next rule adjustment
↓
Adjust confidence direction
```

This is an important step toward making the system improve over time.

## Current System Status

The project now includes:

```text
DART disclosure collection
Disclosure event parsing
Key event selection
Rule-based event scoring
Naver news metadata collection
News feature generation
Stock price data collection
Event-price reaction evaluation
Advanced error-note generation
Machine learning dataset building
Baseline machine learning model
Return prediction model
Daily stock recommender
Single stock predictor
Pending event re-evaluation
Local automation scripts
Scheduled cron automation
Catch-up execution mode
Automation status report
Automation history tracker
Confidence tracker
Execution log generation
```

## Next Step

The next step is to make the recommendation system use these advanced error notes.

For example, if the same event type repeatedly receives:

```text
confidence_adjustment: decrease
```

then future recommendation scores should become more conservative for that event type.

This will make the system closer to a real learning loop.

