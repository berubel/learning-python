# Student Average

a = int(input('First score: '))
b = int(input('Second score: '))
c = int(input('Third score: '))

average = (a + b + c) / 3

#print(f'Average: {average:,.2f}')
print('Average: {}'.format(round(average, 2)))

if average >= 60:
    print('Approved.')
else:
    print('Not approved.')

# The greatest value
print('\nWhat is the biggest number?')
a = int(input('\nFirst value: '))
b = int(input('Second Value: '))
c = int(input('Third Value: '))

if a > b and a > c:
    print('The biggest number is {}. '.format(a))
elif b > a and b > c:
    print('The biggest number is {}. '. format(b))
else:
    print('The biggest number is {}. '.format(c))

# If the number is even or odd
print('\nIs the value even or odd?')
a = int(input('\nType a value: '))

remaind = a % 2

if remaind == 0:
    print('The value is even.')
else:
    print('The value is odd.')

# If there is an even number
a = int(input('\nType the first value: '))
b = int(input('Type the second value: '))

remaindA = a % 2
remaindB = b % 2

if remaindA == 0 or not remaindB > 0:
    print('An even number was typed.')

