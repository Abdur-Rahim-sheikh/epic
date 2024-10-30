# def bin_search(arr, val):
#     lo, high = 0, len(arr)-1
#     while lo<=high:
#         mid = (lo+high)//2
#         if arr[mid] <val:
#             lo = mid + 1
#         elif arr[mid] > val:
#             high = mid -1
        
#         else: return "YES"
#     return "NO"
def get_input():
    return [int(x) for x in input().split()]

n,k = get_input()
arr = set(get_input())
queries = get_input()

for query in queries:
    print("YES" if query in arr else "NO")