from queue import PriorityQueue
import sys
def get_integer_array(m=1, n=1):
    inputs = list(map(int, sys.stdin.read().split()))
    if len(inputs) != m * n:
        raise ValueError("The number of inputs does not match the expected m*n dimensions.")
    
    return [inputs[i * n: (i + 1) * n] for i in range(m)]
class Dijkstra:
    def __init__(self, net):
        self.net = net
        self.weight = [float('inf')]*len(net)

    def dijkstra(self, start, end):
        self.weight[start] = 0
        pq = PriorityQueue()
        pq.put((0,start))
        
        while not pq.empty():
            w, node = pq.get()
            if node==end:
                return w
            for cost,to in self.net[node]:
                if self.weight[to]> w+cost:
                    self.weight[to] = w+cost
                    pq.put((self.weight[to],to))

        return -1



# main part starts
n, start, target = list(map(int, input().split()))
matrix = get_integer_array(n,n)
net = [[] for _ in range(n)]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] < 0: continue
        net[i].append((matrix[i][j],j))


ds = Dijkstra(net)
print(ds.dijkstra(start-1, target-1))


