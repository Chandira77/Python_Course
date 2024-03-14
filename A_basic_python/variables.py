#variables do not need to be declared with any particular type, and can even change type after they have been set
#name = "Ira"
#age = "22"
#Status = "Student"

#name = "Rekha"

#is_adult= True

#print(name +" " + "is a " + Status )
#print(age)
#print(is_adult)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

# casting is done if we want to specify the data type of a variables
x= int(2)
y = int(3)
z = float(4)
print(x)
print(y)
print(z)

#double quotes and a single quotes are same
x = "ira"
print(x)
x = 'ira'
print(x)

#python is a case sensitive
a = "hello world"
# A will not overwrite a
A = "hi dear"
print(a)
print(A)

#many values to multiple variables
#x, y, z = "Orange", "apple", "Graphes"
#print(x)
#print(y)
#print(z)

#Fruits = ["apple", "banana"]
#x, y = Fruits
#print(x)
#print(y)
#print(x, y)

#Global variable
x = "hello world"
def myfun():
    print(x)
myfun()


