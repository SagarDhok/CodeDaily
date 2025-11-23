

#! 944. Delete Columns to Make Sorted
class Solution:
    def minDeletionSize(self, strs):
        delete = 0
        rows = len(strs)
        cols = len(strs[0])

        for c in range(cols):
            for r in range(rows - 1):
                if strs[r][c] > strs[r+1][c]:
                    delete += 1
                    break
        return delete

s = Solution()
strs = ["cba","daf","ghi"]
print(s.minDeletionSize(strs))

strs = ["a","b"]
print(s.minDeletionSize(strs))

strs = ["zyx","wvu","tsr"]
print(s.minDeletionSize(strs))