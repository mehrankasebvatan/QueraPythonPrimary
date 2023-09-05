n, m = map(int, input().split())

stars = 0

for _ in range(n):
    row = input()
    stars += row.count('*')

print(stars)