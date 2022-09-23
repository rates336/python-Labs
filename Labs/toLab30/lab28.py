a = b = c = 10
print('a:', a, ',b:', b, ',c:', c)
print('ID a:', id(a), ',ID b:', id(b), ',ID c:', id(c))
print(a is b is c)

a = 20
print('a:', a, ',b:', b, ',c:', c)
print('ID a:', id(a), ',ID b:', id(b), ',ID c:', id(c))
print(a is b is c)
list_abc = [1, 2, 3]
a = b = c = list_abc
a.append(4)
print('a:', a, ',b:', b, ',c:', c)
print('ID a:', id(a), ',ID b:', id(b), ',ID c:', id(c))
print(a is b is c)

x = 10
y = 10
print(id(x), id(y), x is y, sep='\t')
y += 1 - 1
print(id(x), id(y), x is y, sep='\t')
y = y + 1234567890 - 1234567890
print(id(x), id(y), x is y, sep='\t')
y += 1234567890 - 1234567890
print(id(x), id(y), x is y, sep='\t')

days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
workdays = days.copy()
workdays.remove(days[-2])
workdays.remove(days[-1])
print(days)
print(workdays)


