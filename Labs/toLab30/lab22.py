import datetime


def print_cat():
    txt = r'''
|\---/|
| o_o |
 \_^_/'''
    print(txt)
    return


def print_bear():
    txt = r'''
/  \.-"""-./  \
\    -   -    /
 |   o   o   |
 \  .-'"'-.  /
  '-\__Y__/-'
     `---`'''
    print(txt)
    return


def print_bat():
    txt = r'''
   /\                 /\
  / \'._   (\_/)   _.'/ \
 /_.''._'--('.')--'_.''._\
 | \_ / `;=/ " \=;` \ _/ |
  \/ `\__|`\___/`|__/`  \/
          \(/|\)/       '''
    print(txt)
    return


print_cat(), print_bear(), print_bat()

'''
def days_to_new_year(year=-1, month=-1, day=1):
    import datetime
    if year == -1:
        year = datetime.date.today().year
    if month == -1:
        month = datetime.date.today().month
    suitable_day = datetime.date(year, month, day)
    new_year = datetime.date(suitable_day.year + 1, 1, 1)
    delta = new_year - suitable_day
    # print(delta.days, 'days')
    return delta.days
    '''


def days_to_new_year(*dates):
    import datetime

    for date in dates:
        suitable_day = date
        new_year = datetime.date(suitable_day.year + 1, 1, 1)
        delta = new_year - suitable_day
        print(delta.days, 'days')
    return


# days_to_new_year(datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day)
# days_to_new_year(month=datetime.datetime.today().month, day=datetime.datetime.today().day,
#                  year=datetime.datetime.today().year)
# days_to_new_year(month=datetime.datetime.today().month)
days_to_new_year(datetime.date.today(), datetime.date(2019, 12, 1), datetime.date.today() + datetime.timedelta(-180))
# print(days_to_new_year())


def print_animal(*animal):
    txt = ''
    # if animal == '':
    #     txt = animal
    # el
    for element in animal:
        if element == 'cat':
            txt = r'''
|\---/|
| o_o |
 \_^_/'''
        elif element == 'bear':
            txt = r'''
/  \.-"""-./  \
\    -   -    /
 |   o   o   |
 \  .-'"'-.  /
  '-\__Y__/-'
     `---`'''
        elif element == 'bat':
            txt = r'''
   /\                 /\
  / \'._   (\_/)   _.'/ \
 /_.''._'--('.')--'_.''._\
 | \_ / `;=/ " \=;` \ _/ |
  \/ `\__|`\___/`|__/`  \/
          \(/|\)/       '''
        else:
            print('Can not print the animal please enter other animal')
            print('Your last choice is {:s}'.format(str(element)))

    print(txt)
    return


# print_animal('bat')
print('/1')
# print_animal('bat', 'dadad')
print('/2')
print_animal('bat', 'ddd', 'bear')
print('/3')
print_animal('bat', 'cat', 'bat')
print('/4')
print_animal('badt')
print('/5')
print_animal('badt', 'dadada', 'bear')
print('/6')
print_animal('')



