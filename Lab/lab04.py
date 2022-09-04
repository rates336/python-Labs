# Testing zone
import datetime

print('\nTesting zone\n')
tmpString = 'Loading {1:s} on operation system {0:s}'
print(tmpString.format('Windows', 'Bla bla bla file.XD'))
print('\nEnd Testing zone\n')
# End Testing zone

message = 'Hello %s'
print(message % 'Elo 320 and %s' % 'Elo 420')
print(message % 'Elo 320', '\n' + message % 'Elo 420')

message2 = 'Hello {0:s} and {1:s}'
print(message2.format('Elo 320', 'Elo 5 2 0'))

helloMessage = '%s has %d %s'
print(helloMessage % ('Kate', 1, 'animal'))
# Note
# if in string is only one variable (%) to change you dont have to use brackets, otherwise brackets is necessary
print(helloMessage % ('Chris', 100_000, '$'))

helloMessage2 = '{0:s} has {1:d} {2:s}'
print(helloMessage2.format('Kate', 100_000, 'USD'))
print(helloMessage2.format('Chris', 1, 'dog'))

'''
9. [Trochę trudniejsze, ale cała trudność polega na samodzielnym zbudowaniu napisu formatującego i to w takiej postaci,
że na każdy element w napisie ma zostać przewidziana określona liczba znaków]
Utwórz zmienną line i wpisz do niej tekst pozwalający na wyświetlenie na 20 znakach pewnego napisu,
następnie słowa "costs", następnie na 6 znakach pewnej liczby i następnie znaku €, np:

ICE CREAM            costs      3 €
TRIP TO VENICE       costs    119 €
PIZZA HAWAII         costs      6 €
... BTW, wiesz jak uzyskać znak € z klawiatury? O ile używasz Windows powinien zadziałać prawy ALT + u

10. Korzystając ze zmiennej line i polecenia print,  zamieniaj odpowiednie znaczniki na podane niżej wartości,
tak aby w efekcie został wyświetlony cennik usług:

ICE CREAM    3
TRIP TO VENICE  119
PIZZA HAWAI  6
'''

line = '{0:20s} costs {1:6d}€'
# Note
# Reservation of place for symbols is not equals that "max of symbols", it's number which equalize space format
# If you enter more next symbols has been moved to correct position
print(line.format('Bread', 3), '\n', line.format('Villa in Warsaw', 123_000), '\n', line.format('Study', 3_000), sep='')
print()
print(line.format('Bread', 3))
print(line.format('Study', 3_000))
print(line.format('Villa in Warsaw', 123_000))

# Testing zone
print('\nTesting zone\n')
print(float('inf') / 2)
print('\nEnd Testing zone\n')
# End Testing zone

name = 'yoursName'
age = 20
daysInYear = 365
currentYear = datetime.date.today().year
bornYear = currentYear - age
messageX = '{0:s} is {1:d} years old, so is about {2:d} days old'
print(messageX.format(name, age, daysInYear * age))
print('So He/She/It born in:', bornYear)
messageX = '{0:s} is {1:d} years old, so is about {2:d} days old'
print(messageX.format('Paulina', 18, 18 * 365))
x = 1234567890
y = 12345
print('x = ', x, ', y = ', y, sep='')
print('rest of division x through y is:', x % y, 'and result of integer division is:', x // y)








