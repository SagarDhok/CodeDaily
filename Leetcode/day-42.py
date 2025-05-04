
# Find the Difference
# class Solution:
#     def findTheDifference(self, s: str, t: str) -> str:
#         freq = [0] * 26  

#         for ch in s:
#             freq[ord(ch) - ord('a')] += 1
#             print(freq[ord(ch) - ord('a')])

#         for ch in t:
#             freq[ord(ch) - ord('a')] -= 1
#             if freq[ord(ch) - ord('a')] < 0:
#                 return ch
# s = "a"
# t = "aa"
# sol = Solution()
# print(sol.findTheDifference(s, t)) 

# print(sol.findTheDifference(s, t)) 

def find(s,t):
   for i in t:
       if i not in s:
           return i
       elif s.count(i)<t.count(i):
           return i
s = "ab"
t = "abc"
print(find(s,t))