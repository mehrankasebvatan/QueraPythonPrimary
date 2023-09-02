a = int(input())
b = 0
for s in range(1, a):
    if a % s == 0:
        b += s

if b == a:
    print("YES")
else:
    print("NO")