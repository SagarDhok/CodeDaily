

# Missing number in shuffled array

class Solution:
    def findMissing(self, arr1,arr2):
     sa1=0
     for i in arr1:
         sa1+=i
     sa2 = 0
     for j in arr2:
         sa2+=j
     return sa1-sa2

s = Solution()
arr1 = [4, 8, 1, 3, 7]
arr2= [7, 4, 3, 1]

s.findMissing(arr1,arr2)


arr1= [12, 10, 15, 23, 11, 30] 
arr2 = [15, 12, 23, 11, 30]
print(s.findMissing(arr1,arr2))
