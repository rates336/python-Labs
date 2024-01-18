import os
import itertools


full_list = []


def quantity_files_dirs(path):
    dir_list = []
    file_list = []

    for x in os.scandir(path):
        tmp = os.path.join(path, x)
        if x.is_dir():
            dir_list.append(x)
        else:
            file_list.append(x)
        full_list.append(x)
    print('Number od dirs in this path: {}\nNumber of files in this path: {}'.format(len(dir_list), len(file_list)))
    print(os.listdir(path))


path = r'C:\Python\firstPythonProject\Labs'
quantity_files_dirs(path)
full_list = sorted(full_list, key=lambda a: a.is_dir())
print(full_list)