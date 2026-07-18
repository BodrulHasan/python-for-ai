
s=input("Enter a string: ")
lower_count=0
upper_count=0

# for i in range(0,len(s),1):

for i in s:
     if  i.islower():
        lower_count+=1

     else:
       
        upper_count+=1
    
print("NUmber of upeer case:",upper_count)
print("NUmber of Lower case:",lower_count)

if lower_count>=upper_count:
   print(s.lower())