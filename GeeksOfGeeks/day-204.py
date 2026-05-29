
#! Selection Sort
# Difficulty: EasyAccuracy: 64.33%Submissions: 251K+Points: 2Average Time: 15m
# Given an array arr, use selection sort to sort arr[] in increasing order.

# Examples :

# Input: arr[] = [4, 1, 3, 9, 7]
# Output: [1, 3, 4, 7, 9]
# Explanation: Maintain sorted (in bold) and unsorted subarrays. Select 1. Array becomes 1 4 3 9 7. Select 3. Array becomes 1 3 4 9 7. Select 4. Array becomes 1 3 4 9 7. Select 7. Array becomes 1 3 4 7 9. Select 9. Array becomes 1 3 4 7 9.
# Input: arr[] = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Input: arr[] = [38, 31, 20, 14, 30]
# Output: [14, 20, 30, 31, 38]
# Constraints:
# 1 ≤ arr.size() ≤ 103
# 1 ≤ arr[i] ≤ 106


class Solution:
    
    def selectionSort(self, arr):

        n = len(arr)

        for i in range(n):

            min_index = i

            for j in range(i + 1, n):

                if arr[j] < arr[min_index]:
                    min_index = j

            arr[i], arr[min_index] = arr[min_index], arr[i]

        return arr
s = Solution()
arr = [4, 1, 3, 9, 7]
print(s.selectionSort(arr))


arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(s.selectionSort(arr))

arr = [38, 31, 20, 14, 30]
print(s.selectionSort(arr))