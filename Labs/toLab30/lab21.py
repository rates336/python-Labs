'''
1. Korzystając z rozwiązania poprzedniego LAB-a napisz
w zmiennej allCards zapisz pustą listę
napisz zagnieżdżoną pętlę, która dla każdego koloru z listy colors i dla każdej figury z listy figures
zapamięta w zmiennej aCard figurę (jest to słownik) - uwaga przepisując wartość skorzystaj z metody copy,
która rzeczywiście tworzy kopię obiektu (  aCard = f.copy()  )

do słownika aCard doda właściwość 'Color' o wartości w tej chwili przetwarzanego koloru
obiekt aCard dodaj do listy allCards

2. Zaimportuj moduł random i potasuj karty. Możesz je na tym etapie wyświetlić
3. Utwórz puste listy player1 i player2 i wybraną przez siebie metodą daj im równą ilość kart z allCards
4. Znowu możesz wyświetlić karty obu graczy

5. Ponieważ gra w wojnę trwa tak długo, aż jeden z graczy zostanie bez kart,
to napisz pętlę while, która będzie się wykonywać tak długo jak długo każdy z graczy ma karty

6. Korzystając z metody pop():
w zmiennej card1 zapisz kartę pobraną z listy player1
w zmiennej card2 zapisz kartę pobraną z listy player2

7. Porównaj właściwość 'Power' dla card1 i card2, następnie:
jeżeli karty mają jednakową moc, zwróć je na koniec listy z kartami graczy:
card1 wraca na koniec player1
card2 wraca na koniec player2

jeżeli card1 ma większą moc niż card2, to obie karty dopisz na końcu player1
jeżeli card2 ma większą moc niż card1, to obie karty dopisz na końcy player2

Podejmując wyżej opisaną decyzję wyświetl informację o kartach o tym kto wygrał.
Możesz dodatkowo wyświetlać ilość kart u gracza 1 i 2 lub np. tyle gwiazdek ile kart ma gracz numer 1 - sam zdecyduj

8. Za pętlą ustal kto ma karty i wyświetl informację o tym,  kto wygrał
9. Uruchom skrypt i zobacz jak komputer się bawi. Z opcją pokój rozgrywki mogą nigdy się nie skończyć...
więc w razie czego pamiętaj, że wykonanie skryptu możesz przerwać naciskając CTRL+C
Jedno z uruchomień, które wreszcie się skończyło u mnie wyglądało tak:
'''


import random

styles = ['Heart', 'Diamond', 'Club', 'Spade']
figures = [
    {'Figure': 'Ace',   'Power': 14},
    {'Figure': 'King',  'Power': 13},
    {'Figure': 'Queen', 'Power': 12},
    {'Figure': 'Jack',  'Power': 11},
    {'Figure': '10',    'Power': 10},
    {'Figure': '9',     'Power': 9},
    {'Figure': '8',     'Power': 8},
    {'Figure': '7',     'Power': 7},
    {'Figure': '6',     'Power': 6},
    {'Figure': '5',     'Power': 5},
    {'Figure': '4',     'Power': 4},
    {'Figure': '3',     'Power': 3},
    {'Figure': '2',     'Power': 2}
    ]

deck = []
for style in styles:
    for figure in figures:
        deck.append([figure.get('Figure'), style, figure.get('Power')])
else:
    random.shuffle(deck)
    print(deck)

listOfPlayers = ['Player1', 'Player2']
numberOfPlayers = listOfPlayers.__len__()
playersDecks = {}
for player in listOfPlayers:
    playersDecks[player] = []

counter = 0
counter2 = 0
print('-----------\n')
if deck.__len__() % numberOfPlayers == 0:
    while deck.__len__() // numberOfPlayers > counter:
        for player in playersDecks.keys():
            playersDecks.get(player).append(deck[counter2])
            counter2 += 1
        else:
            counter += 1
    else:
        for player in playersDecks.keys():
            print('============')
            print('Deck player:', player, playersDecks.get(player))
else:
    while deck.__len__() // numberOfPlayers > counter:
        for player in playersDecks.keys():
            playersDecks.get(player).append(deck[counter2])
            counter2 += 1
        else:
            counter += 1
    else:
        divisionRest = deck.__len__() % numberOfPlayers
        counter = 0
        while counter < divisionRest:
            # playersDecks.get(listOfPlayers[counter]).append(deck[counter2 + counter])
            playersDecks.get(list(playersDecks.keys())[counter]).append(deck[counter2 + counter])
            counter += 1
        else:
            for player in playersDecks.keys():
                print('============')
                print('Deck player:', player, playersDecks.get(player))

