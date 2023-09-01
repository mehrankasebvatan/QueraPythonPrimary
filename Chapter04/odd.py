a, b = map(int, input().split())
for s in range(a + 1, b):
    if s % 2 == 1:
        print(s, end=" ")
