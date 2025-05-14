
# Maximum product of two numbers
class Solution:
	def maxProduct(self,arr):
		arr.sort()
		max_product = arr[-1]*arr[-2]
		return max_product

s  = Solution()
arr=  [1, 4, 3, 6, 7, 0] 
print(s.maxProduct(arr))

arr = [1, 100, 42, 4, 23]
print(s.maxProduct(arr))
