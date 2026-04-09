

#! Largest number possible
# Difficulty: EasyAccuracy: 20.26%Submissions: 145K+Points: 2
# Given two numbers n and s , find the largest number that can be formed with n digits and whose sum of digits should be equals to s. Return -1 if it is not possible.

# Examples :

# Input: n = 2, s = 9
# Output: 90
# Explaination: It is the biggest number with sum of digits equals to 9.
# Input: n = 3, s = 20
# Output: 992
# Explaination: It is the biggest number with sum of digits equals to 20.
# Input: n = 1, s = 0
# Output: 0
# Constraints:
# 1 ≤ n ≤ 105
# 0 ≤ s ≤ 105




#User function Template for python3

class Solution:
    def findLargest(self, n, s):
            if s == 0:
                return "0" if n == 1 else "-1"
            
            if s > 9 * n:
                return "-1"
            
            result = []
            
            for _ in range(n):
                digit = min(9, s)
                result.append(str(digit))
                s -= digit
            
            return "".join(result)
s = Solution()
n = 2
s = 9
print(s.findLargest(n,s))

n = 3
s = 20
print(s.findLargest(n,s))

n = 1
s = 0
print(s.findLargest(n,s))


