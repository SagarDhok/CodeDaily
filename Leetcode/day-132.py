

#! 976. Largest Perimeter Triangle
class Solution:
    def largestPerimeter(self, nums):
        nums.sort(reverse=True) 
        
        for i in range(len(nums) - 2):
            a, b, c = nums[i], nums[i+1], nums[i+2]
            if b + c > a:
                return a + b + c
        
        return 0
    
s = Solution()
nums = [2,1,2]
print(s.largestPerimeter(nums))

nums = [1,2,1,10]
print(s.largestPerimeter(nums))

