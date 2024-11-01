import sys
check = lambda x, bit: (x & (1<<bit))
on = lambda x, bit: (x | (1<<bit))
def get_integer_array(m=1, n=1):
    inputs = list(map(int, sys.stdin.read().split()))
    if len(inputs) != m * n:
        raise ValueError("The number of inputs does not match the expected m*n dimensions.")
    
    return [inputs[i * n: (i + 1) * n] for i in range(m)]

def held_karp_tsp(matrix):
    n = len(matrix)
    size = 1 << n
    inf = float("inf")
    dp = [[inf]*size for _ in range(n)]
    prev = [[-1]*size for _ in range(n)]

    for i in range(n):
        dp[i][1<<i] = 0

    for mask in range(1, size):
        for i in range(n):
            if not check(mask, i): continue
            for j in range(n):
                if check(mask, j): continue
                new_mask = on(mask, j)
                val = dp[mask][i] + matrix[i][j]
                if dp[j][new_mask] > val:
                    dp[j][new_mask] = val
                    prev[j][new_mask] = i
    
    shortest = float("inf")
    all_set = (1<<n) - 1
    for i in range(n):
        if shortest > dp[i][all_set]:
            shortest = dp[i][all_set]
            last = i

    path = []
    mask = (1<<n) - 1
    while last!=-1:
        path.append(last)
        next = prev[last][mask]
        mask = mask ^ (1<<last)
        last = next

    return path, shortest


# input starts
n = int(input())
matrix = get_integer_array(n, n)

path, shortest = held_karp_tsp(matrix)
print(shortest)
print(" ".join(map(str, path)))