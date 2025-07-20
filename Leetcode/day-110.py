

#! 821. Shortest Distance to a Character
class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        n = len(s)
        result = [float('inf')] * n
        prev = float('-inf')

        for i in range(n):
            if s[i] == c:
                prev = i
            result[i] = abs(i - prev)

        prev = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            result[i] = min(result[i], abs(i - prev))

        return result
s = Solution()
s = "loveleetcode"
c = "e"
print(s.shortestToChar(s,c))

s = "aaab"
c = "b"
print(s.shortestToChar(s,c))