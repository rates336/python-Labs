# Testing zone
print('\nTesting zone\n')

print('\nEnd Testing zone\n')
# End Testing zone

# Note if you multiplied 5 * 0.2 type of this number is float not integer
# print(type(5), type(0.2), type(5 * 0.2))

v1 = 126 # int
v2 = '126' # str
v3 = 126.0 # float
v4 = '126.0' # str

print('type of variable:', v1, '=', type(v1))
print('type of variable:', v2, '=', type(v2))
print('type of variable:', v3, '=', type(v3))
print('type of variable:', v4, '=', type(v4))

print('\nv1 + v3 =', v1 + v3)
print('v2 + v4 =', v2 + v4)

# 7 - 1 * 0 + 3 + 3 = 13
print(7 - 1 * 0 + 3 + 3)

# 4 ** 5 / 2 ** 3 = 128
print(4 ** 5 / 2 ** 3)

# Task !07
'''
7. To zadanie to raczej matematyczna łamigłówka, niż typowe zadanie z Pythona, 
ale z drugiej strony to "smaczek" bycia programistą lub matematykiem...

Wyobraż sobie, że zepsuła Ci się klawiatura. Działa tylko klawisz 9, klawisze z działaniami +-*/ oraz
klawisze nawiasów i enter. Na dodatek klawisz 9 możesz nacisnąć tylko maksymalnie 4 razy,
bo po kolejnym naciśnięciu.... komputer się restartuje.

Twoim zadaniem jest napisanie na tej zepsutej klawiaturze w interpreterze Python takiego działania,
aby jego wynik wynosił 100
'''
# 9 * 9 + 9 + 9 + 9 ** (9 - 9)
# 99 + 9 / 9
# 999 / 9 - 9 - 9 ** (9 - 9) - 9 ** (9 - 9)
print(9 * 9 + 9 + 9 + 9 ** (9 - 9))
print(99 + 9 / 9)
print(999 / 9 - 9 - 9 ** (9 - 9) - 9 ** (9 - 9))



