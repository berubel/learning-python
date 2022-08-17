from class6 import Calculator
from class7_letter_counter import letter_counter

if __name__ == '__main__':
    calculator = Calculator(10, 10)
    print(calculator.sum())

    words = ['banana', 'apple', 'strawberry']
    total_letters = letter_counter(words)
    print('Total letters: {}'.format(total_letters))

