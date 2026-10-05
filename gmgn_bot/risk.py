"""Risk Management"""


class RiskManager:
    """Manage trading risk"""

    def __init__(self, max_position_ratio: float = 0.10, max_daily_loss_ratio: float = 0.02):
        """
        Args:
            max_position_ratio: Max position size as % of account
            max_daily_loss_ratio: Max daily loss as % of account
        """
        self.max_position_ratio = max_position_ratio
        self.max_daily_loss_ratio = max_daily_loss_ratio

    def check_trade(
        self, account_balance: float, planned_size: float, pnl_ratio: float = 0.0
    ) -> bool:
        """Check if trade is allowed"""
        # Check position size
        if planned_size > account_balance * self.max_position_ratio:
            return False
        # Check daily loss
        if pnl_ratio < -self.max_daily_loss_ratio:
            return False
        return True
