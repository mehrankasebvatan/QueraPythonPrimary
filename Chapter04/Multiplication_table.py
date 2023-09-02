for s in range(1, 11):
    for m in range(1, 11):
        if s > m:
            print(s*m, end=" ")
        elif s == m:
            print(0, end=" ")
        else:
            print(s*m*-1, end=" ")
    print("\n")