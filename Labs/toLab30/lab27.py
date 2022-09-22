import os
import sys

line = input('Please enter price which you can pay for course on udemy\n')

path = r'C:\Python\experiments\pxe\2022-9-21\last2.txt'
try:
    with open(path, 'a') as file:
        file.write(line)
        value = int(line)
        print('The value is saved in file')
except FileNotFoundError as e:
    print('Error opening file')
    print(sys.exc_info()[:2])
except ValueError as e:
    print('Invalid value price, please enter only numbers')
    print(sys.exc_info()[:2])
except:
    print('Some went wrong... Sorry')
    print('Please try again')
else:
    print('Operation successfully completed')
finally:
    print('I am here always ... :)')

