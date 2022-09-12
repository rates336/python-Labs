#  Task !19
'''
Twoim zadaniem jest zbudowanie streszczeń tych definicji poprzez wyświetlenie tylko pierwszych 20 słów z
każdej definicji. Zmień w odpowiedni sposób rozwiązanie zadania 1, tak aby przetwarzana była cała lista
'''

text = 'Mechanical advantage is a measure of the force amplification achieved by using a tool, ' \
       'mechanical device or machine system. The device preserves the input power and simply trades off forces ' \
       'against movement to obtain a desired amplification in the output force. ' \
       'The model for this is the law of the lever. ' \
       'Machine components designed to manage forces and movement in this way are called mechanisms.[1] ' \
       'An ideal mechanism transmits power without adding to or subtracting from it. ' \
       'This means the ideal mechanism does not include a power source, is frictionless, ' \
       'and is constructed from rigid bodies that do not deflect or wear. ' \
       'The performance of a real system relative to this ideal.'

words = ''
counter = 0
for word in text.split(' '):
    if counter < 19:
        words += word + ' '
        counter += 1
    else:
        words += word
        print(words)
        break


definitions = [
    'Mechanical advantage is a measure of the force amplification achieved by using a tool, mechanical device or machine system. The device preserves the input power and simply trades off forces against movement to obtain a desired amplification in the output force. The model for this is the law of the lever. Machine components designed to manage forces and movement in this way are called mechanisms.[1] An ideal mechanism transmits power without adding to or subtracting from it. This means the ideal mechanism does not include a power source, is frictionless, and is constructed from rigid bodies that do not deflect or wear. The performance of a real system relative to this ideal.',
    'Ein Kraftwandler ist eine mechanische Anordnung zur Veränderung einer Kraft in Bezug auf ihren Angriffspunkt, ihre Richtung oder ihren Betrag. Die einfachsten Kraftwandler sind Seile, Stangen, Rollen, schiefe Ebenen und Hebel. Dies sind gleichzeitig die grundlegenden einfachen Maschinen.',
    'La ventaja mecánica es una magnitud adimensional que indica cuánto se amplifica la fuerza aplicada usando un mecanismo (ya sea una máquina simple, una herramienta o un dispositivo mecánico más complejo) para contrarrestar una carga de resistencia.',
    'Cette notion s\'applique de manière évidente dans les systèmes de poulies et de leviers. Elle est centrale dans les systèmes de freinage : on applique une petite force sur un parcours important et l\'on obtient une force importante transmise au système de freinage pour une course de faible distance.'
    ]


counter = 0
counter2 = 0
strTmp = ''
print()
for defTmp in definitions:
    for word in defTmp.split(' '):
        if counter < 20:
            strTmp += word + ' '
            counter += 1
        else:
            counter2 = strTmp.count('.')
            temp = ''
            if counter2 > 0:
                for sentence in strTmp.split('.'):
                    if counter2 > 0:
                        temp += sentence + '.'
                        counter2 -= 1
                    else:
                        print(temp)
                        break
                strTmp = ''
                counter = 0
                break
            else:
                print(strTmp + '...')
                counter = 0
                strTmp = ''
                break

# Alternative
# for defTmp in definitions:
#     for word in defTmp.split(' '):
#         if counter < 20:
#             strTmp += word + ' '
#             counter += 1
#             continue
#         counter2 = strTmp.count('.')
#         temp = ''
#         if counter2 > 0:
#             for sentence in strTmp.split('.'):
#                 if counter2 > 0:
#                     temp += sentence + '.'
#                     counter2 -= 1
#                     continue
#                 print(temp)
#                 break
#             strTmp = ''
#             counter = 0
#             break
#
#             continue
#         print(strTmp + '...')
#         counter = 0
#         strTmp = ''
#         break


# Task !20

'''
woim zadaniem jest stworzenie fragmentu programu, który wyświetla menu z opcjami do wyboru, 
a następnie zależnie od dokonanego wyboru wykona pewne czynności.

Zadeklaruj zmienne:


Napisz pętlę while, która będzie działać w nieskończoność. 
W tej pętli:

wyświetl napis menu z dostępnymi opcjami

wczytaj do zmiennej letter wybór użytkownika

napisz polecenie if, które w przypadku, gdy w letter znajduje się 1

wyświetli informację "Function COFFEE not implemented"

poprosi o naciśnięcie ENTER

wróci na początek pętli while

napisz polecenie  if, które w przypadku, gdy w letter znajduje się 2

wyświetli informację "Function TEA not implemented"

poprosi o naciśnięcie ENTER

wróci na początek pętli while

napisz polecenie if, które w przypadku, gdy w letter znajduje się 3

wyświetli napis znajdujący się w zmiennej smile

poprosi o naciśnięcie ENTER

wróci na początek pętli while

napisz polecenie if, które w przypadku, gdy w letter znajduje sie 0

przerwie działanie nieskończonej pętli while

w każdym pozostałym przypadku wyświetli instrukcję czekając na naciśnięcie ENTER: 
"You need to make a valid choice. Press ENTER and try again!"
'''


menu = '''
Choose what you want me to do for you:
1 - COFFEE
2 - TEA
3 - MAKE ME SMILE
---------------
To stop this script select 0
'''

smile = '''
 
                          oooo$$$$$$$$$$$$oooo
                      oo$$$$$$$$$$$$$$$$$$$$$$$$o
                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
oo $ $ "$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
"$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  """$$$
   "$$$""""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$
    $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$o
   o$$"   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" "$$$$$$ooooo$$$$o
  o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
  $$$$$$$$"$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$""""""""
 """"       $$$$    "$$$$$$$$$$$$$$$$$$$$$$$$$$$$"      o$$$
            "$$$o     """$$$$$$$$$$$$$$$$$$"$$"         $$$
              $$$o          "$$""$$$$$$""""           o$$$
               $$$$o                                o$$$"
                "$$$$o      o$$$$$$o"$$$$o        o$$$$
                  "$$$$$oo     ""$$$$o$$$$$o   o$$$$""
                     ""$$$$$oooo  "$$$o$$$$$$$$$"""
                        ""$$$$$$$oo $$$$$$$$$$
                                """"$$$$$$$$$$$
                                    $$$$$$$$$$$$
                                     $$$$$$$$$$"
                                      "$$$""""
'''
print(menu)
choice = input()
while choice != '0':
    if choice == '3':
        print(smile)
        print('You can decide what you want get later:')
        print(menu)
        choice = input()
        continue
    if choice == '1':
        print('Function tea not implemented')
        print('please press enter')
        choice = input()
        continue
    if choice == '2':
        print('Function coffee not implemented')
        print('please press enter')
        choice = input()
        continue


