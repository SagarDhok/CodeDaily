

#! Smallest Positive Missing
class Solution:
    def missingNumber(self, arr):
        s = set(arr)
        i = 1
        while i in s:
            i += 1
        return i

s = Solution()
arr = [2, -3, 4, 1, 1, 7]
print(s.missingNumber(arr))
arr = [5, 3, 2, 5, 1]
print(s.missingNumber(arr))


arr = [-8, 0, -1, -4, -3]
print(s.missingNumber(arr))