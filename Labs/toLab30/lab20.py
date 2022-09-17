'''
W tym zadaniu zajmiemy się tasowaniem kart. Kto jako dziecko lubił tasować karty? Bo ja nie :)
Wybierz sobie język w jakim wykonasz to zadanie, albo... zrób je po polsku :)

1. Zadeklaruj zmienne opisujące figury kart i kolory:
colors = ['Hearts','Diamonds','Clubs','Spades']
figures = ['Ace','King','Queen','Jack','10','9']

2. Zadeklaruj zmienną allCards jako pustą listę
3. Napisz zagnieżdżoną pętlę, która przechodzi przez colors i figures i dodaje do allCards napis
będący połączniem nazwy koloru i figury
4. Wyświetl allCards - zauważ, że porządek kart jest wg kolorów i figur
5. Zaimportuj moduł random
6. Wymieszaj karty znajdujące się w zmiennej allCards. Wyświetl potasowane karty
7. Pora rozdać karty graczom. Zrobimy to na 2 sposoby. Ale najpierw zadeklaruj puste listy player1 i player2

8. Sposób pierwszy:
Do zmiennej max przypisz wartość określającą długość listy allCards
Napisz pętlę sterowaną przez zmienną i zmieniającą się od zera do max-1, a w tej pętli:
jeżeli i jest parzyste - dodaj element allCards[i] do listy player1
jeżeli i jest nieparzyste - dodaj element allCards[i] do listy player2
Wyświetl karty gracza 1 i 2

9. Sposób drugi - poprzednie rozwiązanie nawiązuje do tego w jaki sposób rozdajemy karty do gry.
Ale skoro karty i tak są wymieszane to w przypadku 24 kart można by pierwszych 12 dać pierwszemu graczowi,
a pozostałe 12 drugiemu. Dlatego: nie korzystając z pętli:
przepisz do player1 elementy z allCards od 0 do 11
przepisz do player2 elementy z allCards od 12 do 23
wyświetl karty obu graczy
'''
import random

colors = ['Heart', 'Diamond', 'Trefl', 'Pik']
figures = ['Ace', 'King', 'Queen', 'Jack', '10', '9']

allCards = []

for color in colors:
    for style in figures:
        allCards.append(style + ' ' + color)
else:
    print(allCards)
newTalion = allCards.copy()
random.shuffle(allCards)
print(allCards)

listOfPlayers = ['Player 1', 'Player 2']
cardPlayer1 = []
cardPlayer2 = []

max = allCards.__len__()
counter = 0
for card in allCards:
    if counter % 2 == 0:
        cardPlayer1.append(card)
    else:
        cardPlayer2.append(card)
    counter += 1
else:
    print('Cards player 1:\n', cardPlayer1)
    print('Cards player 2:\n', cardPlayer2)
counter = 0
cardPlayer1A = allCards[:12]
cardPlayer2A = allCards[12:]
print('========')
print('Cards player 1:\n', cardPlayer1A)
print('Cards player 2:\n', cardPlayer2A)
# Extra work
print('--------------------------')
if listOfPlayers.__len__() < 2 or listOfPlayers.__len__() > 4:
    print('Wrong number of players')
elif listOfPlayers.__len__() == 2:
    cardPlayer1 = []
    cardPlayer2 = []
    pile1 = []
    pile2 = []
    for card in allCards:
        if cardPlayer2.__len__() == pile1.__len__() and pile1.__len__() < 2:
            pile1.append(card)
        elif cardPlayer2.__len__() == pile2.__len__() and pile2.__len__() < 2:
            pile2.append(card)
        elif cardPlayer1.__len__() == cardPlayer2.__len__():
            cardPlayer1.append(card)
        else:
            cardPlayer2.append(card)
    else:
        print('Cards player: ', listOfPlayers[0], '\n', cardPlayer1, sep='')
        print()
        print('Cards player: ', listOfPlayers[1], '\n', cardPlayer2, sep='')
        print()
        print('Cards in pile 1:', '\n', pile1, sep='')
        print('Cards in pile 2:', '\n', pile2, sep='')




