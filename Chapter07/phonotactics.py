n = int(input())
names = []

for _ in range(n):
    name = input()
    names.append(name)

max_unique_letters = 0

for name in names:
    unique_letters = len(set(name))
    if unique_letters > max_unique_letters:
        max_unique_letters = unique_letters

print(max_unique_letters)
