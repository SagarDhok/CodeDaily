
# Ugly Number
class Solution:
    def isUgly(self, n):
        if n <= 0:
            return False
        
        for p in [2, 3, 5]:
            while n % p == 0:
                n = n // p
        
        if n == 1:
            return True
        else:
            return False
        
s = Solution()
n = int(input("Enter a Number : "))
print(s.isUgly(n))
