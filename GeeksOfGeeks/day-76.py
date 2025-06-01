
#!  At least two greater elements

class Solution:
    def findElements(self,arr):
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[i]>arr[j]:
                    arr[i],arr[j]=arr[j],arr[i]
        return arr[:-2]

s = Solution()
arr = [int(i) for i in input("Enter array Elements : ").split()]
print(s.findElements(arr))