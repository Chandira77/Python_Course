"""set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

#set3 = set1.union(set2)
set1.update(set2)
print(set1)
"""

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

#x.intersection_update(y)
#x.symmetric_difference_update(y)
z = x.symmetric_difference(y)

print(x)