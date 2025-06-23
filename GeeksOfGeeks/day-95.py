

#! Longest Increasing Subarray
class Solution:
    def lenOfLongIncSubArr(self, arr):
            
        max_count = 1
        count= 1
        for i in range(len(arr)-1):
          if arr[i]<arr[i+1]:
                       count +=1
                       if count>max_count:
                               max_count = count
          else:
                        count = 1
        return max_count
    
s = Solution()
arr = [ 5, 6, 3, 5, 7, 8, 9, 1, 2]
print(s.lenOfLongIncSubArr(arr))
                   
    
    
arr = [12, 13, 1, 5, 4, 7, 8, 10, 10, 11]
print(s.lenOfLongIncSubArr(arr))