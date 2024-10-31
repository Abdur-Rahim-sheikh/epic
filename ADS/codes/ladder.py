def dfs(n, allowed):
    if n==0 or allowed==0:
        return 1
    
    ans = 1
    for x in range(1,allowed):
        ans+=dfs(n-x, min(x-1,n-x))
    return ans

# inputs
x = int(input())
print(dfs(x,x))