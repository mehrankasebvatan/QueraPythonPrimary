def bmm(a, b, c, d, e):
    x = 1
    for s in range(1, min(a, b, c, d, e) + 1):
        if a % s == 0 and b % s == 0 and c % s == 0 and d % s == 0 and e % s == 0:
            x = s
    return x


f, g, h, i, j = map(int, input().split())
print(bmm(f, g, h, i, j))
