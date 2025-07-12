
#! Why is Melody so chocolaty?

class Solution:
    def max_happiness(self, arr):
        if len(arr) < 2:
            return 0  

        max_sum = arr[0] + arr[1]
        for i in range(2, len(arr)):
            curr_sum = arr[i] + arr[i - 1]
            if curr_sum > max_sum:
                max_sum = curr_sum
        return max_sum

s = Solution()
arr  = [1, 2, 3, 4, 5]
print(s.max_happiness(arr))

arr = [2, 1, 3, 4]
print(s.max_happiness(arr))