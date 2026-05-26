

#! Unique Number I
# Difficulty: EasyAccuracy: 61.81%Submissions: 172K+Points: 2
# Given a unsorted array arr[] of positive integers having all the numbers occurring exactly twice, except for one number which will occur only once. Find the number occurring only once.

# Examples :

# Input: arr[] = [1, 2, 1, 5, 5]
# Output: 2
# Explanation: Since 2 occurs once, while other numbers occur twice, 2 is the answer.
# Input: arr[] = [2, 30, 2, 15, 20, 30, 15]
# Output: 20
# Explanation: Since 20 occurs once, while other numbers occur twice, 20 is the answer.
# Constraints
# 1 ≤  arr.size()  ≤ 106
# 0 ≤ arr[i] ≤ 109

#!Approach - 1
class Solution:
    def findUnique(self, arr):

        ans = 0

        for num in arr:
            ans ^= num

        return ans
s = Solution()
arr = [1, 2, 1, 5, 5]
print(s.findUnique(arr))

arr = [2, 30, 2, 15, 20, 30, 15]
print(s.findUnique(arr))



#!Approach - 2
class Solution:
    def findUnique(self, arr):

        for num in arr:
            if arr.count(num) == 1:
                return num

s = Solution()
arr = [1, 2, 1, 5, 5]
print(s.findUnique(arr))

arr = [2, 30, 2, 15, 20, 30, 15]
print(s.findUnique(arr))




#!Approach - 3
class Solution:
    def findUnique(self, arr):

        freq = {}

        for num in arr:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        for num in freq:
            if freq[num] == 1:
                return num
s = Solution()
arr = [1, 2, 1, 5, 5]
print(s.findUnique(arr))

arr = [2, 30, 2, 15, 20, 30, 15]
print(s.findUnique(arr))