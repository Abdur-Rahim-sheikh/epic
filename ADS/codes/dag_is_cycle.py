def dfs(net,pa, node, visit):
    response = False
    for data in net[node]:
        if visit[data]==2: continue
        if visit[data]==1: return True
        visit[data] +=1
        
        response |= dfs(net, node, data, visit)
        visit[data]+=1
        if response: return True
    return response

n, edge = list(map(int, input().split()))
net = [[] for _ in range(n+1)]
for _ in range(edge):
    x,y = list(map(int, input().split()))
    net[x].append(y)
    

visit = [0]*(n+1)
visit[0] = 2
for i in range(1,n+1):
    if visit[i]: continue
    visit[i] = 1
    response = dfs(net, -1, i, visit)
    
    if response: break

print(int(response))