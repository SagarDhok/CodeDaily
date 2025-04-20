# Value equal to index value
#APPROACH 1 
class Solution:
    def valueEqualToIndex(self, arr):
     
        result = []
        for i in range(len(arr)):
           if arr[i] == i + 1:
            result.append(arr[i])
        return result
    

s = Solution()
arr = [int(i) for i in input("Enter List Of Values : ").split()]
print(s.valueEqualToIndex(arr)  )

#APPROACH 2
def valueEqualToIndex(arr):
 return [ arr[i] for i in range(len(arr)) if arr[i] == i + 1]
print(valueEqualToIndex([15, 2, 45, 4 , 7]))