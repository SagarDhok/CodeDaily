# Last index of One
class Solution:
    def lastIndex(self, s: str) -> int:
        # code here
        for i in range(len(s)-1, -1, -1):
          if s[i] == '1':
           return i
        return -1
s = Solution()
print(s.lastIndex("00001"))
print(s.lastIndex("0"))
