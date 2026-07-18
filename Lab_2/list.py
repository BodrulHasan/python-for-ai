numbers = []

while True:
    n = input()

    if n == "STOP":
        break

    numbers.append(int(n))

for i in numbers:
    if numbers.index(i) == numbers.index(i):
        count = numbers.count(i)
        if i not in numbers[:numbers.index(i)]:
            print(i, "-", count, "times")