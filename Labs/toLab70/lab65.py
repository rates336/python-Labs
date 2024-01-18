import math
import itertools


'''
def find_perfect_number(to_range):

    perfect_numbers = []
    for number in range(1, to_range + 1):
        natural_dividers = []
        for x in range(1, number // 2 + 1):
            if number % x == 0:
                natural_dividers.append(x)
        else:
            if sum(natural_dividers) == number:
                perfect_numbers.append(number)

    else:
        print(perfect_numbers)


find_perfect_number(500)
'''


def find_perfect_number(to_range):

    perfect_numbers = []
    result = []
    for number in range(1, to_range):
        tmp_list = range(1, number // 2 + 1)
        tmp_list = itertools.filterfalse(lambda x: number % x != 0, tmp_list)
        if number == sum(tmp_list):
            perfect_numbers.append(number)
    else:
        for e in result:
            print(e)
        print(perfect_numbers)


find_perfect_number(500)

