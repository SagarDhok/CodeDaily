
#! Array insert at index
class Solution:
    def insertAtIndex(self, arr, sizeOfArray, index, element):
        for i in range(sizeOfArray - 1, index, -1):
            arr[i] = arr[i - 1]
        
        arr[index] = element

sol = Solution()

arr1 = [1, 2, 3, 4, 5, None]
sizeOfArray1 = 6
index1 = 5
element1 = 90
sol.insertAtIndex(arr1, sizeOfArray1, index1, element1)
print("Test Case 1: ", arr1)  

