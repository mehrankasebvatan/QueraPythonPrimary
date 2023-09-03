n, x = map(int, input().split())
base_list = input().split()
base_list = [int(num) for num in base_list]

x = x % n  # Handle cases where x is larger than the length of the list

rotated_list = base_list[-x:] + base_list[:-x]  # Rotate the list using slicing

for m in rotated_list:
    print(m, end=" ")