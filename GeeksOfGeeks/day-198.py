
#! Digits in Factorial
# Difficulty: EasyAccuracy: 29.7%Submissions: 175K+Points: 2
# Given an integer n, find the number of digits in the value of n factorial. 

# Examples :

# Input: n = 5
# Output: 3
# Explanation: Factorial of 5 is 120. Number of digits in 120 is 3 (1, 2, and 0)
# Input: n = 120
# Output: 199
# Explanation: The number of digits in 120! is 199
# Constraints:
# 1 ≤ n ≤ 105

#^ Approach 1
import math

class Solution:
    def digitsInFactorial(self, n):

        if n < 2:
            return 1

        digits = (n * math.log10(n / math.e) +
                 math.log10(2 * math.pi * n) / 2)

        return int(digits) + 1
s = Solution()
print(s.digitsInFactorial(int(input("Enter A Number : "))))



#^ Approach 2

class Solution:
    def digitsInFactorial(self,n):
        
        fact = 1
        for  i in range(1,n+1):
          fact*=i
        
        noofdigits = 0
        
        while fact>0:
          d = fact%10
          noofdigits+=1
          fact = fact//10
          
        return noofdigits
s = Solution()
print(s.digitsInFactorial(int(input("Enter A Number : "))))