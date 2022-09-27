import os.path
import sys
import math
import time

dir_path = r'C:\Python\experiments\pxe\2022-9-27'
file_name1 = 'script01.txt'
file_name2 = 'script02.txt'

value01 = 0
value02 = 0
'''
with open(os.path.join(dir_path, file_name1), 'r') as file:
    exec(file.read())
    try:
        print(results_list[-1])
    except NameError as e:
        print(sys.exc_info()[:2])
with open(os.path.join(dir_path, file_name2), 'r') as file:
    exec(file.read())
'''

formulas_list = ["abs(x**3 - x**0.5)", "abs(math.sin(x) * x**2)"]
z = 0
argument_list = []
for i in range(200_000):
    argument_list.append(i/10)

results_dict = {}
for x in formulas_list:
    results_dict.setdefault(x, [])

for formula in formulas_list:
    currentList = []
    print('Starting work with formule:', formula)
    start = time.time()
    for x in argument_list:
        currentList.append((x, eval(formula)))
    else:
        results_dict[formula] = currentList
    end = time.time()
    z = end - start
    print(z)
    print('time in second:', time.localtime(end - start).tm_sec)

'''
---------------------------------------------------------------------------------------------------------------


---------------------------------------------------------------------------------------------------------------
'''
y = 0
results_dict2 = {}
for formula in formulas_list:
    results_dict2.setdefault(formula, [])

for formula in formulas_list:
    currentList = []
    print('Starting work with formule:', formula)
    start = time.time()
    source = compile(formula, 'in this file', 'eval')
    for x in argument_list:
        currentList.append((x, source))
    else:
        results_dict2[formula] = currentList
    end = time.time()
    y = end - start
    print(y)
    print('time in second:', time.localtime(end - start).tm_sec)

print(z / y)
