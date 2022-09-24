colors = ['red', 'orange', 'green', 'purple', 'blue', 'yellow']


def select_colors(number=0, list_of_colors=None):
    if number < 1 or list_of_colors is None:
        print('Wrong value sent to function')
        print('To function was send number:', number)
        print('To function was send list:', list_of_colors)
        return -1

    return colors[:number]


def to_strong(number=0):
    tmp = 1
    while tmp <= number:
        tmp *= tmp
    else:
        return tmp


def get_all_chances_list(the_list=None, amount_to_return=0, return_more_or_low_quantity=0):
    if the_list is None:
        print('Wrong value sent to function')
        print('To function was send list:', the_list)
        return -1
    len_the_list = len(the_list)
    amount_to_return = len_the_list if amount_to_return == 0 else False
    list_of_all_combinations = []
    counter2 = 1
    tmp_list = []
    if True:
        counter = to_strong(len_the_list) / (to_strong(amount_to_return) * to_strong(len_the_list - amount_to_return))
        while counter > 0:
            loop_list = []
            for x in range(len_the_list):
                tmp_list = [the_list[x]]
                loop_list.append(tmp_list)
            while counter2 < len_the_list:




