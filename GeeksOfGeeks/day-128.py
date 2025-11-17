
#! Minimum move to front operations
class Solution:
    def minMoves(self, arr):
        n = len(arr)
        last = n
        for i in range(n-1, -1, -1):
            if arr[i] == last:
                last -= 1
        return last


s = Solution()
arr = [3, 2, 1, 4]
print(s.minMoves(arr))

arr = [5, 7, 4, 3, 2, 6, 1]
print(s.minMoves(arr))