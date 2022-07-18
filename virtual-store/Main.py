from Client import Client
from Account import Account

class Main:
    pass

print('Project test')

c1 = Client('John', '22222-88888')
name = c1.get_name()
account = Account(name,'0000',0)

print(c1)
print('\nName: {} \nPhone: {}\n'.format(name, c1.phone))
print('Holder: {} \nAccount number: {} \nBalance: {}'.format(account.holder, account.number, account.balance))

# Changing balance
account.balance = 50
# New balance
print('New balance: {}'. format(account.balance))
