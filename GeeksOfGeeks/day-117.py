

#! Farthest Index

class Solution:
    def findIndex(self, arr, x):
        for i in range(-1,-len(arr),-1):
            if arr[i]==x:
                return x
        return -1
s = Solution()
arr= [7, 42, 5, 6, 42, 8, 7, 5, 3, 6, 7] 
x = 7
print(s.findIndex(arr,x))