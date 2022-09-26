def separate(text: str, separator: str, counter: int):
    x = 0
    a = 0
    text = str(text)
    length_sep = len(separator)
    while text.count(separator) > x:
        if text.find(separator, a) != -1:
            x += 1
            a = text.find(separator, a) + length_sep
            if x % counter == 0 and x > 0:
                text = text[:a] + '\n' + text[a:]
    else:
        if text[-1] == '\n':
            text = text[:-1]

    return text


def separate2(text: str, separator: str, counter: int):
    x = 0
    a = 0
    a2 = 0
    text = str(text)
    tab = []

    y = 0
    length_sep = len(separator)
    while text.count(separator) > x:
        if text.find(separator, a) != -1:
            x += 1
            if x % counter == 0 and x > 0:
                a2 = a
                a = text.find(separator, a) + length_sep
                tab.append(text[a2:a])

            else:
                a = text.find(separator, a) + length_sep
    else:
        if text[-1] == '\n':
            text = text[:-1]

    return tab


def separate3(text: str, separator: str, counter: int):
    x = 0
    a = 0
    a2 = 0
    text = str(text)
    tab = []
    tab2 = []
    tab3 = tuple([tab, tab2])
    y = 0
    length_sep = len(separator)
    while text.count(separator) > x:
        if text.find(separator, a) != -1:
            x += 1
            if x % counter == 0 and x > 0:
                a2 = a
                a = text.find(separator, a) + length_sep
                if y % 2 == 0:
                    tab.append(text[a2:a - 1])
                else:
                    tab2.append(text[a2:a - 1])
                y += 1
            else:
                a = text.find(separator, a) + length_sep
    else:
        if text[-1] == '\n':
            text = text[:-1]

    return tab3

