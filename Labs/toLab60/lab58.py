import csv

with open(r'C:\Python\firstPythonProject\Labs\toLab60\expale_file.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # for row in csvreader:
    #     print('|'.join(row))

    # itr = iter(csvfile)
    # print(next(csvfile))
    # print(next(itr))
    while True:
        try:
            print(next(csvfile))
        except StopIteration:
            break
