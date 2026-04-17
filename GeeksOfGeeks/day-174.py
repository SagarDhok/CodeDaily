

#! Permutations of a String
# Difficulty: MediumAccuracy: 34.65%Submissions: 341K+Points: 4
# Given a string s, which may contain duplicate characters, your task is to generate and return an array of all unique permutations of the string. You can return your answer in any order.

# Examples:

# Input: s = "ABC"
# Output: ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"]
# Explanation: Given string ABC has 6 unique permutations.
# Input: s = "ABSG"
# Output: ["ABGS", "ABSG", "AGBS", "AGSB", "ASBG", "ASGB", "BAGS", "BASG", "BGAS", "BGSA", "BSAG", "BSGA", "GABS", "GASB", "GBAS", "GBSA", "GSAB", "GSBA", "SABG", "SAGB", "SBAG", "SBGA", "SGAB", "SGBA"]
# Explanation: Given string ABSG has 24 unique permutations.
# Input: s = "AAA"
# Output: ["AAA"]
# Explanation: No other unique permutations can be formed as all the characters are same.
# Constraints:
# 1 <= s.size() <= 9
# s contains only Uppercase english alphabets

class Solution:
    def findPermutation(self, s):
        res = []
        s = sorted(s)
        used = [False] * len(s)
        
        def backtrack(path):
            if len(path) == len(s):
                res.append("".join(path))
                return
            
            for i in range(len(s)):
                if used[i]:
                    continue
                
                if i > 0 and s[i] == s[i-1] and not used[i-1]:
                    continue
                
                used[i] = True
                path.append(s[i])
                
                backtrack(path)
                
                path.pop()
                used[i] = False
        
        backtrack([])
        return res