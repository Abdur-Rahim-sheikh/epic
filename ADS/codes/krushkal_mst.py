from queue import Queue
import sys

class MinimumSpanningTree:
    def __init__(self, n: int, edges: list[tuple]):
        self.n = n
        self.edges = edges
        self.p = [i for i in range(n)]
        self.mst = [[] for _ in range(n)]
        self.path = []
        
        self.total_cost = 0

    def find(self, x: int) -> int:
        if self.p[x]==x:
            return x
        self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px==py:
            return False
        self.p[px] = py
        return True
    
    def kruskal(self):
        self.edges.sort(key=lambda x: x[0])
        for edge in self.edges:
            if self.union(edge[1], edge[2]):
                self.mst[edge[1]].append(edge[2])
                self.mst[edge[2]].append(edge[1])
                self.total_cost += edge[0]

        return self.total_cost
    
    def get_cost(self) -> int:
        return self.total_cost
    
    def get_path(self) -> list:
        if self.path: return self.path

        start = self.degree.index(1)
        self.path.append(start)
        q = Queue()
        q.put(start)
        visited = [False]*self.n
        visited[start] = True
        while not q.empty():
            node = q.get()
            self.path.append(node)
            for neighbor in self.mst[node]:
                if not visited[neighbor]:
                    q.put(neighbor)
                    visited[neighbor] = True



def get_integer_array(m=1, n=1):
    inputs = list(map(int, sys.stdin.read().split()))
    if len(inputs) != m * n:
        raise ValueError("The number of inputs does not match the expected m*n dimensions.")
    
    return [inputs[i * n: (i + 1) * n] for i in range(m)]

n = int(input())
arr = get_integer_array(n,n)

edges = []
for i in range(n):
    for j in range(n):
        edges.append((arr[i][j], i, j))

mst = MinimumSpanningTree(n, edges)
print(mst.kruskal())
print(mst.get_nodes())