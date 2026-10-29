"""Conservative cutoff for completed Korean-market daily bars."""
from datetime import datetime, time, timedelta, timezone

KST = timezone(timedelta(hours=9))


def completed_price_cutoff(now=None):
    now = now or datetime.now(KST)
    now = now.replace(tzinfo=KST) if now.tzinfo is None else now.astimezone(KST)
    # Leave a buffer beyond the regular close for provider finalization.
    return now.date() if now.time() >= time(16, 0) else now.date() - timedelta(days=1)
