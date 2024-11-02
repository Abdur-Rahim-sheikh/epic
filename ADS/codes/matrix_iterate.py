import sys

def get_integer_array(m=1, n=1):
    inputs = list(map(int, sys.stdin.read().split()))
    if len(inputs) != m * n:
        raise ValueError("The number of inputs does not match the expected m*n dimensions.")
    
    return [inputs[i * n: (i + 1) * n] for i in range(m)]


n,start = list(map(int, input().split()))
matrix = get_integer_array(n,n)

stack =[]
visit = [False]*n
visit[start-1] = True
stack = [start-1]

while stack:
    top = stack.pop()
    for i,val in enumerate(matrix[top]):
        if val and not visit[i]:
            visit[i] = True
            stack.append(i)


print(visit.count(True))