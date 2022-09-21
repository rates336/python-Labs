import datetime
import os.path
import random

filePath = r'C:\Python\experiments\pxe\2022-9-21\orders.txt'

with open(filePath) as file:
    counter = 0
    line = file.readline()
    listOrders = []
    while line:
        listOrders.append(line.replace('\n', '').split(','))
        line = file.readline()

    counter = 0
    for oder in listOrders:
        if len(oder) == 3:
            print(
                'Oder from drugstore: {:20s} item: {:20s} amount: {:5s}'.format(oder[0] + ',', oder[0] + ',', oder[0]))
        else:
            print('The text line is malformed:', oder, sep='\t')

    print('\nAnalysing file finish successfully')

fileName = 'websites.txt'
# with open(os.path.join(os.path.split(filePath)[0], fileName), 'r+') as file:
#     line = file.readline()
#     print(line)
#     file.write('test.pl')

webAddresses = []
with open(os.path.join(os.path.split(filePath)[0], fileName)) as file:
    line = file.readline()
    while line:
        webAddresses.append(line.replace('\n', ''))
        line = file.readline()
    dirPath = os.path.split(file.name)[0]
    fileName = os.path.split(file.name)[1]
fileAbsPath = os.path.join(dirPath, fileName)
fileAbsPath2 = os.path.join(fileName, dirPath)
print(webAddresses)
print(dirPath)
print(fileName)
print(fileAbsPath)
print(fileAbsPath2)
# with open(os.path.join(dirPath, fileName.split('.')[0] + str(datetime.datetime.now().minute) +
#                                 str(datetime.datetime.now().second) + '.' + fileName.split('.')[1])) as file:
tmpX = fileName.split('.')[0] + str(datetime.datetime.now().minute) + \
          str(datetime.datetime.now().second) + '.' + fileName.split('.')[1]
tmpPath = os.path.join(dirPath, tmpX)
fullPath = os.path.join(dirPath, fileName.split('.')[0] + str(datetime.datetime.now().minute) + \
          str(datetime.datetime.now().second) + '.' + fileName.split('.')[1])
with open(fullPath, 'x') as file:
    counter = 0
    while counter < webAddresses.__len__():
        file.writelines(webAddresses[counter] + '\n')
        counter += 1

theFileName = 'websites5650.txt'
thePath = os.path.join(dirPath, theFileName)
if os.path.isfile(fullPath):
    print(os.path.split(fullPath)[1])

    with open(fullPath) as file:
        tabWebs = []
        line = file.readline()
        while line:
            tabWebs.append(line.replace('\n', ''))
            line = file.readline()
        random.shuffle(tabWebs)

    tabPLWebs = []
    with open(os.path.join(os.path.split(fullPath)[0], os.path.split(fullPath)[1].split('.')[0] + 'a.txt'), 'x') as file2:
        counter = 0
        while counter < tabWebs.__len__():
            tmp = tabWebs[counter]
            if tmp.count('.pl') > 0:
                tabPLWebs.append(tmp.replace('.pl', '.gov.PL'))
                file2.write(tabPLWebs[-1].swapcase() + ';\t')
            counter += 1
    with open(os.path.join(os.path.split(fullPath)[0], os.path.split(fullPath)[1].split('.')[0] + 'PL.txt'), 'x') as filePL:
        counter = 0
        while counter < len(tabPLWebs):
            filePL.write(str(counter + 1) + '. \t' + tabPLWebs[counter] + '\n')
            counter += 1
else:
    print('Wrong filName or wrong dir location')
