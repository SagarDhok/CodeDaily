
# Find Peak Element Index in a Non-Adjacent Array
class Solution:
    def peakElement(self,arr):
        if len(arr)==1:
            return 0
        if arr[0]>arr[1]:
            return arr[0]
        for i in range(1,len(arr)-1):
            if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
                # print(arr[i])
                return arr[i]
        if arr[len(arr)-1]>arr[len(arr)-2]:
            return len(arr)-1
        return arr[-1]
ob1 = Solution()
arr = [1, 2, 4, 5, 7, 8, 3]
index = ob1.peakElement(arr)
print(index)
