# to delete a file
import os
if os.path.exists("myfile.txt"):
  os.remove("myfile.txt")
else:
  print("The file does not exist")


# to delete an entire folder and with the help of this function we can only delete empty folders
import os
os.rmdir("N_array")