

#! 883. Projection Area of 3D Shapes
class Solution:
    def projectionArea(self, grid):
        
        n = len(grid)
        xy = sum(1 for i in range(n) for j in range(n) if grid[i][j] > 0)
        yz = sum(max(row) for row in grid)
        zx = sum(max(grid[i][j] for i in range(n)) for j in range(n))
        return xy + yz + zx
