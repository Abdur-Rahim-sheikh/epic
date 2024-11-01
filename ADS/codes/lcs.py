def get_integer_array(m=1, n=1):
    inputs = list(map(int, input().split()))
    if len(inputs) != m * n:
        raise ValueError("The number of inputs does not match the expected m*n dimensions.")
    
    return [inputs[i * n: (i + 1) * n] for i in range(m)]
n = int(input())
seq1 = get_integer_array(1, n)[0]
m = int(input())
seq2 = get_integer_array(1, m)[0]
dp = [0] * (m + 1)

# longest common subsequence 1d dp
for i in range(1, n + 1):
    for j in range(m, 0, -1):
        if seq1[i - 1] == seq2[j - 1]:
            dp[j] = dp[j - 1] + 1
    for j in range(1, m + 1):
        dp[j] = max(dp[j], dp[j - 1])

print(dp[m])
