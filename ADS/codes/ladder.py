dp = dict()
def dfs(n, allowed):
    if n==0:
        return 1
    if allowed==0:
        return 0
    if (n,allowed) in dp:
        return dp[(n,allowed)]
    ans = 0
    for x in range(1,allowed+1):
        if n-x>=0:
            ans+=dfs(n-x, x-1)
    dp[(n,allowed)] = ans
    return ans

# inputs
x = int(input())
print(dfs(x,x))