
# Searching in an Array
# Note: 1-based indexing is followed here.

class Solution:
    def search(self,arr, k):
        # code here
     for i in range(len(arr)):
         if k == arr[i]:
             return i+1
     return -1
s  = Solution()
arr = [int(i) for i in input("Enter List Of Values : ").split()]
k = int(input('Enter A Number : '))
res = s.search(arr,k)
print(f"The First Occurence of element is at Index : {res}")