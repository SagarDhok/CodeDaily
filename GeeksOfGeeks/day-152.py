

#! Check if array is sorted
# Difficulty: EasyAccuracy: 39.37%Submissions: 366K+Points: 2Average Time: 15m
# Given an array arr[], check whether it is sorted in non-decreasing order. Return true if it is sorted otherwise false.

# Examples:

# Input: arr[] = [10, 20, 30, 40, 50]
# Output: true
# Explanation: The given array is sorted.
# Input: arr[] = [90, 80, 100, 70, 40, 30]
# Output: false
# Explanation: The given array is not sorted.
# Constraints:
# 1 ≤ arr.size ≤ 106
# - 109 ≤ arr[i] ≤ 109

class Solution:
    def isSorted(self, arr) -> bool:
        
        for i in range(len(arr)-1):
            if not arr[i] <= arr[i+1]:
                return False
        return True
s = Solution()
arr = [10, 20, 30, 40, 50]
print(s.isSorted(arr))

arr = [90, 80, 100, 70, 40, 30]
print(s.isSorted(arr))