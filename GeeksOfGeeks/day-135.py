
#! Two sum -Pairs with 0 Sum
class Solution:
    def getPairs(self, arr):
        arr.sort()
        left, right = 0, len(arr)-1
        res = []

        while left < right:
            s = arr[left] + arr[right]

            if s == 0:
                res.append([arr[left], arr[right]])
                l, r = arr[left], arr[right]
                while left < right and arr[left] == l:
                    left += 1
                while left < right and arr[right] == r:
                    right -= 1
            elif s < 0:
                left += 1
            else:
                right -= 1

        return res


print(Solution().getPairs([-1, 0, 1, 2, -1, -4]))   # [[-1, 1]]
print(Solution().getPairs([6, 1, 8, 0, 4, -9, -1, -10, -6, -5])) # [[-6, 6], [-1, 1]]
