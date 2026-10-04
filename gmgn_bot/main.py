from __future__ import annotations

from gmgn_bot.client import GMGNClient
from gmgn_bot.config import settings
from gmgn_bot.risk import RiskManager
from gmgn_bot.scanner import TokenScanner
from gmgn_bot.strategies import SimpleMomentumStrategy


def main():
    client = GMGNClient(base_url=settings.base_url, api_key=settings.api_key, timeout=settings.timeout)
    scanner = TokenScanner(min_volume=500000)
    risk = RiskManager(max_position_ratio=0.10, max_daily_loss_ratio=0.02)

    print("[INFO] Starting GMGN bot starter...")

    try:
        health = client.ping()
        print("[INFO] Health check:", health)
    except Exception as exc:
        print("[WARN] Health check failed. Check your GMGN API config:", exc)
        health = None

    sample_markets = [
        {"symbol": "SOL", "price": 150.0, "volume": 2500000, "trend": "bullish"},
        {"symbol": "BONK", "price": 0.00002, "volume": 800000, "trend": "bullish"},
        {"symbol": "WIF", "price": 2.3, "volume": 320000, "trend": "neutral"},
    ]

    candidate = scanner.pick_best(sample_markets)
    print("[INFO] Best candidate from scanner:", candidate)

    if candidate:
        strategy = SimpleMomentumStrategy(symbol=candidate["symbol"])
        signal = strategy.analyze(candidate)
        print("[INFO] Signal result:")
        print(signal)

        account_balance = 1000.0
        planned_size = 100.0
        can_trade = risk.check_trade(account_balance, planned_size, pnl_ratio=0.01)
        print("[INFO] Risk check:", can_trade)

    if health is not None:
        print("[INFO] Bot is ready to be expanded with real market data and order execution logic.")
    else:
        print("[INFO] API config not ready yet. Fill the .env values and update client.py path if needed.")


if __name__ == "__main__":
    main()
