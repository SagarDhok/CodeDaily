
# Move Zeroes
class Solution:
    def moveZeroes(self, nums) :
        
        for i in nums[:]:
            print(i)
            if i == 0:
             nums.append(0)
             nums.remove(0)
        return nums
s= Solution()
nums = [0,1,0,3,12]
res = s.moveZeroes(nums)
print(res)







