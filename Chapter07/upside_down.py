base_list = []
while 1 == 1:
    a = input()
    if a == "End":
        break
    else:
        base_list.append(int(a))
new_list = []
for s in range(0, len(base_list)):
    new_list.append(base_list.pop())
for s in range(0, len(new_list)):
    print(str(new_list[s])[::-1].strip('0'))