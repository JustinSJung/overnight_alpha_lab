"""
Korea Investment Open API client for market data only.

This client intentionally supports quotation endpoints only. It does not
implement trading, order placement, balance, or account APIs.
"""

import os
from datetime import datetime, timedelta
from typing import Any, Optional

import pandas as pd
import requests

try:
    from dotenv import load_dotenv
except Exception:  # pragma: no cover - optional local dependency guard
    def load_dotenv():
        return False


REAL_BASE_URL = "https://openapi.koreainvestment.com:9443"
VIRTUAL_BASE_URL = "https://openapivts.koreainvestment.com:29443"
TOKEN_PATH = "/oauth2/tokenP"
DAILY_PRICE_PATH = "/uapi/domestic-stock/v1/quotations/inquire-daily-itemchartprice"
CURRENT_PRICE_PATH = "/uapi/domestic-stock/v1/quotations/inquire-price"


class KISCredentialsMissing(RuntimeError):
    """Raised when KIS credentials are not available."""


class KISClient:
    """
    Minimal Korea Investment Open API quotation client.
    """

    def __init__(
        self,
        app_key: Optional[str] = None,
        app_secret: Optional[str] = None,
        env: Optional[str] = None,
        timeout: int = 15,
    ):
        load_dotenv()
        self.app_key = app_key or os.getenv("KIS_APP_KEY", "")
        self.app_secret = app_secret or os.getenv("KIS_APP_SECRET", "")
        self.env = (env or os.getenv("KIS_ENV", "real")).strip().lower()
        self.timeout = timeout
        self._access_token = ""

        if not self.app_key or not self.app_secret:
            raise KISCredentialsMissing("KIS credentials are missing.")

        if self.env in {"vts", "virtual", "paper", "mock", "sandbox"}:
            self.base_url = VIRTUAL_BASE_URL
        else:
            self.base_url = REAL_BASE_URL

    def get_access_token(self) -> str:
        if self._access_token:
            return self._access_token

        url = f"{self.base_url}{TOKEN_PATH}"
        payload = {
            "grant_type": "client_credentials",
            "appkey": self.app_key,
            "appsecret": self.app_secret,
        }

        response = requests.post(url, json=payload, timeout=self.timeout)
        response.raise_for_status()
        data = response.json()
        token = data.get("access_token", "")

        if not token:
            raise RuntimeError("KIS access token was not returned.")

        self._access_token = token
        return token

    def _headers(self, tr_id: str) -> dict[str, str]:
        return {
            "content-type": "application/json; charset=utf-8",
            "authorization": f"Bearer {self.get_access_token()}",
            "appkey": self.app_key,
            "appsecret": self.app_secret,
            "tr_id": tr_id,
            "custtype": "P",
        }

    def get_daily_ohlcv(
        self,
        stock_code: str,
        start_date: str,
        end_date: str,
        period_code: str = "D",
        adjusted_price: bool = True,
    ) -> pd.DataFrame:
        """
        Fetch daily OHLCV rows for one domestic stock.
        """

        stock_code = normalize_stock_code(stock_code)
        params = {
            "FID_COND_MRKT_DIV_CODE": "J",
            "FID_INPUT_ISCD": stock_code,
            "FID_INPUT_DATE_1": start_date,
            "FID_INPUT_DATE_2": end_date,
            "FID_PERIOD_DIV_CODE": period_code,
            "FID_ORG_ADJ_PRC": "0" if adjusted_price else "1",
        }

        data = self._get_json(DAILY_PRICE_PATH, "FHKST03010100", params)
        rows = data.get("output2", [])

        if not rows:
            return pd.DataFrame()

        return normalize_daily_ohlcv_rows(rows, stock_code, source="kis")

    def get_current_quote(self, stock_code: str) -> dict[str, Any]:
        """
        Fetch current quotation snapshot for one domestic stock.
        """

        stock_code = normalize_stock_code(stock_code)
        params = {
            "FID_COND_MRKT_DIV_CODE": "J",
            "FID_INPUT_ISCD": stock_code,
        }

        data = self._get_json(CURRENT_PRICE_PATH, "FHKST01010100", params)
        output = data.get("output", {}) or {}
        return normalize_current_quote(output, stock_code)

    def _get_json(self, path: str, tr_id: str, params: dict[str, str]) -> dict[str, Any]:
        url = f"{self.base_url}{path}"
        response = requests.get(
            url,
            headers=self._headers(tr_id),
            params=params,
            timeout=self.timeout,
        )
        response.raise_for_status()
        data = response.json()

        rt_cd = str(data.get("rt_cd", "0"))
        if rt_cd not in {"0", ""}:
            message = data.get("msg1") or data.get("msg_cd") or "KIS request failed."
            raise RuntimeError(str(message))

        return data


def normalize_stock_code(value) -> str:
    if value is None or pd.isna(value):
        return ""

    try:
        return str(int(float(value))).zfill(6)
    except Exception:
        return str(value).strip().zfill(6)


def safe_number(value, default=0.0):
    try:
        if value in {None, ""} or pd.isna(value):
            return default
        return float(str(value).replace(",", ""))
    except Exception:
        return default


def normalize_daily_ohlcv_rows(
    rows: list[dict[str, Any]],
    stock_code: str,
    source: str,
) -> pd.DataFrame:
    normalized_rows = []

    for row in rows:
        date_value = row.get("stck_bsop_date") or row.get("date")
        if not date_value:
            continue

        normalized_rows.append(
            {
                "stock_code": normalize_stock_code(stock_code),
                "date": datetime.strptime(str(date_value), "%Y%m%d").strftime("%Y-%m-%d"),
                "open": safe_number(row.get("stck_oprc")),
                "high": safe_number(row.get("stck_hgpr")),
                "low": safe_number(row.get("stck_lwpr")),
                "close": safe_number(row.get("stck_clpr")),
                "volume": safe_number(row.get("acml_vol")),
                "trading_value": safe_number(row.get("acml_tr_pbmn")),
                "change_rate": safe_number(row.get("prdy_ctrt")),
                "price_source": source,
            }
        )

    if not normalized_rows:
        return pd.DataFrame()

    df = pd.DataFrame(normalized_rows)
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date"])
    df = df.sort_values("date")
    df["date"] = df["date"].dt.strftime("%Y-%m-%d")
    return df


def normalize_current_quote(output: dict[str, Any], stock_code: str) -> dict[str, Any]:
    return {
        "stock_code": normalize_stock_code(stock_code),
        "quote_date": datetime.now().strftime("%Y-%m-%d"),
        "current_price": safe_number(output.get("stck_prpr")),
        "open": safe_number(output.get("stck_oprc")),
        "high": safe_number(output.get("stck_hgpr")),
        "low": safe_number(output.get("stck_lwpr")),
        "previous_close": safe_number(output.get("stck_sdpr")),
        "change_rate": safe_number(output.get("prdy_ctrt")),
        "volume": safe_number(output.get("acml_vol")),
        "trading_value": safe_number(output.get("acml_tr_pbmn")),
        "price_source": "kis",
    }


def default_date_range(days: int = 120) -> tuple[str, str]:
    end_date = datetime.today()
    start_date = end_date - timedelta(days=days)
    return start_date.strftime("%Y%m%d"), end_date.strftime("%Y%m%d")
