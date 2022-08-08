# Sets
numericalSet = {1, 2, 3, 4, 5}
numericalSet.add(5)
numericalSet.discard(2)
print(numericalSet)

setA = {1, 2, 3, 4, 5}
setB = {5, 6, 7, 8}
unionSet = setA.union(setB)
print('\nUnion between sets A and B: {}'.format(unionSet))

intersectionSet = setA.intersection(setB)
print('Intersection between sets A and B: {}'.format(intersectionSet))

differenceSetA = setA.difference(setB)
differenceSetB = setB.difference(setA)
print('Difference between sets A and B: {}'.format(differenceSetA))
print('Difference between sets B and A: {}'.format(differenceSetB))

symmetricDiffSet = setA.symmetric_difference(setB)
print('Difference between sets B and A: {}'.format(symmetricDiffSet))

setA = {1, 2, 3}
setB = {1, 2, 3, 4, 5}

subset = setA.issubset(setB)  # returns true if setA is a subset of setB
print('Set A is a subset of set B: {}'.format(subset))

superset = setB.issuperset(setA)  # returns true if setB is a superset of setA
print('Set B is a superset of set A: {}'.format(superset))

#  Converting lists to sets
listAnimals = ['cat', 'dog', 'duck', 'duck']
setAnimals = set(listAnimals)
print(setAnimals)
