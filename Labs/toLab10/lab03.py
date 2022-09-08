# Notes and Tips
# For change separator use:
# print('Here', 'enter', 'text', sep='_\t_')

# For use "bell" use it:
# print('\a')

# For use a custom symbol from ASCII system enter:
# print('\here ASCII code')

print('TVP1', 'TVP2', 'TVN', 'POLSAT', 'BBC', 'HBO', 'MTV', sep='; ')
print('I like computers', 'TVP1', 'TVP2', 'TVN', 'POLSAT', 'BBC', 'HBO', 'MTV.', sep=' but better is ')
programName = 'BBC'
item = 'News'
time = '18:00'
print('I like watching', item, 'at', time, 'on', programName, '.')
print('I like watching ', item, ' at ', time, ' on ', programName, '.', sep='')

test = item.endswith('q')
print(test)

exampleText = 'This is a text'
print(exampleText.find('is'))
print(exampleText.find('is', exampleText.find('is') + 1 ))

print(exampleText.replace('is', 'SI', exampleText.find('is') + 1))

quote = 'A good programmer is someone who always looks both ways before crossing a one-way street'

print(quote.upper())
print(quote.lower())
print(quote.endswith('street'))
print(quote.isupper())
print(quote.upper().isupper())
print(quote.find('one'), quote.replace('one', '1'), sep='\n')
print(quote.replace('one', '1').replace('both', '2'))
# Alternative
print("['", quote.replace(' ', "', '"), "']", sep='')
print(quote.split(' '))
print(not quote.isdigit(), quote.isdecimal(), quote.isalpha(), quote.replace('-', 'X').replace(' ', '').isalnum())

drive = 'C:\\'
folder = 'Users\\Karol\\PycharmProjects\\firstPythonProject\\Labs\\'
file = 'lab02.py'
print(drive, folder, file, sep='')
path = drive + folder + file
print(path)

# Testing zone
print('\nTesting zone\n')
rPath = r'\n'
rPath = path + rPath
rPath2 = r'TEST\\test'
print(rPath)
print(rPath2)
print('r' + path)
print('\nEnd Testing zone\n')
# End Testing zone


# Task !01
'''
1. Pracujesz w Urzędzie Stanu Cywilnego i ... korzystasz z Pythona. 
Dziewczyna o imieniu Kasia i nazwisku Sowa wychodzi za mąż za chłopaka o nazwisku Mrugała.
Pani Kasia chce zachować oba nazwiska.

Zdefiniuj zmienne firstName, famillyName i lastName i przypisz do nich napisy odpowiadające imieniu,
nazwisku panieńskim i nowym nazwisku. Następnie utwórz zmienną newName i zapisz w niej wynik konkatenacji
(czyli złączenia napisów) dla firstname, spacji, familyName, spacji i lastName. Wyświetl to nowe nazwisko
'''

firstName = 'Kasia'
familyName = 'Sowa'
lastName = 'Mrugała'

newName = familyName + ' ' + familyName + '-' + lastName
print(firstName, familyName, 'married with a boy which has lastname "Mrugała" and She wants have two-segmented lastname.')
print('Her currently lastname is:\n', newName, sep='')
# Alternative
# print('Her currently lastname is:', '\n' + newName)


# Task !02
'''
2. Zdefiniuj zmienną music o następującej zawartości (są to tytuły i autorzy piosenek z filmu Minionki):
"Universal Fanfare" Jerry Goldsmith "Happy Together" Garry Bonner "I'm a Man" Steve Winwood 

Uwaga! Ten napis zawiera zarówno apostrof jak i cudzysłów,
więc musisz zmodyfikować zapis metodami pokazanymi na tej lekcji, żeby zdefiniowanie zmiennej się udało.

3. W powyższym tekście mowa jest o 3 piosenkach. Zmień tekst tak, aby druga i trzecia piosenka podczas
wyswietlania były umieszczone w nowej linii. 
(znowu musisz w tekście dodać pewne znaki specjalne prezentowane na lekcji)
'''

