


#! Stable Sort and Position
class Solution:
    def getIndexInSortedArray(self, arr, k):
            target = arr[k]
    
            count_smaller = 0
            count_equal_before = 0
            
            for i, val in enumerate(arr):
                if val < target:
                    count_smaller += 1
                elif val == target and i < k:
                    count_equal_before += 1
            
            return count_smaller + count_equal_before
    
s= Solution()
arr= [3, 4, 3, 5, 2, 3, 4, 3, 1, 5]
k = 5
print(s.getIndexInSortedArray(arr,k))

arr= [3, 4, 3, 5, 2, 3, 4, 3, 1, 5]
k = 2
print(s.getIndexInSortedArray(arr,k))