text = [('WAW', 'WAW'), ('WAW', 'KRK'), ('WAW', 'GDN'), ('WAW', 'KTW'), ('WAW', 'WMI'), ('WAW', 'WRO'), ('WAW', 'POZ'), ('WAW', 'RZE'), ('WAW', 'SZZ'), ('WAW', 'LUZ'), ('WAW', 'BZG'), ('WAW', 'LCJ'), ('WAW', 'SZY'), ('WAW', 'IEG'), ('WAW', 'RDO'), ('KRK', 'WAW'), ('KRK', 'KRK'), ('KRK', 'GDN'), ('KRK', 'KTW'), ('KRK', 'WMI'), ('KRK', 'WRO'), ('KRK', 'POZ'), ('KRK', 'RZE'), ('KRK', 'SZZ'), ('KRK', 'LUZ'), ('KRK', 'BZG'), ('KRK', 'LCJ'), ('KRK', 'SZY'), ('KRK', 'IEG'), ('KRK', 'RDO'), ('GDN', 'WAW'), ('GDN', 'KRK'), ('GDN', 'GDN'), ('GDN', 'KTW'), ('GDN', 'WMI'), ('GDN', 'WRO'), ('GDN', 'POZ'), ('GDN', 'RZE'), ('GDN', 'SZZ'), ('GDN', 'LUZ'), ('GDN', 'BZG'), ('GDN', 'LCJ'), ('GDN', 'SZY'), ('GDN', 'IEG'), ('GDN', 'RDO'), ('KTW', 'WAW'), ('KTW', 'KRK'), ('KTW', 'GDN'), ('KTW', 'KTW'), ('KTW', 'WMI'), ('KTW', 'WRO'), ('KTW', 'POZ'), ('KTW', 'RZE'), ('KTW', 'SZZ'), ('KTW', 'LUZ'), ('KTW', 'BZG'), ('KTW', 'LCJ'), ('KTW', 'SZY'), ('KTW', 'IEG'), ('KTW', 'RDO'), ('WMI', 'WAW'), ('WMI', 'KRK'), ('WMI', 'GDN'), ('WMI', 'KTW'), ('WMI', 'WMI'), ('WMI', 'WRO'), ('WMI', 'POZ'), ('WMI', 'RZE'), ('WMI', 'SZZ'), ('WMI', 'LUZ'), ('WMI', 'BZG'), ('WMI', 'LCJ'), ('WMI', 'SZY'), ('WMI', 'IEG'), ('WMI', 'RDO'), ('WRO', 'WAW'), ('WRO', 'KRK'), ('WRO', 'GDN'), ('WRO', 'KTW'), ('WRO', 'WMI'), ('WRO', 'WRO'), ('WRO', 'POZ'), ('WRO', 'RZE'), ('WRO', 'SZZ'), ('WRO', 'LUZ'), ('WRO', 'BZG'), ('WRO', 'LCJ'), ('WRO', 'SZY'), ('WRO', 'IEG'), ('WRO', 'RDO'), ('POZ', 'WAW'), ('POZ', 'KRK'), ('POZ', 'GDN'), ('POZ', 'KTW'), ('POZ', 'WMI'), ('POZ', 'WRO'), ('POZ', 'POZ'), ('POZ', 'RZE'), ('POZ', 'SZZ'), ('POZ', 'LUZ'), ('POZ', 'BZG'), ('POZ', 'LCJ'), ('POZ', 'SZY'), ('POZ', 'IEG'), ('POZ', 'RDO'), ('RZE', 'WAW'), ('RZE', 'KRK'), ('RZE', 'GDN'), ('RZE', 'KTW'), ('RZE', 'WMI'), ('RZE', 'WRO'), ('RZE', 'POZ'), ('RZE', 'RZE'), ('RZE', 'SZZ'), ('RZE', 'LUZ'), ('RZE', 'BZG'), ('RZE', 'LCJ'), ('RZE', 'SZY'), ('RZE', 'IEG'), ('RZE', 'RDO'), ('SZZ', 'WAW'), ('SZZ', 'KRK'), ('SZZ', 'GDN'), ('SZZ', 'KTW'), ('SZZ', 'WMI'), ('SZZ', 'WRO'), ('SZZ', 'POZ'), ('SZZ', 'RZE'), ('SZZ', 'SZZ'), ('SZZ', 'LUZ'), ('SZZ', 'BZG'), ('SZZ', 'LCJ'), ('SZZ', 'SZY'), ('SZZ', 'IEG'), ('SZZ', 'RDO'), ('LUZ', 'WAW'), ('LUZ', 'KRK'), ('LUZ', 'GDN'), ('LUZ', 'KTW'), ('LUZ', 'WMI'), ('LUZ', 'WRO'), ('LUZ', 'POZ'), ('LUZ', 'RZE'), ('LUZ', 'SZZ'), ('LUZ', 'LUZ'), ('LUZ', 'BZG'), ('LUZ', 'LCJ'), ('LUZ', 'SZY'), ('LUZ', 'IEG'), ('LUZ', 'RDO'), ('BZG', 'WAW'), ('BZG', 'KRK'), ('BZG', 'GDN'), ('BZG', 'KTW'), ('BZG', 'WMI'), ('BZG', 'WRO'), ('BZG', 'POZ'), ('BZG', 'RZE'), ('BZG', 'SZZ'), ('BZG', 'LUZ'), ('BZG', 'BZG'), ('BZG', 'LCJ'), ('BZG', 'SZY'), ('BZG', 'IEG'), ('BZG', 'RDO'), ('LCJ', 'WAW'), ('LCJ', 'KRK'), ('LCJ', 'GDN'), ('LCJ', 'KTW'), ('LCJ', 'WMI'), ('LCJ', 'WRO'), ('LCJ', 'POZ'), ('LCJ', 'RZE'), ('LCJ', 'SZZ'), ('LCJ', 'LUZ'), ('LCJ', 'BZG'), ('LCJ', 'LCJ'), ('LCJ', 'SZY'), ('LCJ', 'IEG'), ('LCJ', 'RDO'), ('SZY', 'WAW'), ('SZY', 'KRK'), ('SZY', 'GDN'), ('SZY', 'KTW'), ('SZY', 'WMI'), ('SZY', 'WRO'), ('SZY', 'POZ'), ('SZY', 'RZE'), ('SZY', 'SZZ'), ('SZY', 'LUZ'), ('SZY', 'BZG'), ('SZY', 'LCJ'), ('SZY', 'SZY'), ('SZY', 'IEG'), ('SZY', 'RDO'), ('IEG', 'WAW'), ('IEG', 'KRK'), ('IEG', 'GDN'), ('IEG', 'KTW'), ('IEG', 'WMI'), ('IEG', 'WRO'), ('IEG', 'POZ'), ('IEG', 'RZE'), ('IEG', 'SZZ'), ('IEG', 'LUZ'), ('IEG', 'BZG'), ('IEG', 'LCJ'), ('IEG', 'SZY'), ('IEG', 'IEG'), ('IEG', 'RDO'), ('RDO', 'WAW'), ('RDO', 'KRK'), ('RDO', 'GDN'), ('RDO', 'KTW'), ('RDO', 'WMI'), ('RDO', 'WRO'), ('RDO', 'POZ'), ('RDO', 'RZE'), ('RDO', 'SZZ'), ('RDO', 'LUZ'), ('RDO', 'BZG'), ('RDO', 'LCJ'), ('RDO', 'SZY'), ('RDO', 'IEG'), ('RDO', 'RDO')]
text_list = separate(text, '),', 15).split('\n')
text_list = text_list[::2]
for x in text_list:
    print(x)
c = separate2(separate(text, '),', 15).replace('[', '').replace(']', '').replace('),', ')')
                .replace(' (', '('), ')', 1)
print(c)
d = separate3(c, '\'', 2)
print(d)
