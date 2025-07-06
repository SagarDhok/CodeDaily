

#! Reducing Walls
class Solution:
    def reducingWalls(self, arr, k):
            operations = 0
            for height in arr:
                if height > k:
                    operations += (height - k + k - 1) // k  
            return operations
        
s = Solution()
print(s.reducingWalls([int(i) for i in input("Enter Array Elements : ").split()]))

      
     