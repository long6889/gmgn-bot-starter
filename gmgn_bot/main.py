from __future__ import annotations

from gmgn_bot.client import GMGNClient
from gmgn_bot.config import settings
from gmgn_bot.strategies import SimpleMomentumStrategy


def main():
    client = GMGNClient(base_url=settings.base_url, api_key=settings.api_key, timeout=settings.timeout)

    print("[INFO] Starting GMGN bot starter...")

    try:
        health = client.ping()
        print("[INFO] Health check:", health)
    except Exception as exc:
        print("[WARN] Health check failed. Check your GMGN API config:", exc)
        health = None

    symbol = "SOL"
    sample_market = {
        "symbol": symbol,
        "price": 150.0,
        "volume": 2500000,
        "trend": "bullish",
    }

    strategy = SimpleMomentumStrategy(symbol=symbol)
    signal = strategy.analyze(sample_market)

    print("[INFO] Signal result:")
    print(signal)

    if health is not None:
        print("[INFO] Bot is ready to be expanded with real market data and order execution logic.")
    else:
        print("[INFO] API config not ready yet. Fill the .env values and update client.py path if needed.")


if __name__ == "__main__":
    main()
