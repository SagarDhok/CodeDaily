
#! A guy with a mental problem
class Solution:
    def min_time(self, arr1, arr2):
     time1 = 0
     time2=0
     for i in range(len(arr1)):
         if i%2==0:
             time1 += arr1[i]
             time2+=arr2[i]
         else:
             time1 +=arr2[i]
             time2+=arr1[i]
             
     return min(time1,time2)
s = Solution()
arr1 = [2, 1, 2]
arr2 = [3, 2, 1]
print(s.min_time(arr1,arr2))             

arr1 = [1, 3, 1, 2] 
arr2 = [2, 2, 3, 1]
print(s.min_time(arr1,arr2))    