import datetime
import os
import time

# dirPath = r'C:\Python\firstPythonProject\Labs\toLab10'
'''
dirPath = input('Please enter path to dir')
if not os.path.isdir(dirPath):
    print('It\'s not a path to dir')
    print(dirPath)
else:
    fileName = input('Please enter file name with extends')
    if fileName.count('.') == 0:
        fileExtends = input('Please enter the extends of file')
        if fileExtends.count('.') == 0:
            fileExtends = '.' + fileExtends
        fileName = fileName + fileExtends
    fullPath = os.path.join(dirPath, fileName)
    if not os.path.exists(fullPath):
        print('Wrong path')
        print(fullPath)
    else:
        print('Successfully verification path')
        print('Now you will give info about this file')
        print('Last modification:', time.localtime(os.path.getmtime(fullPath)))
        print('Size file of bajt:', os.path.getsize(fullPath), 'converted to KB is:',
              os.path.getsize(fullPath) / 1024)
        print('Home dir is:', os.getcwd())
        print('Relative path to file is:', os.path.relpath(fullPath))
'''

dirStart = r'C:\Python\experiments\exp'
dirEnd = r'C:\Python\experiments\pxe'

if os.path.isdir(dirStart) and os.path.isdir(dirEnd):
    todayToken = '{0}-{1}-{2}'.format(str(datetime.datetime.today().year), str(datetime.datetime.today().month),
                                      str(datetime.datetime.today().day))

    pathOutput = os.path.join(dirEnd, todayToken)

    if not os.path.exists(pathOutput):
        print('Crate new dir')
        print(pathOutput)
    elif os.path.isdir(pathOutput):
        print('Exist yet dir which has the same name')
        print('To the dir will be moved files')
        input('To confirm press enter')
    else:
        print('File which has this name exist Error!')

else:
    print('One or more path to dir is wrong')
    print('dirStart:\t', os.path.isdir(dirStart), '\t\tpath to dir:\t', dirStart)
    print('dirEnd:\t\t', os.path.isdir(dirEnd), '\t\tpath to dir:\t', dirEnd)





