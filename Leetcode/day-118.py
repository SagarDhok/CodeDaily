
#! 892. Surface Area of 3D Shapes
class Solution:
    def surfaceArea(self, grid):
            n = len(grid)
            total = 0
            for i in range(n):
                for j in range(n):
                    v = grid[i][j]
                    if v > 0:
                        total += 6 * v - 2 * (v - 1)
                    if j + 1 < n:
                        total -= 2 * min(v, grid[i][j + 1])
                    if i + 1 < n:
                        total -= 2 * min(v, grid[i + 1][j])
            return total
    
s = Solution()
grid = [[1,2],[3,4]]
print(s.surfaceArea(grid))

grid = [[1,1,1],[1,0,1],[1,1,1]]
print(s.surfaceArea(grid))

grid = [[2,2,2],[2,1,2],[2,2,2]]
print(s.surfaceArea(grid))
