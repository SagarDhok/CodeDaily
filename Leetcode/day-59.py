
# Word Search
class Solution:
 def exist(self,board, word):
    rows, cols = len(board), len(board[0])
    
    def dfs(r, c, i):
        if i == len(word):
            return True
        if r<0 or c<0 or r>=rows or c>=cols or board[r][c] != word[i]:
            return False

        temp = board[r][c]
        board[r][c] = "#"

        result = (dfs(r+1, c, i+1) or
                  dfs(r-1, c, i+1) or
                  dfs(r, c+1, i+1) or
                  dfs(r, c-1, i+1))

        board[r][c] = temp
        return result

    for i in range(rows):
        for j in range(cols):
            if dfs(i, j, 0):
                return True
    return False




s  = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(s.exist(board,word))

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
print(s.exist(board,word))

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
print(s.exist(board,word))