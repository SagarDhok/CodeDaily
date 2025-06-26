

# 628. Maximum Product of Three Numbers
class Solution:
    def maximumProduct(self, nums) :

        nums.sort()

        pro1 = nums[-1]*nums[-2]*nums[-3]
        pro2 = nums[0]*nums[1]*nums[-1]
        return pro1 if pro1>=pro2 else pro2
    
s = Solution()
print(s.maximumProduct([int(i) for i in input("Enter Array Elements : ").split()]))