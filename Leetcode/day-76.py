



from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lm, rm = 0, 0
        w = 0
        while l <= r:
            if height[l] < height[r]:
                if height[l] >= lm:
                    lm = height[l]
                else:
                    w += lm - height[l]
                l += 1
            else:
                if height[r] >= rm:
                    rm = height[r]
                else:
                    w += rm - height[r]
                r -= 1
        return w

sol = Solution()

test_cases = [
    [0,1,0,2,1,0,1,3,2,1,2,1],
    [4,2,0,3,2,5],
    [1,0,2,1,0,1,3],
    [5,4,1,2],
    [2,0,2],
    [3,0,0,2,0,4],
    [],
    [1],
    [2, 1, 2],
    [4, 2, 3]
]

for i, height in enumerate(test_cases, 1):
    result = sol.trap(height)
    print(f"Test Case {i}: {height}")
    print(f"Trapped Water: {result}\n")
