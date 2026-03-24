

#! Non Repeating Character
# Difficulty: EasyAccuracy: 40.43%Submissions: 338K+Points: 2Average Time: 30m
# Given a string s consisting of lowercase English Letters. return the first non-repeating character in s. If there is no non-repeating character, return '$'.

# Examples:

# Input: s = "geeksforgeeks"
# Output: 'f'
# Explanation: In the given string, 'f' is the first character in the string which does not repeat.
# Input: s = "racecar"
# Output: 'e'
# Explanation: In the given string, 'e' is the only character in the string which does not repeat.
# Input: s = "aabbccc"
# Output: '$'
# Explanation: All the characters in the given string are repeating.
# Constraints:
# 1 ≤ s.size() ≤ 105


class Solution:
    def nonRepeatingChar(self, s):
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for ch in s:
            if freq[ch] == 1:
                return ch

        return "$"
    
obj = Solution()
s = "geeksforgeeks"
print(obj.nonRepeatingChar(s))

s = "racecar"
print(obj.nonRepeatingChar(s))

s = "aabbccc"
print(obj.nonRepeatingChar(s))




