x = ["ira" , "ina"]
y = ["ira" , "ina"]
z = x
#is identity operator
print(x is z) #x is the same object as z
print(y  is  x) #x is not the same object as y even if the content is same
print(x == z) #notice the  difference between "is" and "=" .

# is not identity operator
print(x is not z) #x is the same object as z
print(y  is not  x) #x is not the same object as y even if the content is same
print(x != z)