


class Solution:
    def solveNQueens(self, n) :
        res = []
        board = [["."] * n for _ in range(n)]
        
        def isSafe(r, c):
            for i in range(r):
                if board[i][c] == "Q":
                    return False
            i, j = r - 1, c - 1
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1
            i, j = r - 1, c + 1
            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1
            return True

        def solve(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return
            for c in range(n):
                if isSafe(r, c):
                    board[r][c] = "Q"
                    solve(r + 1)
                    board[r][c] = "."

        solve(0)
        return res
sol = Solution()
print(sol.solveNQueens(int(input("Enter A Number : "))))
