
#! Replace all 0's with 5
class Solution: 
    def convertFive(self, n):
     if n == 0:
        return 5
     res = 0
     mul = 1

     while n >0:
        d = n%10
        if d==0:
           d = 5
        res = res + d*mul
        mul = mul*10
        n = n//10
     return res
n = int(input("Enter Number : "))
s = Solution()
print(s.convertFive(n))