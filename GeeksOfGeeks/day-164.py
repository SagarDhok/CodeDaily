

#! Learn to Comment - Python
# Difficulty: BasicAccuracy: 49.28%Submissions: 107K+Points: 1
# Comments are very useful in any language to tell users what is the task of any function or operation. The comments are neglected by the compiler, so whatever you write in the comments won't have any effect on the working of a code.
# In Python, comments can be written as mentioned below:
# # This is a comment
# """ This is also a comment """
# You are given a complete function that outputs a, b, and c. Comment the code that outputs b, so only a and c gets printed.

# Examples: 

# Input: a = 5, b = 6, c = 15
# Output:
# 5
# 15
# Input:a = 5, b = 8, c = 15
# Output:
# 5
# 15

class Solution:

    def printValues(self, a, b, c):
        print(a)
        # print(b)
        print(c)
