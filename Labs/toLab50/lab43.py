import requests
import os
import functools


def save_url_file(url, dir, file, msg):

    print(msg.format(file))

    r = requests.get(url, stream=True)
    file_path = os.path.join(dir, file)

    with open(file_path, "wb") as f:
        f.write(r.content)
        f.close()


msg = "Please wait - the file {} will be downloaded"

url = 'http://mobilo24.eu/spis'
dir = r'C:\Python\experiments\exp\lab42\\'
file = 'spis.html'
save_url_file(url, dir, file, msg)
save_url_default = functools.partial(save_url_file, dir=r'C:\Python\experiments\exp\lab42\\',
                                 msg='Please wait - the file {} will be downloaded')
save_url_default(url, file=file[:file.find('.')] + '2' + file[file.find('.'):])
save_url_default(url, file=file.replace('.', '3.'))
