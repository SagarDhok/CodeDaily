

#! Count Pairs Odd Xor
class Solution:
    def countOddXorPairs(self, arr):
       odd = 0
       for i in arr:
           if i%2!=0:
               odd+=1
               
       even = len(arr)-odd
       
       return odd*even
s = Solution()
arr = [1, 2, 3]
print(s.countOddXorPairs(arr))

arr = [1, 2]
print(s.countOddXorPairs(arr))