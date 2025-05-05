
# Find element at a given Index
class Solution:
    def findElementAtIndex(self,key, arr ):
        # code here
        for i in range(len(arr)):
            if i==key:
                return arr[i]
s = Solution()
key = 2 
arr = [10, 20, 30, 40, 50]
print(s.findElementAtIndex(key,arr))

s = Solution()
key = 4
arr = [10, 20, 30, 40, 50, 60, 70]
print(s.findElementAtIndex(key,arr))