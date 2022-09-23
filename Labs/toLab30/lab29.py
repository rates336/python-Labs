import sys


def show_range(give_list=None):
    if give_list is None:
        give_list = []
    try:
        give_list.append(0)
        give_list.remove(0)
    except:
        print('Wrong type got to the function')
    else:
        print('Select numbers from range 1 to', len(give_list), 'or from range -1 to -' + str(len(give_list)))


data_list = ['load data', 'export data', 'analyze & predict']
choice = ''
while not choice:
    choice = input('Select an operation to make from list using number where 1 is first and -1 is last\n' +
                   str(data_list) + '\n')
    try:
        choice = int(choice)
        if choice > 0:
            print('Your choice is:', data_list[choice - 1])
        elif choice < 0:
            print('Your choice is:', data_list[choice])
        else:
            print('You try to entered value 0 here.')
            show_range(data_list)
    except ValueError as e:
        print('You try to enter a value which is not a integer value')
        print('You enter a value:', choice)
        choice = ''
    except IndexError as e:
        print('You try enter a value out from the range')
        print('Your answer on question is:', choice)
        choice = 0
        show_range(data_list)

