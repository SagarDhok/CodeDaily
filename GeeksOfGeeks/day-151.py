


#! Check Equal Arrays
# Difficulty: EasyAccuracy: 42.18%Submissions: 426K+Points: 2Average Time: 30m
# Given two arrays a[] and b[] of equal size, the task is to find whether the elements in the arrays are equal.
# Two arrays are said to be equal if both contain the same set of elements, arrangements (or permutations) of elements may be different though.
# Note: If there are repetitions, then counts of repeated elements must also be the same for two arrays to be equal.

# Examples:

# Input: a[] = [1, 2, 5, 4, 0], b[] = [2, 4, 5, 0, 1]
# Output: true
# Explanation: Both the array can be rearranged to [0,1,2,4,5]
# Input: a[] = [1, 2, 5], b[] = [2, 4, 15]
# Output: false
# Explanation: a[] and b[] have only one common value.
# Constraints:
# 1 ≤ a.size(), b.size() ≤ 107
# 0 ≤ a[i], b[i] ≤ 109

# Expected Complexities





class Solution:
    def checkEqual(self, a, b) -> bool:
        
        if len(a)!=len(b):
            return False
            
        a.sort()
        b.sort()
        
        for val in range(len(a)):
            if a[val]!=b[val]:
                return False
        return True
            
s = Solution()
a = [1, 2, 5, 4, 0]
b = [2, 4, 5, 0, 1]
print(s.checkEqual(a,b))


a = [1, 2, 5]
b = [2, 4, 15]
print(s.checkEqual(a,b))