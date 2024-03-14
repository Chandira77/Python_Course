"""
greeting = ("hello", "hi", "hey","namastey")
#print(greeting)

(apple, banana, graphes, mango) = greeting
print(apple)
print(banana)
print(graphes)
print(mango)
"""

#The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.

greeting = ("hello", "hi", "hey","namastey")
#print(greeting)

(apple, banana, *graphes) = greeting
print(apple)
print(banana)
print(graphes)
