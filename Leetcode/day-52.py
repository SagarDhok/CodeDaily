

class Solution:
    def canWinNim(self, n) :
        return n % 4 != 0

s = Solution()
print(s.canWinNim(int(input("Enter A Number : ")))