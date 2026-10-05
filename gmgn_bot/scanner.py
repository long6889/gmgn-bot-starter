"""Token Scanner - Filter and pick best tokens"""
from typing import Any, Dict, List, Optional


class TokenScanner:
    """Scanner to filter tokens by volume and trend"""

    def __init__(self, min_volume: float = 100000):
        self.min_volume = min_volume

    def filter_by_volume(self, markets: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Filter markets by minimum volume"""
        return [m for m in markets if m.get("volume", 0) >= self.min_volume]

    def filter_by_trend(self, markets: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Filter markets by bullish trend"""
        return [m for m in markets if m.get("trend") == "bullish"]

    def pick_best(
        self, markets: List[Dict[str, Any]]
    ) -> Optional[Dict[str, Any]]:
        """Pick the best candidate"""
        filtered = self.filter_by_volume(markets)
        filtered = self.filter_by_trend(filtered)
        if filtered:
            # Pick the one with highest volume
            return max(filtered, key=lambda x: x.get("volume", 0))
        return None
