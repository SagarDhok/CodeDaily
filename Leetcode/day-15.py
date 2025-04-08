# Valid Parentheses
class Solution:
    def isValid(self,s) :
        dict = {"(":")","{":"}","[":"]"}
        lst = []
        for char in s:
            if char in dict : 
                lst.append(dict[char])
            elif not list or char!=lst.pop():
                return False
        return not lst
    
obj = Solution()
s = input("Enter Brackets : ")
res = obj.isValid(s)
print(res)


