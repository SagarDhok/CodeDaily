

# Arranging Coins

class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        while n >= i:
            n -= i
            i += 1
        return i - 1
s = Solution()
print(s.arrangeCoins(n = int(input("Enter A number : " ))))
