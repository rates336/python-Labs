import requests
import os
import shutil


def save_url_to_file(url, file_path):

    r = requests.get(url, stream=True)
    with open(file_path, "wb") as f:
        f.write(r.content)


url = 'http://www.mobilo24.eu/spis/'
thr_dir = r'C:\Python\experiments\exp\lab54'
tmp_file = 'download.tmp'
file = 'spis.html'

tmp_file_path = os.path.join(thr_dir, tmp_file)
file_path = os.path.join(thr_dir, file)

try:
    if os.path.isfile(tmp_file_path):
        os.remove(tmp_file_path)

    save_url_to_file(url, tmp_file_path)
    file_path = tmp_file_path
except Exception as e:
    print('Something went bad, try again or fix it:')
    e.with_traceback()
else:
    print('All is good, operation completed')
finally:
    if os.path.isfile(tmp_file_path):
        os.remove(tmp_file_path)
    print('Temp file deleted')

