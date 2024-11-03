import sys
sys.setrecursionlimit(2*10**5)

class ArticulationPoint:
    def __init__(self, net):
        self.net = net
        self.n = len(net)
        self.vin = [0]*self.n
        self.low = [0]*self.n
        self.counter = 1
        self.cut_point = []

    def dfs(self, node, pa=-1):
        self.vin[node] = self.low[node] = self.counter
        self.counter+=1
        free_child = 0
        cut = False
        for to in self.net[node]:
            if to==pa: continue
            if self.vin[to]>0:
                self.low[node] = min(self.low[node], self.vin[to])
                continue
            
            self.dfs(to, node)
            free_child+=1
            self.low[node] = min(self.low[node], self.low[to])
            if self.low[to]>=self.vin[node] and pa!=-1:
                cut = True
            
        if cut: self.cut_point.append(node)
        elif pa==-1 and free_child>=2:
            self.cut_point.append(node)

    def get_cut_points(self):
        for i in range(self.n):
            if self.vin[i]>0: continue
            self.dfs(i)

        return self.cut_point

# main part starts
n, edge = list(map(int, input().split()))
net = [[] for _ in range(n)]
for _ in range(edge):
    x,y = list(map(int, input().split()))
    net[x-1].append(y-1)
    net[y-1].append(x-1)

ap = ArticulationPoint(net)
cut_points = ap.get_cut_points()
cut_points.sort()
# print(ap.vin, ap.low)
print(len(cut_points))
print(" ".join(map(lambda x: str(x+1), cut_points)))

