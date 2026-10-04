from __future__ import annotations

from typing import Dict, List, Optional


class TokenScanner:
    """Simple scanner skeleton for GMGN-style token discovery.

    In production, this component can call market APIs, websocket feeds,
    or a list of newly launched tokens and then filter by volume, momentum,
    liquidity, or wallet activity.
    """

    def __init__(self, min_volume: float = 500000.0):
        self.min_volume = min_volume

    def scan(self, markets: List[Dict]) -> List[Dict]:
        candidates: List[Dict] = []
        for market in markets:
            if not isinstance(market, dict):
                continue
            symbol = market.get("symbol")
            volume = float(market.get("volume", 0) or 0)
            trend = market.get("trend", "neutral")

            if symbol and volume >= self.min_volume:
                candidates.append({
                    "symbol": symbol,
                    "volume": volume,
                    "trend": trend,
                    "price": market.get("price", 0),
                })
        return candidates

    def pick_best(self, markets: List[Dict]) -> Optional[Dict]:
        candidates = self.scan(markets)
        if not candidates:
            return None
        return sorted(candidates, key=lambda x: x["volume"], reverse=True)[0]
