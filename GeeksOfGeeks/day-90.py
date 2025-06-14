

# Count pair sum

class Solution:
    def countPairs(self, arr1, arr2, x):
        count = 0
        i = 0
        j = len(arr2) - 1

        while i < len(arr1) and j >= 0:
            total = arr1[i] + arr2[j]
            if total == x:
                count += 1
                i += 1
                j -= 1
            elif total < x:
                i += 1
            else:
                j -= 1
        return count



s = Solution()
x = 10
arr1= [1, 3, 5, 7]
arr2 = [2, 3, 5, 8] 
print(s.countPairs(arr1,arr2,x))

x = 5
arr1 = [1, 2, 3, 4]
arr2 = [5, 6, 7, 8]
print(s.countPairs(arr1,arr2,x))