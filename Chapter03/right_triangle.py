a, b, c = map(int, input().split())
if a != 0 and b != 0 and c != 0:
    if a + b + c == 180:
        if a == 90 or b == 90 or c == 90:
            print("Bale")
        else:
            print("Na")
    else:
        print("Na")
else:
    print("Na")
