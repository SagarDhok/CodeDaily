



#! Two Sum - Pair with Given Sum
class Solution:
    def twoSum(self, arr, target):
        seen = set()

        for num in arr:
            needed = target - num

            if needed in seen:
                return True

            seen.add(num)

        return False

s = Solution()
arr = [0, -1, 2, -3, 1]
target = -2
print(s.twoSum(arr,target))

arr = [1, -2, 1, 0, 5]
target = 0
print(s.twoSum(arr,target))

arr = [11]
target = 11
print(s.twoSum(arr,target))