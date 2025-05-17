

# Pow(x, n)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n
        
s = Solution()
x = float(input("Enter x : "))
n = float(input("Enter y : "))
print(s.myPow(x,n))