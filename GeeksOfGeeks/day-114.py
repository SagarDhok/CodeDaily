
#! Perfect Array
class Solution:
    def isPerfect(self, arr):
        n = len(arr)
        i = 0

        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1

        while i + 1 < n and arr[i] == arr[i + 1]:
            i += 1

        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1

        return i == n - 1

sol = Solution()

print(sol.isPerfect([1, 8, 8, 8, 3, 2]))   
print(sol.isPerfect([1, 1, 2, 2, 1]))      