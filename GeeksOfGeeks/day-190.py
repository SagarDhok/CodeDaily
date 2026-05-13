


#! String Duplicates Removal
# Difficulty: EasyAccuracy: 58.68%Submissions: 247K+Points: 2Average Time: 15m
# Given a string s which may contain lowercase and uppercase characters. The task is to remove all duplicate characters from the string and find the resultant string. The order of remaining characters in the output should be same as in the original string.

# Example 1:

# Input: s = "geEksforGEeks"
# Output: "geEksforG"
# Explanation: After removing duplicate characters such as E, e, k, s, we have string as "geEksforG".
# Example 2:

# Input: s = "HaPpyNewYear"
# Output: "HaPpyNewYr"
# Explanation: After removing duplicate characters such as e, a, we have string as "HaPpyNewYr".
# Constraints:
# 1 ≤ N ≤ 106
# String contains uppercase and lowercase english letters.

# Expected Complexities
# Company Tags


class Solution:

    def removeDuplicates(self, s):

        res = ""

        for ch in s:
            if ch not in res:
                res += ch

        return res

s = Solution()
print(s.removeDuplicates(input("Enter A string : ")))



class Solution:

    def removeDuplicates(self, s):

                s = list(s)
                seen = set()

                j = 0

                for i in range(len(s)):
                                if s[i] not in seen:
                                 seen.add(s[i])
                                 s[j] = s[i]
                                 j += 1
 
                result = "".join(s[:j])
                return result
s = Solution()
print(s.removeDuplicates(input("Enter A string : ")))


class Solution:
    def removeDups(self, s):
        seen = set()
        result = ""
        
        for ch in s:
            if ch not in seen:
                seen.add(ch)
                result += ch
        
        return result
print(s.removeDuplicates(input("Enter A string : ")))