#text type 
x = "Hello world"  #String data type
print(x)
print(type(x))


# Numeric type
x = 20              # integer value
print(x)            #display value of x
print(type(x))      #display the data type of x


x = 20.5            #float value
print(x)
print(type(x))

x = 1j              #Complex value
print(x)
print(type(x))

# sequence types
x = ["Apple", "banana", "Graphes"]     #list value
print(x)
print(type(x))

x = ("Apple", "Banana", "Graphes")     # Tuple value ( notice the bracket around x values in both list and tuples values)
print(x)
print(type(x))

x = range(8)                           # range value 
print(x)                               # the output of this is range(0,8)
print(type(x))

#mapping types
x = {"name" : "Ira", "age" : 22}      #dict value
print(x)
print(type(x))

# Set types
x = {"Apple", "Banana", "mango"}      # Set values
print(x)
print(type(x))

x = frozenset({"Apple", "Banana", "Mango"})   # frozenset
print(x)
print(type(x))

# Boolean type
x = True                              #bool values
print(x)

#binary types
x = b"hey"                            # bytes values
print(x)

x = bytearray(4)                      #bytearray values
print(x)

x = memoryview(bytes(4))              #memoryview values
print(x)
print(type(x))





 