
# Elements in the Range

class Solution:
    def check_elements(self, arr,  A, B):
                for i in range(A,B+1):
                 if i not in arr:
                  return False
                return True
n = 7
A = 2
B = 5
arr =  [1, 4, 5, 2, 7, 8, 3]
s = Solution()
print(s.check_elements(arr,A,B))

A = 2
B = 6
arr = [1, 4, 5, 2, 7, 8, 3]
print(s.check_elements(arr,A,B))