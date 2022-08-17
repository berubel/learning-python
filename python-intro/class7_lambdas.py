letter_counter = lambda words_list: [len(word) for word in words_list]

animals = ['dog', 'cat', 'turtle']
print(letter_counter(animals))

sum = lambda a, b: a + b
print(sum(5, 10))

calculator = {
    'sum': lambda a, b: a + b,
    'sub': lambda a, b: a - b,
    'div': lambda a, b: a / b,
    'mult':lambda a, b: a * b
}

print(type(calculator))
sum = calculator['sum']
sub = calculator['sub']
div = calculator['div']
mult = calculator['mult']

print(sum(10, 10))
print(mult(5, 5))

