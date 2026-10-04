from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class SignalResult:
    symbol: str
    action: str  # buy / sell / hold
    confidence: float
    reason: str
    metadata: Optional[Dict[str, Any]] = None


class SimpleMomentumStrategy:
    """Skeleton strategy for learning.

    Đây là strategy mẫu để anh bắt đầu. Logic thực tế sẽ cần dữ liệu market,
    indicator, signal, risk, và order logic.
    """

    def __init__(self, symbol: str, min_confidence: float = 0.6):
        self.symbol = symbol
        self.min_confidence = min_confidence

    def analyze(self, market_data: Dict[str, Any]) -> SignalResult:
        # Placeholder logic: anh sẽ thay bằng signal thực tế dựa trên price / volume / RSI / trend / whale signals
        price = market_data.get("price", 0)
        volume = market_data.get("volume", 0)
        trend = market_data.get("trend", "neutral")

        if price <= 0:
            return SignalResult(
                symbol=self.symbol,
                action="hold",
                confidence=0.0,
                reason="Invalid market data",
                metadata=market_data,
            )

        if trend == "bullish" and volume > 0:
            action = "buy"
            confidence = 0.75
            reason = "Strong bullish trend with positive volume"
        elif trend == "bearish":
            action = "sell"
            confidence = 0.72
            reason = "Bearish trend detected"
        else:
            action = "hold"
            confidence = 0.35
            reason = "Neutral market condition"

        if confidence < self.min_confidence:
            action = "hold"

        return SignalResult(
            symbol=self.symbol,
            action=action,
            confidence=confidence,
            reason=reason,
            metadata={
                "price": price,
                "volume": volume,
                "trend": trend,
            },
        )
