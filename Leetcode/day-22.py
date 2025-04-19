
# Missing Number
nums = [0,3,1]
n = len(nums)
s = 0
for i in range(n+1):
   s += i

array_sum = sum(nums)  

missing_value = s-array_sum
print(missing_value)

class Solution:
    def missingNumber(self,nums):
        for val in range(len(nums)+1):
            if val in nums:
                pass
            else:
                return val    
                
s = Solution()                
res = s.missingNumber([3,0,1])
print(res)