import time
import calendar
import math

'''
ZADANIE 1

Załaduj moduł math
Wyświetl informację o ilości elementów w obu listach
Napisz instrukcję if, która:

-jeśli liczba elementów na obu listach jest taka sama, to rozpocznie przetwarzanie danych, które opiszemy dalej 
(na razie wystarczy np wyświetlić napis "ok")
-jeśli liczba elementów nie jest zgodna wyświetli informację "inputdata and factortable need to have equal number of elements"

Ciąg dalszy skryptu piszesz w pierwszej części polecenia if
Napisz pętlę, która przechodzi przez wszystkie elementy listy input  data
Ciąg dalszy piszesz w tej pętli

wylicz wartość minvalue, która ma wynosić:
<wartość n-tego elementu z inputdata> - <wartość n-tego elementu z factortable> * <wartość n-tego elementu z inputdata>
oraz wartość maxvalue, która ma wynosić:
<wartość n-tego elementu z inputdata> + <wartość n-tego elementu z factortable> * <wartość n-tego elementu z inputdata>

Wyświetl wyliczone wartości

Wyznacz liczby
mininteger, która ma być największą liczbą całkowitą mniejszą od minvalue (funkcja floor)
oraz
maxinteger, która ma być najmniejszą liczbą całkowitą większą of maxVALUE (funkcja ceil)

Wyświetl liczby: mininteger, n-ty element listy inputdata i maxinteger
'''


print(time.time())
print(time.localtime(time.time()))

print(calendar.month(2002, 6))
print(calendar.monthcalendar(2002, 6))
print(calendar.monthrange(2002, 6))
calendar.setfirstweekday(6)
print(calendar.firstweekday())
print(calendar.monthcalendar(2002, 6))
print(calendar.month(2002, 6))
calendar.setfirstweekday(0)
print(calendar.month(2002, 6))
print(calendar.isleap(2000))
print(calendar.calendar(2019))


inputData = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
factorTable = [0, 0.01, 0.02, 0.03, 0.05, 0.08, 0.13, 0.21, 0.34, 0.55, 0.89]
minValues = []
maxValues = []
print(inputData.__len__())
print(factorTable.__len__())

if inputData.__len__() == factorTable.__len__():
    for element in inputData:
        for element2 in factorTable:
            minValues.append((element - element2 * element).__round__(2))
            maxValues.append((element + element2 * element).__round__(2))
    print(minValues)
    print(maxValues)
else:
    print('inputData and factorTable need to have equal number of elements')

print(math.floor(min(minValues)))
print(math.ceil(max(maxValues)))
print(inputData[-1])


