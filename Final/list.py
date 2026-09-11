numbers = []

while True:
    n = input("Enter Number:")

    if n=="s":
        break
    numbers.append(int(n))

seen =[]
for i in numbers:

    if i not in seen:
        count = numbers.count(i)

        print(i,"->",count,"times")
        seen.append(i)

    