

#! Pair With Difference
# Difficulty: EasyAccuracy: 27.25%Submissions: 297K+Points: 2Average Time: 15m
# Given an array, arr[] and an integer x, return true if there exists a pair of elements in the array whose absolute difference is x, otherwise, return false.

# Examples:

# Input: arr[] = [5, 20, 3, 2, 5, 80], x = 78
# Output: true
# Explanation: Pair (2, 80) have an absolute difference of 78.
# Input: arr[] = [90, 70, 20, 80, 50], x = 45
# Output: false
# Explanation: There is no pair with absolute difference of 45.
# Input: arr[] = [1], x = 1
# Output: false
# Constraints:
# 1<= arr.size() <=106 
# 1<= arr[i] <=106 
# 0<= x <=105



class Solution:
    def findPair(self, arr, x):
        # code here
        
            arr.sort()
            for i in range(len(arr)):
                for j in range(i+1, len(arr)):
                    if arr[j]-arr[i]==x:
                        return True
            return False
                    
s = Solution()
arr = [5, 20, 3, 2, 5, 80]
x = 78
print(s.findPair(arr,x))


arr = [90, 70, 20, 80, 50]
x = 45
print(s.findPair(arr,x))




from typing import List
class Solution:
    def findPair(self, arr: List[int], x: int) -> bool:
        arr.sort()
        
        i, j = 0, 1
        n = len(arr)
        
        while i < n and j < n:
            if i != j and abs(arr[j] - arr[i]) == x:
                return True
            
            elif abs(arr[j] - arr[i]) < x:
                j += 1
            else:
                i += 1
          
            if i == j:
                j += 1
        
        return False

s = Solution()
arr = [5, 20, 3, 2, 5, 80]
x = 78
print(s.findPair(arr,x))


arr = [90, 70, 20, 80, 50]
x = 45
print(s.findPair(arr,x))


