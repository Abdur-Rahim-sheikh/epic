# bipartite coloring
def dfs_color(colors, net, node, color):
    response = True
    for val in net[node]:
        if colors[val]==color:
            return False
        if colors[val]!=-1: continue
        colors[val] = not color
        response &= dfs_color(colors, net, val, colors[val])
        if not response:
            return response

    return response

n, edge = list(map(int, input().split()))
net = [[] for _ in range(n+1)]
for _ in range(edge):
    a, b = list(map(int, input().split()))
    net[a].append(b)
    net[b].append(a)

colors = [-1]*(n+1)
response = True
for i in range(1, n):
    if colors[i]!=-1: continue
    colors[i] = 0
    response &= dfs_color(colors, net, i, 0)
    if not response:break

print("YES" if response else "NO")