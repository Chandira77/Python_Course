# Multiplication table 
# To take input from the user
num = int(input("Enter a number you want to make multipliacation table"))
# Iterate 10 times from i = 1 to 10
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)