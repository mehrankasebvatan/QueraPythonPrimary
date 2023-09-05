n, m = map(int, input().split())

a = []
for _ in range(n):
    row = list(map(int, input().split()))
    a.append(row)

b = []
for _ in range(n):
    row = list(map(int, input().split()))
    b.append(row)

c = []
for i in range(n):
    row = []
    for j in range(m):
        val = a[i][j] + b[i][j]
        row.append(val)
    c.append(row)

for row in c:
    for val in row:
        print(val, end=' ')
    print()
