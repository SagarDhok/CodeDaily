
#! 7. Reverse Integer
# Medium
# Topics
# premium lock icon
# Companies
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
 

# Constraints:

# -231 <= x <= 231 - 1
 
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 4,784,633/15.2M
# Acceptance Rate
# 31.5%
# Topics
# icon
# Companies




class Solution:
    def reverse(self, x: int) -> int:
        val = -1 if x<0 else 1
        x = abs(x)

        r =0
        while x>0:
            d = x%10
            r = r*10+d
            x = x//10
        result = r*val

        if result < -2**31 or result > 2**31 - 1:
            return 0

        return result

        
s = Solution()
print(s.reverse(123))
print(s.reverse(-123))
print(s.reverse(120))