"""
DART disclosure data collector.

This script collects disclosure list data from OpenDART
and saves the result as a CSV file under data/raw.
"""

import json
import os
import time
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import pandas as pd
import requests
from dotenv import load_dotenv


DART_LIST_URL = "https://opendart.fss.or.kr/api/list.json"
KST = ZoneInfo("Asia/Seoul")
PAGE_COUNT = 100
MAX_PAGE_RETRIES = 3
RETRY_BACKOFF_SECONDS = 2
BETWEEN_PAGE_SLEEP_SECONDS = 0.3


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


def fetch_page(api_key: str, date_yyyymmdd: str, page_no: int) -> dict | None:
    """
    Fetch one page of the DART disclosure list, retrying transient failures
    up to MAX_PAGE_RETRIES times. Returns the parsed JSON response, or None
    if every attempt failed.
    """
    params = {
        "crtfc_key": api_key,
        "bgn_de": date_yyyymmdd,
        "end_de": date_yyyymmdd,
        "page_no": page_no,
        "page_count": PAGE_COUNT,
    }

    for attempt in range(1, MAX_PAGE_RETRIES + 1):
        try:
            response = requests.get(DART_LIST_URL, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()
        except Exception as error:
            print(f"  page {page_no} attempt {attempt}/{MAX_PAGE_RETRIES} failed: {error}")
            if attempt < MAX_PAGE_RETRIES:
                time.sleep(RETRY_BACKOFF_SECONDS * attempt)
            continue

        if data.get("status") != "000":
            print(
                f"  page {page_no} attempt {attempt}/{MAX_PAGE_RETRIES} returned "
                f"status={data.get('status')}, message={data.get('message')}"
            )
            if attempt < MAX_PAGE_RETRIES:
                time.sleep(RETRY_BACKOFF_SECONDS * attempt)
            continue

        return data

    return None


def collect_disclosures(date_yyyymmdd: str) -> tuple[pd.DataFrame, dict]:
    """
    Collect the FULL DART disclosure list for a specific date, paging
    through every page the API reports (not just the first PAGE_COUNT
    rows). A single-page fetch was silently truncating most days: DART's
    page_count cap is 100 but total_count has been observed at 451-2,069
    on ordinary trading days, so the old code was keeping roughly 5-20% of
    each day's disclosures with no signal that anything was missing.

    Returns (disclosures_df, meta) where meta records total_count,
    total_page, fetched_rows, failed_pages, and a "complete"/"partial"/
    "empty"/"error" status -- so callers/logs never have to guess whether
    a day's data is whole.
    """
    api_key = get_dart_api_key()

    first_page = fetch_page(api_key, date_yyyymmdd, 1)
    if first_page is None:
        print(f"DART API request failed for page 1 of {date_yyyymmdd} after {MAX_PAGE_RETRIES} attempts.")
        return pd.DataFrame(), {
            "date": date_yyyymmdd,
            "total_count": None,
            "total_page": None,
            "fetched_rows": 0,
            "pages_fetched": 0,
            "failed_pages": [1],
            "status": "error",
        }

    total_count = first_page.get("total_count", 0) or 0
    total_page = first_page.get("total_page", 1) or 1

    all_items = list(first_page.get("list", []))
    pages_fetched = 1
    failed_pages: list[int] = []

    for page_no in range(2, total_page + 1):
        time.sleep(BETWEEN_PAGE_SLEEP_SECONDS)
        page = fetch_page(api_key, date_yyyymmdd, page_no)
        if page is None:
            print(f"  page {page_no}/{total_page} of {date_yyyymmdd}: giving up after {MAX_PAGE_RETRIES} attempts.")
            failed_pages.append(page_no)
            continue
        items = page.get("list", [])
        if not items:
            # An empty page mid-range means we've reached the end of real
            # data even if total_page implied more -- stop, don't keep
            # requesting pages that can only ever come back empty.
            print(f"  page {page_no}/{total_page} of {date_yyyymmdd}: empty, stopping pagination early.")
            break
        all_items.extend(items)
        pages_fetched += 1

    fetched_rows = len(all_items)

    if not all_items:
        status = "empty"
    elif failed_pages:
        status = "partial"
    elif fetched_rows != total_count:
        # Fetched every page the API told us about but the row count still
        # doesn't reconcile -- not the failure mode this fix targets, but
        # worth flagging rather than silently trusting the total.
        print(
            f"WARNING: {date_yyyymmdd} fetched_rows ({fetched_rows}) does not match "
            f"total_count ({total_count}) even though all {total_page} pages were fetched."
        )
        status = "partial"
    else:
        status = "complete"

    meta = {
        "date": date_yyyymmdd,
        "total_count": total_count,
        "total_page": total_page,
        "fetched_rows": fetched_rows,
        "pages_fetched": pages_fetched,
        "failed_pages": failed_pages,
        "status": status,
    }

    print(
        f"DART collection for {date_yyyymmdd}: status={status}, "
        f"fetched_rows={fetched_rows}/{total_count}, "
        f"pages_fetched={pages_fetched}/{total_page}, failed_pages={failed_pages}"
    )

    if status == "partial":
        print(
            f"WARNING: DART collection INCOMPLETE for {date_yyyymmdd} -- "
            f"only {fetched_rows}/{total_count} disclosures collected "
            f"({len(failed_pages)} page(s) failed). Downstream key-event "
            f"selection for this date is working from partial data."
        )

    if not all_items:
        return pd.DataFrame(), meta

    return pd.DataFrame(all_items), meta


def save_raw_data(df: pd.DataFrame, date_yyyymmdd: str) -> str:
    """Save disclosure data to CSV."""
    output_dir = "data/raw"
    os.makedirs(output_dir, exist_ok=True)

    output_path = f"{output_dir}/dart_disclosures_{date_yyyymmdd}.csv"
    df.to_csv(output_path, index=False, encoding="utf-8-sig")

    return output_path


def save_collection_meta(meta: dict) -> str:
    """
    Persist pagination/completeness metadata alongside the raw CSV, so a
    partial collection is a durable, inspectable fact rather than something
    only visible in that run's console log.
    """
    output_dir = "data/raw"
    os.makedirs(output_dir, exist_ok=True)

    output_path = f"{output_dir}/dart_disclosures_meta_{meta['date']}.json"
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(meta, file, ensure_ascii=False, indent=2)

    return output_path


def main():
    today = kst_business_day_yyyymmdd()

    print(f"Collecting DART disclosures for {today}...")

    df, meta = collect_disclosures(today)
    meta_path = save_collection_meta(meta)
    print(f"Saved collection metadata to: {meta_path}")

    if df.empty:
        print("No data saved.")
        return

    output_path = save_raw_data(df, today)

    print(f"Collected {len(df)} disclosures.")
    print(f"Saved to: {output_path}")
    print(df[["corp_name", "report_nm", "rcept_dt"]].head())


if __name__ == "__main__":
    main()
