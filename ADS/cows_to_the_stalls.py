n,m = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]

def count_cows(arr, min_dist):
    count = 1
    last_pos = arr[0]
    for i in range(1, len(arr)):
        if arr[i] - last_pos >= min_dist:
            count += 1
            last_pos = arr[i]
    return count

ans = 0
mid = arr[n-1]
while mid:
    while count_cows(arr, ans+mid) >= m:
        ans += mid
    mid //= 2

print(ans)