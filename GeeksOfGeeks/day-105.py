
#! Minimum sum of two elements from two arrays
class Solution:
    def minSum(self, arr1, arr2):
        n = len(arr1)

        arr1_min = float('inf')
        arr1_second_min = float('inf')
        arr1_min_index = -1

        arr2_min = float('inf')
        arr2_second_min = float('inf')
        arr2_min_index = -1

        for i in range(n):
            if arr1[i] < arr1_min:
                arr1_second_min = arr1_min
                arr1_min = arr1[i]
                arr1_min_index = i
            elif arr1[i] < arr1_second_min:
                arr1_second_min = arr1[i]

            if arr2[i] < arr2_min:
                arr2_second_min = arr2_min
                arr2_min = arr2[i]
                arr2_min_index = i
            elif arr2[i] < arr2_second_min:
                arr2_second_min = arr2[i]

        if arr1_min_index != arr2_min_index:
            return arr1_min + arr2_min
        else:
            return min(arr1_min + arr2_second_min, arr1_second_min + arr2_min)

s = Solution()
arr1 = [5, 4, 13, 2, 1]
arr2 = [2, 3, 4, 6, 5]
print(s.altProduct([arr1,arr2]))

arr1 = [5, 4, 13, 1]
arr2 = [3, 2, 6, 1]
print(s.altProduct([arr1,arr2]))
