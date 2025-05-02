
#  !Smaller and Larger
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
arr = [int(i) for i in input("Enter List Of Values : ").split()]
target = int(input("Enter Your Target : "))
print(s.getMoreAndLess(arr,target))