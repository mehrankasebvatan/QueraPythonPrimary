def fib(n):
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)


a = int(input())
s = 0
for i in range(1, a + 1):
    s += fib(i)
print(s)
