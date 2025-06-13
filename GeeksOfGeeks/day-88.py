

# Type of array
class Solution:
    def detect_array_type(self, arr):
        n = len(arr)
        asc = 0
        dsc = 0

        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                asc += 1
            elif arr[i] < arr[i + 1]:
                dsc += 1

        if asc == 0:
            return 1
        elif dsc == 0:
            return 2
        elif asc == 1 and arr[-1] < arr[0]:
            return 4
        elif dsc == 1 and arr[-1] > arr[0]:
            return 3
        else:
            return -1

        
s = Solution()
arr = [int(i) for i in input("Enter list of numbers : ").split()]
print(s.maxNtype(arr))