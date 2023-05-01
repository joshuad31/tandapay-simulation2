"""
User account instance
"""


class UserAccount(object):
    
    def __init__(self, bundling: int = 0):
        self.bundling = bundling
        self.wallet = 0
        self.savings = 0
        self.monthly_accounts = {f"m_{i}": 0 for i in range(self.bundling + 1)}

    def transaction(self, source: str, dest: str, amount: int) -> bool:
        """ Conducts a transaction and returns success/failure """
        # validate balances

        # transfer
        dest += amount
        source -= amount
        return True

    def transfer_month_accounts(self) -> None:
        """Move month account balances to next, send to wallet if overflow"""
        pass

    def pay_premium(self, premium: int) -> bool:
        """Transfers premium amount from wallet to m_0 account"""
        # validate balances
        # transfer from wallet to m_0
        # transfer month accounts so balances move down the line
        pass
