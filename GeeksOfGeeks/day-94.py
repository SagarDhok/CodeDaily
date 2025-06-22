

#! The problem of identical arrays

class Solution:
    def isIdentical(self, a, b):
        
        if len(a)!=len(b):
            return False
            
        freq_a = {}
        for i in a:
           if i not in freq_a:
               freq_a[i]=1
           else:
               freq_a[i]+=1
               
        freq_b = {}
        for i in b:
           if i not in freq_b:
               freq_b[i]=1
           else:
               freq_b[i]+=1
               
        
        for key in  freq_a:
            if key not in  freq_b:
                return False
                
            if  freq_b[key]!= freq_a[key]:
                return False
        return True
    

s = Solution()
a = [1, 2, 3, 4, 5]
b = [3, 4, 1, 2, 5]
print(s.isIdentical(a,b))


a = [1, 2, 4]
b = [3, 2, 1]
print(s.isIdentical(a,b))