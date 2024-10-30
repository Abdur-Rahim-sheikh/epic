class QuickSort:
    def __init__(self, arr):
        self.arr = arr
    
    def sort(self):
        self.quick_sort(0, len(self.arr) - 1)
        return self.arr
    def quick_sort(self, low, high):
        if low >= high:
            return
        pi = self.partition(low, high)
        self.quick_sort(low, pi - 1)
        self.quick_sort(pi + 1, high)

    def partition(self, low, high):
        idx = self.median_of_three(low, high)
        self.arr[idx],self.arr[high] = self.arr[high], self.arr[idx]
        pivot = self.arr[high]
        i = low
        for j in range(low, high):
            if self.arr[j] < pivot:
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
                i += 1
        self.arr[i], self.arr[high] = self.arr[high], self.arr[i]
        return i

    def median_of_three(self, low, high):
        mid = (low + high) // 2  # Middle index
        
        if self.arr[low] < self.arr[mid]:
            if self.arr[mid] < self.arr[high]:
                return mid
            elif self.arr[low] < self.arr[high]:
                return high
            else:
                return low
        else:
            if self.arr[low] < self.arr[high]:
                return low
            elif self.arr[mid] < self.arr[high]:
                return high
            else:
                return mid

# original code
n = int(input())
arr = [int(x) for x in input().split()]
qs = QuickSort(arr)
arr = qs.sort()

presentation = list(map(str, arr))
print(" ".join(presentation))