
# Multiply Array
class Solution:
    def product(self, arr):
        pr= 1
        for i in arr:
            pr*=i
        return pr
    
    
s = Solution()
print("Product : ",s.product([int(i) for i in input("Enter Values : ").split()]))