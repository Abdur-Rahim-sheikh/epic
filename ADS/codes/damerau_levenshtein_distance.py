def damerau_levenshtein(s,t):
    INF = float('inf')
    n,m = len(s)+1, len(t)+1
    dp = [[INF]*n for _ in range(m)]
    for i in range(m): dp[i][0] = i
    for j in range(n): dp[0][j] = j

    for i in range(1,m):
        for j in range(1,n):
            x = min(dp[i][j], dp[i-1][j]+1,dp[i][j-1]+1)
            
            x = min(x, dp[i-1][j-1]+(t[i-1]!=s[j-1]))
            if i>1 and j>1 and t[i-1]==s[j-2] and t[i-2]==s[j-1]:
                x = min(x, dp[i-2][j-2]+1)
            
            dp[i][j] = x

    return dp[-1][-1]


# code starts here
s,t = input(), input()
print(damerau_levenshtein(s,t))