
#! 39. Combination Sum
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, path, total):
            if total == target:
                res.append(path[:])
                return
            if total > target:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, total + candidates[i])
                path.pop()

        backtrack(0, [], 0)
        return res
s = Solution()
candidates = [2,3,6,7]
target = 7
print(s.combinationSum(candidates,target))


candidates = [2]
target = 1
print(s.combinationSum(candidates,target))