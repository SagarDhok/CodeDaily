

#! Reverse Words
# Difficulty: EasyAccuracy: 56.08%Submissions: 437K+Points: 2Average Time: 20m
# Given a string s, reverse the string without reversing its individual words. Words are separated by dots(.).

# Note: The string may contain leading or trailing dots(.) or multiple dots(.) between two words. The returned string should only have a single dot(.) separating the words, and no extra dots should be included.

# Examples :

# Input: s = "i.like.this.program.very.much"
# Output: "much.very.program.this.like.i"
# Explanation: The words in the input string are reversed while maintaining the dots as separators, resulting in "much.very.program.this.like.i".
# Input: s = "..geeks..for.geeks."
# Output: "geeks.for.geeks"
# Explanation: After removing extra dots and reversing the whole string, the input string becomes "geeks.for.geeks".
# Input: s = "..home....."
# Output: "home"
# Explanation: The input string contains only one word with extra dots around it. After removing the extra dots, the output is "home".
# Constraints:
# 1 ≤ s.length() ≤ 106
# String s contains only lowercase English alphabets and dots


class Solution:
    def reverseWords(self, s):
        s = s.split(".")
        res = ""
        for ch in s[::-1]:
             if ch.isalpha():
                  res = res + ch + "."
        return res[:-1]


obj= Solution()
s = "i.like.this.program.very.much"
print(obj.reverseWords(s))

s = "..geeks..for.geeks."
print(obj.reverseWords(s))

s = "..home....."
print(obj.reverseWords(s))


class Solution:
    def reverseWords(self, s):
        words = s.split(".")
        filtered = []

        for word in words:
            if word:
                filtered.append(word)

        filtered.reverse()
        return ".".join(filtered)
    
obj= Solution()
s = "i.like.this.program.very.much"
print(obj.reverseWords(s))

s = "..geeks..for.geeks."
print(obj.reverseWords(s))

s = "..home....."
print(obj.reverseWords(s))