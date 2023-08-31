a = int(input())
b = int(input())

c = int(a / 100)
d = int((a - (c * 100)) / 10)
dd = int(a % 100)
e = dd % 10

f = int(b / 100)
g = int((b - (f * 100)) / 10)
hh = int(b % 100)
h = hh % 10

i = (e * 100) + (d * 10) + c
j = (h * 100) + (g * 10) + f

if i == j:
    print(a, "=", b)
elif i < j:
    print(a, "<", b)
else:
    print(b, "<", a)
