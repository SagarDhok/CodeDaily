
#! Maximum Element in Array
class Solution:
    def largest(self, arr ):
        mv = 0
        for i in arr:
            if i>mv:
                mv = i
                
        return mv
s= Solution()
print(s.largest([1, 8, 7, 56, 90]))
print(s.largest([5, 5, 5, 5]))
print(s.largest([10]))