import sys

def get_integer_array(m, n):
    data = sys.stdin.read().strip().split()
   
    return [list(map(int, data[i * n: (i + 1) * n])) for i in range(m)]


# start input
m,n = [int(x) for x in input().split()]
arr = get_integer_array(m,n)
ans = 0
for i in range(0,len(arr)):
    for j in range(0, len(arr[0])):
        if i and j and arr[i][j]:
            arr[i][j] = min(arr[i-1][j],arr[i-1][j-1],arr[i][j-1]) + 1
        
        if arr[i][j]>ans:
            ans = arr[i][j]
            coordinate = [i-ans+2,j-ans+2]

print(f"{ans}\n{coordinate[0]} {coordinate[1]}")