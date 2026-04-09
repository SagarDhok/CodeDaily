
# Arithmetic Number
# Difficulty: EasyAccuracy: 16.63%Submissions: 191K+Points: 2Average Time: 10m
# Given three integers  'a' denotes the first term of an arithmetic sequence, 'c' denotes the common difference of an arithmetic sequence and an integer 'b'. you need to tell whether 'b' exists in the arithmetic sequence or not. Return 1 if b is present in the sequence. Otherwise, returns 0.

# Examples:

# Input: a = 1, b = 3, c = 2
# Output: true
# Explaination: 3 is the second term of the sequence starting with 1 and having a common difference 2.
# Input: a = 1, b = 2, c = 3
# Output: false
# Explaination: 2 is not present in the sequence.
# Input: a = 1, b = 2, c = 4
# Output: false
# Explaination: 2 is not present in the sequence.
# Constraints:
# -109 ≤ a, b, c ≤ 109

class Solution:
    def inSequence(self, a, b, c):
        if c == 0:
            return 1 if a == b else 0
        
        if (b - a) % c == 0 and (b - a) // c >= 0:
            return 1
        
        return 0
s = Solution()
a = int(input("Enter Value of A : "))
b = int(input("Enter Value of B : "))
c = int(input("Enter Value of C : "))
print(s.inSequence(a,b,c))