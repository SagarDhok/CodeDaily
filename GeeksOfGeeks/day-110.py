

#! Maximum Perimeter of Triangle from array

class Solution:
    def maxPerimeter(self, arr):
        arr.sort()
        a,b,c = arr[-3],arr[-2],arr[-1]
        if a + b > c:
            return a + b + c
        else:
            return -1
        
s= Solution()
arr = [6, 1, 6, 5, 8, 4]
print(s.maxPerimeter(arr))


arr = [7, 55, 20, 1, 4, 33, 12]
print(s.maxPerimeter(arr))

