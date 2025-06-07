

# Minimize the Heights II

class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        arr.sort()
        ans = arr[n - 1] - arr[0]
        for i in range(1, n):
            if arr[i] - k < 0:
                continue
            max_val = max(arr[i - 1] + k, arr[n - 1] - k)
            min_val = min(arr[0] + k, arr[i] - k)
            ans = min(ans, max_val - min_val)
        return ans

ob = Solution()
arr = [int(i) for i in input("Enter list of numbers : ").split()]
k = int(input("Enter A number : "))
print(ob.getMinDiff(arr, k))  
