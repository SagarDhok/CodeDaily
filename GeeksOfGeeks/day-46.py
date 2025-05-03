
# Multiply the Sums of Left and Right Halves of an Array
class Solution:
    def multiply(self, arr):
        n = len(arr)
        mid = n // 2
        left_sum = sum(arr[:mid])
        right_sum = sum(arr[mid:])
        return left_sum * right_sum

sol = Solution()
print(sol.multiply([1, 2, 3, 4])) 
print(sol.multiply([1, 2]))   
print(sol.multiply([64, 73, 42, 53, 79, 91, 5, 46, 85]))  \
