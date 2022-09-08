q = 'the eyes'

print(q)
print(q[1].upper() + q[2:3] + q[5])
print(q[0].upper() + q[1:3] + q[5])
print(q[q.__len__() - 1:].upper() + q[1:3] + '/' + q[1].upper() + q[2:3])
print(q[q.__len__() - 1:].upper() + q[q.__len__() - 2:q.__len__() - 1] + q[0])
print(q[q.__len__() - 3:q.__len__() - 2].upper() + q[q.__len__() - 2:])
# See

# They see
print(q[0]+q[1]+q[2]+q[5]+q[3]+q[7]+q[4]+q[6])

x = 'a gentleman'
print(x)
print(x[3] + x[6] + x[7] + x[2] + x[0] + x[4] + x[5] + x[1] + x[8:])

y = 'the morse code'
print(y)
# goal - here come dots
print(q[1:3] + y[6] + y[8:10] + \
      y[y.__len__() - 4:y.__len__() - 2] + y[4] + y[y.__len__() - 1] + \
      y[3] + y[y.__len__() - 2] + y[5] + y[0] + y[7])


# Task !08
'''
5. Zostajesz zatrudniony w firmie, która wykonuje analizę oglądalności poszczególnych programów TV.
Na bardzo początkowym etapie, Twój program musi przeczytać dane z pliku tekstowego z zapisanym harmonogramem 
poszczególnych programów. Plik zawiera linie zbudowane tak, że tytuł programu znajduje się w cudzysłowie,
a kończy się napisem o:, po którym następuje godzina, np tak:

'Program "Kropka nad i" nadamy o: 22:00'
Musisz wyodrębnić tytuł programu i godzinę o której zostanie nadany. W tym celu:

Do zmiennej line wpisz tekst "'Program "Kropka nad i" nadamy o: 22:00'"
Do zmiennej time wyodrębnij samą tylko godzinę (musisz poszukać znaku dwukropek i pobrać wszystkie dalsze znaki)
Wyświetl napis time
Do zmiennej tmp wyodrębnij fragment tekstu ze zmiennej line rozpoczynający się za znakiem cudzysłów do końca
Do zmiennej title wyodrębnij z tmp fragment tekstu od początku do znaku cudzysłów
Wyświetl title i time
To samo wykonaj dla linii
'Program "Pytanie na śniadanie" nadamy o: 6:00'
'''
print()
message = 'Program "Kropka nad i" nadamy o: 22:00'
a = message[message.find('\"') + 1:]
title1 = a[:a.find('\"')]
# Alternative
# title1 = message[message.find('\"') + 1:
#             message[message.find('\"') + 1:]
#             .find('\"') +
#             (message.__len__() -
#             message[message.find('\"') + 1:].__len__()) # Alternative: message.find('\"') + 1
#         ]

time1 = message[message.find(':') + 2:]
print('a:', a)
print('title1:', title1)
print('time1:', time1)
message2 = 'Program "Pytanie na śniadanie" nadamy o: 6:00'
title2 = message2[message2.find('\"') + 1: message2[message2.find('\"') + 1:].find('\"') +
        (message2.__len__() - message2[message2.find('\"') + 1:].__len__())]
time2 = message2[message2.find(':') + 2:]
print('title2:', title2)
print('time2:', time2)

# Task !09
'''
1. W tym zadaniu możesz się spodziewać ciekawego wyniku. (jeżeli chcesz sprawdzić jego działanie
w innym roku niż 2017 to zmień liczbę 1017, np dla roku bieżącego 2019 należy użyć 1019):

>>> Zapisz swój numer buta i pomnóż przez 5. Do tego dodaj 50. Całość pomnóż przez 20, a następnie dodaj 1017. 
Odejmij od tego swój rok urodzenia. Wyszła 4cyfrowa liczba. 
Pierwsze dwie cyfry to Twój numer buta a dwie ostatnie to Twój wiek.<<<

2. Kolejne działanie z tego samego cyklu:
>>>Pomyśl liczbę nieujemną całkowitą. Pomnóż ją przez 2, dodaj 10, podziel przez 2, odejmnij początkową liczbę.
Powinno wyjść 5 - zawsze. <<<
'''

shoeNr = 46
result = (shoeNr * 5 + 50) * 20 + 1022
# 50 * 20 + 1022 = current year
# shoeNr * 100 = xx00
# current year - birthYear = age
# xx00 + age = shoeNr_age

selectedNr = 1
result2 = (selectedNr * 2 + 10) / 2 - selectedNr
# 10 / 2 = 5
# * 2 / 2 = * 1
# (selectedNr - selectedNr) * 1 + 5
# () = 0
# 0 * 1 + 5 = 0 + 5 = 5

result3 = 6
result4 = 50

print(2 + 2 * 2)
print(7 + 7 / 7 + 7 * 7 - 7)

# Task !10

'''
4. Wykładowca mówi studentom. Zaliczysz semestr jeżeli masz obecność co najmniej 80% i średnią >= 3.0 lub 
zaliczyłeś pracę semestralną. Zbuduj wyrażenie w Python które stwierdzi czy student, który ma obecność 0.85,
średnią 3.5 i nie zaliczył pracy semestralnej zda czy nie.

5. Wykładowca zmienił zdanie. Aby zaliczyć semest trzeba: mieć obecność co najmniej 80%,średnią >=3.0 i zaliczoną pracę.
Czy teraz student zda?

6. Zmieniamy dane studenta. Teraz ma obecność 40%. średnią 2.5 ale zaliczył pracę semestralną.
Sprawdź wg którego z kryterów student zaliczy semestr.
'''

frequency1 = 0.85
average1 = 3.5
exam1 = False

isPromoted = (frequency1 >= 0.8 and average1 >= 3.0) or exam1
print('4 Promoted status:', isPromoted)


frequency2 = 0.85
average2 = 3.5
exam2 = False

isPromoted = frequency2 >= 0.8 and average2 >= 3.0 and exam2
print('5 Promoted status:', isPromoted)


frequency3 = 0.4
average3 = 2.5
exam3 = True

isPromoted1 = (frequency3 >= 0.8 and average3 >= 3.0) or exam3
isPromoted2 = frequency3 >= 0.8 and average3 >= 3.0 and exam3
print('6a Promoted status:', isPromoted1)
print('6b Promoted status:', isPromoted2)

