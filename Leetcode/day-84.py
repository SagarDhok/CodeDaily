
#   Reshape the Matrix
class Solution:
    def matrixReshape(self, mat, r ,c):
        if len(mat) * len(mat[0]) == r * c:
            flat = [num for row in mat for num in row]
            new_mat = []
            for i in range(r):
                start = i * c
                end = (i + 1) * c
                row = flat[start:end]
                new_mat.append(row)
            return new_mat
        else:
            return mat
        
s = Solution()
mat = [[1, 2], [3, 4]]
r = 1
c = 4
print(s.matrixReshape(mat,r,c))


mat = [[1, 2], [3, 4]]
r =2
c = 4
print(s.matrixReshape(mat,r,c))