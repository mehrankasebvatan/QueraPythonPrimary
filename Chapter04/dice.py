a = 1
b = 2
c = 3
x = 0
y = 0
z = 0

while a != b or a != c or b != c:
    a, b, c = map(int, input().split())
    if a == b or a == c or b == c:
        continue
    else:
        if min(a, b, c) == a:
            x += 1
        elif min(a, b, c) == b:
            y += 1
        else:
            z += 1

if x > y and x > z:
    print("Eyval Bijan!")
else:
    print("Ey baba! Eshkal nadare.")