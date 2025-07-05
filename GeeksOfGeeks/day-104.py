

#! Sum of alternate product
class Solution:
    def altProduct(self, arr):
        arr.sort()
        start = 0
        end = len(arr)-1
        product = 0
        while start<=end:
             product+=arr[start]*arr[end]
             start+=1
             end-=1
        
        return product
s = Solution()
print(s.altProduct([int(i) for i in input("Enter Array Elements : ").split()]))

      
     