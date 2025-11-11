

#! Array Searching

class Solution:
    def search(self,arr, x):
        
        for i in range(len(arr)):
                       if arr[i] == x:
                               return i
                       
        return -1
    
s = Solution()
arr = [1, 2, 3, 4]
x = 3
print(s.search(arr,x))

arr = [10, 8, 30, 4, 5]
x = 5
print(s.search(arr,x))

arr = [10, 8, 30]
x = 6
print(s.search(arr,x))