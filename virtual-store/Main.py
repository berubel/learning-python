from Client import Client
from Account import Account

class Main:
    pass

print('Project test')

c1 = Client('John', '22222-88888')
account = Account(c1.name,'0000',0)

print(c1)
print('\nName: {} \nPhone: {}\n'.format(c1.name, c1.phone))
print('Holder: {} \nAccount number: {} \nBalance: {}'.format(account.holder, account.number, account.balance))
