"""GMGN API Client"""
import requests
from typing import Any, Dict, Optional


class GMGNClient:
    """Wrapper to call GMGN.ai API"""

    def __init__(self, base_url: str, api_key: str, timeout: int = 30):
        self.base_url = base_url
        self.api_key = api_key
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"Bearer {api_key}"})

    def ping(self) -> Dict[str, Any]:
        """Health check"""
        try:
            resp = self.session.get(f"{self.base_url}/health", timeout=self.timeout)
            resp.raise_for_status()
            return resp.json()
        except Exception as e:
            raise Exception(f"Ping failed: {e}")

    def get_market(self, symbol: str) -> Dict[str, Any]:
        """Get market data for a symbol"""
        try:
            resp = self.session.get(
                f"{self.base_url}/market/{symbol}", timeout=self.timeout
            )
            resp.raise_for_status()
            return resp.json()
        except Exception as e:
            raise Exception(f"Get market failed for {symbol}: {e}")

    def get_wallet_balance(self) -> Dict[str, Any]:
        """Get wallet balance"""
        try:
            resp = self.session.get(
                f"{self.base_url}/wallet/balance", timeout=self.timeout
            )
            resp.raise_for_status()
            return resp.json()
        except Exception as e:
            raise Exception(f"Get wallet balance failed: {e}")

    def place_order(
        self, symbol: str, side: str, size: float, price: Optional[float] = None
    ) -> Dict[str, Any]:
        """Place an order"""
        try:
            payload = {"symbol": symbol, "side": side, "size": size, "price": price}
            resp = self.session.post(
                f"{self.base_url}/order/place",
                json=payload,
                timeout=self.timeout,
            )
            resp.raise_for_status()
            return resp.json()
        except Exception as e:
            raise Exception(f"Place order failed: {e}")
