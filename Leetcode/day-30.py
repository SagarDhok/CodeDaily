#  Range Sum Query - Immutable
class NumArray:

    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        s = 0
        for i in range(left, right + 1):
            s += self.nums[i]
        return s

nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)

print(obj.sumRange(0, 2))  
