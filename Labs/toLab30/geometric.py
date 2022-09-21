import math


def give_geom_seq_element(a1=2, factor=2, index=2, return_tab_numbers=False, return_sum=False):
    # Function which give possibility to counting for geometric sequence
    a = a1
    tab_values_a = [a1]
    counter = 1
    sum_all = a

    while counter < index:
        a *= factor
        tab_values_a.append(a)
        counter += 1
        sum_all += a

    if return_tab_numbers:
        if return_sum:
            tab_values_a.append(sum_all)
            return tab_values_a
        else:
            return tab_values_a
    else:
        return tab_values_a[index - 1]


def give_factor_for_geom_seq(a1, a2, number_first_element=1, index=0, return_factor=True, return_tab_numbers=False,
                             return_sum=False):

    factor = a2 / a1
    counter = number_first_element
    a = a1
    while counter > 1:
        a /= factor
        counter -= 1

    if return_factor and not return_tab_numbers:
        return factor
    elif index > 0:
        if return_factor:
            tab = give_geom_seq_element(a, factor, index, return_tab_numbers)
            tab.append(factor)
            return tab
            # return give_geom_seq_element(a, factor, index, return_tab_numbers, return_sum).append(factor)
        else:
            return give_geom_seq_element(a, factor, index, return_tab_numbers, return_sum)
    else:
        return a


def geo_square_function(a='a', b='a', c='a', return_tab=False, return_sum=False, x='0'):

    if not str(a).isdecimal() or not str(b).isdecimal() or not str(c).isdecimal() or not str(x).isdecimal():
        while not str(a).isdecimal() or a == '0':
            a = input('Please input decimal value for a, which is not equal to 0:')
        else:
            a = int(a)

        while not str(b).isdecimal():
            b = input('Please input decimal value for b:')
        else:
            b = int(b)

        while not str(c).isdecimal():
            c = input('Please input decimal value for c:')
        else:
            c = int(c)

        while not str(x).isdecimal():
            x = input('Please input decimal value for x:')
        else:
            x = int(x)

    tab = []
    sum_f = 0
    counter = 0
    if x != 0:
        while counter < x:
            tab.append(a * counter ** 2 + b * counter + c)
            sum_f += tab[counter]
            counter += 1
        if return_sum:
            if return_tab:
                tab.append(sum_f)
                return tab
            else:
                return sum_f
        elif return_tab:
            return tab
        else:
            return tab[-1]
    else:
        delta = (b ** 2) - (4 * a * c)
        print(delta)
        if delta >= 0:
            x1 = (-b - math.sqrt(delta)) / (2 * a)
            x2 = (-b + math.sqrt(delta)) / (2 * a)
            tab.append(x1)
            tab.append(x2)
            return tab
        else:
            print('The function do not have any solution')
            return

