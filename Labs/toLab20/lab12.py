numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]

lengthNumbers = numbers.__len__() - 1
temp = 0
operationTab = []
operationTab2 = []
operationVariable = 0
operationVariable2 = 0
while temp < lengthNumbers:
    if numbers[temp] ** 2 == numbers[temp + 1]:
        print('Found new match pair of numbers /2')
        operationTab.append(str(numbers[temp]) + ', ' + str(numbers[temp + 1]))
        operationVariable += 1
    temp += 1
temp = 0
while temp < lengthNumbers - 1:
    if numbers[temp] ** 2 == numbers[temp + 1] and numbers[temp + 1] ** 2 == numbers[temp + 2]:
        print('Found new match of numbers /3')
        operationTab2.append(str(numbers[temp]) + ', ' + str(numbers[temp + 1]) + ', ' + str(numbers[temp + 2]))
        operationVariable2 += 1
    temp += 1

# Alternative
# while temp < lengthNumbers:
#     if numbers[temp] ** 2 == numbers[temp + 1]:
#         if numbers[temp + 1] ** 2 == numbers[temp +2]:
#             print('Found new match pair of numbers /2')
#             operationTab.append(str(numbers[temp]) + ', ' + str(temp + 1))
#             operationVariable += 1
#             print('Found new match of numbers /3')
#             operationTab2.append(str(numbers[temp]) + ', ' + str(numbers[temp + 1]) + ', ' + \
#                                                 str(numbers[temp + 2]))
#             operationVariable2 += 1
#         else:
#             print('Found new match pair of numbers /2')
#             operationTab.append(str(numbers[temp]) + ', ' + str(temp + 1))
#             operationVariable += 1
#     temp += 1
# else:
#     print('Finish analyzing this list')
#     operationVariable = 0
#     operationVariable2 = 0

lengthOperationTab = operationTab.__len__()
lengthOperationTab2 = operationTab2.__len__()
temp = 0
while temp < lengthOperationTab2:
    print('OT1-' + str(temp) + ' :', operationTab[temp], '\t\tOT2-' + str(temp) + ':', operationTab2[temp])
    temp += 1
else:
    while temp < lengthOperationTab:
        print('OT1-' + str(temp) + ':', operationTab[temp])
        temp += 1
    else:
        print('Done')

texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
temp = 0
lengthTexts = texts.__len__() - 2
operationList = []
opTemp = 0
while temp < lengthTexts:
    if texts[temp].__len__() == texts[temp + 1].__len__():
        print('Founded new matching pair')
        operationList.append(texts[temp] + ' : ' + texts[temp + 1])
    temp += 1
else:
    print('Done')
temp = 0
while temp < operationList.__len__():
    print(operationList[opTemp])
    opTemp += 1
    temp += 1
