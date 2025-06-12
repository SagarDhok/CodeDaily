

# Array Partition
class Solution:
    def arrayPairSum(self, nums) :
        nums.sort()

        min_sum = 0
        for i in range(0,len(nums),2):
              min_sum+=nums[i]
        return min_sum
        
s = Solution()

print(s.arrayPairSum([int(i) for i in input("Enter Values : ").split()]))