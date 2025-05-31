
# Ishaan Loves Chocolates
class Solution:
    def chocolates(self, arr) :
        start = 0
        end = len(arr) - 1
        
        while start < end:
            if arr[start] > arr[end]:
                start += 1
            else:
                end -= 1
        
        return arr[start]

s = Solution()

arr = [5, 3, 1, 6, 9]
print(s.chocolates(arr))

arr = [5, 9, 2, 6]
print(s.chocolates(arr))