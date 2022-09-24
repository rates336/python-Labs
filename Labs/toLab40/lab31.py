import datetime
import sys
import urllib.request
import os


price = 123
bonus = 23

bonus_granted = False
'''
if bonus_granted:
    price -= bonus
 
print(price)
'''
price -= bonus if bonus_granted else False
print(price)


rating = 5
''' 
if rating == 5:
    print('very good')
elif rating == 4:
    print('good')
else:
    print('weak')
'''

print('Very good') if rating == 5 else print('Good') if rating == 4 else print('Weak')

today_weekday = datetime.datetime.today().weekday()
print('I help to my mam') if today_weekday == 1 else \
    print('I washing closes') if today_weekday == 2 or today_weekday == 3 else \
    print('I have a duty') if today_weekday == 4 else \
    print('I have 2 meetups') if today_weekday == 5 else \
    print('You have a lessens') if today_weekday == 6 else \
    print('Sunday is for us')


list_pages = {'mobilo': 'http://www.mobilo24.eu/', 'udemy': 'https://www.udemy.com/',
              'google': 'https://www.Google.com/', 'abecadlo': 'www.abecadlozpiecaspadlo.abcd/qvx'}
pathToDir = r'C:\Python\experiments\pxe\2022-9-24'

with open(pathToDir + '\\' + list(list_pages.keys())[0] + '.txt', 'a+') as file:
    file.write(list(list_pages.keys())[0] + '.txt')
file.close()
for key in list_pages.keys():
    fullPath = os.path.join(pathToDir, key + '.html')
    url = list_pages.get(key)
    try:
        urllib.request.urlretrieve(url, fullPath)
    except ValueError as e:
        print('Wrong source sent:', key)
        print(sys.exc_info()[:2])

    with open(fullPath, 'a') as file:
        file.write('\n')
else:
    print('Operation finished')
