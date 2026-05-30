



class Solution:
    def minDist(self, arr, x, y):
        last = -1
        ans = float('inf')

        for i in range(len(arr)):
            if arr[i] == x or arr[i] == y:

                if last != -1 and arr[i] != arr[last]:
                    ans = min(ans, i - last)

                last = i

        return ans if ans != float('inf') else -1
s = Solution()
arr = [1, 2, 3, 2]
x = 1
y = 2
print(s.minDist(arr,x,y))

arr = [86, 39, 90, 67, 84, 66, 62]
x = 42
y = 12
print(s.minDist(arr,x,y))