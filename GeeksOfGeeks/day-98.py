

# Sum Array Puzzle
class Solution:
    def sumArray(self, arr):
        sum = 0
        for i in arr:
          sum+=i
        
        for i in range(len(arr)):
          arr[i] = sum-arr[i]
                
        return arr
    
s = Solution()
print(s.sumArray([int(i) for i in input("Enter Array Values : ").split()]))