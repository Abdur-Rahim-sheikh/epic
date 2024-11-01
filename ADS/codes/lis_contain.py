from bisect import bisect_left as search


n,a,k,b,m = map(int, input().split())

seq = [a]
for _ in range(n-1):
    a = (a*k + b)%m
    seq.append(a)

lis_index = [0]
lis = [seq[0]]
pred = [-1]*n

for i in range(n):
    val = seq[i]
    
    idx = search(lis, val)
    if len(lis)==idx:
        lis.append(val)
        lis_index.append(i)
    else: 
        lis[idx] = val
        lis_index[idx] = i

    if idx>0:
        pred[i] = lis_index[idx-1]
    
print(len(lis))
idx = lis_index[-1]
i = len(lis)-1
# print(pred, seq, lis)
while idx!=-1:
    lis[i] = seq[idx]
    idx = pred[idx]
    i -= 1

print(" ".join(map(str,lis)))