class Wallet:

    def __init__(self, balance, withdrawAmount, depositAmount):

        self.balance = balance
        self.withdrawAmount = withdrawAmount
        self.depositAmount = depositAmount

    def _get_balance(self):
        return self._balance
    
    def _set_balance(self, balance):
        self._balance = balance

    def _get_withdrawAmount(self):
        return self._withdrawAmount
    
    def _set_withdrawAmount(self, withdrawAmount):
        self._withdrawAmount = withdrawAmount
    
    def _get_depositAmount(self):
        return self._depositAmount
    
    def _set_depositAmount(self, depositAmount):
        self._depositAmount = depositAmount

    def deposit(self, amount : float):
        self._ += amount

    def withdraw(self, amount : float):
        if self._balance < amount:
            print("vous êtes à découvert")
        else:
            self._balance -= amount

    balance = property(_get_balance, _set_balance)
    withdrawAmount = property(_get_withdrawAmount, _set_withdrawAmount)
    depositAmount = property(_get_depositAmount, _set_depositAmount)