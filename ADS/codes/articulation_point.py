class ArticulationPoint:
    def __init__(self, net):
        self.net = net
        self.n = len(net)
        self.vin = [0]*self.n
        self.low = [0]*self.n
        self.counter = 0
        self.cut_point = []

    def dfs(self, node, pa=-1):
        self.vin[node] = self.low[node] = self.counter
        self.counter+=1
        free_child = 0
        self.visit[node] = True
        for to in self.net[node]:
            if to==pa: continue
            if self.visit[to]:
                self.low[node] = min(self.low[node], self.vin[to])
                continue
            
            self.dfs(to, node)
            free_child+=1
            self.low[node] = min(self.low[node], self.low[to])
            if self.low[to]>=self.low[node]:
                self.cut_point.append(node)
        
        if pa==-1 and free_child>=2:
            self.cut_point.append(node)

    def get_cut_points(self):
        for i in range(self.n):
            if self.visit[i]: continue
            self.dfs(i)
