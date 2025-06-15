
# Distribute Candies
class Solution:
    def distributeCandies(self, candyType) :
        
      lst = set(candyType )

      if len(lst)>len(candyType)//2:

        return len(candyType)//2
      else : 
           return len(lst)
      
s= Solution()
candyType = [1,1,2,2,3,3]
print(s.distributeCandies(candyType))


candyType = [1,1,2,3]
print(s.distributeCandies(candyType))

candyType = [6,6,6,6]
print(s.distributeCandies(candyType))

