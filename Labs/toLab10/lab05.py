# Task !06
'''
Zostajesz zatrudniony(a) do stworzenia oprogramowania pokładowego nowoczesnego samochodu.
Aktualnie Twoim zadaniem jest oprogramowanie sterownika odpowiedzialnego za automatyczne włączanie
świateł mijania w samochodzie. Będziesz pracować z następującymi zmiennymi:

- isAutomaticMode - zmienna logiczna, o następującym znaczeniu: wartość True oznacza,
że kierowca ustawił pokrętło sterujące światłem na tryb automatyczny.
Sterownik ma podejmować decyzję o zapaleniu świateł tylko jeżeli wartość tej zmiennej to True,
ale zapalenie świateł zależy jeszcze od kolejnych warunków,

- is80PercentLight - zmienna logiczna o następującym znaczeniu: wartość True oznacza, że "chyba" mamy dzień,
bo jest dość dużo światła. Światła w samochodzie powinny być zgaszone o ile nie ma innych warunków,
które wpływałyby na to, że światła mają się świecić. Jeśli wartość zmiennej to False,
tzn. że jest dość ciemno i światła powinny się zaświecić, oczywiście o ile jesteśmy w trybie automatycznym

- isDirectLight - zmienna logiczna o następującym znaczeniu: wartość True oznacza, że nisko położone słońce
świeci wprost w oczy kierowcy. Wprawdzie ciemno nie jest, ale w takich warunkach światła powinny się zaświecić,
oczywiście jeśli jesteśmy w trybie automatycznym

- isRainy - zmienna logiczna o następującym znaczeniu: wartość True oznacza, że pada deszcz,
jest mgła lub mamy do czynienia z innymi niekorzystnymi warunkami atmosferycznymi.
O ile jesteśmy w trybie automatycznym, to należy zaświecić światła



Do zmiennej turnLightsOn zapisz wynik wyrażenia, które w oparciu o w/w zmienne ustali,
czy światła mają zostać zapalone czy nie.
'''

isAutomaticMode = True
is80PercentLight = False
isDirectLight = False
isRainy = False
isTurnedLightsOn = isAutomaticMode and (is80PercentLight or isDirectLight or isRainy)
messageX = '{1:s} {0:s}'
print(messageX.format(str(isAutomaticMode), 'Automatic mode:'))
print(messageX.format(str(is80PercentLight), 'Is the light good:'))
print(messageX.format(str(isDirectLight), 'Is sun low:'))
print(messageX.format(str(isRainy), 'Is it rainy:'))
print(messageX.format(str(isTurnedLightsOn), '\nTURN LIGHTS ON:'))




