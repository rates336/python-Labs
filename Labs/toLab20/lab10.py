# Task !11
'''
Pracujesz dla firmy odzieżowej, której celem jest wypromowanie nowej kolekcji ubrań.
Firma ogłosiła konkurs, który ma na celu zdobywanie "lajków" i "udostępnień" na Facebooku.

Jeśli strona firmy otrzyma danego dnia co najmniej 500 "lajków" i co najmniej 100 "udostępnień",
to ceny spadną o 10%. Na razie masz napisać fragment programu,
który rozstrzygnie czy warunki promocji są spełnione czy nie. Jeśli już wiesz jak to zrobić "GO ON!",
a jeśli chcesz, aby Cię trochę pokierować - zajrzyj do kolejnych punktów:
'''

conditionLikes = 500
conditionShares = 100

currentlyLikes = 702
currentlyShares = 195

if currentlyLikes >= conditionLikes and currentlyShares >= conditionShares:
    print('Promo is active now, all things has a discount extra 10%.')
else:
    print('Promo condition is not satisfied.')

# Alternative
# if not currentlyLikes >= conditionLikes:
#     print('To promo yet lacking likes:', conditionLikes - currentlyLikes)
# elif not currentlyShares >= conditionShares:
#     print('To promo need more shares:', conditionShares - currentlyShares)
# else:
#     print('Promo is active now, all items has extra discount about 10%.')

# Task !12
'''
Pracujesz dla restauracji, która chce nagrodzić klientów zamawiających w dni robocze (poza weekendem) 
pizze lub duży napój. Klienci spełniający warunki promocji dostaną kupon na darmowego burgera. 

Na razie piszesz polecenie decydujące o spełnieniu warunków promocji. 
Do dyspozycji masz zmienne:

isPizzaOrdered - o wartości True/False, która informuje, czy klient kupił Pizzę

isBigDrinkOrdered - o wartości True/False, która informuje, czy klient zamówił duży napój

isWeekend - o wartości True/False, która informuje, czy jest weekend

Napisz polecenie IF, które w przypadku, gdy klient kupił pizzę lub duży napój w dzień poza weekendem,
wyświetli informację o kuponie na Burgera, a w przeciwnym razie wyświetli komunikat zachęcający do dalszych zakupów.

Zmieniaj wejściowe warunki logiczne i testuj, czy polecenie zwraca oczekiwany napis.
'''

isPizzaOrdered = True
isBigDrinkOrdered = True
isWeekend = False

if isWeekend:
    print('Today is weekend, go in work week to get coupon for buys which have pizza or big drink')
elif not isPizzaOrdered and not isBigDrinkOrdered:
    print('If you will get a coupon need bought pizza or big drink, if you buy twice you will get better offer')
elif not isPizzaOrdered:
    print()
elif not isBigDrinkOrdered:
    print('You must bought pizza or big drink to get a coupon')
else:
    if isPizzaOrdered and isBigDrinkOrdered:
        print('You will get coupon for set with a selected burger.')
    else:
        print('You will get coupon for a burger.')

# Alternative
# if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
#     # Bonus code
#     if isPizzaOrdered and isBigDrinkOrdered:
#         print('You will get coupon for set with a selected burger.')
#     else:
#         print('You will get coupon for a burger.')
# else:
#     print('Conditions to get a coupon is not satisfied.')

# Task !13

'''
3. Twój zespół opracowuje przeglądarkę internetową w Pythonie! Twoim zadaniem jest sprawdzenie, czy operacja 
pobierania pliku na dysk ma się szansę udać, czy jest od razu skazana na porażkę ze względu na brak miejsca na dysku. 

Na wejściu masz następujące zmienne:

diskSize - zmienna numeryczna (np. o wartości 140) oznaczająca wielkość dysku w GB

diskSizeUsed - zmienna numeryczna (np. o wartości 133) oznaczająca ilość zajętego miejsca na dysku w GB

fileSize - zmienna numeryczna (np o wartości 10) oznaczająca wielkość pobieranego pliku w GB

Zbuduj polecenie IF, które w przypadku, gdy jest wystarczająco wolnego miejsca na dysku wyświetli komunikat
"File can be downloaded". W przypadku, gdy plik jest za duży, ma być wyświetlony komunikat o braku miejsca na dysku
Zmieniając parametry wejściowe przetestuj działanie polecenia
'''

diskSize = 140
diskSizeUsed = 133
fileSize = 11

if diskSize - diskSizeUsed < fileSize:
    print('You dont have enough size in drive for the File.')
else:
    print('File can be downloaded.')

# Task !14

'''
Tym razem pomożemy lekarzom przeprowadzając wstępną analizę: czy pacjent ma grypę, czy tylko przeziębienie 
(zakładamy, że pacjentowi coś dolega, w tym zadaniu mamy tylko pomóc zdiagnozować czy to jest grypa czy przeziębienie):
'''

musclePain = False
fever = True
weakness = True

print('suspicion of influenza' if musclePain and fever and weakness else 'The flu is unlikely')
print('Just take a rest!' if weakness and (musclePain or fever) else 'You may be cold')

isMan = True
print('suspicion of influenza' if (musclePain and fever and weakness) or \
    ((musclePain or fever or weakness) and isMan) else 'The flu is unlikely')


# Task !15
'''
Zmieniamy temat. Pilot przed wystartowaniem powinien sprawdzić listę kontrolną.
Właśnie piszesz kod, który odpowiada za wyświetlenie napisu "CHECK IS COMPLETED" jeżeli lista kontrolna
została już pomyślnie wykonana i zamknięta, w przeciwnym razie powinien być wyświetlany komunikat
"CHECK NOT DONE YET!". Zmienna True/False, która zawiera informację o tym czy lista kontrolna została
już wykonana nazywa się isCheckCompleted. 

Korzystając z ternary operator przygotuj polecenie if wyświetlające odpowiedni komunikat
'''

isCheckCompleted = True
print('check is completed' if isCheckCompleted else 'check not done yet!')
isCheckCompleted = False
print('check is completed' if isCheckCompleted else 'check not done yet!')
