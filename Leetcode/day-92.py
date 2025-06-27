

#! 643. Maximum Average Subarray I

class Solution:
    def findMaxAverage(self, nums, k):
        window_sum = sum(nums[:k])  
        max_sum = window_sum

        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)

        return max_sum / k
s = Solution()
print(s.findMaxAverage([int(i) for i in input("Enter Array Elements : ").split()]))




class Solution:
    def findMaxAverage(self, nums, k) :
        max_avg = float("-inf")
        curr_avg = 0
        for i in range(len(nums) - k + 1):
            window = nums[i:i+k]

            curr_avg = sum(window)/k

            if curr_avg>max_avg:
                max_avg=curr_avg
        return max_avg
s = Solution()
print(s.findMaxAverage([int(i) for i in input("Enter Array Elements : ").split()]))
