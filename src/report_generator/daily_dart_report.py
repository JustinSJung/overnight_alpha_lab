"""
Daily DART report generator.

This script reads the latest parsed DART disclosure CSV file
and generates a Markdown report for portfolio/blog use.
"""

import os
from datetime import datetime

import pandas as pd


EVENT_LABELS = {
    "supply_contract": "Supply Contract",
    "paid_in_capital_increase": "Paid-in Capital Increase",
    "bonus_issue": "Bonus Issue",
    "convertible_bond": "Convertible Bond",
    "bond_with_warrant": "Bond with Warrant",
    "major_shareholder_change": "Major Shareholder Change",
    "insider_or_major_holder": "Insider or Major Holder Disclosure",
    "earnings_guidance": "Earnings Guidance",
    "lawsuit": "Lawsuit",
    "disclosure_violation": "Disclosure Violation",
    "investment_decision": "Investment Decision",
    "merger": "Merger",
    "spin_off": "Spin-off",
    "other": "Other",
    "unknown": "Unknown",
}


def get_latest_processed_file(processed_dir: str = "data/processed") -> str:
    """
    Find the latest parsed DART disclosure CSV file.
    """

    if not os.path.exists(processed_dir):
        raise FileNotFoundError(f"Processed data directory not found: {processed_dir}")

    csv_files = [
        file for file in os.listdir(processed_dir)
        if file.startswith("parsed_dart_disclosures_") and file.endswith(".csv")
    ]

    if not csv_files:
        raise FileNotFoundError("No parsed DART disclosure CSV files found.")

    csv_files.sort(reverse=True)
    return os.path.join(processed_dir, csv_files[0])


def extract_date_from_filename(file_path: str) -> str:
    """
    Extract date from filename and convert YYYYMMDD to YYYY-MM-DD.
    """

    filename = os.path.basename(file_path)
    date_part = filename.replace("parsed_dart_disclosures_", "").replace(".csv", "")

    return datetime.strptime(date_part, "%Y%m%d").strftime("%Y-%m-%d")


def format_event_label(event_type: str) -> str:
    """
    Convert event type code to readable label.
    """

    return EVENT_LABELS.get(event_type, event_type)


def build_event_summary(df: pd.DataFrame) -> str:
    """
    Build Markdown table for event type summary.
    """

    event_counts = df["event_type"].value_counts().reset_index()
    event_counts.columns = ["event_type", "count"]

    lines = []
    lines.append("| Event Type | Count |")
    lines.append("|---|---:|")

    for _, row in event_counts.iterrows():
        label = format_event_label(row["event_type"])
        count = row["count"]
        lines.append(f"| {label} | {count} |")

    return "\n".join(lines)


def build_key_disclosures(df: pd.DataFrame) -> str:
    """
    Build Markdown table for key disclosures.
    """

    key_event_types = [
        "supply_contract",
        "paid_in_capital_increase",
        "bonus_issue",
        "convertible_bond",
        "bond_with_warrant",
        "major_shareholder_change",
        "earnings_guidance",
        "lawsuit",
        "disclosure_violation",
        "investment_decision",
        "merger",
        "spin_off",
    ]

    key_df = df[df["event_type"].isin(key_event_types)].copy()

    if key_df.empty:
        return "No key disclosures were detected."

    lines = []
    lines.append("| Company | Disclosure | Event Type | Date |")
    lines.append("|---|---|---|---|")

    for _, row in key_df.head(30).iterrows():
        company = row.get("corp_name", "")
        report = row.get("report_nm", "")
        event_type = format_event_label(row.get("event_type", ""))
        date = row.get("rcept_dt", "")

        lines.append(f"| {company} | {report} | {event_type} | {date} |")

    return "\n".join(lines)


def build_insight_notes(df: pd.DataFrame) -> str:
    """
    Build simple analysis notes for the daily report.
    """

    total_count = len(df)
    key_count = len(df[df["event_type"] != "other"])

    supply_count = len(df[df["event_type"] == "supply_contract"])
    financing_count = len(
        df[
            df["event_type"].isin(
                [
                    "paid_in_capital_increase",
                    "convertible_bond",
                    "bond_with_warrant",
                ]
            )
        ]
    )
    insider_count = len(df[df["event_type"] == "insider_or_major_holder"])

    lines = []
    lines.append(f"- Total disclosures collected: {total_count}")
    lines.append(f"- Classified non-other events: {key_count}")
    lines.append(f"- Supply contract disclosures: {supply_count}")
    lines.append(f"- Financing-related disclosures: {financing_count}")
    lines.append(f"- Insider or major holder disclosures: {insider_count}")
    lines.append("")
    lines.append("## Model Notes")
    lines.append("")
    lines.append(
        "This report is an early-stage event classification output. "
        "The next step is to compare these events with next-day opening price reactions."
    )

    return "\n".join(lines)


def generate_markdown_report(df: pd.DataFrame, report_date: str) -> str:
    """
    Generate full Markdown report content.
    """

    event_summary = build_event_summary(df)
    key_disclosures = build_key_disclosures(df)
    insight_notes = build_insight_notes(df)

    report = f"""# {report_date} DART Event Report

## Overview

This report summarizes DART disclosures collected after market close and classifies them into event types for next-day market reaction analysis.

## Event Type Summary

{event_summary}

## Key Disclosures

{key_disclosures}

## Daily Insight Notes

{insight_notes}

## Disclaimer

This report is for data science research and portfolio purposes only. It is not investment advice.
"""

    return report


def save_report(markdown_content: str, report_date: str) -> str:
    """
    Save Markdown report.
    """

    output_dir = "reports/daily_prediction"
    os.makedirs(output_dir, exist_ok=True)

    output_path = f"{output_dir}/{report_date}_dart_event_report.md"

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(markdown_content)

    return output_path


def main():
    print("Generating daily DART event report...")

    input_path = get_latest_processed_file()
    report_date = extract_date_from_filename(input_path)

    print(f"Input file: {input_path}")
    print(f"Report date: {report_date}")

    df = pd.read_csv(input_path)

    markdown_content = generate_markdown_report(df, report_date)
    output_path = save_report(markdown_content, report_date)

    print(f"Report saved to: {output_path}")


if __name__ == "__main__":
    main()
