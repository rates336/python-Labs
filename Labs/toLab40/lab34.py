import builtins
from typing import Optional

banknotes_coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]
dict_denominations = {}

for element in banknotes_coins:
    dict_denominations.setdefault(element, 0)
else:
    print('Finish adding elements to dictionary')


def deposit_money(*money: float):
    list_of_money = []
    if money is None and list_of_money is None:
        print('Error because all elements is None')
    # elif list_of_money is None:
    elif len(list_of_money) == 0:
        list_of_money = list(money)
    elif money is not None:
        list_of_money.extend(money)

    print(list_of_money)
    for x in list_of_money:
        if banknotes_coins.count(x) == 0:
            list_of_money.remove(x)
            print('You can not deposit:', x, 'because is not a money')
        else:
            dict_denominations[x] += 1
    else:
        print('All is done')
        print(list_of_money)

    sum_of_money = sum(list_of_money)
    print('Operation finished successfully, amount money of your account was increased by', sum_of_money)

    return sum_of_money


print(deposit_money(0.1, 1, 10, 11, 0.5, 0.01, 1, 1))
the_list = list(dict_denominations.keys())
the_list.sort(key=float, reverse=True)

for key in the_list:
    print(key, ': ', dict_denominations.get(key), sep='')

