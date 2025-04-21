
# Move Zeroes
# class Solution:
#     def moveZeroes(self, nums) :
        
#         for i in nums[:]:
#             print(i)
#             if i == 0:
#              nums.append(0)
#              nums.remove(0)
#         return nums
# s= Solution()
# nums =  [int(i) for i in input("Enter List Of Values : ").split()]
# res = s.moveZeroes(nums)
# print(res)




# class Solution:
#     def moveZeroes(self, nums) :
#        nzi = 0
#        for i in range(len(nums)) :
#            if nums[i]!= 0:
#                nums[nzi] = nums[i]
#                nzi+=1
#        for i in range(nzi,len(nums)):
#            nums[i] = 0
#        return nums
       
# s= Solution()
# nums =  [int(i) for i in input("Enter List Of Values : ").split()]
# res = s.moveZeroes(nums)
# print(res)






class Solution:
    def moveZeroes(self, nums) :
       nzi = 0
       for i in range(len(nums)) :
           if nums[i]!= 0:
               nums[nzi],nums[i] = nums[i],nums[nzi]
               nzi+=1
       return nums
       
       
s= Solution()
nums = [int(i) for i in input("Enter List Of Values : ").split()]
res = s.moveZeroes(nums)
print(res)
