import os
import requests


path = r'C:\Python\firstPythonProject\Labs\toLab60\url_adresses'
extension = '.pl'
list_url = []


def gen_get_files(dir):
    for file in os.listdir(dir):
        if file.count('.txt') > 0:
            with open(os.path.join(path, file)) as c_file:
                c_line = c_file.readline()
                if '.pl' in c_line:
                    list_url.append(c_line)
                    yield c_line


gen_get_files(path)


#To do yet