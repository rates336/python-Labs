import random as r


sweet = 0
sour = 0
salty = 0
taste_tab = [sweet, sour, salty]
tab_name_tastes = ['sweet', 'sour', 'salty']


def draw_blend(taste_tab):
    temp_place = r.randint(0, len(taste_tab) - 1)
    temp_sum = 0
    x = 0
    while x < len(taste_tab) - 1:
        temp = r.randint(0, 100 - temp_sum)
        taste_tab[temp_place] = temp
        temp_sum += temp
        if temp_place < len(taste_tab) - 1:
            temp_place += 1
        else:
            temp_place = 0
        x += 1
    else:
        if temp_place < len(taste_tab):
            taste_tab[temp_place] = 100 - temp_sum
        else:
            taste_tab[0] = 100 - temp_sum
        tmp = 0
        for x in taste_tab:
            print(tab_name_tastes[tmp], ': ', x, end='\t  ', sep='')
            tmp += 1


for x in range(1, 11):
    print('Draw', x, end='  \t\t')
    draw_blend(taste_tab)
    print()


# import random
#
#
# def random_with_sum(number_of_values, asserted_sum):
#     trial = 0
#     numbers = list(range(number_of_values))
#     while True:
#
#         trial += 1
#         for i in range(number_of_values):
#             numbers[i] = random.randint(1, 101)
#
#         if sum(numbers) == asserted_sum:
#             yield ((trial, numbers))
#             trial = 0
#
#
# for i in range(10):
#     (number_of_trials, numbers) = next(random_with_sum(3, 100))
#     print(number_of_trials, numbers)