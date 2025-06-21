
#! Sum of distinct elements

class Solution:
    def findSum(self, arr):
        max_val = 100001
        visited = [0] * max_val
        total = 0
        for i in range(len(arr)):
            if visited[arr[i]] == 0:
                total += arr[i]
                visited[arr[i]] = 1
        return total
s = Solution()
arr = [int(i) for i in input("Enter Values : ").split()]
print(s.findSum(arr))


class Solution:
  def findSum(self,arr):	
     dis_array= []
     for i in range(len(arr)):
        duplicate = False	    
        for j in range(len(dis_array)):
          if arr[i]==dis_array[j]:
           duplicate=True
           break
        if not duplicate :
          dis_array+=[arr[i]]
     s = 0
     for val in dis_array: 
      s +=val
     return s
s = Solution()
arr = [int(i) for i in input("Enter Values : ").split()]
print(s.findSum(arr))
      

