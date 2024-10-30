class mergeSort:
    def sort(self, arr):
        self.arr = arr
        return self.divide(0,len(arr)-1)
    
    def divide(self, lo, hi):
        if hi-lo<=0:
            return self.arr[lo:hi+1]
        mid = (lo+hi)//2
        left = self.divide(lo, mid)
        right = self.divide(mid+1,hi)
        return self.merge(left, right)
    
    def merge(self, left, right):
        tem = []

        i,j = 0,0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                tem.append(left[i])
                i+=1
            else: 
                tem.append(right[j])
                j+=1
        if i==len(left):
            tem+=right[j:]
        else: tem+=left[i:]
        return tem


# original code starts
x = int(input())
arr = [int(x) for x in input().split()]
msort = mergeSort()
arr_sorted = msort.sort(arr)

present = map(str, arr_sorted)
print(" ".join(present))