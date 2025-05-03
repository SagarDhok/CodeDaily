
# Find the Difference
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq = [0] * 26  

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        for ch in t:
            freq[ord(ch) - ord('a')] -= 1
            if freq[ord(ch) - ord('a')] < 0:
                return ch
