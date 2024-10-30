class mergeSort:
    def sort(self, arr):
        # Start the recursive sorting process
        self.arr = arr
        self.temp = [0] * len(arr)  # Temporary array to assist with merging
        self.divide(0, len(arr) - 1)
        return self.arr
    
    def divide(self, lo, hi):
        # Recursive division of the array
        if lo >= hi:
            return
        mid = (lo + hi) // 2
        self.divide(lo, mid)
        self.divide(mid + 1, hi)
        self.merge(lo, mid, hi)
    
    def merge(self, lo, mid, hi):
        # Merge function using indices rather than slicing
        i, j, k = lo, mid + 1, lo
        
        # Copy data to temporary array to help with in-place merging
        self.temp[lo:hi + 1] = self.arr[lo:hi + 1]
        
        while i <= mid and j <= hi:
            if self.temp[i] <= self.temp[j]:
                self.arr[k] = self.temp[i]
                i += 1
            else:
                self.arr[k] = self.temp[j]
                j += 1
            k += 1
        
        # Copy any remaining elements from left side
        while i <= mid:
            self.arr[k] = self.temp[i]
            i += 1
            k += 1

        # Right side elements are already in place, no need to copy

# Original code execution starts
x = int(input())
arr = list(map(int, input().split()))
msort = mergeSort()
arr_sorted = msort.sort(arr)

# Output the sorted array
print(" ".join(map(str, arr_sorted)))
