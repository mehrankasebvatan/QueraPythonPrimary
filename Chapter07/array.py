q = int(input())
arr = []

for _ in range(q):
    op = input().split()
    if op[0] == "+":
        i = int(op[1])
        x = int(op[2])
        arr.insert(i - 1, x)
    elif op[0] == "-":
        i = int(op[1])
        del arr[i - 1]

    if len(arr) == 0:
        print("EMPTY")
    else:
        print(" ".join(map(str, arr)))
