a = input()
b = 0
if a.__contains__("s"):
    b += 10
if a.__contains__("7"):
    b += 5
if a.__contains__("*"):
    b += 30
print(b)
