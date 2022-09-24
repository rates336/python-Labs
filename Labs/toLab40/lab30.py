import sys


def words_in_file(path):
    path = str(path)
    try:
        list_words = []
        with open(path) as file:
            for line in file:
                line = line.replace('\n', '')
                list_words.extend(line.split(' '))

            while True:
                try:
                    list_words.remove('')
                except ValueError:
                    print('All words from file added to list')
                    break

        print(list_words)
        return len(list_words)
    except FileNotFoundError as e:
        print('You sent wrong path')
        print('You sent path:', path)
        # print(sys.exc_info()[:2])
        return


number_of_words = words_in_file(r'C:\Python\experiments\pxe\2022-9-24\file29.txt')
print(number_of_words)


