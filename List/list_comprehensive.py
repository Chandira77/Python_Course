fruits = ["apple", "banana", "graphes"]
"""
newlist = []
for x in fruits:
   if "a" in x:
        newlist.append(x)
print(newlist)

"""
# mathi comment gareko sabai code lai one line maa yesari lekhinxa
#newlist = [x for x in fruits if "a" in x]
#print(newlist)

#newlist = [ x for x in fruits if x != "apple"] # it is a condition that filter the item, it only accept true items.
#newlist = [x.upper() for x in fruits]
#newlist = ['fruit' for x in fruits]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)


