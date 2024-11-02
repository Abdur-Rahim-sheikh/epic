def topo_sort(net, node, visit, order):
    visit[node] = 1
    response = False
    for data in net[node]:
        if visit[data]==2: continue
        if visit[data]==1: return True
        
        response |= topo_sort(net, data, visit,order)
        
        if response: return True
    visit[node] = 2
    order.append(node)
    return response

n, edge = list(map(int, input().split()))
net = [[] for _ in range(n+1)]
for _ in range(edge):
    x,y = list(map(int, input().split()))
    net[x].append(y)
    

visit = [0]*(n+1)
visit[0] = 2
order = []
for i in range(1,n+1):
    if visit[i]: continue
    response = topo_sort(net, i, visit,order)
    
    if response: break

if response: print(-1)
else:
    print(" ".join(map(str, order[::-1])))