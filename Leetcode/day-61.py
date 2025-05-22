
# Squares of a Sorted Array
def myabs(x):
  if x<0:
    return -x
  else:
    return x

class Solution:
    def sortedSquares(self, nums):
        arr = []
        for i in nums:
         arr.append(myabs(i)*myabs(i))

        arr.sort()
        return arr
s = Solution()
nums = [-4,-1,0,3,10]
print(s.sortedSquares(nums))


nums = [-7,-3,2,3,11]
print(s.sortedSquares(nums))