s = input("Enter a string: ")
output = ""
flag = False

for ch in s:
    if flag == True:
        if ch.islower():
            output += ch
        else:
            break
    else:
        if ch.islower():
            continue
        else:
            flag = True

if len(output) > 0:
    print([output])
else:
    print("Blank")