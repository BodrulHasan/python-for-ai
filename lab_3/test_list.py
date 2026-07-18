numbers = []

for i in range(10):
    value = int(input("Enter a value: "))
    numbers.append(value)
print("Taken list:",numbers)

for i in range(len(numbers)):
    counter = numbers.count(numbers[i])
    if counter > 1:
        
        print("After Slice:",numbers[0:i+1])
        break
 

