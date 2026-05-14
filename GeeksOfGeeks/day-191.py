

#! Find Transition Point
# Difficulty: EasyAccuracy: 37.9%Submissions: 285K+Points: 2Average Time: 20m
# Given a sorted array, arr[] containing only 0s and 1s, find the transition point, i.e., the first index where 1 was observed, and before that, only 0 was observed.  If arr does not have any 1, return -1. If array does not have any 0, return 0.

# Examples:

# Input: arr[] = [0, 0, 0, 1, 1]
# Output: 3
# Explanation: index 3 is the transition point where 1 begins.
# Input: arr[] = [0, 0, 0, 0]
# Output: -1
# Explanation: Since, there is no "1", the answer is -1.
# Input: arr[] = [1, 1, 1]
# Output: 0
# Explanation: There are no 0s in the array, so the transition point is 0, indicating that the first index (which contains 1) is also the first position of the array.
# Input: arr[] = [0, 1, 1]
# Output: 1
# Explanation: Index 1 is the transition point where 1 starts, and before it, only 0 was observed.
# Constraints:
# 1 ≤ arr.size() ≤ 105
# 0 ≤ arr[i] ≤ 1


class Solution:
    def transitionPoint(self, arr): 
        if arr[0] == 1:
            return 0
        for i in range(len(arr)-1):
                if arr[i]==0 and arr[i+1]==1:
                        return i+1
                
        return -1
    
s = Solution()
arr = [0, 0, 0, 1, 1]
print(s.transitionPoint(arr))

arr = [0, 0, 0, 0]
print(s.transitionPoint(arr))

arr = [1, 1, 1]
print(s.transitionPoint(arr))

arr = [0, 1, 1]
print(s.transitionPoint(arr))




class Solution:
    def transitionPoint(self, arr):

        for i in range(len(arr)):
            if arr[i] == 1:
                return i

        return -1
    
s = Solution()
arr = [0, 0, 0, 1, 1]
print(s.transitionPoint(arr))

arr = [0, 0, 0, 0]
print(s.transitionPoint(arr))

arr = [1, 1, 1]
print(s.transitionPoint(arr))

arr = [0, 1, 1]
print(s.transitionPoint(arr))