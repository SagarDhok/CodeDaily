
class Solution:
    def getMoreAndLess(self, arr, target):
     lc = 0
     gc = 0
     for i in arr:
       if i<=target:
           lc +=1
       if i>=target:
          gc +=1
     return [lc,gc]		
s = Solution()
arr = [1, 2, 8, 10, 11, 12, 19]
target = 0
s.getMoreAndLess()