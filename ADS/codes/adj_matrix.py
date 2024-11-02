n,conn = list(map(int, input().split()))

adj = [['0']*n for _ in range(n)]

for _ in range(conn):
    a,b = map(int, input().split())
    a-=1
    b-=1
    adj[a][b] = '1'


ans = "\n".join(" ".join(row)for row in adj)
print(ans)
