
#! Triplet Family
class Solution:
    def findTriplet(self, arr):
       arr.sort()
       for i in range(len(arr)):
           for j in range(i+1,len(arr)):
               s = arr[i]+arr[j]
               if s in arr[j+1:]:
                   return True
       return False
         
s = Solution()
arr = [int(i) for i in input("Enter list of numbers : ").split()]
print(s.findTriplet(arr))