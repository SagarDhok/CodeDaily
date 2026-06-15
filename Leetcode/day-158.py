
#! 434. Number of Segments in a String
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given a string s, return the number of segments in the string.

# A segment is defined to be a contiguous sequence of non-space characters.

 

# Example 1:

# Input: s = "Hello, my name is John"
# Output: 5
# Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]
# Example 2:

# Input: s = "Hello"
# Output: 1
 

# Constraints:

# 0 <= s.length <= 300
# s consists of lowercase and uppercase English letters, digits, or one of the following characters "!@#$%^&*()_+-=',.:".
# The only space character in s is ' 

class Solution:
    def countSegments(self, s: str) -> int:
      count = 0
      for i in range(len(s)):
         if s[i]!= " " and (i==0 or s[i-1]==" "):
            count+=1
      return
         
        
        
sol = Solution()
s = "Hello, my name is John"
print(sol.countSegments(s))

s = "Hello"
print(sol.countSegments(s))



# class Solution:
#     def countSegments(self, s: str) -> int:
#      word_list = s.split()
#      count = 0
#      for word in word_list:
#         count+=1
#      return count
               

# sol = Solution()
# s = "Hello, my name is John"
# print(sol.countSegments(s))

# s = "Hello"
# print(sol.countSegments(s))