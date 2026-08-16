#Reusable
a = 30; #global variable


def sum (n1,n2,n3):
    # # a = 20
    # # b = 10  #local variable
    # print(n1+n2)
    global a
  
    addition=n1+n2+n3
    return addition
 

# sum(100,200)

addition= sum(100,200,10)
print(addition)