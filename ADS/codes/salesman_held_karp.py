# Read input
n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]

# Initialize dp and prev arrays
INF = float('inf')
size = 1 << n
dp = [[INF] * n for _ in range(size)]
prev = [[-1] * n for _ in range(size)]

# Initialize starting positions
for u in range(n):
    dp[1 << u][u] = 0
# helper function
check = lambda mask, i: mask & (1 << i)
# DP with bitmasking
for mask in range(size):
    for u in range(n):
        if not check(mask, u): continue
        for v in range(n):
            if check(mask,v): continue
            next_mask = mask | (1 << v)
            new_cost = dp[mask][u] + cost[u][v]
            if new_cost < dp[next_mask][v]:
                dp[next_mask][v] = new_cost
                prev[next_mask][v] = u

# Find the minimum cost and ending vertex
full_mask = (1 << n) - 1
min_cost = INF
end_vertex = -1
for u in range(n):
    if dp[full_mask][u] < min_cost:
        min_cost = dp[full_mask][u]
        end_vertex = u

# Reconstruct the path
path = []
mask = full_mask
u = end_vertex
while u != -1:
    path.append(u + 1)  # Convert to 1-based indexing for output
    temp_u = prev[mask][u]
    mask ^= (1 << u)
    u = temp_u

path.reverse()

# Output the results
print(min_cost)
print(' '.join(map(str, path)))
