import cmath

PI = 3.14
radius = 5
fieldOfCircle = (radius.__pow__(2) * PI).__round__(2)
circuitOfCircle = (radius * 2 * PI).__round__(2)
diameterOfCircle = (radius * 2)
print('Circuit which radius =', radius, 'have:')
print('Field:', fieldOfCircle, '\nCircuit:', circuitOfCircle, '\nDiameter:', diameterOfCircle)

# Function round
# round(), __round__()
# first place is number which will be rounded, second is accuracy which number will be rounded

# Example using
# round(25.7552, 2) = 25.75,    round(25.405, 2) = 25.41,   round(25.404, 2) = 25.4
# number.__round__(4) is equals to round(number, 4)

rectangleSiteA = 5.15
rectangleSiteB = 4.04
circuitOfRectangle = ((rectangleSiteA + rectangleSiteB) * 2).__round__(2)
fieldOfRectangle = (rectangleSiteA * rectangleSiteB).__round__(2)
diagonalOfRectangle = cmath.sqrt(rectangleSiteB.__pow__(2) + rectangleSiteA.__pow__(2))
# diagonalOfRectangle = round(diagonalOfRectangle, 2)
# Future task 02
# find how to change it to can round it
'''
Traceback (most recent call last):
  File "C:/Users/Karol/PycharmProjects/firstPythonProject/Lab/lab02.py", line 24, in <module>
    diagonalOfRectangle = round(diagonalOfRectangle, 2)
TypeError: type complex doesn't define __round__ method
'''

print('\nCircuit which sites =', rectangleSiteA, 'and', rectangleSiteB, 'have:')
print('Field:', fieldOfRectangle, '\nCircuit:', circuitOfRectangle, '\nDiameter:', diagonalOfRectangle)

trapezeSiteA = 10.2
trapezeSiteB = 8.2
trapezeArm = 2.45
trapezeArm2 = trapezeArm
