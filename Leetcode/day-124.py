

#! 922. Sort Array By Parity II
class Solution:
    def sortArrayByParityII(self, nums):
        
        even = [i for i in nums if i % 2 == 0]
        odd = [i for i in nums if i % 2 != 0]

        res = []
        for k,v in zip(even,odd):
            res.append(k)
            res.append(v)

        return res
    
s = Solution()
nums = [4,2,5,7]
print(s.sortArrayByParityII(nums))



class Solution:
    def sortArrayByParityII(self, nums):
        even = [i for i in nums if i % 2 == 0]
        odd  = [i for i in nums if i % 2 != 0]

        res = [0] * len(nums)
        i = 0
        while i < len(even):
            res[2*i] = even[i]
            res[2*i + 1] = odd[i]
            i += 1

        return res

    
s = Solution()
nums = [4,2,5,7]
print(s.sortArrayByParityII(nums))