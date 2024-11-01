from queue import PriorityQueue
import sys
class MinimumSpanningTree:
    def __init__(self, n: int, net: list[list]):
        self.n = n
        self.net = net
        self.mst = []
        self.total_cost = 0
    
    def prims(self):
        visited = [False]*self.n
        
        pq = PriorityQueue()
        pq.put((0, 0, -1))
        while not pq.empty():
            cost, node, parent = pq.get()
            
            if visited[node]:
                continue
            if parent!=-1:
                self.mst.append((parent, node))
                self.total_cost += cost
            visited[node] = True
            for edge in self.net[node]:
                if not visited[edge[1]]:
                    pq.put((edge[0], edge[1], node))
        return self.total_cost
    
    def get_cost(self) -> int:
        return self.total_cost
    
    def get_nodes(self) -> list:
        return self.mst


def get_integer_array(m=1, n=1):
    inputs = list(map(int, sys.stdin.read().split()))
    if len(inputs) != m * n:
        raise ValueError("The number of inputs does not match the expected m*n dimensions.")
    
    return [inputs[i * n: (i + 1) * n] for i in range(m)]

n = int(input())
arr = get_integer_array(n,n)

net = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        net[i].append((arr[i][j], j))
        net[j].append((arr[i][j], i))

mst = MinimumSpanningTree(n, net)
print(mst.prims())
print(mst.get_nodes())