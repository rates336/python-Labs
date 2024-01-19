'''
import os
import zipfile
import requests


class FileFromWeb:

    def __int__(self, url, path):
        url = self.url
        path = self.path

    def __enter__(self):
        response = requests.get(self.url)
        with open(self.path, 'wb') as f:
            f.write(response.content)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


with FileFromWeb('https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip',
                 r'C:\Python\firstPythonProject\Labs\toLab70') as f:
    with zipfile.ZipFile(f.path, 'r') as z:
        a_file = z.namelist()[0]
        print(a_file)
        os.chdir(r'C:\Python\firstPythonProject\Labs\toLab70')
        z.extract(a_file, '.', None)
'''
import os
import zipfile
import requests


class FileFromWeb:

    def __init__(self, url, tmp_file):
        self.url = url
        self.tmp_file = tmp_file

    def __enter__(self):
        # download
        response = requests.get(self.url)
        with open(self.tmp_file, 'wb') as f:
            f.write(response.content)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):

        if (exc_type is FileNotFoundError) or (exc_type is KeyError):
            print('File is not exist in indicated path')
            return True
        else:
            return False


with FileFromWeb('https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip', r'C:\Python\firstPythonProject\Labs\toLab70\SomeFileName.zip') as f:
    with zipfile.ZipFile(f.tmp_file, 'r') as z:
        a_file = z.namelist()[0]
        print(a_file)
        os.chdir(r'C:\Python\firstPythonProject\Labs\toLab70')
        z.extract(a_file, '.', None)

