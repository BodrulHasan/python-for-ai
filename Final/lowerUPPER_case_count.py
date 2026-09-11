s = input("Enter a string with lower and UPPER case letters:")

lower_case = 0
upper_case = 0

for i in s:

   if  i.islower():
    lower_case+=1

   else: 
     upper_case+=1

print("Number of Lower case letters:",lower_case)
print("Number of Upper case letters:",upper_case)

if lower_case>=upper_case:
   print(i.islower())
else:
  print("Number of Upper case counted more than lower case ")
