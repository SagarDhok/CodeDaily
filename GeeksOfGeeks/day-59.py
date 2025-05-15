
# Find unique element
class Solution:
    def find_unique(self, arr):
        count = {}
        for i  in arr:
          if i in count:
            count[i]+=1
          else:
            count[i]=1
        for j in count:
          if count[j]==1:
              return j
s = Solution()
print(s.find_unique([6, 2, 5, 2, 2, 6, 6]))
print(s.find_unique( [2, 2, 2, 10, 2]))