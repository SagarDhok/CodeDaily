



class Solution:
    def checkStatus(self, a, b, flag):
        return (
            ((a >= 0) ^ (b >= 0)) and not flag
        ) or (
            (a < 0 and b < 0) and flag
        )
s = Solution()
a = 1
b = -1
flag = False
print(s.checkStatus(a,b,flag))

a = -182
b = -9121
flag = True
print(s.checkStatus(a,b,flag)) 


a = 5
b = 3
flag = True
print(s.checkStatus(a,b,flag)) 