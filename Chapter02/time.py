a = int(input())
b = int(a / 3600)
c = a - (int(b * 3600))
d = int(c / 60)
e = c % 60
print(b, ":", d, ":", e)
