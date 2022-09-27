# Task !29
"""
Na przekręcie z wpłatomatem z poprzedniego zadania postanawiasz wraz ze swoim szefem
otworzyć linie lotnicze "Flying Python". Linie będą krajowe. Oto wykaz portów lotniczych:

1. Zbuduj listę tupletów symbolizujących port początkowy i końcowy. Wykonaj połączenie każdy-z-każdym
2. Wyeliminuj z powyższej listy połączenie z portu do tego samego portu
3. Ponieważ połączenie z A do B dubluje się z połączeniem z B do A -
wygeneruj możliwe połączenia krajowe pomijając takie zdublowane trasy.
4. Policz ilość generowanych połączeń w krokach 1,2,3
"""
'''
[('WAW', 'WAW'), ('WAW', 'KRK'), ('WAW', 'GDN'), ('WAW', 'KTW'), ('WAW', 'WMI'), ('WAW', 'WRO'), ('WAW', 'POZ'), ('WAW', 'RZE'), ('WAW', 'SZZ'), ('WAW', 'LUZ'), ('WAW', 'BZG'), ('WAW', 'LCJ'), ('WAW', 'SZY'), ('WAW', 'IEG'), ('WAW', 'RDO'), ('KRK', 'WAW'), ('KRK', 'KRK'), ('KRK', 'GDN'), ('KRK', 'KTW'), ('KRK', 'WMI'), ('KRK', 'WRO'), ('KRK', 'POZ'), ('KRK', 'RZE'), ('KRK', 'SZZ'), ('KRK', 'LUZ'), ('KRK', 'BZG'), ('KRK', 'LCJ'), ('KRK', 'SZY'), ('KRK', 'IEG'), ('KRK', 'RDO'), ('GDN', 'WAW'), ('GDN', 'KRK'), ('GDN', 'GDN'), ('GDN', 'KTW'), ('GDN', 'WMI'), ('GDN', 'WRO'), ('GDN', 'POZ'), ('GDN', 'RZE'), ('GDN', 'SZZ'), ('GDN', 'LUZ'), ('GDN', 'BZG'), ('GDN', 'LCJ'), ('GDN', 'SZY'), ('GDN', 'IEG'), ('GDN', 'RDO'), ('KTW', 'WAW'), ('KTW', 'KRK'), ('KTW', 'GDN'), ('KTW', 'KTW'), ('KTW', 'WMI'), ('KTW', 'WRO'), ('KTW', 'POZ'), ('KTW', 'RZE'), ('KTW', 'SZZ'), ('KTW', 'LUZ'), ('KTW', 'BZG'), ('KTW', 'LCJ'), ('KTW', 'SZY'), ('KTW', 'IEG'), ('KTW', 'RDO'), ('WMI', 'WAW'), ('WMI', 'KRK'), ('WMI', 'GDN'), ('WMI', 'KTW'), ('WMI', 'WMI'), ('WMI', 'WRO'), ('WMI', 'POZ'), ('WMI', 'RZE'), ('WMI', 'SZZ'), ('WMI', 'LUZ'), ('WMI', 'BZG'), ('WMI', 'LCJ'), ('WMI', 'SZY'), ('WMI', 'IEG'), ('WMI', 'RDO'), ('WRO', 'WAW'), ('WRO', 'KRK'), ('WRO', 'GDN'), ('WRO', 'KTW'), ('WRO', 'WMI'), ('WRO', 'WRO'), ('WRO', 'POZ'), ('WRO', 'RZE'), ('WRO', 'SZZ'), ('WRO', 'LUZ'), ('WRO', 'BZG'), ('WRO', 'LCJ'), ('WRO', 'SZY'), ('WRO', 'IEG'), ('WRO', 'RDO'), ('POZ', 'WAW'), ('POZ', 'KRK'), ('POZ', 'GDN'), ('POZ', 'KTW'), ('POZ', 'WMI'), ('POZ', 'WRO'), ('POZ', 'POZ'), ('POZ', 'RZE'), ('POZ', 'SZZ'), ('POZ', 'LUZ'), ('POZ', 'BZG'), ('POZ', 'LCJ'), ('POZ', 'SZY'), ('POZ', 'IEG'), ('POZ', 'RDO'), ('RZE', 'WAW'), ('RZE', 'KRK'), ('RZE', 'GDN'), ('RZE', 'KTW'), ('RZE', 'WMI'), ('RZE', 'WRO'), ('RZE', 'POZ'), ('RZE', 'RZE'), ('RZE', 'SZZ'), ('RZE', 'LUZ'), ('RZE', 'BZG'), ('RZE', 'LCJ'), ('RZE', 'SZY'), ('RZE', 'IEG'), ('RZE', 'RDO'), ('SZZ', 'WAW'), ('SZZ', 'KRK'), ('SZZ', 'GDN'), ('SZZ', 'KTW'), ('SZZ', 'WMI'), ('SZZ', 'WRO'), ('SZZ', 'POZ'), ('SZZ', 'RZE'), ('SZZ', 'SZZ'), ('SZZ', 'LUZ'), ('SZZ', 'BZG'), ('SZZ', 'LCJ'), ('SZZ', 'SZY'), ('SZZ', 'IEG'), ('SZZ', 'RDO'), ('LUZ', 'WAW'), ('LUZ', 'KRK'), ('LUZ', 'GDN'), ('LUZ', 'KTW'), ('LUZ', 'WMI'), ('LUZ', 'WRO'), ('LUZ', 'POZ'), ('LUZ', 'RZE'), ('LUZ', 'SZZ'), ('LUZ', 'LUZ'), ('LUZ', 'BZG'), ('LUZ', 'LCJ'), ('LUZ', 'SZY'), ('LUZ', 'IEG'), ('LUZ', 'RDO'), ('BZG', 'WAW'), ('BZG', 'KRK'), ('BZG', 'GDN'), ('BZG', 'KTW'), ('BZG', 'WMI'), ('BZG', 'WRO'), ('BZG', 'POZ'), ('BZG', 'RZE'), ('BZG', 'SZZ'), ('BZG', 'LUZ'), ('BZG', 'BZG'), ('BZG', 'LCJ'), ('BZG', 'SZY'), ('BZG', 'IEG'), ('BZG', 'RDO'), ('LCJ', 'WAW'), ('LCJ', 'KRK'), ('LCJ', 'GDN'), ('LCJ', 'KTW'), ('LCJ', 'WMI'), ('LCJ', 'WRO'), ('LCJ', 'POZ'), ('LCJ', 'RZE'), ('LCJ', 'SZZ'), ('LCJ', 'LUZ'), ('LCJ', 'BZG'), ('LCJ', 'LCJ'), ('LCJ', 'SZY'), ('LCJ', 'IEG'), ('LCJ', 'RDO'), ('SZY', 'WAW'), ('SZY', 'KRK'), ('SZY', 'GDN'), ('SZY', 'KTW'), ('SZY', 'WMI'), ('SZY', 'WRO'), ('SZY', 'POZ'), ('SZY', 'RZE'), ('SZY', 'SZZ'), ('SZY', 'LUZ'), ('SZY', 'BZG'), ('SZY', 'LCJ'), ('SZY', 'SZY'), ('SZY', 'IEG'), ('SZY', 'RDO'), ('IEG', 'WAW'), ('IEG', 'KRK'), ('IEG', 'GDN'), ('IEG', 'KTW'), ('IEG', 'WMI'), ('IEG', 'WRO'), ('IEG', 'POZ'), ('IEG', 'RZE'), ('IEG', 'SZZ'), ('IEG', 'LUZ'), ('IEG', 'BZG'), ('IEG', 'LCJ'), ('IEG', 'SZY'), ('IEG', 'IEG'), ('IEG', 'RDO'), ('RDO', 'WAW'), ('RDO', 'KRK'), ('RDO', 'GDN'), ('RDO', 'KTW'), ('RDO', 'WMI'), ('RDO', 'WRO'), ('RDO', 'POZ'), ('RDO', 'RZE'), ('RDO', 'SZZ'), ('RDO', 'LUZ'), ('RDO', 'BZG'), ('RDO', 'LCJ'), ('RDO', 'SZY'), ('RDO', 'IEG'), ('RDO', 'RDO')]


'''
ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

