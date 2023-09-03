a = 0
x = ""
b = [0] * 10
while a < 10:
    b[a] = int(input())
    a += 1
for s in range(1, 11):
    if s != 10:
        x += str(b[10 - s]) + "-"
    else:
        x += str(b[0])

print(x)