music = '"Universal Fanfare" Jerry Goldsmith "Happy Together" Garry Bonner "I\'m a Man" Steve Winwood'
print('\n', music, sep='')
# Alternative
# music = '"Universal Fanfare" Jerry Goldsmith "Happy Together" Garry Bonner "I' + "'m a Man"+ '" Steve Winwood'
# print(music)

print(music.replace(' "', '\n"'))

# Task !03
'''
4. Przygotuj kilka poleceń print, które wyświetlą taki oto ascii art:
(\(\ 
( -.-) 
O_(")(")
'''
aa1 = '(\\'
print(aa1 + aa1)
# Alternative
# print('(\\(\\')
# aa1 = r'(\(\'
# print(aa1)

print('( -.-)')
# Alternative
# print('( ', '.', ') ', sep='-')
# print('( ', '.-) ', sep='-')

print('O_(")(")')
# Alternative
# aa2 = '(")'
# print('0_' + aa2 + aa2)
# print('0', aa2 + aa2, sep='_')
# print('0_', aa2, aa2, sep='')

# Testing zone
print('\nTesting zone\n')
testStr = '100'
print(type(int(testStr)))
print('\nEnd Testing zone\n')
# End Testing zone


article = '''This article is about the comedy group. For their TV show frequently called Monty Python, see Monty Python\'s Flying Circus.
"Pythonesque" redirects here. For the play by Roy Smiles, see Pythonesque (play).
"The Pythons" redirects here. For the documentary film about the group, see The Pythons (film).'''

print(article.upper())
print(article.lower().replace('monty', 'flying'))
print(article.split(' '))
print(article.lower().find('python'))
print(r'to print the \ you need to put \ twice in your text like this: \\')
print('or method which I used upper ;)')
print('The best hits of \'80s!!!')
print("The best hits of \'80s!!!")
print("The best hits of '80s!!!")

# Task !04
'''
9. Teraz zrobisz "mini kalkulator" do kantoru wymiany walut. Chcemy wyświetlić tabelkę w postaci:
cur   exchange amount
USD   3.65     64.10958904109589
EUR   4.23     55.31914893617021
w tym celu:
-najpierw zadeklaruj zmienną amountPLN i wpisz do niej wartość 234
-następnie wyświetl teksty rozdzielając wartości tabulatorem, tak aby to co zostanie wypisane na ekranie przypominało tabelkę 
(skorzystaj do tego z kilku poleceń print, jednolinijkowy print byłby zbyt trudny do zrozumienia)
-wartości w kolumnie amount wylicz dzieląc amountPLN przez aktualny kurs USD i EUR (w tym przykładzie są to 3.65 i 4.23)
'''
# Future task 03
# Connect to web and track price exchange and show currently here
# USD xx.yy = xx.yy PLN
# EUR xx.yy = xx.yy PLN
# GBP xx.yy = xx.yy PLN
# EUR xx.yy = xx.yy USD
# EUR xx.yy = xx.yy GBP
# USD xx.yy = xx.yy GBP

amountPLN = 234
priceExchangePLNtoUSD = 3.65
priceExchangePLNtoEUR = 4.23
amountOfExchangePLNtoUSD = (amountPLN / priceExchangePLNtoUSD).__round__(2)
amountOfExchangePLNtoEUR = (amountPLN / priceExchangePLNtoEUR).__round__(2)

priceExchange = 'USD\t' + str(priceExchangePLNtoUSD) + '\t' + str(amountOfExchangePLNtoUSD) + '\nEUR\t' + str(priceExchangePLNtoEUR) + '\t' + str(amountOfExchangePLNtoEUR)
print('You can change amount ', amountPLN, ' PLN to:\n', priceExchange, sep='')

valueAsText = '123.45'
factor = 1.23
print('value is', valueAsText, 'factor is', factor, 'value * factor = ', float(valueAsText) * factor)



