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
        pivot = self.arr[high]
        i = low
        for j in range(low, high):
            if self.arr[j] < pivot:
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
                i += 1
        self.arr[i], self.arr[high] = self.arr[high], self.arr[i]
        return i
    

if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    sort = QuickSort(arr)
    print(sort.sort())