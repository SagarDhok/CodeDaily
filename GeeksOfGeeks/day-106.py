
#! Shortest un-ordered subarray

class Solution:
    def shortestUnorderedSubarray(self, arr):  
        n = len(arr)
        for i in range(n - 2):
            if (arr[i] < arr[i+1] > arr[i+2]) or (arr[i] > arr[i+1] < arr[i+2]):
                return 3
        return 0

s = Solution()
print(s.shortestUnorderedSubarray([int(i) for i in input("Enter Array Elements : ").split()]))