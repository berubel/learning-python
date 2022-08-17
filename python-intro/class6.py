class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mult(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


if __name__ == '__main__':
    calculator = Calculator(10, 2)
    print('Sum: {}'.format(calculator.sum()))
    print('Subtraction: {}'.format(calculator.sub()))
    print('Multiplication: {}'.format(calculator.mult()))
    print('Division: {}'.format(calculator.div()))
