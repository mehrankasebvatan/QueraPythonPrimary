a, b, c = input().split()
a = int(a)
b = int(b)

while a > 0:
    for s in range(1, a + 1):
        for m in range(1, a + 1):
            print(c * a)
        a -= b
