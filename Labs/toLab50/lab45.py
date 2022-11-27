text_list = ['x', 'xxx', 'xxxxx', 'xxxxxxx', '']

f = lambda x: len(x)
for x in text_list:
    print(len(x))
r = '['
for x in text_list:
    r += str(f(x)) + ', '
else:
    r = r[:-2] + ']'
    print(r)
print(list(map(f, text_list)))
print(list(map(lambda x: len(x), text_list)))
print(list(map(lambda x: len(x), ['x', 'xxx', 'xxxxx', 'xxxxxxx', ''])))

