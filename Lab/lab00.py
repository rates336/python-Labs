from datetime import date

print('Hello Python on this PC!')
print('Nice to see you ;)')

input('Press enter to continue')


print(23 - 28)
print((18 - 0) * 12 * 500, 'PLN', (18 - 2) * 12 * 500, 'PLN', 'difference', (18 - 0) * 12 * 500 - (18 - 2) * 12 * 500, 'PLN')
print()


print(date.today())

print(date.today().strftime("%A"))

text = 'test'
print(text == 'test')


# Task !00

'''
Ten skrypt policzy ile razy mrugamy okiem w czasie X lat.
Zakladamy ze:
-liczba mrugniec na minute to 20
-liczba minut w godzinie to 60
-liczba godzin w dobie 24
-liczba lat (czyli nasz X) 50
Uwaga: jezeli przyjac ze spimy 8 godzin to liczba godzin na dobe
powinna wynosic 16
'''
hertzOfBlinked = 20
x = 50
print('In', x, 'years human blinks', 20 * 60 * 24 * 365 * x, 'times')
# Number minutes in hour is 60
hour = 60
# Number hours in day is 24
day = 24
# Number days in year is 365
year = 365
numberOFBlinks = hertzOfBlinked * hour * day * year * x;
print('In', x, 'years human blinks', numberOFBlinks, 'times')
print(numberOFBlinks / 1_000_000, 'mln')
test = 'alfa2'
print(test.split('a', 5))

print('In 5 hours 5 fly will be eaten by 5 spiders')
print('so in 100 hours 100 spiders eat 2000 flies')


