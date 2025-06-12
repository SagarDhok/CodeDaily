

# Minimum Product of k Integers
class Solution:
    def minProduct(self, arr, k):
        arr.sort()
        product = 1
        mod = 10**9 + 7
        k = len(arr) if k>len(arr) else k
        for i in range(k):
            product = (product * arr[i]) % mod
        return product

    
s = Solution()
arr = [1, 2, 3, 4, 5]
k = 2
print(s.minProduct(arr,k))

arr = [9, 10, 8]
k = 3
print(s.minProduct(arr,k))

arr = [17, 20, 13, 15, 12, 20, 19, 20, 13, 20, 11, 11, 16, 18, 15, 15, 12, 14]
k = 10
print(s.minProduct(arr,k))



