import random

randNumbersTab = []
counter = 0
while counter < 10:
    randNumbersTab.append(random.randint(1, 100))
    counter += 1
else:
    print(randNumbersTab)

expectedNumber = random.randint(1, 100)
counter = 0
currentNumber = -1
while expectedNumber != currentNumber:
    currentNumber = random.randint(1, 100)
    counter += 1
else:
    print('Number:', expectedNumber, '=', currentNumber)
    print('Times needed to draw it:', counter)


countries = [
    'Uruguay', 'Russia', 'Saudi Arabia', 'Egypt', 'Spain', 'Portugal', 'Iran', 'Morocco', 'France', 'Denmark', 'Peru',
    'Australia', 'Croatia', 'Argentina', 'Nigeria', 'Iceland', 'Brazil',  'Switzerland',  'Serbia',  'Costa Rica',
    'Sweden', 'Mexico', 'Korea Republic', 'Germany', 'Belgium', 'England', 'Tunisia', 'Panama', 'Colombia', 'Japan',
    'Senegal', 'Poland'
    ]
print(countries)
random.shuffle(countries)
print(countries)

groupNumber = 0

for country in countries:
    if countries.index(country) % 4 == 0:
        groupNumber += 1
        print('<<----  Group', groupNumber, ' ---->>')
    print(country)


numberMin = 1
numberMax = 6
dice = random.randint(numberMin, numberMax)
throwADice = 10
counter = 0
diceHistory = {'Dice_1': 0, 'Dice_2': 0, 'Dice_3': 0, 'Dice_4': 0, 'Dice_5': 0, 'Dice_6': 0}
while counter < throwADice:
    dice = random.randint(numberMin, numberMax)
    if dice == 1:
        print('   o')
    elif dice == 2:
        print('o   o')
    elif dice == 3:
        print('o')
        print('   o')
        print('      o')
    elif dice == 4:
        print('o   o')
        print('o   o')
    elif dice == 5:
        print('o   o')
        print('  o')
        print('o   o')
    else:
        print('o   o')
        print('o   o')
        print('o   o')

    print('---------')
    counter += 1
    diceHistory[('Dice_' + str(dice))] = diceHistory.get('Dice_' + str(dice)) + 1

print(diceHistory)
