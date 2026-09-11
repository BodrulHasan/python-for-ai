marks = [444,14,54,21,44,45]

print("Marks:",marks)
# store = []
# for i in marks:
#     if i>40:
#         store.append(i)
#     else:
#         continue
# print(store)

marks.append(99)

marks.insert(0,555)
marks.insert(0,"Bodrul")

print("Lenth of the marks  list:" ,len(marks))

print("After insert Marks:",marks)

del marks[0]
print("After delate 0 index Marks:",marks)

marks.pop()

print("After pop last value Marks:",marks)

marks.append(44)

marks.sort()
print("After sort value of Marks:",marks)

print(marks.count(44)) 

print(marks.index(54))

marks.reverse()

print("After reverse Marks:",marks)



print("After slice:",marks[3:])
print("After slice:",marks[3:4])