box = 'cola:9 bottles: 1 litr'
print(box)
box = box.upper()
print(box)
box = box.lower()
print(box)
print(box.split('a', 2))
# Task for future 01
# Find how to use split and how to delete from string a few letters which are not next letter
# Example
# box = "cola:9 bottles: 1 litr"
# expected return "cl:9 bttls: 1 ltr"
# easy version of function is: box.split("aeiouy")
# but this is not working

# Current solution

'''
tempString = box
tempString = tempString.split('a')
tempString = tempString.split('e')
tempString = tempString.split('i')
tempString = tempString.split('o')
tempString = tempString.split('u')
tempString = tempString.split('y')
print(tempString)
'''
# To the operation is created other function
# .strip('chars')

# Correct solution
print(box.strip('aeiouy'))
