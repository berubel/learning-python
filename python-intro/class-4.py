listNumbers = [11, 3, 5, 7, 1]
listAnimals = ['cat', 'dog', 'turtle', 'ant']

for animal in listAnimals:
    print(animal)

print('\n')
total = 0
for number in listNumbers:
    print(number)
    total += number
print('\n'.format(total))

print(sum(listNumbers))  # Another way to sum elements in the list
print(max(listNumbers))  # Shows the biggest element in the list
print(min(listAnimals))  # Shows the smallest element in the list

if 'wolf' in listAnimals:
    print('\nThere is a wolf in the list.')
else:
    print('\nThere is not a wolf in the list. It will be included.')
    listAnimals.append('wolf')  # Add a new element at the last index
    print(listAnimals)

listAnimals.pop()  # Remove the last element or the index in the parameter
print(listAnimals)

if 'dog' in listAnimals:  # Remove by the value of the element
    listAnimals.remove('dog')

listAnimals.sort()
listNumbers.sort()

print(listAnimals)
print(listNumbers)

listAnimals.reverse()
print(listAnimals)

newList = listAnimals * 3  # Repeat the list
print(newList)

# Tuples
tupleNumbers = (1, 10, 20, 5)  # Tuples are immutable
print(len(tupleNumbers))

tupleAnimals = tuple(listAnimals)  # Convert a list to tuple
print(type(tupleAnimals))

listNumbers2 = list(tupleNumbers)  # Convert a tuple to list
print(listNumbers2)
