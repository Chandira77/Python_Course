x = ("apple", "banana", "cherry", "mango")
y = list(x)
#y[1] = "kiwi"
#x = tuple(y)

#convert tuple into a list (one cannnot change tuple so that to change tuple one shoule convert tuple into list and then add or remove item from list )
"""
x = ("apple", "banana", "cherry", "mango")
y = list(x)
y.append("avocado")
x = tuple(y)
print(x)
"""

# add tuple into a tuple
"""
x = ("aeroplane", "ball", "cat")
y = ("dog",)
x += y
print(x)
"""

# Convert the tuple into a list, remove "apple", and convert it back into a tuple
x = ("apple", "banana", "cherry", "mango")
y = list(x)
y.remove("apple")
x = tuple(y)
print(x)
# del x
# print(x)
