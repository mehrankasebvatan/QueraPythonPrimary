x = [0] * 10
jam = 0
t = 0
for i in range(10):
    x[i] = float(input())
    jam += x[i]
miangin = jam / 10
for i in range(10):
    if x[i] > miangin:
        t += 1
print(t)
