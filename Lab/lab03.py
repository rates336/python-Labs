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
folder = 'Users\\Karol\\PycharmProjects\\firstPythonProject\\Lab\\'
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
