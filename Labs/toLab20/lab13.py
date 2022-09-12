# Task !18
'''
2. Poniższy program ma za zadanie (w nieco dziwny sposób!) utworzyć napis o długości 10 znaków zapisany w zmiennej text.
Niestety coś poszło nie tak. Korzystając z debuggera znajdź przyczynę.
W odpowiedziach znajdziesz poprawną wersję skryptu z komentarzem
'''

text = ''
number = 10
condition = True

while condition:
    text += 'x'
    print(text)

    if len(text) > number:
        condition = False


data = ['Error:File cannot be open', 'Error:No free space on disk', 'Error:File missing',
        'Warning:Internet connection lost', 'Error:Access denied']

for errorMessage in data:
    print(errorMessage.upper())

elements = ['', '']
for errorMessage in data:
    elements[0] += errorMessage.split(':')[0] + ', '
    elements[1] += errorMessage.split(':')[1] + ', '

elements2 = []
for errorMessage in data:
    elements2 = errorMessage.split(':')

print(elements[0], elements[1].upper() if elements[0].count('Error') > 0 else elements[0], sep='\n')
print(elements2[0], elements2[1].upper() if elements2[0].__eq__('Error') else elements2[1])


string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'


for strA in range(10):
    print(string_A)

for strB in range(9):
    if strB % 2 == 0:
        print(string_A)
    else:
        print(string_B)

for tmp in range(1, 10):
    print('x' * tmp)

for strTmp in range(1, 10):
    if strTmp % 2 == 0:
        print('o' * strTmp)
    else:
        print('x' * strTmp)


x = 10
table = ''
lastResult = 1
for tmpX in range(1, x + 1):
    table += '{1:2d}! =\t{0:7d}\n'.format(lastResult * tmpX, tmpX)
    lastResult *= tmpX

print(table)

list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']

for tmpNoun in list_noun:
    for tmpAdj in list_adj:
        print(tmpAdj, tmpNoun)
