n = int(input())

total_sum = 0
step_sum = 0
for i in range(1, n + 1):
    step_sum += i
    total_sum += step_sum
    numbers = '+'.join(str(x) for x in range(1, i + 1))
    print(f"{numbers} = {step_sum}")

print(f"Total sum of series is: {total_sum}")
