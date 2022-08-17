score = int(input('Type a score between 0 and 10: '))
while not 10 >= score >= 0:
    score = int(input('You typed an invalid score. Try again: '))

# a = 0
# while a < 10:
#     print(a)
#     a += 1

# Prime numbers in the range
print('\nPrime numbers in the range')
i = int(input('Type a number: '))

for i in range(i):
    div = 0
    for x in range(1, i+1):
        remaind = i % x
        if remaind == 0:
            div += 1

    if div == 2:  # Prime numbers are only divisible by two numbers, one and itself.
        print(i)

# Is it a prime number?
a = int(input('\nType a number: '))

div = 0
for x in range(1, a+1):
    remaind = a % x
    if remaind == 0:
        div += 1

if div == 2:  # Prime numbers are only divisible by two numbers, one and itself.
    print('The number {} is a prime number.'.format(a))
else:
    print('The number {} is not a prime number.'.format(a))
