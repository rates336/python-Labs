import random

numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]

lengthNumbers = numbers.__len__() - 1
temp = 0
operationTab = []
operationTab2 = []
operationVariable = 0
operationVariable2 = 0
while temp < lengthNumbers:
    if numbers[temp] ** 2 == numbers[temp + 1]:
        print('Found new match pair of numbers /2')
        operationTab.append(str(numbers[temp]) + ', ' + str(numbers[temp + 1]))
        operationVariable += 1
    temp += 1
temp = 0
while temp < lengthNumbers - 1:
    if numbers[temp] ** 2 == numbers[temp + 1] and numbers[temp + 1] ** 2 == numbers[temp + 2]:
        print('Found new match of numbers /3')
        operationTab2.append(str(numbers[temp]) + ', ' + str(numbers[temp + 1]) + ', ' + str(numbers[temp + 2]))
        operationVariable2 += 1
    temp += 1

# Alternative
# while temp < lengthNumbers:
#     if numbers[temp] ** 2 == numbers[temp + 1]:
#         if numbers[temp + 1] ** 2 == numbers[temp +2]:
#             print('Found new match pair of numbers /2')
#             operationTab.append(str(numbers[temp]) + ', ' + str(temp + 1))
#             operationVariable += 1
#             print('Found new match of numbers /3')
#             operationTab2.append(str(numbers[temp]) + ', ' + str(numbers[temp + 1]) + ', ' + \
#                                                 str(numbers[temp + 2]))
#             operationVariable2 += 1
#         else:
#             print('Found new match pair of numbers /2')
#             operationTab.append(str(numbers[temp]) + ', ' + str(temp + 1))
#             operationVariable += 1
#     temp += 1
# else:
#     print('Finish analyzing this list')
#     operationVariable = 0
#     operationVariable2 = 0

lengthOperationTab = operationTab.__len__()
lengthOperationTab2 = operationTab2.__len__()
temp = 0
while temp < lengthOperationTab2:
    print('OT1-' + str(temp) + ' :', operationTab[temp], '\t\tOT2-' + str(temp) + ':', operationTab2[temp])
    temp += 1
else:
    while temp < lengthOperationTab:
        print('OT1-' + str(temp) + ':', operationTab[temp])
        temp += 1
    else:
        print('Done')

texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
temp = 0
lengthTexts = texts.__len__() - 2
operationList = []
opTemp = 0
while temp < lengthTexts:
    if texts[temp].__len__() == texts[temp + 1].__len__():
        print('Founded new matching pair')
        operationList.append(texts[temp] + ' : ' + texts[temp + 1])
    temp += 1
else:
    print('Done')
temp = 0
while temp < operationList.__len__():
    print(operationList[opTemp])
    opTemp += 1
    temp += 1

previousNumber = 0
number = 1

while previousNumber < 50:
    print('Sum of 2 next numbers is:', previousNumber + number)
    # Alternative
    # print(previousNumber * 2 + 1)
    # print(number * 2 - 1)
    number += 1
    previousNumber = number
else:
    print('Done')


# Task !17
'''
Teraz napiszesz... poniek??d prost?? gr??. 
Zasady s?? proste. Komputer wymy??li sobie liczb?? od 0 do 20, a Ty musisz j?? zgadn????!

Polecenia
import random
my_number = random.randint(0,20)
wygeneruj?? liczb?? losow?? i umieszcz?? jej warto???? w zmiennej my_number (wi??cej o module random w dalszej cz??????i kursu).

Zadeklaruj zmienn?? guess i przypisz jej warto???? -1 
(to warto???? spoza zakresu losowanych liczb - czyli na pewno nie jest r??wna wylosowanej liczbie)

Wy??wietl instrukcj?? do gry - przynajmniej s??owa "Guess my number!"
Wykonuj p??tl?? while tak d??ugo jak warto???? w zmiennej guess jest r????na od warto??ci my_number
poleceniem
guess = int(input())

wczytaj odpowied?? u??ytkownika (uwaga program nie jest odporny na wprowadzenie w tym miejscu np. 
napisu zamiast liczby - o obs??udze b????d??w opowiadam w ostatnim module kursu)

Sprawd?? warto???? liczby guess i je??eli jest r??wna my_number, to wy??wietl gratulacje
w przeciwnym razie je??li guess jest wi??ksze od my_number wy??wietl "
Sorry- my number is smaller than your guess, Try again!"
w przeciwnym razie wy??wietl  "Sorry- my number is greater than your guess, Try again!"

A teraz pobaw si?? kilka razy ;)
'''
tab = []
trials = 0
while tab.__len__() < 50:
    tab.append(random.randint(0, 19))
else:
    print(tab)

my_number = random.randint(0, 19)
guess = -1
print('Hi your role is try to guess number which computer selected')
guessComputer = -1
while guess != my_number:
    guess = int(input())
    if my_number > guess:
        print('It\'s not this number, number is higher than your type, Try again!')
    else:
        print('It\'s not this number, number is lower than your type, Try again!')
    trials += 1
else:
    print('Congratulation, You won, the number is:', guess)
    print('and your number of trials is:', trials)
    trials = 0

while guessComputer != my_number and trials < 50:
    guessComputer = tab[trials]
    print(guessComputer)
    trials += 1
else:
    print('Computer numbers of trials is:', trials)

















