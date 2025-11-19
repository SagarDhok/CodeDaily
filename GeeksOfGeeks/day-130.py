

#! Make Co-prime Array
from math import gcd

class Solution:
    def countCoPrime(self, arr):
        insertions = 0
        for i in range(len(arr) - 1):
            if gcd(arr[i], arr[i+1]) != 1:
                insertions += 1
        return insertions

sol = Solution()
print(sol.countCoPrime([2, 7, 28]))
print(sol.countCoPrime([5, 10, 20]))
