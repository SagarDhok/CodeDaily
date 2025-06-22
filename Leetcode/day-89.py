


# 598. Range Addition II
from typing import List

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n 
        min_a = min(op[0] for op in ops)
        min_b = min(op[1] for op in ops)
        
        return min_a * min_b


s = Solution()
m = 3
n = 3,
ops = [[2,2],[3,3]]
print(s.maxCount(m,n,ops))

m = 3
n = 3
ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
print(s.maxCount(m,n,ops))

m = 3
n = 3
ops = []
print(s.maxCount(m,n,ops))



