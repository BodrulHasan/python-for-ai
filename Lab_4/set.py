m=[2,4,6,4,6,6,8]  #list

n= set(m)


print(n)

n.add(10)
print(n)

n.discard(2)
n=list( set(m))  # list to set
print(n)


