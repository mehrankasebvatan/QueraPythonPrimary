a, b = map(int, input().split())
c = 1
for s in range(1, min(a, b) + 1):
    if a % s == 0 and b % s == 0:
        c = s
print(c)