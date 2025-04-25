
#! Count of smaller elements
class Solution:
    def countOfElements(self, x, arr):
        count = 0
        for i in arr:
            if i<=x:
                count+=1
        return count
s = Solution()
print(s.countOfElements(9,[10, 1, 2, 8, 4, 5] ))
print(s.countOfElements(2,[1, 2, 2, 5, 7, 2, 9]  ))