

#! 137. Single Number II
# Medium
# Topics
# premium lock icon
# Companies
# Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.


 

# Example 1:

# Input: nums = [2,2,3,2]
# Output: 3
# Example 2:

# Input: nums = [0,1,0,1,0,1,99]
# Output: 99
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -231 <= nums[i] <= 231 - 1
# Each element in nums appears exactly three times except for one element which appears once.
 
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 856,237/1.3M
# Acceptance Rate
# 66.7%
# Topics
# icon
# Companies
# Similar Questions
# Discussion (187


class Solution:
    def singleNumber(self, nums):
      freq = {}
      for val in nums:
        freq[val] = freq.get(val,0)+1

      for key in nums:
        if freq[key]==1:
            return key 
     
s= Solution()

nums = [2,2,3,2]
print(s.singleNumber(nums))

nums = [0,1,0,1,0,1,99]
print(s.singleNumber(nums))