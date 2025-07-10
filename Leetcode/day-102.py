
#! 733. Flood Fill
class Solution:
    def floodFill(self,image,sr,sc,color) :
        
      
        start_color = image[sr][sc]
        if start_color == color:
            return image

        def dfs(r, c):
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
                return
            if image[r][c] != start_color:
                return
            image[r][c] = color
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image
    
s = Solution()
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
print(s.floodFill(image,sr,sc,color))


image = [[0,0,0],[0,0,0]]
sr = 0
sc = 0
color = 0
print(s.floodFill(image,sr,sc,color))