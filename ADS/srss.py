C = int(input())
fun = lambda x: x**2 + x**0.5
ans = 0
lo, high = 0, C
it = 100
while it:
    it-=1
    mid = (lo+high)/2
    if fun(mid) <=C:
        ans = mid
        lo = mid
    else:
        high = mid

print(ans)