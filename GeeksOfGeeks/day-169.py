

#! Bubble Sort
# Difficulty: EasyAccuracy: 59.33%Submissions: 350K+Points: 2Average Time: 15m
# Given an array, arr[]. Sort the array using bubble sort algorithm.

# Examples :

# Input: arr[] = [4, 1, 3, 9, 7]
# Output: [1, 3, 4, 7, 9]
# Explanation: After Sorting the array in ascending order of their values is [1, 3, 4, 7, 9].
# Input: arr[] = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Explanation: Sort the array in ascending order of their values.
# Input: arr[] = [1, 2, 3, 4, 5]
# Output: [1, 2, 3, 4, 5]
# Explanation: An array that is already sorted should remain unchanged after applying bubble sor

class Solution:
    def bubbleSort(self,arr):
        n = len(arr)
        
        for i in range(n):
            for j in range(n - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        
        return arr

s = Solution()
arr = [4, 1, 3, 9, 7]
print(s.bubbleSort(arr))


arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(s.bubbleSort(arr))

arr = [1, 2, 3, 4, 5]
print(s.bubbleSort(arr))
