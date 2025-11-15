

#! 908. Smallest Range I

class Solution:
    def smallestRangeI(self, nums, k):
        maxi = nums[0]
        mini = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > maxi:
                maxi = nums[i]
            if nums[i] < mini:
                mini = nums[i]
        diff = (maxi - k) - (mini + k)
        if diff < 0:
            return 0
        return diff

s = Solution()
nums = [1]
k = 0
print(s.smallestRangeI(nums,k))

nums = [0,10]
k = 2
print(s.smallestRangeI(nums,k))

nums = [1,3,6]
k = 3
print(s.smallestRangeI(nums,k))



class Solution:
    def smallestRangeI(self, nums, k):
             return max(0, (max(nums) - k) - (min(nums) + k))

s = Solution()
nums = [1]
k = 0
print(s.smallestRangeI(nums,k))

nums = [0,10]
k = 2
print(s.smallestRangeI(nums,k))

nums = [1,3,6]
k = 3
print(s.smallestRangeI(nums,k))

