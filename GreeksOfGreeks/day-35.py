# First and Second Smallests
class Solution:
    def minAnd2ndMin(self, arr):
        mv1 = float("inf")
        mv2 = float("inf")

        for i in arr:
          if i<mv1:
            mv2 = mv1
            mv1 = i
          if i<mv2 and i!=mv1:
            mv2 = i
        
        if mv1 != float("inf") and mv2 != float("inf"):
            return [mv1, mv2]
        else:
            return [-1]


s = Solution()
arr = [int(i) for i in input("Enter List Of Values : ").split()]
print(s.minAnd2ndMin(arr))