air_connections = [(port, port2) for port in ports for port2 in ports if port != port2]
print(len(air_connections))
print(air_connections)

i = 0
length_list = len(air_connections)
list_air = air_connections.copy()
while i < length_list:
    if (i // 7) % 4 in [1, 3]:
        air_connections.remove(list_air[i])
    i += 1
print(air_connections)
print(len(air_connections))
routes = [(start, stop) for start in ports for stop in ports if start < stop]
print(routes)
print(len(routes))

# Task !30
"""
W tym zadaniu należy przerobić listy z poprzedniego LAB do postaci generatora. Nieco problematyczne 
będzie ustalenie ile wartości jest generowanych przez generator, bo w tym celu... trzeba go przejść!

Jeżeli taki opis Ci wystarcza to GO! GO! GO!

A tu dokładniejsza instrukcja:
Na przekręcie z wpłatomatem z poprzedniego zadania postanawiasz wraz ze swoim szefem otworzyć 
linie lotnicze"Flying Python". Linie będą krajowe. Oto wykaz portów lotniczych:
ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']
         
1. Zbuduj generator tupletów symbolizujących port początkowy i końcowy. Wykonaj połączenie każdy-z-każdym
2. Wyeliminuj z powyższego generatora połączenie z portu do tego samego portu
3. Ponieważ połączenie z A do B dubluje się z połączeniem z B do A - 
wygeneruj możliwe połączenia krajowe pomijając takie zdublowane trasy.
4. Policz ilość generowanych połączeń w krokach 1,2,3. W tym celu napisz pętlę for, 
która: wyświetli wygenerowane wartości i policzy je
"""
ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

gen_routes = ((x, y) for x in ports for y in ports if x > y)
print(next(gen_routes))
print(next(gen_routes))
counter = 2
for route in gen_routes:
    print(route)
    counter += 1
else:
    print(counter)