# input('To start press enter')
counterMoves = 0


# Future task
# Make possibility play more than only 2 players
print()
while playersDecks.get(listOfPlayers[0]).__len__() > 0 and playersDecks.get(listOfPlayers[0]).__len__() > 0 and \
        counterMoves < 10_000:

    counterMoves += 1
    print('\nConsole:\t', playersDecks.get(listOfPlayers[0])[0], '\t\tvs:\t\t', playersDecks.get(listOfPlayers[1])[0])
    if playersDecks.get(listOfPlayers[0])[0][2] > playersDecks.get(listOfPlayers[1])[0][2]:
        print('\t>>', listOfPlayers[1], 'lost card:', playersDecks.get(listOfPlayers[1])[0])
        playersDecks.get(listOfPlayers[0]).append(playersDecks.get(listOfPlayers[1])[0])
        playersDecks.get(listOfPlayers[1]).remove(playersDecks.get(listOfPlayers[1])[0])
        playersDecks.get(listOfPlayers[0]).append(playersDecks.get(listOfPlayers[0])[0])
        playersDecks.get(listOfPlayers[0]).remove(playersDecks.get(listOfPlayers[0])[0])
        continue

    if playersDecks.get(listOfPlayers[0])[0][2] < playersDecks.get(listOfPlayers[1])[0][2]:
        print('\t>>', listOfPlayers[0], 'lost card:', playersDecks.get(listOfPlayers[0])[0])
        playersDecks.get(listOfPlayers[1]).append(playersDecks.get(listOfPlayers[0])[0])
        playersDecks.get(listOfPlayers[0]).remove(playersDecks.get(listOfPlayers[0])[0])
        playersDecks.get(listOfPlayers[1]).append(playersDecks.get(listOfPlayers[1])[0])
        playersDecks.get(listOfPlayers[1]).remove(playersDecks.get(listOfPlayers[1])[0])
        continue

    print('Players have the same power on card')
    print(listOfPlayers[0], 'card:', playersDecks.get(listOfPlayers[0])[0], 'vs:',
          listOfPlayers[1], 'card:', playersDecks.get(listOfPlayers[1])[0])
    playersDecks.get(listOfPlayers[0]).append(playersDecks.get(listOfPlayers[0])[0])
    playersDecks.get(listOfPlayers[0]).remove(playersDecks.get(listOfPlayers[0])[0])
    playersDecks.get(listOfPlayers[1]).append(playersDecks.get(listOfPlayers[1])[0])
    playersDecks.get(listOfPlayers[1]).remove(playersDecks.get(listOfPlayers[1])[0])


else:
    print('\n\n\n\n\n/`/`/`__________________________________________________`\\`\\`\\')
    tab = '\t\t\t\t'
    if playersDecks.get(listOfPlayers[0]).__len__() > playersDecks.get(listOfPlayers[1]).__len__():
        print(tab, listOfPlayers[0], 'won the game!')
        print(tab, listOfPlayers[0], 'has', playersDecks.get(listOfPlayers[0]).__len__(), 'cards in his deck')
        print(tab,'Game finished in ', counterMoves, 'moves')
        print(tab, 'Congratulations', listOfPlayers[0], '!!!')
        print(tab, 'Thanks for game all players')
        print(tab, 'Deck of winner player:', '\n')
        print(playersDecks.get(listOfPlayers[0]))
    elif playersDecks.get(listOfPlayers[0]).__len__() < playersDecks.get(listOfPlayers[1]).__len__():
        print(tab, listOfPlayers[1], 'won the game!')
        print(tab, listOfPlayers[1], 'has', playersDecks.get(listOfPlayers[1]).__len__(), 'cards in his deck')
        print(tab, 'Game finished in ', counterMoves, 'moves')
        print(tab, 'Congratulations', listOfPlayers[1], '!!!')
        print(tab, 'Thanks for game all players')
        print(tab, 'Deck of winner player:''\n')
        print(playersDecks.get(listOfPlayers[1]))
    else:
        print(tab, 'It\'s draw')
        print(tab, 'Congratulations', listOfPlayers[0], 'and', listOfPlayers[1], '!!!')
        print(tab, 'Game finished in ', counterMoves, 'moves')
        print(tab, 'Deck of player:', listOfPlayers[0], '\n')
        print(playersDecks.get(listOfPlayers[0]))
        print(tab, 'Deck of player:', listOfPlayers[1], '\n')
        print(playersDecks.get(listOfPlayers[1]))


