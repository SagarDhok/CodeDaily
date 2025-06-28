
#! 674. Longest Continuous Increasing Subsequence
class Solution:
    def findLengthOfLCIS(self, nums):
        
        max_count = 1
        count = 1
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
             count+=1
             if count>max_count:
                max_count = count

            else:
                count =1
        return max_count
    
s = Solution()
print(s.findLengthOfLCIS([int(i) for i in input("Enter Array Elementents : ").split()]))