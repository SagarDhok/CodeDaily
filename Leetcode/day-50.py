
# Kth Largest Element in an Array
class Solution:
    def findKthLargest(self, nums, k):
        nums.sort()
        return nums[-k]
    

s = Solution()
nums = [3,2,1,5,6,4]
k = 2
print(s.findKthLargest(nums,k))


nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(s.findKthLargest(nums,k))