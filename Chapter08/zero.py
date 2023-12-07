def count_sequences(n):
    if n == 1:
        return 2

    dp = [0] * (n + 1)
    dp[1] = 2
    dp[2] = 3

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# Read input
n = int(input())

# Calculate the count of sequences
result = count_sequences(n)

# Print the result
print(result)