"""
DART disclosure data collector.

This script collects disclosure list data from OpenDART
and saves the result as a CSV file under data/raw.
"""

import os
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import pandas as pd
import requests
from dotenv import load_dotenv


DART_LIST_URL = "https://opendart.fss.or.kr/api/list.json"
KST = ZoneInfo("Asia/Seoul")


def kst_business_day_yyyymmdd(now_utc: datetime | None = None) -> str:
    """
    Most recently completed Korean trading day (KST calendar date, rolled
    back over weekends to the prior Friday) as of `now_utc`.

    Using datetime.today() (naive local/UTC "today") here breaks whenever
    this job runs off its normal ~22:20 UTC schedule: GitHub Actions
    scheduled runs can fire hours late (observed: 7/24, 8/7, 8/27, 8/28), and
    a UTC morning/midday run maps to the SAME KST calendar day (still
    in-progress -- disclosures not yet fully filed) instead of the prior,
    fully-completed KST business day the normal 22:20 UTC -> 07:2x KST
    schedule happens to land on. That off-by-one produced a single-digit
    disclosure count on every affected run vs. teens/twenties normally.
    Computing explicitly from KST removes the dependency on what time this
    happens to run.
    """
    if now_utc is None:
        now_utc = datetime.now(timezone.utc)
    elif now_utc.tzinfo is None:
        now_utc = now_utc.replace(tzinfo=timezone.utc)

    business_day = now_utc.astimezone(KST).date() - timedelta(days=1)
    while business_day.weekday() >= 5:  # Saturday=5, Sunday=6
        business_day -= timedelta(days=1)
    return business_day.strftime("%Y%m%d")


def get_dart_api_key() -> str:
    """Load DART API key from .env file."""
    load_dotenv()
    api_key = os.getenv("DART_API_KEY")

    if not api_key:
        raise ValueError("DART_API_KEY is missing. Please check your .env file.")

    return api_key


def collect_disclosures(date_yyyymmdd: str) -> pd.DataFrame:
    """Collect DART disclosure list for a specific date."""
    api_key = get_dart_api_key()

    params = {
        "crtfc_key": api_key,
        "bgn_de": date_yyyymmdd,
        "end_de": date_yyyymmdd,
        "page_no": 1,
        "page_count": 100,
    }

    response = requests.get(DART_LIST_URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    status = data.get("status")
    message = data.get("message")

    if status != "000":
        print(f"DART API returned status={status}, message={message}")
        return pd.DataFrame()

    disclosures = data.get("list", [])

    if not disclosures:
        print("No disclosures found.")
        return pd.DataFrame()

    df = pd.DataFrame(disclosures)
    return df


def save_raw_data(df: pd.DataFrame, date_yyyymmdd: str) -> str:
    """Save disclosure data to CSV."""
    output_dir = "data/raw"
    os.makedirs(output_dir, exist_ok=True)

    output_path = f"{output_dir}/dart_disclosures_{date_yyyymmdd}.csv"
    df.to_csv(output_path, index=False, encoding="utf-8-sig")

    return output_path


def main():
    today = kst_business_day_yyyymmdd()

    print(f"Collecting DART disclosures for {today}...")

    df = collect_disclosures(today)

    if df.empty:
        print("No data saved.")
        return

    output_path = save_raw_data(df, today)

    print(f"Collected {len(df)} disclosures.")
    print(f"Saved to: {output_path}")
    print(df[["corp_name", "report_nm", "rcept_dt"]].head())


if __name__ == "__main__":
    main()
