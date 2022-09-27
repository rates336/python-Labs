# Task !30
"""
W tym zadaniu stworzysz mały kalkulator. Użytkownik wprowadzi wzór funkcji np.:

2*x
math.sin(x)
3*x**2+2*x-4
a program wyznaczy wartości tej funkcji dla x z przedziału (0,10) z dokładnością 0.1

1. Zaimportuj moduł math
2. Utwórz pustą listę argument_list

3. Napisz pętlę, która do listy argument_list doda
100 wartości
zaczynając od zera
gdzie każda kolejna jest o 0.1 większa od poprzedniej

4. Poproś użytkownika o wprowadzenie wzoru. Wzór zapisz w zmiennej formula.
Użytkownik wprowadzając ten wzór powinien skorzystać ze zmiennej x do tego aby oznaczyć argument funkcji

5. Dla każdego elementu x z listy argument_list oblicz wartość funkcji wprowadzonej
przez użytkownika i wyświetl jej wynik
"""
import sys


def calc_fuu_values(pattern: str, numeric_interval=(0, 10), accuracy=0.1):
    x = numeric_interval[0].__round__(4)
    dict_function = {}
    the_pattern: float = 0
    while x < numeric_interval[1]:
        try:
            the_pattern = float(eval(pattern)).__round__(4)
        except:
            print(sys.exc_info()[:2])
        dict_function.setdefault((pattern, x), the_pattern)
        x = (x + accuracy).__round__(4)

    print('description:    ' + '(eval_pattern, value_x, result)')
    return dict_function


separator = '-' * 20
print(calc_fuu_values('2*x'))
print(separator)
print(calc_fuu_values('__import__("math").sin(x)'))
print(separator)
print(calc_fuu_values('3*x**2+2*x-4'))






