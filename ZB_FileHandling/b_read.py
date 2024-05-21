f = open("test.txt", "r")

#print(f.read())

# you can return 5 charecter of this file
#print(f.read(5))

#you can return two lines by using readline()
# print(f.readline())
# print(f.readline())

#using loop you can return whole para line by line
f = open("test.txt", "r")
for x in f:
  print(x)

f.close()