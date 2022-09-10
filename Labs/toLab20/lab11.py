# Testing zone
print('\nTesting zone\n')
# print(100 - int('A'))

print('\nEnd Testing zone\n')
# End Testing zone


# Task !16
'''
1. Tym razem pracujesz w LOT i masz za zadanie rozpocząć programowanie rozkładu miejsc w samolocie.
(Patrz https://www.lot.com/pl/pl/boeing-737-800-rozklad-miejsc lub ilustracja na końcu tego laboratorium)

Należy wyświetlić napisy:
Row number 1
Row number 2
...
Row number 30
Row number 31
'''
x = 0
while x < 31:
    print(x + 1, 'place')
    x += 1
else:
    print('WC')

y = 0
while y < 13:
    print((y + 1) ** 2)
    print((y + 1) ** 3)
    y += 1
else:
    print('Finish')

z = 0
while z < 16:
    print(2 ** z)
    z += 1
else:
    print('Done')

print(5 * 'x')

w = 0
while w < 20:
    # print(((20 - w) / 2 * 1) + (w * 'x' + 'x') + ((20 - w) / 2 * 1))
    print(int((20 - w) / 2) * ' ' + (w * 'x' + 'x') + int((20 - w) / 2) * ' ')
    w += 2
