
# Swap kth elements

class Solution:
    def swapKth(self, arr, k):
        
            arr[k-1],arr[-k] = arr[-k],arr[k-1]
            return arr
s = Solution()
arr = [1, 2, 3, 4, 5, 6, 7, 8]
k = 3
print(s.swapKth(arr,k))

s = Solution()
arr= [5, 3, 6, 1, 2]
k = 2
print(s.swapKth(arr,k))