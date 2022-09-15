import math
import statistics
from statistics import median, median_low, median_high
percent = [2.606255012, 1.222935044, 1.283079391, 3.628708901, 6.856455493, 4.911788292,
           2.886928629, 0.781876504, 0.962309543, 2.265437049, 6.816359262, 3.688853248,
           3.468323978, 5.633520449, 4.530874098, 1.984763432, 0.922213312, 3.327987169,
           4.190056135, 5.493183641, 1.864474739, 10.60545309, 2.425821973, 2.726543705,
           8.740978348, 6.174819567]

countries = ['Ukraine', 'Spain', 'Slovenia', 'Lithuania', 'Austria', 'Estonia',
             'Norway', 'Portugal', 'United Kingdom', 'Serbia', 'Germany', 'Albania',
             'France', 'Czech Republic', 'Denmark', 'Australia', 'Finland', 'Bulgaria',
             'Moldova', 'Sweden', 'Hungary', 'Israel', 'Netherlands', 'Ireland',
             'Cyprus', 'Italy']

sumOfPoints = 4988


maxScore = max(percent)
minScore = min(percent)


for country in countries:
    print(country + ':', int(percent[countries.index(country)]), 'in integer %')
    print(country + ':', round(percent[countries.index(country)], 2), 'rounded to next 2 numbers decimal')
    print(country + ':', (sumOfPoints / 100 * percent[countries.index(country)]).__round__(2), 'amount of points')
    print()

percent.sort()
print('median:', statistics.median(percent))
print('median low:', statistics.median_low(percent))
print('median high:', statistics.median_high(percent))
print(median(percent))
print(median_low(percent))
print(median_high(percent))

degree = 360
rad = 180 / math.pi
deg = math.pi * rad / 180
print(degree / rad)
print(math.radians(degree))
degree = 45
print(degree / rad)
print(math.radians(degree))


# Task !28
'''
6. Pizzeria oferuje pizze:

small - promień 22 cm, cena, 11.50
big - promień 27 cm, cena 15.60
family - promień 38cm, cena 22.00

Zadeklaruj zmienne small_pizza_r, big_pizza_r, family_pizza_r oraz 
small_pizza_price, big_pizza_price, family_pizza_price i zapisz w nich w/w wartości.

7. Oblicz pole powierzchni pizz w metrach kwadratowych
8. Wyznacz cenę metra kwadratowego pizzy small, big i family
'''
pizzaRadius = {'small': 22, 'big': 27, 'family': 38}
pizzaPrice = {'small': 11.5, 'big': 15.6, 'family': 22.0}


for pizza in pizzaRadius.keys():
    print('Field', pizza, 'pizza is:', ((pizzaRadius.get(pizza).__pow__(2) * math.pi).__round__(2) / 10_000).__round__(2))
    print('Price from one square meter for', pizza, 'pizza is:', (pizzaPrice.get(pizza) /
        ((pizzaRadius.get(pizza).__pow__(2) * math.pi.__round__(3)).__round__(2) / 10_000)).__round__(2))

print(dir(math))
