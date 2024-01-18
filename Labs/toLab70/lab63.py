import itertools as it
import math

notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

for permute in it.permutations(notes, 4):
    print(permute)
else:
    print(math.factorial(len(notes)) - math.factorial(3))

for x in it.permutations(notes, 4):
    print(x)

print(math.factorial(len(notes)) / math.factorial(len(notes) - 4))

a = 0
for permute_r in it.product(notes, repeat=4):
    print(permute_r)
    a += 1
else:
    print(a)