

#! Rearranging array
class Solution:    
    def Rearrange(self, arr):
        arr.sort()
        i = 0
        j = len(arr) - 1
        result = []

        while i <= j:
            if i == j:
                result.append(arr[i])
            else:
                result.append(arr[i])
                result.append(arr[j])
            i += 1
            j -= 1

        
        for k in range(len(arr)):
            arr[k] = result[k]
        return arr
s = Solution()
print(s.Rearrange([int(i) for i in input("Enter Array Elements : ").split()]))

      