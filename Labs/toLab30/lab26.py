import sys

file_path = r'C:\Python\experiments\pxe\2022-9-21\orders2.txt'

with open(file_path) as file:
    counter = 1
    for line in file:
        line = line.replace('\n', '')
        order = line.split(',')
        pharmacy_name = item = amount = -1
        try:
            pharmacy_name = order[0]
            item = order[1]
            amount = int(order[2])
        except ValueError as e:
            print('\n\t\t\t\t\t>> Error Info <<')
            print('Value is not a digit')
            print(str(counter) + '.\t' + line)
            print(sys.exc_info()[:2])
            print('\t\t\t\t\t>> Error Info <<\n')
        except IndexError as e:
            print('\n\t\t\t\t\t>> Error Info <<')
            print('This element is not exist')
            print(str(counter) + '.\t' + line)
            print(sys.exc_info()[:2])
            print('\t\t\t\t\t>> Error Info <<\n')
        except e:
            print('\n------>>>   Error Info   <<<------')
            if pharmacy_name == -1:
                print('pharmacy_name has invalid value')
            if item == -1:
                print('item has invalid value')
            if amount == -1:
                print('amount has invalid value')
            print(sys.exc_info()[:2])
            print(str(counter) + '.\t' + line)
            print('------>>>   Error Info   <<<------\n')
        print('Order from drugstore %s, item: %s, amount: %d' % (pharmacy_name, item, amount))
        counter += 1
print("Processing finished")

