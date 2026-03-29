

#! Insertion Sort
# Difficulty: EasyAccuracy: 66.61%Submissions: 274K+Points: 2Average Time: 15m
# Given an array arr[] of positive integers.The task is to complete the insertsort() function which is used to implement Insertion Sort.

# Examples:

# Input: arr[] = [4, 1, 3, 9, 7]
# Output: [1, 3, 4, 7, 9]
# Explanation: The sorted array will be [1, 3, 4, 7, 9].
# Input: arr[] = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Explanation: The sorted array will be [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
# Input: arr[] = [4, 1, 9]
# Output: [1, 4, 9]
# Explanation: The sorted array will be [1, 4, 9].
# Constraints:
# 1 ≤ arr.size() ≤ 1000
# 1 ≤ arr[i] ≤ 10000


class Solution:
    def insertionSort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            
            arr[j + 1] = key
        
        return arr
s  = Solution()
arr = [4, 1, 3, 9, 7]
print(s.insertionSort(arr))

arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(s.insertionSort(arr))

arr= [4, 1, 9]
print(s.insertionSort(arr))



#! Bubble Sort

class Solution:
    def bubbleSort(self, arr):
        n = len(arr)
        
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        
        return arr
    

s  = Solution()
arr = [4, 1, 3, 9, 7]
print(s.insertionSort(arr))

arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(s.insertionSort(arr))

arr= [4, 1, 9]
print(s.insertionSort(arr))