

#! Alternative sorting 
class Solution:
    def alternateSort(self,arr):
        
        arr.sort()
        result = [0]*len(arr)
        k = 0
        start = 0
        end = len(arr)-1
        
        while start<=end:
            
            result[k]=arr[end]
            k+=1
            end -=1
            
            if start<=end:
                result[k]=arr[start]
                k+=1
                start+=1
        return result 


s = Solution()
arr = [7, 1, 2, 3, 4, 5, 6]
print(s.alternateSort(arr))

arr = [1, 6, 9, 4, 3, 7, 8, 2]
print(s.alternateSort(arr))