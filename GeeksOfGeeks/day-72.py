

# Sort first half in ascending and second half in descending
class Solution:
    def customSort(self, arr):
      mid = len(arr) // 2
      return sorted(arr[:mid]) + sorted(arr[mid:], reverse=True)
    
s = Solution()
arr = [10, 20, 30, 40]
print(s.customSort(arr))
arr= [5, 4, 6, 2, 3, 8, 9, 7]
print(s.customSort(arr))