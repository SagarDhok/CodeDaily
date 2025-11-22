

#! Rotate Array
class Solution:
    def rotateArr(self, arr, d):
        n = len(arr)
        d = d % n
        arr[:] = arr[d:] + arr[:d]

s = Solution()
arr = [1, 2, 3, 4, 5]
d = 2
print(s.rotateArr(arr,d))

arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
d = 3
print(s.rotateArr(arr,d))

arr = [7, 3, 9, 1]
d = 9
print(s.rotateArr(arr,d))
  