class Wallet:

    def __init__(self, balance=0):

        self.balance = balance

    def _get_balance(self):
        return self._balance
    
    def _set_balance(self, balance):
        self._balance = balance

    def deposit(self, amount : float):
        self._ += amount

    def withdraw(self, amount : float):
        if self._balance < amount:
            print("vous êtes à découvert")
        else:
            self._balance -= amount
    def __str__(self):
        return "Votre compte".center(30, "-") + "\n" + "Vous avez " + str(self.balance) + "$"
    
    def affichage(self):
        return str(self)

    

    balance = property(_get_balance, _set_balance)
