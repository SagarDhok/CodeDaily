

#! 747. Largest Number At Least Twice of Others
#*Approach - 1
class Solution:
    def dominantIndex(self, nums):
        first = second = -1
        index = 0

        for i, num in enumerate(nums):
            if num > first:
                second = first
                first = num
                index = i
            elif num > second:
                second = num

        return index if first >= 2 * second else -1

s = Solution()
nums = [3,6,1,0]
print(s.dominantIndex(nums))

nums = [1,2,3,4]
print(s.dominantIndex(nums))



#*Approach - 2
class Solution:
    def dominantIndex(self, nums):
        max_num = max(nums)
        max_index = nums.index(max_num)

        for num in nums:
            if num != max_num and max_num < 2 * num:
                return -1
        return max_index
s = Solution()
nums = [3,6,1,0]
print(s.dominantIndex(nums))

nums = [1,2,3,4]
print(s.dominantIndex(nums))
