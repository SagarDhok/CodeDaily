
#! Longest Common Prefix of Strings
# Difficulty: EasyAccuracy: 29.52%Submissions: 320K+Points: 2Average Time: 15m
# Given an array of strings arr[]. Return the longest common prefix among each and every strings present in the array. If there's no prefix common in all the strings, return "".

# Examples :

# Input: arr[] = ["geeksforgeeks", "geeks", "geek", "geezer"]
# Output: "gee"
# Explanation: "gee" is the longest common prefix in all the given strings.
# Input: arr[] = ["hello", "world"]
# Output: ""
# Explanation: There's no common prefix in the given strings.
# Constraints:
# 1 ≤ |arr| ≤ 103
# 1 ≤ |arr[i]| ≤ 103


class Solution:
    def longestCommonPrefix(self, arr):
        if not arr:
            return ""
        
        arr.sort()
        first = arr[0]
        last = arr[-1]
        
        prefix = ""
        for i in range(min(len(first), len(last))):
            if first[i] == last[i]:
                prefix += first[i]
            else:
                break
        
        return prefix
          
s = Solution()
arr = ["geeksforgeeks", "geeks", "geek", "geezer"]
print(s.longestCommonPrefix(arr))

arr = ["hello", "world"]
print(s.longestCommonPrefix(arr))
