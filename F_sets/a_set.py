set1 = {"apple", "ball", "cat"}
set1 = {1,2,3}
set3 = {True, False}
set4 = {"apple", 1, 2, True, False} # The values True and 1 are considered the same value in sets, and are treated as duplicates. and same as False and 0
#print(set1)
print(set4)
print(len(set4))
print(type(set4))

#constructor using the word set
set5 = set(("hi", "hello", "hey"))
print(set5)