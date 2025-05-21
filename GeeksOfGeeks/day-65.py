

class Solution:
    def mergeNsort(self, arr, brr):
        arr3 = set(arr+brr)
        return sorted(arr3)


s = Solution()
arr1 = [11, 1, 8]
arr2 = [10, 11]
print(s.mergeNsort(arr1,arr2))


arr1= [7, 1, 5, 3, 9]
arr2  = [8, 4, 3, 5, 2, 6]
print(s.mergeNsort(arr1,arr2))