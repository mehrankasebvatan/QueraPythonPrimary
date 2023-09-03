def sDraw(x):
    for i in range(1, x + 1):
        print("*" * x)


def tDraw(x):
    for i in range(1, x + 1):
        print("*" * (x + 1 - i))


a, b = input().split()
a = int(a)
if b == "s":
    sDraw(a)
elif b == "t":
    tDraw(a)
