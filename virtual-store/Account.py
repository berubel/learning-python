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
            print('\nThe balance can not be negative.')
        else:
            self._balance = balance

    def deposit(self,value):
        self._balance = value

    def withdrawal(self,value):
        if(self._balance >= value):
            print("\nSucessful withdrawal!")
        else:
            print('\nInsufficient balance.')

    def account_statement(self):
        print('\nClient: {} \nAccount number: {} \nBalance: {}'.format(self.holder, self.number, self.balance))

