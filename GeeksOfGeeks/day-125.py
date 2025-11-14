

#! Reading books
class Solution:
    def maxPoint(self, k,arr1,arr2):
         
        ans = 0
        for t,p in zip(arr1,arr2):
            times = k//t
            ans = max(ans,times*p)
        return ans
    
s= Solution()
k = 10
arr1 = [3, 4, 5]
arr2 = [4, 4, 5]
print(s.maxPoint(k,arr1,arr2))

k = 12
arr1 = [8, 5]
arr2 = [100, 5]
print(s.maxPoint(k,arr1,arr2))