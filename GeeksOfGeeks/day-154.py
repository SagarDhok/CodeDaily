

#! Find triplets with zero sum
# Difficulty: MediumAccuracy: 25.81%Submissions: 353K+Points: 4Average Time: 20m
# Given an array arr[] of integers, determine whether it contains a triplet whose sum equals zero. Return true if such a triplet exists, otherwise, return false.

# Examples:

# Input: arr[] = [0, -1, 2, -3, 1]
# Output: true
# Explanation: The triplet [0, -1, 1] has a sum equal to zero.
# Input: arr[] = [1, 2, 3]
# Output: false
# Explanation: No triplet with a sum of zero exists.
# Input: arr[] = [-5, 3, 2, -1, 0, 1]
# Output: true
# Explanation: The triplet [-5, 3, 2] has a sum equal to zero.
# Constraints:
# 1 ≤ arr.size() ≤ 103
# -106 ≤ arr[i] ≤ 106


class Solution:
    def findTriplets(self, arr):
        arr.sort()
        n = len(arr)

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                total = arr[i] + arr[left] + arr[right]

                if total == 0:
                    return True
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return False
    
s = Solution()
arr = [0, -1, 2, -3, 1]
print(s.findTriplets(arr))

arr = [1, 2, 3]
print(s.findTriplets(arr))

arr = [-5, 3, 2, -1, 0, 1]
print(s.findTriplets(arr))