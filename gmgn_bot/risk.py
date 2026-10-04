from __future__ import annotations


class RiskManager:
    """Simple risk control skeleton.

    - Limits max position size
    - Prevents overtrading
    - Supports stop loss / take profit placeholders
    """

    def __init__(self, max_position_ratio: float = 0.10, max_daily_loss_ratio: float = 0.02):
        self.max_position_ratio = max_position_ratio
        self.max_daily_loss_ratio = max_daily_loss_ratio

    def allowed_position_size(self, account_balance: float, risk_per_trade: float = 0.01) -> float:
        if account_balance <= 0:
            return 0.0
        return max(0.0, account_balance * min(self.max_position_ratio, risk_per_trade))

    def should_stop(self, pnl_ratio: float) -> bool:
        return pnl_ratio <= -self.max_daily_loss_ratio

    def check_trade(self, account_balance: float, planned_size: float, pnl_ratio: float = 0.0) -> bool:
        allowed = self.allowed_position_size(account_balance)
        if planned_size > allowed:
            return False
        if self.should_stop(pnl_ratio):
            return False
        return True
