
#! island perimeter
class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        perimeter = 0
        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    if i == 0 or grid[i - 1][j] == 0:
                        perimeter += 1
                    if i == rows - 1 or grid[i + 1][j] == 0:
                        perimeter += 1
                    if j == 0 or grid[i][j - 1] == 0:
                        perimeter += 1
                    if j == cols - 1 or grid[i][j + 1] == 0:
                        perimeter += 1

        return perimeter

s = Solution()
grid = [[0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]]
print(s.islandPerimeter(grid))

grid = [[1]]
print(s.islandPerimeter(grid))

grid = [[1,0]]
print(s.islandPerimeter(grid))
