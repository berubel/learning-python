class Account:
    def __init__(self, holder, number, balance):
        self.holder = holder
        self.number = number
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        if balance < 0:
            print('The balance can not be negative.')
        else:
            self._balance = balance
