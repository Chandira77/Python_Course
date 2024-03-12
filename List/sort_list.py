"""
list1 = ["apple", "ball", "cat", "dog"]
list2 = [ 1,3,65,74,43]
#list1.sort()
list1.sort(reverse=True)
list1.sort(key = str.lower)
print(list1)
print(list2)

"""
 # sort the list based on how close to 20
def myfunc(n):
  return abs(n - 60)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)