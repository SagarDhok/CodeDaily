

# Reverse sub array
class Solution:
 def reverseSubArray(self,arr,l,r):
       arr[l-1:r]=arr[l-1:r][::-1]
       return arr
 
s = Solution()
arr = [1, 2, 3, 4, 5, 6, 7]
l = 2
r = 4
print(s.reverseSubArray(arr,l,r))


arr = [1, 6, 7, 4]
l = 1
r = 4
print(s.reverseSubArray(arr,l,r))
