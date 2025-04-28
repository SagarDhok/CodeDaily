
#! Who has the majority?
#APPROACH - 1
class Solution:
    def majorityWins(self, arr, x, y):
      cx = 0
      cy = 0
      for i in arr:
          if i == x :
              cx = cx+1
          elif i == y:
              cy = cy+1
      return x if cx > cy else y if  cy > cx else min(x,y)
s = Solution()
print(s.majorityWins([1,1,2,2,3,3,4,4,4,4,5], 4, 5)) 
print(s.majorityWins([1,2,3,4,5,6,7,8], 4, 7)) 

#APPROACH - 2
class Solution:
    def majorityWins(self, arr, x, y):
        cx = arr.count(x)
        cy = arr.count(y)
        
        return x if cx > cy else y if  cy > cx else min(x,y)
print(s.majorityWins([1,1,2,2,3,3,4,4,4,4,5], 4, 5)) 
print(s.majorityWins([1,2,3,4,5,6,7,8], 4, 7)) 