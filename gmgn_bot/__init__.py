from __future__ import annotations

import json
from typing import Any, Dict, Optional

import requests

from .config import settings


class GMGNClient:
    """Simple API client template for GMGN.ai.

    This starter intentionally avoids hard-coding production endpoints
    because API contracts may change. Anh can update methods based on the
    actual GMGN.ai documentation or API response schema.
    """

    def __init__(self, base_url: Optional[str] = None, api_key: Optional[str] = None, timeout: Optional[int] = None):
        self.base_url = (base_url or settings.base_url).rstrip("/")
        self.api_key = api_key or settings.api_key
        self.timeout = timeout or settings.timeout

    def _headers(self) -> Dict[str, str]:
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        return headers

    def _request(self, method: str, path: str, params: Optional[Dict[str, Any]] = None, payload: Optional[Dict[str, Any]] = None):
        url = f"{self.base_url}{path}"
        response = requests.request(
            method=method.upper(),
            url=url,
            params=params,
            data=json.dumps(payload) if payload is not None else None,
            headers=self._headers(),
            timeout=self.timeout,
        )

        try:
            response.raise_for_status()
        except requests.HTTPError as exc:
            body = response.text
            raise RuntimeError(f"API request failed: {method.upper()} {path} -> {response.status_code}: {body}") from exc

        if response.content:
            try:
                return response.json()
            except ValueError:
                return response.text
        return {}

    def ping(self):
        """Health check placeholder"""
        return self._request("GET", "/health")

    def get_market(self, symbol: str):
        """Example placeholder for fetching market data.

        Replace with actual GMGN.ai endpoint when anh has the exact path.
        """
        return self._request("GET", "/market", params={"symbol": symbol})

    def get_token(self, token_address: str):
        """Example placeholder for token detail API."""
        return self._request("GET", "/token", params={"address": token_address})

    def get_wallet_balance(self, wallet_address: str):
        """Example placeholder for wallet data."""
        return self._request("GET", "/wallet/balance", params={"address": wallet_address})

    def place_order(self, payload: Dict[str, Any]):
        """Example placeholder for order submission."""
        return self._request("POST", "/orders", payload=payload)
