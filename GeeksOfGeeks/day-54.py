
# First 1 in a Sorted Binary Array

class Solution:
    def firstIndex(self, arr):
                for i in range(len(arr)):
                 if arr[i] == 1:
                  return i
                
                return -1
                
arr = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
s =Solution()
print(s.firstIndex(arr))

                
arr = [0, 0, 0, 0]
s =Solution()
print(s.firstIndex(arr))