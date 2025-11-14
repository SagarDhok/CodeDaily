

#! 905. Sort Array By Parity
class Solution:
    def sortArrayByParity(self, nums):
        evenarr = []
        oddarr = []
        for i in nums:
            if i%2==0:
                    evenarr.append(i)
            else:
                    oddarr.append(i)
        return evenarr+oddarr
        
s = Solution()
nums = [3,1,2,4]
print(s.sortArrayByParity(nums))

nums = [0]
print(s.sortArrayByParity(nums))