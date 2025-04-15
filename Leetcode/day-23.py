
# Find All Missing Numbers in an Array 

class Solution:
    def findDisappearedNumbers(self, nums):
        n = 0
        while n < len(nums):
            index = nums[n]
            if index < 0:
                index = -index
            index -= 1

            if nums[index] > 0:
                nums[index] = -nums[index]

            n += 1

        result = []
        i = 0
        while i < len(nums):
            if nums[i] > 0:
                result.append(i + 1)
            i += 1

        return result

s = Solution()
print(s.findDisappearedNumbers([4,3,2,7,8,2,3,1])) 
