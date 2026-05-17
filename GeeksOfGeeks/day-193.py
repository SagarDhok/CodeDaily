

#! Move all negative elements to end
# Difficulty: EasyAccuracy: 56.24%Submissions: 252K+Points: 2
# Given an unsorted array arr[ ] having both negative and positive integers. Place all negative elements at the end of the array without changing the order of positive elements and negative elements.

# Note: Don't return any array, just in-place on the array.

# Examples:

# Input : arr[] = [1, -1, 3, 2, -7, -5, 11, 6 ]
# Output : [1, 3, 2, 11, 6, -1, -7, -5]
# Explanation: By doing operations we separated the integers without changing the order.
# Input : arr[] = [-5, 7, -3, -4, 9, 10, -1, 11]
# Output : [7, 9, 10, 11, -5, -3, -4, -1]
# Constraints:
# 1 ≤ arr.size ≤ 106
# -109 ≤ arr[i] ≤ 109


class Solution:
    def segregateElements(self, arr):

        pos = []
        neg = []

        for val in arr:
            if val > 0:
                pos.append(val)
            else:
                neg.append(val)

        arr[:] = pos + neg

        return arr
    
s = Solution()
arr= [1, -1, 3, 2, -7, -5, 11, 6 ]
print(s.segregateElements(arr))

arr = [-5, 7, -3, -4, 9, 10, -1, 11]
print(s.segregateElements(arr))