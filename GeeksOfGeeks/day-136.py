
#! Maximum Product Subarray
class Solution:
   def maxProduct(self,arr):
            maxProd = arr[0]
            currMax = currMin = arr[0]
        
            for n in arr[1:]:
                if n < 0:
                    currMax, currMin = currMin, currMax   
        
                currMax = max(n, currMax * n)
                currMin = min(n, currMin * n)
        
                maxProd = max(maxProd, currMax)
        
            return maxProd


s  = Solution()
arr = [-2, 6, -3, -10, 0, 2]
print(s.maxProduct(arr))

arr = [-1, -3, -10, 0, 6]
print(s.maxProduct(arr))

arr = [2, 3, 4]
print(s.maxProduct(arr))

