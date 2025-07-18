
#! Tough Competitors
class Solution:
    def minDiff(self, arr):
        arr.sort()
        min_diff = float("inf")
        
        for i in range(len(arr) - 1):
            curr_diff = arr[i+1] - arr[i]
            if curr_diff < min_diff:
                min_diff = curr_diff
        
        return min_diff

s = Solution()
arr = [9, 4, 12, 6]
print(s.minDiff(arr))

arr = [4, 9, 1, 32, 12]
print(s.minDiff(arr))