1

#! Largest product
class Solution:
    def findMaxProduct(self, arr, k):
        n = len(arr)
        if k > n:
            return 0

        max_product = 0

        for i in range(n - k + 1):
            product = 1
            for j in range(i, i + k):
                product *= arr[j]
            max_product = max(max_product, product)

        return max_product
s = Solution()
print(s.findMaxProduct([int(i) for i in input("Enter Array Elements : ").split()]))

      
     
 