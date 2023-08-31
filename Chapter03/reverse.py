a = input()
b = input()

al = len(a)
bl = len(b)

ra = a[al::-1]
rb = b[bl::-1]

if ra == rb:
    print(a, "=", b)
elif ra < rb:
    print(a, "<", b)
else:
    print(b, "<", a)
