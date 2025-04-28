
# Add Digits
#APPRAOCH - 1
class Solution:
    def addDigits(self, num: int) -> int:
        s = 0

        while num >= 10:
            while num > 0:
                digit = num % 10  
                s = s + digit  
                num = num // 10  
            
            num = s  
            s = 0  
        
        return num  
s = Solution()
print(s.addDigits(38))  
print(s.addDigits(0)) 


