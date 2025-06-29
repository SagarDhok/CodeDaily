




#! Last duplicate element in a sorted array
class Solution:
    def dupLastIndex(self, arr):
     for i in range(len(arr) - 1, 0, -1):
         
         
         if arr[i] == arr[i - 1]:
             return [i, arr[i]]
     return [-1, -1]

arr= [1, 5, 5, 6, 6, 7]
print(Solution().dupLastIndex(arr))



