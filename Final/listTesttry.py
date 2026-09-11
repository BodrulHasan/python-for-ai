numbers = []

for i in range(10):

    value = int(input("Enter number:"))

    numbers.append(value)

print("Take",numbers)

for i in range(len(numbers)):

    counter = numbers.count(numbers[i]) 
    if counter > 1:
        print("After slice:",numbers[0:i+1])
        break