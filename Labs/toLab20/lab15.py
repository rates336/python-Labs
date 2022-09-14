# Task !21
'''
ZADANIE 1

Na konto została wpłacona kwota initialCapital w wysokości 20000. Oprocentowanie na koncie to percent = 0.03.
Klient banku postanawia oszczędzać przez maxTimeYears = 10 lat. Po każdym roku oszczędzania zarobiona kwota jest
dodawana do oszczędności i zarabia odsetki przez pozostały czas.

Zadeklaruj wymagane zmienne, a następnie stwórz pętlę, która wyświetli informację o tym ile pieniędzy jest na koncie
pod koniec roku, kiedy odsetki się kapitalizują. Dodaj na zakończenie informację o całkowitej kwocie zarobionej w banku.
'''

initialCapital = 20_000
percentCapitalized = 0.03

maxTimeYears = 10
counter = 0
while counter < maxTimeYears:
    initialCapital *= (1 + 0.03)
    print(initialCapital.__round__(2))
    counter += 1
else:
    print('Total amount of money:', initialCapital.__round__(4))

# Task !22
'''
ZADANIE 2

Dana jest liczba całkowita dodatnia number = 20730906, Oblicz sumę cyfr tej liczby.
'''

number = 20_730_906
tempNumber = 0
tempSum = 0
lengthNumber = len(str(number))
tempList = []
print(lengthNumber)
while 0 < lengthNumber:
    tempList.append((number - tempNumber) // (10 ** (lengthNumber - 1)))
    tempNumber += tempList[-1] * (10 ** (lengthNumber - 1))
    tempSum += tempList[-1]
    lengthNumber -= 1
else:
    print(tempSum)

# Task !23

'''
ZADANIE 3

Dany jest tekst:

United Space Alliance: This company provides major support to NASA for
various projects, such as the space shuttle. One of its projects is to
create Workflow Automation System (WAS), an application designed to
manage NASA and other third-party projects. The setup uses a central
Oracle database as a repository for information. Python was chosen over
languages such as Java and C++ because it provides dynamic typing and
pseudo-code–like syntax and it has an interpreter. The result is that
the application is developed faster, and unit testing each piece is easier.

policz ile jest w nim słów dłuższych od wordLength = 6
'''

text = 'United Space Alliance: This company provides major support to NASA for various projects, such as the space \
shuttle. One of its projects is to create Workflow Automation System (WAS), an application designed to manage NASA \
and other third-party projects. The setup uses a central Oracle database as a repository for information. \
Python was chosen over languages such as Java and C++ because it provides dynamic typing and pseudo-code–like \
syntax and it has an interpreter. The result is that the application is developed faster, \
and unit testing each piece is easier.'

counter = 0
txt = ''
for tmpStr in text.split(' '):
    if tmpStr.strip(',./;\'[]-=`\\|<>?:"{}_+~!@#$%^&*()123456789\n\t\r').replace('-', '').__len__() > 6:
        counter += 1
else:
    print('Numbers of words longer from 6 letters is:', counter)


# Task !24
'''
ZADANIE 1

Ciąg Fibonacciego to ciąg rozpoczynający się od 0 i 1 a każda kolejna liczba to suma dwóch poprzednich, np:

0
1
0+1 = 1
1+1 = 2
1+2 = 3
2+3 = 5
....

Korzystając z pętli for napisz program, który wyliczy fibonacciIterations=20 pierwszych elementów ciągu Fibonacciego
'''


x = 20
counter = 0
tmpInt = 0
while counter < x:
    tmpInt += counter
    counter += 1
else:
    print('Final result', tmpInt)

# Alternative
tmpInt = x * (x/2) - 5 * (x / 10)
print(tmpInt)

# Task !25
'''
ZADANIE 2

Masz dany tekst:

Industrial Light & Magic: In this case, you find Python
used in the production process for scripting complex,
computer graphic-intensive films. Originally, Industrial
Light & Magic relied on Unix shell scripting, but it was
found that this solution just couldn’t do the job. Python
was compared to other languages, such as Tcl and Perl, and
chosen because it’s an easier-to-learn language that the
organization can implement incrementally. In addition, Python
can be embedded within a larger software system as a scripting
language, even if the system is written in a language such as
C/C++. It turns out that Python can successfully interact with
these other languages in situations in which some languages can’t.
Twoim zadaniem jest wyświetlić tylko te słowa, które zawierają literkę "p"
'''

text = 'Industrial Light & Magic: In this case, you find Python used in the production process for scripting complex, \
computer graphic-intensive films. Originally, Industrial Light & Magic relied on Unix shell scripting, but it was \
found that this solution just couldn’t do the job. Python was compared to other languages, such as Tcl and Perl, and \
chosen because it’s an easier-to-learn language that the organization can implement incrementally. In addition, Python \
can be embedded within a larger software system as a scripting language, even if the system is written in a language \
such as C/C++. It turns out that Python can successfully interact with these other languages in situations in which \
some languages can’t.'

counter = 0
for tmpStr in text.split(' '):
    tmpStr = tmpStr.strip(',./;\'[]-=`\\|<>?:"{}_+~!@#$%^&*()123456789\n\t\r')
    # if tmpStr.lower().find('p') > 0 or tmpStr.find('P') > 0:
    # if tmpStr.lower().count('p') > 0:
    if tmpStr.lower() in 'p':
        print(tmpStr)
        counter += 1
else:
    print('Numbers of words which have letter "p" is:', counter)


# Task !26
'''
Dany masz słownik:

dictionary={'A':'80%-100%','B':'60%-80%','C':'50-60%','D':'less then 50%'} 

Wyświetl zestawienie w postaci (kolejność nie jest istotna):

A - 80%-100%
B - 60%-80%
C - 50-60%
D - less then 50%
'''

dictionary = {'A': '80%-100%', 'B': '60%-80%', 'C': '50-60%', 'D': 'less then 50%'}

for variable in dictionary:
    print(variable, '-', dictionary.get(variable))


# Task !27
'''
ZADANIE 4 ***

Należy policzyć ile razy w w/w tekście występowały poszczególne słowa
'''


text = 'Industrial Light & Magic: In this case, you find Python used in the production process for scripting complex, \
computer graphic-intensive films. Originally, Industrial Light & Magic relied on Unix shell scripting, but it was \
found that this solution just couldn’t do the job. Python was compared to other languages, such as Tcl and Perl, and \
chosen because it’s an easier-to-learn language that the organization can implement incrementally. In addition, Python \
can be embedded within a larger software system as a scripting language, even if the system is written in a language \
such as C/C++. It turns out that Python can successfully interact with these other languages in situations in which \
some languages can’t.'

dictWords = {}
for tmpStr in text.split(' '):
    tmpStr = tmpStr.strip(',./;\'[]-=`\\|<>?:"{}_~!@#$%^&*()123456789\n\t\r').lower()
    if tmpStr.__len__() > 0:
        dictWords.setdefault(tmpStr, 0)
        dictWords[tmpStr] = dictWords.get(tmpStr) + 1

print(dictWords)
print(dictWords.__len__())
