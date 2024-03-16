set1 = {"apple", "ball", "cat"}
#set1.remove("apple")   # If the item to remove does not exist, remove() will raise an error.

#set1.discard("apple")   # If the item to remove does not exist, discard() will NOT raise an error.

#x = set1.pop() #Remove a random item by using the pop() method:
#print(x)

#set1.clear()  #The clear() method empties the set:

del set1()  #The del keyword will delete the set completely: output = SyntaxError: cannot delete function call
print(set1)
