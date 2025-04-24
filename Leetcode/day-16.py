class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        k = 1  
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        
        return k


obj = Solution()
nums = [1,1,2]
res = obj.removeDuplicates(nums)
print(res)


class Solution:

    def removeDuplicates(self, nums):
       unique = []
       for i in nums : 
           if i not in unique:
               unique.append(i)
      
       for i in range(len(unique)):
           nums[i] = unique[i]
       
       return len(unique)
s=Solution()    
nums = [1,1,2]
result = s.removeDuplicates(nums)
print(result)