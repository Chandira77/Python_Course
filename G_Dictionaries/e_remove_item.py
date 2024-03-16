thisdict = {
  "school": "sanothimi",
  "faculty": "BICT",
  "Eyear": 2030
}
# thisdict.pop({"faculty" : "BICT"})  output = TypeError: unhashable type: 'dict'
#thisdict.pop("faculty")
#thisdict.popitem()
del thisdict()   #SyntaxError: cannot delete function call
#thisdict.clear()
print(thisdict)