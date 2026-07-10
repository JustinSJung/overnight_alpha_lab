"""
Statistical evaluation helpers for Overnight Alpha Lab.
"""

import math


def wilson_lower_bound(success: int, total: int, z: float = 1.96) -> float:
    """
    Return the Wilson score lower bound for a binomial success proportion.
    """

    if total <= 0:
        return 0.0

    phat = success / total
    z2 = z * z
    denominator = 1 + z2 / total
    center = phat + z2 / (2 * total)
    margin = z * math.sqrt((phat * (1 - phat) + z2 / (4 * total)) / total)

    return max(0.0, (center - margin) / denominator)


def reliability_score_from_wilson(success: int, total: int) -> float:
    """
    Convert Wilson lower bound to a 0-100 reliability score.
    """

    return wilson_lower_bound(success, total) * 100


def safe_percentage(numerator, denominator) -> float:
    """
    Return numerator / denominator * 100, or 0.0 when unavailable.
    """

    try:
        denominator = float(denominator)
        if denominator == 0:
            return 0.0
        return float(numerator) / denominator * 100
    except Exception:
        return 0.0


def classify_confidence_status(reliability_score: float) -> tuple[str, str]:
    """
    Classify reliability score into dashboard status labels.
    """

    if reliability_score < 30:
        return "NOT READY", "준비 부족"
    if reliability_score < 50:
        return "EARLY STAGE", "초기 검증 단계"
    if reliability_score < 65:
        return "WATCHLIST", "관찰 가능 단계"
    if reliability_score < 80:
        return "MODERATE CONFIDENCE", "중간 신뢰도"
    return "HIGH CONFIDENCE", "높은 신뢰도"
