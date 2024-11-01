n = int(input())
arr = list(map(int, input().split()))
dp = [-1]*n
arr.sort()
def dfs(idx):
    if idx==0:
        return 10**5
    if dp[idx]!=-1:
        return dp[idx]
    
    ans = arr[idx] - arr[0]
    for i in range(idx-1):
        ans = min(ans, dfs(i) + arr[idx]-arr[i+1])
    dp[idx] = ans
    return ans
dfs(n-1)
# print(arr)
# print(dp)
print(dp[-1])