x = int(input('Type a number to be the numerator: '))
y = int(input('Type a number to be the denominator: '))
test = [1, 10]
f = open('test.txt', 'r')

try:
    text = f.read()
    div = x / y
    print(f'The result is {div}')
    test[1] = div
    z = a

except BaseException as ex:
    print('Unknown error. Error: {}.'.format(ex))
except ZeroDivisionError:
    print('It is impossible to divide a number by zero.')
except IndexError:
    print('Error accessing invalid index.')
else:
    print('Run when no exception occurs.')
finally:
    print('Always run. Closing the file.')
    text = f.close()
