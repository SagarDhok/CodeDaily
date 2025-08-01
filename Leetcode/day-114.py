


#! 867. Transpose Matrix

class Solution:
    def transpose(self, matrix):
        return [[matrix[r][c] for r in range(len(matrix))] for c in range(len(matrix[0]))]

s= Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(s.transpose(matrix))

matrix = [[1,2,3],[4,5,6]]
print(s.transpose(matrix))