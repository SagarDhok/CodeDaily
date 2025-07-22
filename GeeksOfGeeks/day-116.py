


#! Elements before which no element is bigger
class Solution:
    def count_elements(self, arr):
        count = 0
        max_so_far = float('-inf')

        for num in arr:
            if num > max_so_far:
                count += 1
                max_so_far = num

        return count
s = Solution()

arr = [10, 40, 23, 35, 50, 7]
print(s.count_elements(arr))

arr = [5, 4, 1]
print(s.count_elements(arr))