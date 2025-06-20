

# Absolute Difference of 1
class Solution:
    def getDigitDiff1AndLessK(self, arr, k):
        
        result = []
        
        for i in arr:
            if i<10 or i>=k:
                continue
            
        
            val = i
            pre_digit = val%10
            val//=10
            
            valid = True
            
            while val>0:
                cur_digit = val%10
                diff= cur_digit-pre_digit
                
                if diff!=1 and diff!=-1:
                  valid = False
                  break
               
                pre_digit = cur_digit 
                val//=10
                
            if valid:
                result.append(i)
                
        return result
    
s= Solution()
arr = [7, 98, 56, 43, 45, 23, 12, 8]
k = 54
print(s.getDigitDiff1AndLessK(arr,k))



arr = [87, 89, 45, 235, 465, 765, 123, 987, 499, 655]
k = 1000
print(s.getDigitDiff1AndLessK(arr,k))